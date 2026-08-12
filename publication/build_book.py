#!/usr/bin/env python3
"""Build the illustrated PDF and EPUB reader editions.

The manuscript stays in the repository root as one Markdown file per chapter.
This script adds publication metadata, typography, navigation, and illustrations
without rewriting the source chapters.
"""

from __future__ import annotations

import argparse
import html
import re
import shutil
import uuid
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree

from PIL import Image as PILImage
from PIL import ImageDraw, ImageFont
from reportlab import rl_config

# PDF files are binary artifacts already. Keeping JPEG streams binary avoids
# roughly 25% ASCII85 overhead without recompressing or changing the images.
rl_config.useA85 = 0

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A5
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Flowable,
    Frame,
    Image,
    KeepTogether,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
)
from reportlab.platypus.tableofcontents import TableOfContents


ROOT = Path(__file__).resolve().parents[1]
PUBLICATION = ROOT / "publication"
IMAGES = PUBLICATION / "images"
TMP_PDF = ROOT / "tmp" / "pdfs"
PDF_IMAGE_CACHE = TMP_PDF / "images"
PDF_OUTPUT = ROOT / "output" / "pdf"
EPUB_OUTPUT = ROOT / "output" / "epub"

EPUB_IMAGE_MAX_EDGE = 1600
EPUB_IMAGE_QUALITY = 86
EPUB_COVER_QUALITY = 90
EPUB_MAX_FILE_SIZE = 20 * 1024 * 1024

PDF_PLATE_DPI = 300
PDF_IMAGE_QUALITY = 86
PDF_IMAGE_SUBSAMPLING = 1
PDF_COVER_QUALITY = 94
PDF_MAX_FILE_SIZE = 12 * 1024 * 1024

TITLE = "Если бы я вам рассказал про Сильвера"
SHORT_TITLE = "Если бы я вам рассказал про Сильвера"
AUTHORS = ["Аскар Рахимбердиев", "ChatGPT", "Claude"]
AUTHORS_LINE = "Аскар Рахимбердиев, ChatGPT и Claude"
AUTHORS_COVER_LINE = " · ".join(AUTHORS)
SOURCE_SHORT = "По мотивам романа Роберта Льюиса Стивенсона"
SOURCE_FULL = "По мотивам романа Роберта Льюиса Стивенсона «Остров сокровищ»"
LANGUAGE = "ru"
PUBLICATION_YEAR = "2026"
IDENTIFIER = "urn:uuid:" + str(uuid.uuid5(uuid.NAMESPACE_URL, TITLE + "|" + "|".join(AUTHORS)))

SLUG = "esli-by-ya-vam-rasskazal-pro-silvera"
FINAL_PDF = PDF_OUTPUT / f"{SLUG}.pdf"
REVIEW_PDF = PDF_OUTPUT / f"{SLUG}-illustrated-review.pdf"
FINAL_EPUB = EPUB_OUTPUT / f"{SLUG}.epub"
FRONT_PREVIEW = TMP_PDF / f"{SLUG}-front-matter-preview.pdf"

MANUSCRIPT_FILES = [f"chapter-{number:02d}.md" for number in range(1, 22)]
MANUSCRIPT_FILES += ["interlude-smollett.md"]
MANUSCRIPT_FILES += [f"chapter-{number:02d}.md" for number in range(22, 35)]

ILLUSTRATIONS = {
    "chapter-01.md": (
        "illustration-ch01-billy-bones-arrival.png",
        "Билли Бонс приходит к двухэтажному мотелю «Адмирал Бенбоу».",
    ),
    "chapter-03.md": (
        "illustration-ch03-blind-visitor.png",
        "Слепой посетитель удерживает Джима у двери мотеля.",
    ),
    "chapter-04.md": (
        "illustration-ch04-motel-coins.png",
        "Мать и Джим считают монеты в разгромленном мотеле.",
    ),
    "chapter-06.md": (
        "illustration-ch06-trelawney-map.png",
        "Джим, Ливси и Трелони разбирают карту и бумаги Бонса.",
    ),
    "chapter-07.md": (
        "illustration-ch07-boston-harbor.png",
        "Джим впервые видит «Испаньолу» в зимнем Бостонском порту.",
    ),
    "chapter-08.md": (
        "illustration-ch08-silver-meets-jim.png",
        "Джим впервые встречает Джона Сильвера в «Подзорной трубе».",
    ),
    "chapter-09.md": (
        "illustration-ch09-smollett-cabin.png",
        "Капитан Смоллетт объясняет свои опасения в каюте.",
    ),
    "chapter-11.md": (
        "illustration-ch11-apple-barrel.png",
        "Спрятавшийся в высокой яблочной бочке Джим подслушивает заговорщиков.",
    ),
    "chapter-13.md": (
        "illustration-ch13-island-resort.png",
        "Джим пробирается к заброшенному островному недострою.",
    ),
    "chapter-14.md": (
        "illustration-ch14-silver-and-tom.png",
        "Сильвер уговаривает Тома у ржавой трубы.",
    ),
    "chapter-15.md": (
        "illustration-ch15-ben-gunn.png",
        "Джим впервые встречает Бена Ганна.",
    ),
    "chapter-17.md": (
        "illustration-ch17-overloaded-dinghy.png",
        "Последний рейс перегруженного тузика к берегу.",
    ),
    "chapter-18.md": (
        "illustration-ch18-raising-the-flag.png",
        "Капитан Смоллетт поднимает американский флаг над конторой.",
    ),
    "chapter-20.md": (
        "illustration-ch20-silver-smollett-parley.png",
        "Сильвер и Смоллетт ведут переговоры у входа в контору.",
    ),
    "chapter-21.md": (
        "illustration-ch21-waiting-before-assault.png",
        "Защитники конторы ждут штурма в тени раскалённого бетона.",
    ),
    "chapter-22.md": (
        "illustration-ch22-ben-launches-coracle.png",
        "Бен спускает на воду сделанное им корытце.",
    ),
    "chapter-24.md": (
        "illustration-ch24-anchor-chain.png",
        "Джим карабкается на «Испаньолу» по якорной цепи.",
    ),
    "chapter-26.md": (
        "illustration-ch26-jim-and-hands.png",
        "Джим и Израэль Хэндс сходятся на палубе «Испаньолы».",
    ),
    "chapter-28.md": (
        "illustration-ch28-silver-protects-jim.png",
        "Сильвер объявляет пленного Джима своим.",
    ),
    "chapter-30.md": (
        "illustration-ch30-livesey-treats-jim.png",
        "Доктор Ливси осматривает и перевязывает руки Джима.",
    ),
    "chapter-32.md": (
        "illustration-ch32-flints-voice.png",
        "Люди Сильвера слышат голос Флинта у заброшенного театра.",
    ),
    "chapter-34.md": (
        "illustration-ch34-homecoming-hands.png",
        "Вернувшийся Джим показывает матери руки.",
    ),
}

# Each illustration is inserted immediately after the paragraph that establishes
# the depicted scene. Exact textual anchors make the placement survive ordinary
# reflow while failing loudly if the manuscript wording changes later.
ILLUSTRATION_ANCHORS = {
    "chapter-01.md": "Высокий, тяжёлый, в тёмном бушлате с поднятым воротником.",
    "chapter-03.md": "Рука взялась ниоткуда.",
    "chapter-04.md": "А потом она села на пол, придвинула лампу и стала считать.",
    "chapter-06.md": "Карта была не из книжек.",
    "chapter-07.md": "Обе уходили в серое небо.",
    "chapter-08.md": "У ворот верфи он пожал нам руки",
    "chapter-09.md": "Предлагаю три вещи.",
    "chapter-11.md": "Сильвер сидел, привалившись к бочке спиной",
    "chapter-13.md": "Первым был бассейн.",
    "chapter-14.md": "Сильвер сел сам, на трубу",
    "chapter-15.md": "Бен Ганн, — сказал он, не открывая глаз",
    "chapter-17.md": "Капитан сидел на корме с журналом на коленях.",
    "chapter-18.md": "Наверху флаг развернулся и встал",
    "chapter-20.md": "Я смотрел на него из темноты, в упор",
    "chapter-21.md": "Редрут открыл спасённую чайницу.",
    "chapter-22.md": "Бен спустил корыто в затишек за скалой",
    "chapter-24.md": "Потом пошла цепь.",
    "chapter-26.md": "Я долез до краспиц, обхватил мачту ногами и достал револьвер.",
    "chapter-28.md": "Он мой, — сказал Сильвер.",
    "chapter-30.md": "засыпал мои ладони жёлтым порошком и бинтовал заново",
    "chapter-32.md": "Это было лицо человека, который узнал голос.",
    "chapter-34.md": "Я показал.",
}

COVER_ART = IMAGES / "cover-art.png"
COVER = IMAGES / "cover.png"

PAGE_WIDTH, PAGE_HEIGHT = A5
INNER_MARGIN = 19 * mm
OUTER_MARGIN = 15 * mm
TOP_MARGIN = 17 * mm
BOTTOM_MARGIN = 19 * mm
TEXT_WIDTH = PAGE_WIDTH - INNER_MARGIN - OUTER_MARGIN
TEXT_HEIGHT = PAGE_HEIGHT - TOP_MARGIN - BOTTOM_MARGIN


def first_existing(paths: list[str]) -> Path:
    for raw_path in paths:
        path = Path(raw_path).expanduser()
        if path.exists():
            return path
    raise FileNotFoundError(f"None of these font paths exists: {paths}")


BODY_REGULAR = first_existing(
    [
        "/System/Library/Fonts/Supplemental/Georgia.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
    ]
)
BODY_BOLD = first_existing(
    [
        "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
        str(BODY_REGULAR),
    ]
)
BODY_ITALIC = first_existing(
    [
        "/System/Library/Fonts/Supplemental/Georgia Italic.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf",
        str(BODY_REGULAR),
    ]
)
TITLE_REGULAR = first_existing(
    [
        "~/Library/Fonts/Montserrat-Regular.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        str(BODY_REGULAR),
    ]
)
TITLE_MEDIUM = first_existing(
    [
        "~/Library/Fonts/Montserrat-Medium.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        str(TITLE_REGULAR),
    ]
)
TITLE_SEMIBOLD = first_existing(
    [
        "~/Library/Fonts/Montserrat-SemiBold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        str(TITLE_MEDIUM),
    ]
)


def register_pdf_fonts() -> None:
    font_specs = {
        "BookBody": BODY_REGULAR,
        "BookBodyBold": BODY_BOLD,
        "BookBodyItalic": BODY_ITALIC,
        "BookTitle": TITLE_REGULAR,
        "BookTitleMedium": TITLE_MEDIUM,
        "BookTitleSemibold": TITLE_SEMIBOLD,
    }
    for name, path in font_specs.items():
        if name not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont(name, str(path)))
    pdfmetrics.registerFontFamily(
        "BookBody",
        normal="BookBody",
        bold="BookBodyBold",
        italic="BookBodyItalic",
        boldItalic="BookBodyItalic",
    )


def load_font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size=size)


def centered_text(
    draw: ImageDraw.ImageDraw,
    canvas_width: int,
    y: int,
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int, int],
    *,
    stroke_width: int = 0,
    stroke_fill: tuple[int, int, int, int] | None = None,
) -> int:
    box = draw.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    width = box[2] - box[0]
    height = box[3] - box[1]
    x = (canvas_width - width) / 2
    draw.text(
        (x, y),
        text,
        font=font,
        fill=fill,
        stroke_width=stroke_width,
        stroke_fill=stroke_fill,
    )
    return height


def build_cover() -> Path:
    image = PILImage.open(COVER_ART).convert("RGBA")
    width, height = image.size

    shade = PILImage.new("RGBA", image.size, (0, 0, 0, 0))
    shade_pixels = shade.load()
    fade_end = int(height * 0.43)
    for y in range(fade_end):
        alpha = int(92 * (1 - y / fade_end) + 20)
        for x in range(width):
            shade_pixels[x, y] = (4, 11, 14, alpha)
    image = PILImage.alpha_composite(image, shade)

    draw = ImageDraw.Draw(image)
    cream = (240, 228, 201, 255)
    pale = (218, 214, 199, 255)
    shadow = (8, 14, 15, 200)

    author_font = load_font(TITLE_MEDIUM, 21)
    title_font = load_font(TITLE_SEMIBOLD, 59)
    title_last_font = load_font(TITLE_SEMIBOLD, 77)
    source_font = load_font(TITLE_MEDIUM, 19)

    centered_text(
        draw,
        width,
        68,
        AUTHORS_COVER_LINE.upper(),
        author_font,
        pale,
        stroke_width=1,
        stroke_fill=shadow,
    )

    title_lines = [
        ("ЕСЛИ БЫ Я ВАМ", title_font),
        ("РАССКАЗАЛ ПРО", title_font),
        ("СИЛЬВЕРА", title_last_font),
    ]
    y = 145
    for line, font in title_lines:
        line_height = centered_text(
            draw,
            width,
            y,
            line,
            font,
            cream,
            stroke_width=2,
            stroke_fill=shadow,
        )
        y += line_height + 22

    rule_width = 300
    rule_y = y + 5
    draw.line(
        ((width - rule_width) / 2, rule_y, (width + rule_width) / 2, rule_y),
        fill=(190, 174, 142, 210),
        width=2,
    )
    y = rule_y + 28
    for line in ["ПО МОТИВАМ РОМАНА", "РОБЕРТА ЛЬЮИСА СТИВЕНСОНА"]:
        line_height = centered_text(
            draw,
            width,
            y,
            line,
            source_font,
            pale,
            stroke_width=1,
            stroke_fill=shadow,
        )
        y += line_height + 12

    image.convert("RGB").save(COVER, quality=95)
    return COVER


def pdf_ready_image(
    source_path: Path,
    *,
    quality: int = PDF_IMAGE_QUALITY,
    subsampling: int = PDF_IMAGE_SUBSAMPLING,
    max_width: int | None = None,
) -> Path:
    """Create a print-sharp JPEG without embedding more pixels than the page uses."""

    PDF_IMAGE_CACHE.mkdir(parents=True, exist_ok=True)
    output_path = PDF_IMAGE_CACHE / f"{source_path.stem}.jpg"
    with PILImage.open(source_path) as source:
        image = source.convert("RGB")
        if max_width and image.width > max_width:
            target_height = round(image.height * max_width / image.width)
            image = image.resize(
                (max_width, target_height),
                PILImage.Resampling.LANCZOS,
            )
        image.save(
            output_path,
            format="JPEG",
            quality=quality,
            subsampling=subsampling,
            optimize=True,
            progressive=True,
            dpi=(PDF_PLATE_DPI, PDF_PLATE_DPI),
        )
    return output_path


def epub_image_name(source_name: str) -> str:
    """Return the JPEG filename used for a master image inside the EPUB."""

    return f"{Path(source_name).stem}.jpg"


def write_epub_image(
    source_path: Path,
    output_path: Path,
    *,
    quality: int,
    subsampling: int = 1,
) -> None:
    """Write a screen-sized JPEG while preserving the master PNG in the repo."""

    with PILImage.open(source_path) as source:
        image = source.convert("RGB")
        image.thumbnail(
            (EPUB_IMAGE_MAX_EDGE, EPUB_IMAGE_MAX_EDGE),
            PILImage.Resampling.LANCZOS,
        )
        image.save(
            output_path,
            format="JPEG",
            quality=quality,
            subsampling=subsampling,
            optimize=True,
            progressive=True,
        )


def read_chapter(path: Path) -> tuple[str, list[str]]:
    source = path.read_text(encoding="utf-8").strip()
    blocks = [block.strip() for block in re.split(r"\n\s*\n", source) if block.strip()]
    if not blocks or not blocks[0].startswith("# "):
        raise ValueError(f"Missing H1 title in {path}")
    title = blocks[0][2:].strip()
    return title, blocks[1:]


INLINE_MARKUP = re.compile(r"(`[^`\n]+`|\*[^*\n]+\*)")


def paragraph_markup(text: str, *, target: str) -> str:
    """Convert the two inline conventions used by the manuscript.

    Backticks mark printed matter such as signs and initials; asterisks mark
    lyrics or another deliberately italic voice. All other source text is
    escaped before the publication markup is added.
    """

    normalized = " ".join(part.strip() for part in text.splitlines())
    output: list[str] = []
    for part in INLINE_MARKUP.split(normalized):
        if not part:
            continue
        if part.startswith("`") and part.endswith("`"):
            value = html.escape(part[1:-1])
            if target == "pdf":
                output.append(f'<font name="BookTitleMedium" size="9.2">{value}</font>')
            else:
                output.append(f'<span class="inscription">{value}</span>')
        elif part.startswith("*") and part.endswith("*"):
            value = html.escape(part[1:-1])
            output.append(f"<i>{value}</i>" if target == "pdf" else f"<em>{value}</em>")
        else:
            output.append(html.escape(part))
    return "".join(output)


class ChapterHeading(Paragraph):
    def __init__(self, text: str, style: ParagraphStyle, key: str):
        super().__init__(html.escape(text), style)
        self.chapter_title = text
        self.bookmark_key = key


def inline_illustration(image_path: Path) -> KeepTogether:
    """Fit a landscape plate into the text measure without breaking the scene."""

    target_width = round(TEXT_WIDTH / 72 * PDF_PLATE_DPI)
    ready_path = pdf_ready_image(image_path, max_width=target_width)
    with PILImage.open(ready_path) as source:
        source_width, source_height = source.size
    width = TEXT_WIDTH
    height = width * source_height / source_width
    image = Image(str(ready_path), width=width, height=height)
    image.hAlign = "CENTER"
    return KeepTogether([Spacer(1, 4 * mm), image, Spacer(1, 5 * mm)])


class BookDocTemplate(BaseDocTemplate):
    def __init__(self, filename: str, **kwargs):
        super().__init__(filename, **kwargs)
        self.current_chapter = ""

        cover_frame = Frame(
            0,
            0,
            PAGE_WIDTH,
            PAGE_HEIGHT,
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0,
            id="cover-frame",
        )
        text_frame = Frame(
            INNER_MARGIN,
            BOTTOM_MARGIN,
            TEXT_WIDTH,
            TEXT_HEIGHT,
            leftPadding=0,
            rightPadding=0,
            topPadding=0,
            bottomPadding=0,
            id="text-frame",
        )
        self.addPageTemplates(
            [
                PageTemplate(id="Cover", frames=[cover_frame], onPage=draw_front_page),
                PageTemplate(id="Front", frames=[text_frame], onPage=draw_front_page),
                PageTemplate(id="Chapter", frames=[text_frame], onPage=draw_chapter_page),
                PageTemplate(id="Body", frames=[text_frame], onPage=draw_body_page),
            ]
        )

    def afterFlowable(self, flowable: Flowable) -> None:
        if isinstance(flowable, ChapterHeading):
            self.current_chapter = flowable.chapter_title
            key = flowable.bookmark_key
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(flowable.chapter_title, key, level=0, closed=False)
            self.notify("TOCEntry", (0, flowable.chapter_title, self.page, key))


def draw_front_page(canvas, doc) -> None:
    canvas.saveState()
    canvas.setTitle(TITLE)
    canvas.setAuthor(", ".join(AUTHORS))
    canvas.setSubject(SOURCE_FULL)
    canvas.setKeywords("литературный ремейк, Остров сокровищ, Роберт Льюис Стивенсон")
    canvas.restoreState()


def draw_page_number(canvas, doc) -> None:
    page = canvas.getPageNumber()
    canvas.setFont("BookTitle", 7.5)
    canvas.setFillColor(colors.HexColor("#66645f"))
    y = 10.5 * mm
    if page % 2 == 0:
        canvas.drawString(OUTER_MARGIN, y, str(page))
    else:
        canvas.drawRightString(PAGE_WIDTH - OUTER_MARGIN, y, str(page))


def draw_chapter_page(canvas, doc) -> None:
    canvas.saveState()
    draw_page_number(canvas, doc)
    canvas.restoreState()


def draw_body_page(canvas, doc) -> None:
    canvas.saveState()
    draw_page_number(canvas, doc)
    canvas.setFont("BookTitle", 7.1)
    canvas.setFillColor(colors.HexColor("#77736c"))
    header = SHORT_TITLE if canvas.getPageNumber() % 2 == 0 else doc.current_chapter
    if len(header) > 64:
        header = header[:61].rstrip() + "…"
    canvas.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 10.5 * mm, header)
    canvas.setStrokeColor(colors.HexColor("#c6c1b7"))
    canvas.setLineWidth(0.35)
    canvas.line(INNER_MARGIN, PAGE_HEIGHT - 12.5 * mm, PAGE_WIDTH - OUTER_MARGIN, PAGE_HEIGHT - 12.5 * mm)
    canvas.restoreState()


def pdf_styles() -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "body": ParagraphStyle(
            "Body",
            parent=base["BodyText"],
            fontName="BookBody",
            fontSize=10.4,
            leading=14.8,
            alignment=TA_JUSTIFY,
            firstLineIndent=5.2 * mm,
            spaceAfter=0.65 * mm,
            textColor=colors.HexColor("#211f1b"),
            allowWidows=0,
            allowOrphans=0,
        ),
        "first": ParagraphStyle(
            "First",
            parent=base["BodyText"],
            fontName="BookBody",
            fontSize=10.4,
            leading=14.8,
            alignment=TA_JUSTIFY,
            firstLineIndent=0,
            spaceAfter=0.65 * mm,
            textColor=colors.HexColor("#211f1b"),
            allowWidows=0,
            allowOrphans=0,
        ),
        "chapter": ParagraphStyle(
            "Chapter",
            parent=base["Heading1"],
            fontName="BookTitleSemibold",
            fontSize=16.2,
            leading=21,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#20211f"),
            spaceBefore=25 * mm,
            spaceAfter=15 * mm,
            keepWithNext=True,
        ),
        "interlude": ParagraphStyle(
            "Interlude",
            parent=base["Heading1"],
            fontName="BookTitleMedium",
            fontSize=15.2,
            leading=20,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#20211f"),
            spaceBefore=25 * mm,
            spaceAfter=15 * mm,
            keepWithNext=True,
        ),
        "scene": ParagraphStyle(
            "Scene",
            parent=base["BodyText"],
            fontName="BookTitle",
            fontSize=8.8,
            leading=12,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#77736c"),
            spaceBefore=5 * mm,
            spaceAfter=5 * mm,
        ),
        "front-title": ParagraphStyle(
            "FrontTitle",
            parent=base["Title"],
            fontName="BookTitleSemibold",
            fontSize=25,
            leading=31,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#20211f"),
            spaceAfter=14 * mm,
        ),
        "front-authors": ParagraphStyle(
            "FrontAuthors",
            parent=base["BodyText"],
            fontName="BookTitleMedium",
            fontSize=11.2,
            leading=17,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#33332f"),
            spaceAfter=12 * mm,
        ),
        "front-source": ParagraphStyle(
            "FrontSource",
            parent=base["BodyText"],
            fontName="BookBodyItalic",
            fontSize=10.7,
            leading=16,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#55524c"),
            spaceAfter=8 * mm,
        ),
        "colophon": ParagraphStyle(
            "Colophon",
            parent=base["BodyText"],
            fontName="BookBody",
            fontSize=9.3,
            leading=14,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#4f4c46"),
            spaceAfter=3 * mm,
        ),
        "contents-title": ParagraphStyle(
            "ContentsTitle",
            parent=base["Heading1"],
            fontName="BookTitleSemibold",
            fontSize=18,
            leading=23,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#20211f"),
            spaceBefore=15 * mm,
            spaceAfter=12 * mm,
        ),
    }


def cover_flowable() -> Image:
    ready_cover = pdf_ready_image(
        COVER,
        quality=PDF_COVER_QUALITY,
        subsampling=0,
    )
    return Image(str(ready_cover), width=PAGE_WIDTH, height=PAGE_HEIGHT)


def front_matter_story(styles: dict[str, ParagraphStyle], include_contents: bool) -> list[Flowable]:
    story: list[Flowable] = [cover_flowable(), NextPageTemplate("Front"), PageBreak()]
    story.extend(
        [
            Spacer(1, 27 * mm),
            Paragraph(html.escape(TITLE), styles["front-title"]),
            Paragraph(html.escape(AUTHORS_LINE), styles["front-authors"]),
            Spacer(1, 4 * mm),
            Paragraph(html.escape(SOURCE_FULL), styles["front-source"]),
            Spacer(1, 34 * mm),
            Paragraph(PUBLICATION_YEAR, styles["front-authors"]),
            PageBreak(),
            Spacer(1, 55 * mm),
            Paragraph(
                "Литературный ремейк с событийной структурой романа Роберта Льюиса Стивенсона «Остров сокровищ», перенесённой в США и Карибы начала 1950-х годов.",
                styles["colophon"],
            ),
            Paragraph(f"Авторы этой версии: {html.escape(AUTHORS_LINE)}.", styles["colophon"]),
            Paragraph(
                "Иллюстрации созданы с помощью OpenAI под художественной и редакторской координацией авторов.",
                styles["colophon"],
            ),
            Paragraph("Первое электронное издание, 2026.", styles["colophon"]),
        ]
    )
    if include_contents:
        story.extend([PageBreak(), Paragraph("Содержание", styles["contents-title"]), Spacer(1, 3 * mm)])
        toc = TableOfContents()
        toc.levelStyles = [
            ParagraphStyle(
                "TOCLevel1",
                fontName="BookBody",
                fontSize=9.4,
                leading=13.2,
                leftIndent=0,
                rightIndent=9 * mm,
                firstLineIndent=0,
                spaceBefore=1.1 * mm,
                textColor=colors.HexColor("#33312d"),
            )
        ]
        story.append(toc)
    return story


def chapter_story(styles: dict[str, ParagraphStyle]) -> list[Flowable]:
    story: list[Flowable] = []
    for index, filename in enumerate(MANUSCRIPT_FILES):
        path = ROOT / filename
        title, blocks = read_chapter(path)

        story.extend([NextPageTemplate("Chapter"), PageBreak()])

        style = styles["interlude"] if filename.startswith("interlude") else styles["chapter"]
        key = f"section-{index + 1:02d}"
        story.append(ChapterHeading(title, style, key))
        story.append(NextPageTemplate("Body"))

        chapter_body: list[Flowable] = []
        first_paragraph = True
        illustration = ILLUSTRATIONS.get(filename)
        illustration_anchor = ILLUSTRATION_ANCHORS.get(filename)
        illustration_inserted = False
        for block in blocks:
            if block == "---":
                chapter_body.append(Paragraph("• &nbsp;&nbsp; • &nbsp;&nbsp; •", styles["scene"]))
                first_paragraph = True
                continue
            paragraph_style = styles["first"] if first_paragraph else styles["body"]
            chapter_body.append(Paragraph(paragraph_markup(block, target="pdf"), paragraph_style))
            first_paragraph = False

            normalized_block = " ".join(part.strip() for part in block.splitlines())
            if illustration and illustration_anchor and illustration_anchor in normalized_block:
                if illustration_inserted:
                    raise ValueError(f"Illustration anchor occurs more than once in {filename}")
                image_name, _alt = illustration
                chapter_body.append(inline_illustration(IMAGES / image_name))
                illustration_inserted = True

        if illustration and not illustration_inserted:
            raise ValueError(f"Illustration anchor not found in {filename}: {illustration_anchor!r}")
        story.extend(protect_chapter_ending(chapter_body))
    return story


def protect_chapter_ending(flowables: list[Flowable]) -> list[Flowable]:
    """Keep short punch-line endings from becoming one-line final pages."""

    trailing_count = 0
    trailing_characters = 0
    for flowable in reversed(flowables):
        if not isinstance(flowable, Paragraph) or flowable.style.name not in {"Body", "First"}:
            break
        paragraph_length = len(flowable.getPlainText())
        if trailing_count >= 4 or (trailing_count >= 2 and trailing_characters + paragraph_length > 1800):
            break
        trailing_count += 1
        trailing_characters += paragraph_length

    if trailing_count < 2:
        return flowables
    start = len(flowables) - trailing_count
    return [*flowables[:start], KeepTogether(flowables[start:])]


def build_pdf(output: Path, *, front_only: bool = False) -> Path:
    register_pdf_fonts()
    build_cover()
    if PDF_IMAGE_CACHE.exists():
        shutil.rmtree(PDF_IMAGE_CACHE)
    output.parent.mkdir(parents=True, exist_ok=True)
    styles = pdf_styles()
    doc = BookDocTemplate(
        str(output),
        pagesize=A5,
        leftMargin=0,
        rightMargin=0,
        topMargin=0,
        bottomMargin=0,
        title=TITLE,
        author=", ".join(AUTHORS),
        subject=SOURCE_FULL,
        pageCompression=1,
    )
    story = front_matter_story(styles, include_contents=not front_only)
    try:
        if not front_only:
            story.extend(chapter_story(styles))
            doc.multiBuild(story)
        else:
            doc.build(story)
    finally:
        if PDF_IMAGE_CACHE.exists():
            shutil.rmtree(PDF_IMAGE_CACHE)
    if not front_only and output.stat().st_size > PDF_MAX_FILE_SIZE:
        raise ValueError(
            f"PDF is unexpectedly large: {output.stat().st_size / 1024 / 1024:.1f} MiB "
            f"(limit: {PDF_MAX_FILE_SIZE / 1024 / 1024:.0f} MiB)"
        )
    return output


def xhtml_document(title: str, body: str, *, extra_head: str = "") -> str:
    return f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ru" lang="ru">
<head>
  <meta charset="utf-8"/>
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" type="text/css" href="../styles/book.css"/>
  {extra_head}
</head>
<body>
{body}
</body>
</html>
'''


def chapter_xhtml(filename: str, title: str, blocks: list[str]) -> str:
    body: list[str] = [f'<section class="chapter" epub:type="chapter" xmlns:epub="http://www.idpf.org/2007/ops">']
    body.append(f"<h1>{html.escape(title)}</h1>")
    illustration = ILLUSTRATIONS.get(filename)
    illustration_anchor = ILLUSTRATION_ANCHORS.get(filename)
    illustration_inserted = False
    first_paragraph = True
    for block in blocks:
        if block == "---":
            body.append('<div class="scene-break" aria-hidden="true">•&#160;&#160;•&#160;&#160;•</div>')
            first_paragraph = True
            continue
        css_class = ' class="no-indent"' if first_paragraph else ""
        body.append(f"<p{css_class}>{paragraph_markup(block, target='epub')}</p>")
        first_paragraph = False

        normalized_block = " ".join(part.strip() for part in block.splitlines())
        if illustration and illustration_anchor and illustration_anchor in normalized_block:
            if illustration_inserted:
                raise ValueError(f"Illustration anchor occurs more than once in {filename}")
            image_name, alt = illustration
            epub_name = epub_image_name(image_name)
            body.append(
                f'<figure class="plate"><img src="../images/{html.escape(epub_name)}" alt="{html.escape(alt)}"/></figure>'
            )
            illustration_inserted = True

    if illustration and not illustration_inserted:
        raise ValueError(f"Illustration anchor not found in {filename}: {illustration_anchor!r}")
    body.append("</section>")
    return xhtml_document(title, "\n".join(body))


EPUB_CSS = '''@charset "utf-8";
html { -webkit-text-size-adjust: 100%; }
body {
  margin: 5%;
  color: #211f1b;
  background: #fff;
  font-family: Georgia, "Times New Roman", serif;
  line-height: 1.48;
  text-rendering: optimizeLegibility;
}
h1 {
  margin: 3.5em 0 2.1em;
  text-align: center;
  font-family: Montserrat, Arial, sans-serif;
  font-size: 1.48em;
  line-height: 1.25;
  font-weight: 600;
  page-break-after: avoid;
  break-after: avoid;
}
p {
  margin: 0 0 .32em;
  text-align: justify;
  text-indent: 1.35em;
  widows: 2;
  orphans: 2;
}
p.no-indent, h1 + p { text-indent: 0; }
.scene-break {
  margin: 1.7em 0;
  text-align: center;
  color: #77736c;
  letter-spacing: .18em;
}
.inscription {
  font-family: Montserrat, Arial, sans-serif;
  font-size: .92em;
  letter-spacing: .015em;
}
.plate {
  margin: 0 0 2.3em;
  text-align: center;
  page-break-inside: avoid;
  break-inside: avoid;
}
.plate img { width: 100%; height: auto; }
.title-page {
  min-height: 85vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}
.title-page h1 { margin: 0 0 1.6em; font-size: 2em; }
.authors { font-family: Montserrat, Arial, sans-serif; margin: 0 0 2.2em; }
.source { font-style: italic; text-indent: 0; text-align: center; }
.year { margin-top: 4em; text-indent: 0; text-align: center; }
.colophon { margin-top: 35vh; font-size: .9em; color: #4f4c46; }
.colophon p { text-indent: 0; text-align: left; margin-bottom: .7em; }
body.cover { margin: 0; padding: 0; text-align: center; background: #071014; }
body.cover img { width: 100%; height: auto; display: block; }
nav ol { list-style: none; padding-left: 0; }
nav li { margin: .45em 0; }
nav a { color: inherit; text-decoration: none; }
'''


def build_epub(output: Path) -> Path:
    build_cover()
    output.parent.mkdir(parents=True, exist_ok=True)
    staging = ROOT / "tmp" / "epub"
    if staging.exists():
        shutil.rmtree(staging)
    (staging / "META-INF").mkdir(parents=True)
    (staging / "OEBPS" / "text").mkdir(parents=True)
    (staging / "OEBPS" / "styles").mkdir(parents=True)
    (staging / "OEBPS" / "images").mkdir(parents=True)

    (staging / "mimetype").write_text("application/epub+zip", encoding="ascii")
    (staging / "META-INF" / "container.xml").write_text(
        '''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>
''',
        encoding="utf-8",
    )
    (staging / "OEBPS" / "styles" / "book.css").write_text(EPUB_CSS, encoding="utf-8")

    cover_name = epub_image_name(COVER.name)
    write_epub_image(
        COVER,
        staging / "OEBPS" / "images" / cover_name,
        quality=EPUB_COVER_QUALITY,
        subsampling=0,
    )
    for image_name, _alt in ILLUSTRATIONS.values():
        epub_name = epub_image_name(image_name)
        write_epub_image(
            IMAGES / image_name,
            staging / "OEBPS" / "images" / epub_name,
            quality=EPUB_IMAGE_QUALITY,
        )

    cover_xhtml = f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ru" lang="ru">
<head><meta charset="utf-8"/><title>Обложка</title><link rel="stylesheet" type="text/css" href="../styles/book.css"/></head>
<body class="cover"><div epub:type="cover" xmlns:epub="http://www.idpf.org/2007/ops"><img src="../images/{cover_name}" alt="Обложка книги"/></div></body>
</html>
'''
    (staging / "OEBPS" / "text" / "cover.xhtml").write_text(cover_xhtml, encoding="utf-8")

    title_body = f'''<section class="title-page" epub:type="titlepage" xmlns:epub="http://www.idpf.org/2007/ops">
  <h1>{html.escape(TITLE)}</h1>
  <p class="authors">{html.escape(AUTHORS_LINE)}</p>
  <p class="source">{html.escape(SOURCE_FULL)}</p>
  <p class="year">{PUBLICATION_YEAR}</p>
</section>'''
    (staging / "OEBPS" / "text" / "title.xhtml").write_text(
        xhtml_document(TITLE, title_body), encoding="utf-8"
    )

    colophon_body = f'''<section class="colophon" epub:type="copyright-page" xmlns:epub="http://www.idpf.org/2007/ops">
  <p>Литературный ремейк с событийной структурой романа Роберта Льюиса Стивенсона «Остров сокровищ», перенесённой в США и Карибы начала 1950-х годов.</p>
  <p>Авторы этой версии: {html.escape(AUTHORS_LINE)}.</p>
  <p>Иллюстрации созданы с помощью OpenAI под художественной и редакторской координацией авторов.</p>
  <p>Первое электронное издание, 2026.</p>
</section>'''
    (staging / "OEBPS" / "text" / "colophon.xhtml").write_text(
        xhtml_document("Выходные данные", colophon_body), encoding="utf-8"
    )

    chapter_items: list[tuple[str, str, str]] = []
    for index, filename in enumerate(MANUSCRIPT_FILES, start=1):
        title, blocks = read_chapter(ROOT / filename)
        chapter_name = f"section-{index:02d}.xhtml"
        (staging / "OEBPS" / "text" / chapter_name).write_text(
            chapter_xhtml(filename, title, blocks), encoding="utf-8"
        )
        chapter_items.append((f"section-{index:02d}", chapter_name, title))

    nav_links = "\n".join(
        f'      <li><a href="text/{name}">{html.escape(title)}</a></li>'
        for _item_id, name, title in chapter_items
    )
    nav_xhtml = f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="ru" lang="ru">
<head><meta charset="utf-8"/><title>Содержание</title><link rel="stylesheet" type="text/css" href="styles/book.css"/></head>
<body>
  <nav epub:type="toc" id="toc"><h1>Содержание</h1><ol>
{nav_links}
  </ol></nav>
</body>
</html>
'''
    (staging / "OEBPS" / "nav.xhtml").write_text(nav_xhtml, encoding="utf-8")

    nav_points = "\n".join(
        f'''    <navPoint id="nav-{index}" playOrder="{index}">
      <navLabel><text>{html.escape(title)}</text></navLabel>
      <content src="text/{name}"/>
    </navPoint>'''
        for index, (_item_id, name, title) in enumerate(chapter_items, start=1)
    )
    toc_ncx = f'''<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head><meta name="dtb:uid" content="{IDENTIFIER}"/></head>
  <docTitle><text>{html.escape(TITLE)}</text></docTitle>
  <navMap>
{nav_points}
  </navMap>
</ncx>
'''
    (staging / "OEBPS" / "toc.ncx").write_text(toc_ncx, encoding="utf-8")

    manifest_chapters = "\n".join(
        f'    <item id="{item_id}" href="text/{name}" media-type="application/xhtml+xml"/>'
        for item_id, name, _title in chapter_items
    )
    spine_chapters = "\n".join(
        f'    <itemref idref="{item_id}"/>' for item_id, _name, _title in chapter_items
    )
    manifest_images = "\n".join(
        f'    <item id="image-{index}" href="images/{epub_image_name(image_name)}" media-type="image/jpeg"/>'
        for index, (image_name, _alt) in enumerate(ILLUSTRATIONS.values(), start=1)
    )
    creators = "\n".join(
        f'    <dc:creator id="creator-{index}">{html.escape(author)}</dc:creator>'
        for index, author in enumerate(AUTHORS, start=1)
    )
    modified = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    content_opf = f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="book-id" xml:lang="ru">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="book-id">{IDENTIFIER}</dc:identifier>
    <dc:title>{html.escape(TITLE)}</dc:title>
{creators}
    <dc:language>{LANGUAGE}</dc:language>
    <dc:source>{html.escape(SOURCE_FULL)}</dc:source>
    <dc:date>{PUBLICATION_YEAR}</dc:date>
    <meta property="dcterms:modified">{modified}</meta>
    <meta name="cover" content="cover-image"/>
  </metadata>
  <manifest>
    <item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>
    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
    <item id="css" href="styles/book.css" media-type="text/css"/>
    <item id="cover-image" href="images/{cover_name}" media-type="image/jpeg" properties="cover-image"/>
    <item id="cover" href="text/cover.xhtml" media-type="application/xhtml+xml"/>
    <item id="title" href="text/title.xhtml" media-type="application/xhtml+xml"/>
    <item id="colophon" href="text/colophon.xhtml" media-type="application/xhtml+xml"/>
{manifest_images}
{manifest_chapters}
  </manifest>
  <spine toc="ncx">
    <itemref idref="cover" linear="yes"/>
    <itemref idref="title"/>
    <itemref idref="colophon"/>
{spine_chapters}
  </spine>
</package>
'''
    (staging / "OEBPS" / "content.opf").write_text(content_opf, encoding="utf-8")

    validate_epub_tree(staging)
    with zipfile.ZipFile(output, "w") as archive:
        archive.write(staging / "mimetype", "mimetype", compress_type=zipfile.ZIP_STORED)
        for path in sorted(staging.rglob("*")):
            if path.is_dir() or path == staging / "mimetype":
                continue
            archive.write(path, path.relative_to(staging).as_posix(), compress_type=zipfile.ZIP_DEFLATED)
    shutil.rmtree(staging)
    return output


def validate_epub_tree(staging: Path) -> None:
    xml_suffixes = {".xml", ".xhtml", ".opf", ".ncx"}
    for path in staging.rglob("*"):
        if path.suffix in xml_suffixes:
            ElementTree.parse(path)


def validate_epub_archive(path: Path) -> None:
    if path.stat().st_size > EPUB_MAX_FILE_SIZE:
        raise ValueError(
            f"EPUB is unexpectedly large: {path.stat().st_size / 1024 / 1024:.1f} MiB "
            f"(limit: {EPUB_MAX_FILE_SIZE / 1024 / 1024:.0f} MiB)"
        )
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        expected_images = {
            f"OEBPS/images/{epub_image_name(COVER.name)}",
            *(
                f"OEBPS/images/{epub_image_name(image_name)}"
                for image_name, _alt in ILLUSTRATIONS.values()
            ),
        }
        missing_images = expected_images.difference(names)
        if missing_images:
            raise ValueError(
                "Missing EPUB images:\n" + "\n".join(sorted(missing_images))
            )
        unexpected_pngs = [
            name
            for name in names
            if name.startswith("OEBPS/images/") and name.endswith(".png")
        ]
        if unexpected_pngs:
            raise ValueError(
                "Unoptimized PNG images found in EPUB:\n"
                + "\n".join(sorted(unexpected_pngs))
            )
        if not names or names[0] != "mimetype":
            raise ValueError("EPUB mimetype is not the first archive entry")
        if archive.read("mimetype") != b"application/epub+zip":
            raise ValueError("Invalid EPUB mimetype")
        if archive.getinfo("mimetype").compress_type != zipfile.ZIP_STORED:
            raise ValueError("EPUB mimetype must be stored without compression")
        for name in names:
            if Path(name).suffix in {".xml", ".xhtml", ".opf", ".ncx"}:
                ElementTree.fromstring(archive.read(name))


def validate_inputs() -> None:
    missing = [str(ROOT / name) for name in MANUSCRIPT_FILES if not (ROOT / name).exists()]
    missing += [str(COVER_ART)] if not COVER_ART.exists() else []
    for image_name, _alt in ILLUSTRATIONS.values():
        if not (IMAGES / image_name).exists():
            missing.append(str(IMAGES / image_name))
    if missing:
        raise FileNotFoundError("Missing publication inputs:\n" + "\n".join(missing))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--front-preview", action="store_true", help="Build only cover and front matter PDF")
    parser.add_argument(
        "--review-pdf",
        action="store_true",
        help="Build a separate illustrated review PDF without replacing the final PDF",
    )
    parser.add_argument("--pdf", action="store_true", help="Build the full PDF")
    parser.add_argument("--epub", action="store_true", help="Build the full EPUB")
    parser.add_argument("--all", action="store_true", help="Build both final formats")
    args = parser.parse_args()

    validate_inputs()
    if not any([args.front_preview, args.review_pdf, args.pdf, args.epub, args.all]):
        parser.error("Choose --front-preview, --review-pdf, --pdf, --epub, or --all")

    built: list[Path] = []
    if args.front_preview:
        built.append(build_pdf(FRONT_PREVIEW, front_only=True))
    if args.review_pdf:
        built.append(build_pdf(REVIEW_PDF))
    if args.pdf or args.all:
        built.append(build_pdf(FINAL_PDF))
    if args.epub or args.all:
        epub = build_epub(FINAL_EPUB)
        validate_epub_archive(epub)
        built.append(epub)

    for path in built:
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
