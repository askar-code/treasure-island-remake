# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A Russian-language creative writing project: a chapter-by-chapter remake of Stevenson's `Остров сокровищ` (Treasure Island) reimagined through the lens of Salinger's `Над пропастью во ржи` (Catcher in the Rye). Setting is moved from 18th-century England to early-1950s United States. There is no code — only Markdown drafts and planning documents. All prose and discussion happens in Russian.

## Three load-bearing documents

Read these before touching any chapter — most creative decisions live here, not in the chapters themselves:

1. `writing-plan.md` — the live status document. Holds the production rules, the "Уже сделано" / "Принятые сюжетные решения" log, and the per-chapter status table. **Update this file** whenever a chapter status changes or a new plot decision is committed.
2. `remake-goal-catcher-rye.md` — the canonical mapping doc: time, places, characters, objects, voice rules, thematic constraints. This is the source of truth for *how* to translate any element from the original into the remake.
3. `treasure-island-plot-by-chapter.md` — chapter-by-chapter plot summary of the original. Used as the event-mechanics skeleton: each remake chapter must perform the same plot function as the matching original chapter.

When these conflict, `writing-plan.md` (most recent decisions) wins over `remake-goal-catcher-rye.md` (general rules) wins over `treasure-island-plot-by-chapter.md` (raw original plot).

## Structural rules (do not violate without asking)

- **34-to-34 mapping.** The remake has exactly 34 chapters, one per original chapter, in order. Each chapter file is named `chapter-NN-draft.md`.
- **Length is not a target.** Reference is ~3000–3500 words, but cut if cutting helps and expand to 6000 if the chapter genuinely needs it. Never pad to hit a number. Only add a scene, action, conflict, object, or voice beat if the chapter actually needs it.
- **Strip explanatory tails.** If a sentence only restates the effect of the sentence before it, delete it. Dialogue stays short and does not circle the same point.
- **Voice = Jim, age 16–17.** First person, simple teenage vocabulary, no literary flourishes. Sarcasm, shame, anger, resentment are the main register. Mild profanity (`жопа`, `хрен`, `посрать`, `черт`) is allowed but rare — only when the sentence is genuinely fake without it.
- **Plot function preserved, surface translated.** Each remake chapter performs the same plot function as the matching original chapter, but voice, objects, social setting, and details are recast into the 1950s-US remake setting per `remake-goal-catcher-rye.md`.

## Working on a chapter

- Drafts live in `chapter-NN-draft.md` at the repo root. Treat the file's existence as "draft exists" — current status (rewritten for voice / explanatory tails cleaned / etc.) is in the table at the bottom of `writing-plan.md`.
- Before editing or writing a chapter, re-read: (a) the matching chapter section in `treasure-island-plot-by-chapter.md`, (b) the relevant character/object/place entries in `remake-goal-catcher-rye.md`, and (c) the "Принятые сюжетные решения" section of `writing-plan.md` for committed deviations from the mapping doc (e.g. treasure relocated from Maine coast to the Caribbean, with origin tied to post-war Nazi-extracted goods).
- After finishing or revising a chapter, update the status row in `writing-plan.md`. If a new plot decision was made, add a bullet to "Принятые сюжетные решения" — that's how future sessions learn it happened.

## What there is not

No build system, no tests, no lint, no package manager, no CI. The only ignored file is `.DS_Store`. Drafts are committed directly to `main`.
