# Иллюстрации: карта, аудит и точные промпты

Этот файл хранит воспроизводимую историю книжных изображений. Для каждого принятого или рассматриваемого кадра фиксируются сцена, исходный вызов генерации, цепочка правок, итоговый файл и редакторский статус.

Тексты в блоках `prompt` ниже — сохранённые итоговые `revised_prompt` из журнала генерации, а не пересказ задним числом.

## Рабочий договор

- Визуальная непрерывность персонажей определяется `../materials/visual-character-bible.md`.
- У каждого повторяющегося крупным планом персонажа должен быть утверждённый графический якорь. Текстовое описание само по себе не гарантирует одинаковое лицо.
- Новый промпт и все последующие правки сохраняются здесь вместе с идентификаторами исходных изображений.
- После каждой генерации отдельно проверяются: состав людей, возраст, лица, сторона протеза или ранения, число тростей и оружия, руки, одежда, эпоха, физический масштаб, свет и отсутствие случайного текста.
- Изображение не попадает в PDF или EPUB только потому, что оно красиво. Статус `принято` ставится после смыслового и визуального аудита.
- Обложка считается отдельным изображением. Авторский просмотр охватывал двадцать пять внутренних кандидатов; в итоговую читательскую сборку вошли двадцать две внутренние иллюстрации плюс обложка.

## Итоговый отбор: двадцать две внутренние иллюстрации

Все двадцать пять кандидатов прошли общий авторский просмотр. Файлы трёх исключённых кадров к главам 23, 29 и 33 удалены из рабочего набора; их промпты и идентификаторы сохранены ниже как история решений. Остальные двадцать два файла используются сборщиком PDF и EPUB.

| № | Глава | Итоговый файл | Сцена | Статус |
|---:|---:|---|---|---|
| 1 | 1 | `images/illustration-ch01-billy-bones-arrival.png` | Приход Билли Бонса к двухэтажному `Адмиралу Бенбоу` | В книге; исправлены мотель, стулья и вывеска |
| 2 | 3 | `images/illustration-ch03-blind-visitor.png` | Слепой хватает Джима за запястье | В книге; полностью пересобрана анатомия хвата |
| 3 | 4 | `images/illustration-ch04-motel-coins.png` | Мать и Джим считают долг до цента | В книге |
| 4 | 6 | `images/illustration-ch06-trelawney-map.png` | Карта и бумаги в кабинете Трелони | В книге; фигура Трелони исправлена |
| 5 | 7 | `images/illustration-ch07-boston-harbor.png` | `Испаньола` в зимнем Бостоне | В книге |
| 6 | 8 | `images/illustration-ch08-silver-meets-jim.png` | Первое рукопожатие Джима и Сильвера | В книге; основной якорь Сильвера, фартук исправлен |
| 7 | 9 | `images/illustration-ch09-smollett-cabin.png` | Предупреждение Смоллетта в каюте | В книге; три пальца и фигура Трелони исправлены |
| 8 | 11 | `images/illustration-ch11-apple-barrel.png` | Разговор у яблочной бочки | В книге; высокая бочка и исторический правый протез |
| 9 | 13 | `images/illustration-ch13-island-resort.png` | Первый вид заброшенного курорта | В книге |
| 10 | 14 | `images/illustration-ch14-silver-and-tom.png` | Сильвер уговаривает Тома у ржавой трубы | В книге; момент до убийства |
| 11 | 15 | `images/illustration-ch15-ben-gunn.png` | Первая встреча с Беном Ганном | В книге; основной якорь Бена |
| 12 | 17 | `images/illustration-ch17-overloaded-dinghy.png` | Последний рейс перегруженного тузика | В книге |
| 13 | 18 | `images/illustration-ch18-raising-the-flag.png` | Смоллетт поднимает флаг | В книге |
| 14 | 20 | `images/illustration-ch20-silver-smollett-parley.png` | Переговоры Сильвера и Смоллетта | В книге; лицо Сильвера возвращено к основному якорю |
| 15 | 21 | `images/illustration-ch21-waiting-before-assault.png` | Тихий час перед штурмом | В книге; отдельный платок, чистая рубашка Трелони и целый Редрут |
| 16 | 22 | `images/illustration-ch22-ben-launches-coracle.png` | Бен спускает корытце для Джима | В книге |
| 17 | 23 | `images/illustration-ch23-coracle.png` | Джим режет манильский канат | Исключено на авторском просмотре; файл удалён |
| 18 | 24 | `images/illustration-ch24-anchor-chain.png` | Джим карабкается по якорной цепи | В книге; возвращены ботинки и светлая рубаха |
| 19 | 26 | `images/illustration-ch26-jim-and-hands.png` | Джим и Израэль Хэндс на `Испаньоле` | В книге |
| 20 | 28 | `images/illustration-ch28-silver-protects-jim.png` | Сильвер объявляет Джима своим | В книге; исправлены живая нога и снятый протез |
| 21 | 29 | `images/illustration-ch29-black-mark.png` | Чёрная метка Сильверу | Исключено: Бобби слишком похож на Джима; файл удалён |
| 22 | 30 | `images/illustration-ch30-livesey-treats-jim.png` | Ливси перевязывает Джима | В книге |
| 23 | 32 | `images/illustration-ch32-flints-voice.png` | Голос Флинта у театра | В книге; пять людей и небольшая ручная яма |
| 24 | 33 | `images/illustration-ch33-empty-cache.png` | Пустой тайник | Исключено: Бобби снова похож на Джима; файл удалён |
| 25 | 34 | `images/illustration-ch34-homecoming-hands.png` | Возвращение: мать просит показать руки | В книге |

## Аудит ранних файлов

Ниже сохранена история первой шестикартинной сборки и промежуточных замен. Эти имена больше не относятся к текущему рабочему набору: сами ранние файлы удалены при издательской уборке, а промпты, идентификаторы генераций и контрольные суммы оставлены для воспроизводимости решений.

| Файл | Источник | Вердикт | Что проверить или исправить |
|---|---|---|---|
| `images/cover-art.png` | `exec-af0073c7-ea3a-4c98-a6a8-e96846553c0a` | Исправленный кандидат готов | `exec-eda4a3ca-1c71-496d-898b-dc156ea26331`: одна трость, правая сторона протеза, тёмная кепка; рабочий файл не подменять до авторского просмотра листа сравнения. |
| `images/cover.png` | Типографика поверх `cover-art.png` | Пересобрать после правки | Текст и композиция обложки сохраняются. |
| `images/illustration-01-motel-coins.png` | `exec-5f27755d-34f5-49ed-8519-aea789997703` | Принято | Использовать как якорь матери и дополнительный якорь шестнадцатилетнего Джима. |
| `images/illustration-02-boston-harbor.png` | `exec-921a92ee-c8d8-4049-8263-8560157e6745` | Принято | Лицо Джима неразличимо; персонажной коллизии нет. |
| `images/illustration-03-island-resort.png` | `exec-8926a921-f164-4140-b393-5ae0e0676c0d` | Принято | Джим со спины; сохранить его силуэт, волосы и одежду в близких сценах. |
| `images/illustration-04-siege.png` | `exec-488c8c69-fc53-4ab1-ba19-5f29a7a12a5a` | Исправленный кандидат готов | `images/illustration-04-siege-candidate.png` (`exec-4801a4d5-bbb3-49e9-8981-729ad6a88375`): тихий час до первого выстрела; Трелони протирает патрон отдельным платком, винтовка лежит рядом; целый Редрут у шести кружек и жестяного кофейника, Джим сортирует боеприпасы. Рабочий файл не подменять до авторского подтверждения. |
| `images/illustration-05-coracle.png` | `exec-52314481-e301-4794-b845-3d91137f1789` | Исправленный кандидат готов | `exec-6e766360-be25-4742-a5ed-2e77bb61cfdb`: бинт только на правой руке с ножом; левая рука голая и держит канат. |
| `images/illustration-06-empty-pit.png` | `exec-92588dc4-a972-4708-9dff-0ebe54875c60` | Отвергнуто | Старую концепцию с гигантской ямой и символическими предметами не использовать и удалить из сборки после замены. |
| `images/illustration-15-empty-cache.png` | `exec-25343a7a-733e-48a2-b252-a856fde8512e` | Исправленный кандидат готов | `exec-f9ca0ab1-e981-4e2b-a47e-770d33329ba9`: масштаб ямы и пять людей сохранены; Сильвер в кепке, правый протез рядом с одной палкой; Бобби, Винс и Андерсон разведены по паспорту. |

## Обложка

### Исходное изображение

- Итоговый файл: `images/cover-art.png`
- Вызов: `exec-af0073c7-ea3a-4c98-a6a8-e96846553c0a`
- SHA-256: `a5c4cddc5578944cc3019c4076367ec0cd4fbeb054e32cf984a81b7f7de9533c`
- Статус: композиция и живопись приняты; дальнюю фигуру Сильвера исправить.

```prompt
Use case: historical-scene
Asset type: text-free front-cover artwork for a literary novel, portrait 2:3 composition
Primary request: a haunting, restrained cover image for a Russian literary reimagining of Treasure Island set in 1952–1953 America and the Caribbean
Scene/backdrop: a wet winter highway beside a small run-down New England roadside motel at dusk; the road recedes toward darkness and subtly transforms in atmosphere into a black-green tropical sea near the horizon, suggesting the whole journey without a literal collage
Subject: a sixteen-year-old boy seen from behind in a worn jacket, standing under the motel office light and watching the road; far away, only as a small ambiguous silhouette, a tall one-legged sailor with a cane; no close-up face
Style/medium: sophisticated hand-painted mid-century book-jacket illustration, dry brush and screenprint texture, literary rather than pulp, period-authentic 1950s visual language
Composition/framing: strong vertical cover composition, boy in lower third, road as leading line, generous calm negative space in upper third for later typography; no border
Lighting/mood: cold motel light, wet asphalt reflections, restrained menace, loneliness, distrust, no adventure glamour
Color palette: petrol blue, charcoal, tobacco brown, muted rust, one sickly tropical green accent
Constraints: historically plausible 1952 details; no modern cars, clothes, signs, technology or road markings; no treasure chest, skull, pirate hat, tropical postcard clichés, parrots, maps, coins, weapons, logos, watermark, letters or any text; do not romanticize the one-legged man; no photorealism, no cartoon look
```

## Иллюстрация 2: мать и Джим считают долг

- Итоговый файл: `images/illustration-01-motel-coins.png`
- Вызов: `exec-5f27755d-34f5-49ed-8519-aea789997703`
- SHA-256: `89175e6fec441bbb5a70f3fa097472be1941f7bea8a13d4051fcd183c90dff36`
- Статус: принято.

```prompt
Use case: historical-scene
Asset type: text-free interior book illustration, landscape 3:2
Input images: Image 1 is a style reference only; do not copy its composition
Primary request: illustrate the emotional center of the early chapters of the same 1952 literary novel
Scene/backdrop: the wrecked bar and office of a small New England roadside motel at night in winter, broken window patched badly, overturned furniture, cold darkness outside
Subject: a worn middle-aged mother and her sixteen-year-old son at a scarred table, counting scattered coins by one desk lamp; the mother is exact and controlled, the boy exhausted and watchful; show them in three-quarter view but do not make faces portrait-specific
Style/medium: match Image 1's sophisticated mid-century hand-painted book-jacket language, dry brush and screenprint grain; restrained literary realism, slightly simplified shapes
Composition/framing: horizontal full-width book plate, table and hands central, broken motel room receding behind them, clear silhouette and generous dark margins
Lighting/mood: one warm lamp against winter blackness; grief expressed through work and objects, not melodrama
Color palette: near-monochrome charcoal and tobacco brown with muted rust and cold petrol-blue shadows
Constraints: historically plausible 1952 clothing, coins, lamp and motel furnishings; no modern objects; no pirate costumes, ships, treasure chest, map, skull, guns, glamour, text, letters, logos or watermark
```

## Иллюстрация 4: `Испаньола` в Бостоне

### Первичная генерация

- Вызов: `exec-0abaab4f-f9be-44fa-a429-e280bed5d107`

```prompt
Use case: historical-scene
Asset type: text-free interior book illustration, landscape 3:2
Input images: Image 1 is a style reference only; do not copy its composition
Primary request: illustrate the departure phase of the same 1952 literary novel
Scene/backdrop: a cold working harbor in Boston in winter 1952, weathered warehouses, cranes and dock equipment appropriate to the period
Subject: a sixteen-year-old boy with one small bag stands on the pier looking up at a sturdy two-masted auxiliary schooner being refitted; working crew on deck, practical rigging, no luxury-yacht polish
Style/medium: match Image 1's sophisticated mid-century hand-painted book-jacket language, dry brush and screenprint grain; literary realism
Composition/framing: horizontal full-width book plate, boy small in foreground, hull and masts rising across frame, deep harbor perspective
Lighting/mood: pale winter morning, apprehension mixed with the first possibility of escape, not triumphant adventure
Color palette: charcoal, cold petrol blue, weathered cream, tobacco brown, restrained rust
Constraints: historically plausible 1952 harbor, clothing, vehicles, rigging and auxiliary schooner; no modern container cranes, modern yachts, plastic, modern safety gear or skyscrapers; no pirate flags, treasure imagery, tropical clichés, readable ship name, text, letters, logos or watermark
```

### Принятая световая правка

- Итоговый файл: `images/illustration-02-boston-harbor.png`
- Вызов: `exec-921a92ee-c8d8-4049-8263-8560157e6745`
- SHA-256: `0532559b47338319ae02ced589f0e2ab92a6c0f1249072a67a021d496383c235`

```prompt
Use case: lighting-weather
Asset type: corrected interior book illustration
Input images: Image 1 is the edit target
Primary request: change the Boston harbor scene from gloomy overcast to a clear, cold, bright winter morning that carries a real sense of departure and possibility
Precise edit: pale clean blue sky with thin high clouds, low winter sunlight striking the schooner's masts, rigging and weathered cream surfaces; brighter steel-blue harbor water with crisp reflections; snow and wet dock catch light; boy and working crew remain fully readable; retain ordinary working-harbor grit without making the scene dark
Mood: apprehension and first escape, a wide world opening, restrained hope rather than triumph or doom
Invariants: preserve exact composition, boy's pose and bag, two-masted auxiliary schooner, all workers, dock, warehouses, cranes, period details and dry-brush mid-century illustration texture
Constraints: no sunset, no storm, no tropical light, no modern port equipment, no luxury-yacht polish, no extra people, no readable ship name, text, logos or watermark
```

## Иллюстрация 7: островной курорт

### Первичная генерация

- Вызов: `exec-bfe9a892-092e-46b6-a546-aa7f134aadc6`

```prompt
Use case: historical-scene
Asset type: text-free interior book illustration, landscape 3:2
Input images: Image 1 is a style reference only; do not copy its composition
Primary request: illustrate the first sight of the island in the same 1953 literary novel
Scene/backdrop: an abandoned prewar Caribbean resort project swallowed by mangroves and heat: raw concrete hotel shell, broken mesh fence, rusted pump pipe, empty service yard and black-green tidal water
Subject: a sixteen-year-old boy, small and partly hidden, moving alone through tall wet grass toward the concrete ruins; no heroic pose
Style/medium: match Image 1's sophisticated mid-century hand-painted book-jacket language, dry brush and screenprint grain; restrained literary realism
Composition/framing: horizontal full-width book plate, oppressive concrete geometry against dense vegetation, figure dwarfed by place, layered depth
Lighting/mood: noon glare filtered into sickly green shadow, humidity, insects, abandoned labor, threat without visible attacker
Color palette: black-green, concrete gray, tarnished ochre, petrol-blue shadow, a small rust accent
Constraints: plausible early-1940s unfinished resort infrastructure as seen in 1953; no modern resort, no picturesque beach, treasure chest, skull, pirate costume, map, parrot, readable signage, text, letters, logos or watermark
```

### Принятая световая правка

- Итоговый файл: `images/illustration-03-island-resort.png`
- Вызов: `exec-8926a921-f164-4140-b393-5ae0e0676c0d`
- SHA-256: `e8c0c14bcaec695a9f6f0737f54e805017a9875047a6106f4ae69a43c814b6d9`

```prompt
Use case: lighting-weather
Asset type: corrected interior book illustration
Input images: Image 1 is the edit target
Primary request: change the lighting and color atmosphere from dark overcast gloom to harsh brilliant Caribbean midday sun
Precise edit: open the sky to intense pale tropical blue with high white glare; flood the raw concrete ruins, rusted pump and wet vegetation with strong direct sunlight and crisp broken shadows; make the shallow tidal water visibly sparkle blue-green; lift the foreground enough that the boy, wire mesh and grass remain clearly readable; use sun-bleached concrete, vivid but natural humid greens and turquoise reflected light
Mood: beauty and danger existing at the same time, oppressive heat rather than storm darkness
Invariants: preserve the exact composition, boy's pose and identity, all buildings, fence, pump, water, vegetation, period detail and painterly dry-brush texture
Constraints: no sunset, no storm clouds, no fantasy saturation, no modern resort, no extra people, text, logos or watermark
```

## Иллюстрация 11: ожидание штурма

### Первичная генерация

- Вызов: `exec-e1422e8a-aba8-4b6a-bb71-88fcbab90100`

```prompt
Use case: historical-scene
Asset type: text-free interior book illustration, landscape 3:2
Input images: Image 1 is a style reference only; do not copy its composition
Primary request: illustrate the siege phase of the same 1953 literary novel
Scene/backdrop: the service office and yard of an unfinished Caribbean resort, low raw-concrete walls, rusted wire mesh, improvised firing apertures, water trough, mangroves beyond
Subject: a tense small group defending the concrete enclosure: a sixteen-year-old boy crouches low passing ammunition, one older man watches through the mesh with a rifle, another wounded figure remains in shadow; figures practical and exhausted, no heroic poses
Style/medium: match Image 1's sophisticated mid-century hand-painted book-jacket language, dry brush and screenprint grain; restrained literary realism
Composition/framing: horizontal full-width book plate viewed from inside the dim enclosure toward blinding exterior heat; concrete geometry and hands doing work are more important than faces
Lighting/mood: hard tropical noon outside, deep cool shadow inside, waiting before violence, flies and heat implied
Color palette: concrete gray, black-green, tobacco brown, muted rust, petrol-blue shadow
Constraints: plausible 1953 clothes, rifles and unfinished resort infrastructure; no graphic wounds, no action-movie muzzle flashes, no pirate costume, no fort palisade, no modern tactical gear, treasure imagery, readable signage, text, letters, logos or watermark
```

### Исправление боеприпасов

- Вызов: `exec-76ae0227-5ca5-49b5-a519-868645eae84f`

```prompt
Use case: precise-object-edit
Asset type: corrected interior book illustration
Input images: Image 1 is the edit target
Primary request: change only the ammunition in the crouching teenage boy's hands
Precise edit: remove the flexible linked machine-gun ammunition belt entirely. Replace it with two or three small rigid 1950s rifle cartridge clips in his hands, plus a few ordinary loose brass rifle cartridges sorted in small separate piles on the concrete floor beside him. The rifle clips must look rigid and compact, not like a belt, chain, bandolier, or modern magazine.
Invariants: preserve the boy's identity, pose, hands as naturally as possible, all other people, rifles, room, wire mesh, concrete, composition, lighting, palette, brush texture, period atmosphere and every other object unchanged
Constraints: no machine-gun belt, no linked ammunition, no modern detachable box magazine, no extra weapons, no text, no logo, no watermark
```

### Светлый промежуточный вариант

- Вызов: `exec-f4203dfe-5cfd-4746-9472-21564c860d4e`

```prompt
Use case: lighting-weather
Asset type: corrected interior book illustration
Input images: Image 1 is the edit target
Primary request: make this daytime Caribbean siege illustration substantially brighter and sun-struck while preserving its tension
Precise edit: harsh near-white tropical noon pours through both large openings and bounces off pale raw concrete, lifting the entire interior exposure; outside sky is clear blue, palms and distant water are vivid in heat haze; keep readable shadow under the roof but show the boy, loose cartridges, small rigid clips, wounded figure, rifleman and concrete surfaces clearly; light shirts should appear sun-bleached
Mood: waiting for violence in unbearable heat, not a dark bunker or storm
Invariants: preserve the exact composition, all three people, poses, loose cartridges and rigid clips, rifles, mesh fence, concrete geometry and painterly dry-brush texture
Constraints: no machine-gun belt or linked ammunition, no muzzle flash, no modern gear, no extra figures, text, logos or watermark
```

### Принятый средний свет

- Итоговый файл: `images/illustration-04-siege.png`
- Вызов: `exec-488c8c69-fc53-4ab1-ba19-5f29a7a12a5a`
- SHA-256: `62c6cf5d8be3ead4874ab11d5889bd7574bb667da129b5c828a2e2f35cbfd5e2`

```prompt
Image 1 is the edit target and must control composition, people, objects, anatomy, architecture, and narrative detail. Image 2 is only a reference for the brighter tropical exterior and improved legibility.

Edit Image 1 with a middle lighting treatment between the two references:
- Keep the siege room unmistakably cool, dim, oppressive, and shadowed inside the unfinished concrete shelter.
- Lift the interior bounced daylight by about 35–40 percent compared with Image 1, so all three men's faces, white shirts, the ammunition boxes, loose cartridges and rigid clips are clearly readable in print.
- Do not make the interior pale, sunny, beige, uniformly bright, washed out, or cheerful as in Image 2. Deep shadows must remain in the corners, behind the wounded man, beneath the window ledges, and around the foreground.
- Preserve a strong cinematic exposure contrast: outside is blazing tropical noon with blue sky, bright turquoise water, white glare, and sunlit palms; inside remains several stops darker and cooler.
- The rifleman and Jim should have narrow warm rim light and reflected daylight, while their shadow sides remain substantial.
- Concrete walls should be dark charcoal/cool gray in shadow, not near-black and not cream.
- Keep exactly the original composition and every narrative object from Image 1. Keep loose cartridges and rigid ammunition clips only; absolutely no flexible machine-gun belt.
- No text or lettering. Realistic painterly 1930s adventure-book illustration, horizontal 3:2.

The emotional result should be: brilliant island day visible just outside, exhausted defenders trapped in a hard, airless half-darkness within.
```

## Иллюстрация 12: корытце у борта `Испаньолы`

- Итоговый файл: `images/illustration-05-coracle.png`
- Вызов: `exec-52314481-e301-4794-b845-3d91137f1789`
- SHA-256: `190262f06ef8921689e2374da90dea662ced6e9530fc6a32884eaff13c5a967e`
- Статус: композиция и свет приняты; физику рук исправить по главе 23.

```prompt
Use case: historical-scene
Asset type: text-free interior book illustration, landscape 3:2
Input images: Image 1 is a style reference only; do not copy its composition
Primary request: illustrate the nighttime sea ordeal in the same 1953 literary novel
Scene/backdrop: black tropical water at night just outside a reef, low swell, no moonlit postcard beauty
Subject: a sixteen-year-old boy alone in a tiny awkward tarred homemade coracle, close beside the towering dark hull of a practical two-masted auxiliary schooner; he cuts the last three hemp strands of a thick anchor cable with a small knife, his hands wrapped in dirty cloth
Style/medium: match Image 1's sophisticated mid-century hand-painted book-jacket language, dry brush and screenprint grain; restrained literary realism
Composition/framing: horizontal full-width plate, very low waterline viewpoint, tiny bowl-like boat and boy dwarfed by black hull; cable and three remaining strands clearly readable as physical action
Lighting/mood: one weak yellow cabin light high on the schooner, wet black surfaces, exhaustion and danger, no swashbuckling
Color palette: near-black petrol blue, charcoal, tarnished ochre light, muted rust
Constraints: physically plausible small coracle and 1950s auxiliary schooner; no galleon, pirate flag, heroic sword pose, treasure imagery, shark, storm spectacle, modern boat hardware, text, letters, logos or watermark
```

## Отвергнутая старая яма

Эта цепочка сохранена только как отрицательная история. Её нельзя использовать как основу новой сцены.

### Исходная символическая композиция

- Вызов: `exec-c4e1e37b-9c93-4a8d-9a8d-54eaf1eae44e`

```prompt
Use case: historical-scene
Asset type: text-free interior book illustration, landscape 3:2
Input images: Image 1 is a style reference only; do not copy its composition
Primary request: illustrate the late revelation of the same 1953 literary novel without showing treasure
Scene/backdrop: a humid overgrown Caribbean hillside with an old excavation pit in hard earth, abandoned wartime traces and dense vegetation closing around it
Subject: in the sharp foreground lie a rusted loop of wire, a small tarnished numbered brass tag, and intact metal-framed eyeglasses clouded by corrosion; beyond them the pit is unmistakably empty; several exhausted figures stand small and separated at its rim, including the silhouette of a tall one-legged man with a cane, but no one poses heroically
Style/medium: match Image 1's sophisticated mid-century hand-painted book-jacket language, dry brush and screenprint grain; restrained literary realism
Composition/framing: horizontal full-width plate, objects in foreground carry the meaning, empty pit in middle distance, people secondary and unreadable as portraits
Lighting/mood: late hard afternoon after rain, tarnished green light, anticlimax, suspicion, moral residue rather than victory
Color palette: black-green, damp earth brown, oxidized brass, charcoal, muted rust, small pale sky opening
Constraints: no treasure chest, coins, jewels, map, skull-and-crossbones, pirate costume, celebratory pose, modern objects, graphic corpse detail, readable numbers, text, letters, logos or watermark
```

### Световая правка

- Вызов: `exec-4d9c20e8-526e-4e7b-9069-31625ab65a18`

```prompt
Use case: lighting-weather
Asset type: corrected interior book illustration
Input images: Image 1 is the edit target
Primary request: change the empty-pit scene from storm-dark to bright late-afternoon Caribbean sunlight
Precise edit: clear most of the heavy clouds into a luminous blue tropical sky; strong warm sun strikes the wet earth, rusted wire, brass tag and glasses so every foreground object is easy to read; surrounding foliage should be vivid humid green with sunlit edges; figures at the rim remain small and separated but clearly silhouetted in light; the empty pit stays visually central
Mood: anticlimax and moral residue under almost offensively beautiful weather, not horror-movie gloom
Invariants: preserve composition, exact foreground objects, empty pit, number and placement of distant figures including the one-legged silhouette, vegetation, perspective and painterly dry-brush texture
Constraints: no treasure, coins, chest, graphic remains, sunset orange cast, storm, extra figures, text, logos or watermark
```

### Неудачная попытка уменьшить яму

- Итоговый отвергнутый файл: `images/illustration-06-empty-pit.png`
- Вызов: `exec-92588dc4-a972-4708-9dff-0ebe54875c60`
- SHA-256: `708d628ff88220ee9b7be426a43f98ef33c822f7cc71a84c4c881ce70a23e825`

```prompt
Edit the provided landscape illustration. This is a precise geometry-and-scale correction, not a new composition.

Keep unchanged:
- the same wide 3:2 landscape framing, camera height, luminous tropical midday sunlight, blue sky, clouds, lush island vegetation, realistic painterly book-illustration style and warm/cool palette;
- the foreground still life exactly recognizable: the coil of old wire, round brass tag, and broken round spectacles on damp earth;
- the same small group of men around the excavation, their 1930s clothing, poses and relative placement, including the tall one-legged man with a cane;
- no text, no lettering, no treasure, no chest, no heavy machinery.

Change only the excavation:
- Replace the enormous crater/quarry with a compact rectangular cache pit that was clearly dug by hand with ordinary shovels in part of one day.
- Real-world dimensions should read as about 2.5 metres long, 1.8 metres wide, and 1.3 metres deep: just large enough for two adult men to stand inside chest-deep and for several wooden crates to have once fitted.
- Give it fairly straight shovel-cut earthen sides and a mostly flat bottom, with one faint straight rectangular crate impression in a corner.
- Put only a modest mound of freshly dug soil around the rim, consistent with this small volume.
- The pit must occupy only a small central part of the clearing, not span the whole image. It must not resemble a bomb crater, quarry, house foundation, archaeological trench, swimming pool, or excavator work.
- Preserve generous intact ground and vegetation around it. Keep the men close enough to establish scale: the pit is roughly the length of one and a half standing men, not a landscape-scale excavation.

Narrative mood: glaring tropical brightness over the bitter discovery of an already emptied, hand-dug cache.
```

## Иллюстрация 15: новая пустая яма

### Полностью новая композиция

- Вызов: `exec-1825387e-9f1c-4450-a19d-7d8bd9d500be`

```prompt
Create a completely new illustration from scratch. Do not imitate or preserve any previous pit image.

A horizontal 3:2 realistic painterly illustration for a serious literary adventure novel set in the early 1950s Caribbean. Late afternoon on a bright tropical island, warm lowering sunlight, hard blue sky still visible, lush vegetation around the service yard of an abandoned unfinished concrete outdoor theatre. The emotional moment is not discovery of treasure but the sick realization that the cache was emptied years ago.

Composition: medium-wide three-quarter view from slightly above the rim, close enough to read the people and the pit clearly. At the center is one compact rectangular hand-dug cache hole, approximately 2.5 metres long, 1.8 metres wide and 1.3 metres deep. Straight shovel-cut earthen walls, flat bottom, modest spoil piles, absolutely not a crater, quarry, construction foundation or archaeological trench.

Inside the small pit stand two exhausted adult working men chest-deep in red-brown soil. Bobby has frozen after saying it is empty. Vince, muddy and disbelieving, is on his knees feeling along one bottom corner where a clean rectangular pressure mark shows that wooden crates once stood there. Between them are only three remnants: a half-rotten plank, a torn piece of black tarred canvas, and another broken board with a faded partial military shipping stencil; the lettering may be fragmentary and indistinct, never decorative. There is no treasure, chest, gold, coins, jewels or intact crate.

At the rim stands Long John Silver, a heavy powerful forty-eight-year-old man with one leg and a practical early prosthesis, leaning on a plain wooden cane. His fingers are white around the cane but his face is controlled. Beside him stands Jim Hawkins, a lean sixteen-year-old boy with bandaged, damaged hands, dusty white shirt and dark trousers. A short eight-foot line is tied loosely around Jim's belt and ends in Silver's fist. Two other tired men remain farther back near empty metal water cans and ordinary shovels. Behind them rises the stained unfinished concrete theatre wall with a black service doorway.

Make the human scale unmistakable: the pit is only about one and a half standing men long, and two men inside fill most of it. Show intact ground close around all four sides. No foreground still life, no giant glasses, no brass tag, no wire coil, no skeleton, no excavator, no machinery.

Lighting and mood: beautiful warm island light over a bitter, dangerous discovery; readable faces, dusty sweat, red earth, long shadows. Historically plausible 1950s work clothes and tools. Natural anatomy, restrained expressions, cinematic but not glossy, rich painterly brush texture, no captions, no typography, no border.
```

### Исправление состава и травм

- Текущий файл: `images/illustration-15-empty-cache.png`
- Вызов: `exec-25343a7a-733e-48a2-b252-a856fde8512e`
- SHA-256: `b5f9c895db8ffa41568eba6f4f57a948a6cea7e0e4716d8e6ab165d3d4cc7a5d`
- Статус: композиция принята; внешность Сильвера, Бобби, Винса и Андерсона исправить после утверждения визуальных замков.

```prompt
Make a precise continuity correction to the provided illustration. Preserve the camera, compact hand-dug rectangular pit, the two muddy men inside it, Long John Silver, Jim with bandaged hands and short waist line, late-afternoon tropical lighting, abandoned concrete theatre, soil, boards, canvas and painterly style.

There must be exactly five human beings in the entire image:
1) Silver at the rim with one leg, practical prosthesis and cane;
2) sixteen-year-old Jim beside him with both hands bandaged and the rope tied at his belt;
3) Bobby inside the pit, chest-deep;
4) Vince inside the pit on his knees checking the empty crate impression;
5) Anderson alone in the background near one empty metal oil can.

Currently there are two men behind Jim near the doorway. Remove both of those background figures and replace them with only one injured Anderson. Anderson stands slightly apart beside the empty can, exhausted, one arm immobilized/held under his shirt because of a broken collarbone. He carries no shovel, no rifle and no tool. Keep ordinary shovels lying on the ground near the spoil pile instead.

Do not add any new person, silhouette, reflection or distant worker. Exactly five people total. Keep the pit realistically small and hand dug. No treasure or foreground symbolic objects. No other changes.
```

## Кандидат 1: слепой у двери мотеля

- Исходный файл генерации: `exec-58ee6f93-8b68-4ede-888d-86da22b7dd7e.png`
- Вызов: `exec-58ee6f93-8b68-4ede-888d-86da22b7dd7e`
- SHA-256: `fd6d6517a19c5eba322d2565f12c04e1bd760cd5e41f8695732547dea1971161`
- Статус: сохранить композицию и лица, заменить только трость.

```prompt
Create a brand-new horizontal 3:2 realistic painterly book illustration for a serious early-1950s adventure novel. Winter night at a shabby roadside motel on the cold New England coast. Wet sleet, black road, yellow porch lamp, warped wooden steps, wind from an unseen gray sea. A lean sixteen-year-old boy with tousled dark hair has just cracked open the motel door. A blind former sailor in a soaked dark wool coat suddenly grips the boy's wrist with a dry wire-like hand and pulls him inward. The blind man is thin, controlled and terrifying rather than monstrous; a measuring cane is tucked under his raised arm, dark glasses pushed deliberately onto his forehead, scarred empty eye area kept mostly in shadow and not shown graphically. His begging posture has vanished and his voice has become businesslike. Inside behind the boy: dim counter, staircase, steaming kettle, worn linoleum. The boy is frightened into silence because his dying father and mother are upstairs. Composition close and diagonal, the grip is the center, exterior rain behind them and warm weak interior light. Historically plausible 1950s clothing and motel details. Restrained fear, no gore, no supernatural imagery, no captions, no legible signage, no border. Rich textured brushwork matching a classic literary adventure illustration, cinematic natural light, not glossy concept art.
```

## Кандидат 3: бумаги и карта в кабинете Трелони

- Исходный файл генерации: `exec-074d9f33-df7d-4d3f-8f2c-ed17f98cccb7.png`
- Вызов: `exec-074d9f33-df7d-4d3f-8f2c-ed17f98cccb7`
- SHA-256: `ebb1b35c6dbf4f01d2fdcd425ab37e853e4f1f527a32deb9`
- Статус: содержание и мизансцена верны; стиль слишком похож на кинематографическую фотографию. Трелони ошибочно темноволосый, хотя в рукописи он седой. Нужна живописная правка: сохранить позы и предметы, но привести Джима, Ливси и Трелони к утверждённым якорям, сделать Трелони большим, седым и краснолицым.

```prompt
Create a brand-new horizontal 3:2 realistic painterly literary illustration set in early-1950s America. Night in the enormous book-lined study of a wealthy old New England house: shelves to the ceiling, dark wood, globe, model yacht under glass, black rotary telephone, shaded lamps, deep chairs, winter darkness at tall windows. On a kitchen-sized polished table lie the actual evidence from a dead sailor's folder: ordinary folded topographic map, newspaper clippings, black notebook, photographs, Spanish forms and a cream hotel-opening card. The map is mundane and worn, with one small island circled and a tiny pencil cross; do not make it a yellow pirate treasure map and do not render readable text.

A lean dark-haired sixteen-year-old boy sits only on the front edge of an oversized armchair, coat still slightly damp, staring at the two tiny pencil marks with dread rather than excitement. A trim middle-aged doctor in a sober suit has just opened the folder and watches carefully. A tall broad wealthy man in shirtsleeves leans over the map, astonished, one hand braced on the table. An elderly formal servant stands back with a tray. The emotional contrast is wealth and warm lamplight around small cheap papers that have already caused deaths. Exact 1950s objects, no modern screens, no gold, no skulls, no treasure chest, no fantasy glow, no captions, no legible typography. Horizontal 3:2, rich restrained painterly brushwork, natural anatomy, serious literary adventure-book tone.
```

## Кандидат 5: предупреждение Смоллетта

- Исходный файл генерации: `exec-d8692a8e-1360-4c64-8e0e-b8f42465031e.png`
- Вызов: `exec-d8692a8e-1360-4c64-8e0e-b8f42465031e`
- SHA-256: `404fdbe10bcf666f49c8db16a79c4598fe55c48d621a6cf00c9c01e2c9f8938e`
- Статус: живопись, лица и композиция приняты как основа; исправить жест Смоллетта с двух пальцев на три.

```prompt
Create a brand-new horizontal 3:2 realistic painterly book illustration set aboard a working two-masted schooner in Boston harbor in the early 1950s. Cold pale winter daylight enters a cramped varnished cabin through round ports; outside are masts, gray water and traces of snow. Captain Smollett, a short lean severe older seaman with close-cropped bristly gray hair, blue-shaved clean face, plain dark captain's jacket without insignia and mirror-clean boots, stands at the end of a small table. One hand rests flat on the table, the other raises three fingers as he says plainly that he dislikes the voyage, the crew and his first mate. His expression is controlled, dry, unsmiling.

Facing him: a tall broad wealthy owner flushed with offended pride, and a trim middle-aged doctor in a sober suit who listens with professional calm. At the cabin doorway, a lean sixteen-year-old dark-haired boy pretends to polish an already-clean brass handrail while eavesdropping. On the table: ship papers, coffee cups and one ring of keys, no treasure map. The cabin should feel tight and practical, with a hint of cold busy deck beyond. Historically plausible schooner, clothing and objects; no uniforms with invented medals, no pirates, no weapons display, no captions or text. Rich textured brushwork, natural faces and hands, restrained wit and tension, classic serious adventure-novel illustration, not glossy concept art.
```

## Контрольный проход после утверждения визуальных замков

Визуальные замки утверждены 10 августа 2026 года. Семь исправленных изображений проверены в полном размере и на парных листах `до / после`. Пока автор не подтвердит сами кадры, принятые рабочие PNG в `images/` не подменяются.

| Сцена | Цепочка вызовов | Выбранный кандидат | SHA-256 |
|---|---|---|---|
| Обложка | `exec-e419bb99-668e-49e3-b850-6a1466dcd8d0` → `exec-f3882dff-903b-4b57-ab1d-4b473d3f315d` → `exec-eda4a3ca-1c71-496d-898b-dc156ea26331` | `exec-eda4a3ca-1c71-496d-898b-dc156ea26331.png` | `3ccf0784fd6ccdd7cc9db147838f0bd2cd8ce20720fc4ef3d5a116013ee01d09` |
| Слепой у мотеля | `exec-06ab4c25-f44d-4f17-8337-46947261a9cf` | `exec-06ab4c25-f44d-4f17-8337-46947261a9cf.png` | `208e8df262fde43bfcef06f9d08babd24f340c4a12dc106c1ac72c48154538e6` |
| Карта в кабинете | `exec-1bd503d0-64cf-46e1-8d43-1279a6e5b8a5` → `exec-7546a0d9-b487-45dc-b22c-d26459a31164` → `exec-6ee4cc93-9df5-4656-8813-cc0af46c1115` | `exec-6ee4cc93-9df5-4656-8813-cc0af46c1115.png` | `8be13510eeea73c5c09c4420e65d76d935757ebb6bfe7b23aa854a119e497b38` |
| Три возражения Смоллетта | `exec-691ad28a-cdc4-49e9-88e0-23cc22191ed3` → `exec-2c84611d-05b6-43ce-a629-7b444145f217` → `exec-9347b908-8b81-4300-8953-2baf92ddcb2b` | `exec-9347b908-8b81-4300-8953-2baf92ddcb2b.png` | `17e14211f128b5ef43dc8b9f1eb6bc87fc281cb45383ed0a1f008266e52f7491` |
| Ожидание штурма | `exec-4bc962cf-9d14-41d7-8e61-ef64b9af436f` → `exec-4d11f368-7a56-409f-af3f-163597f5cb7c` → `exec-4801a4d5-bbb3-49e9-8981-729ad6a88375` → `exec-6ebc0004-b75c-43c1-9794-72391a8aefc9` | `images/illustration-04-siege-candidate.png` (`exec-4801a4d5-bbb3-49e9-8981-729ad6a88375.png`) | `4e61871b78843205ac2d2be9b0f2c02ed69e6a80be4a638c8f436b0ec01dfdb1` |
| Коракл у борта | `exec-6e766360-be25-4742-a5ed-2e77bb61cfdb` | `exec-6e766360-be25-4742-a5ed-2e77bb61cfdb.png` | `c27446eceb7a5bdb04db197b5f63644ca0762ef9958d3807386c7861fa08ef69` |
| Пустой тайник | `exec-7dde56c6-124a-4444-a96d-b9d1e51badc5` → `exec-50206c25-72c1-4fb5-9938-400db736ed85` → `exec-f9ca0ab1-e981-4e2b-a47e-770d33329ba9` | `exec-f9ca0ab1-e981-4e2b-a47e-770d33329ba9.png` | `f1508a56ae65d21d86995800c5976ddabf1d9836bfaec1822405c0693e08fafd` |

Промежуточный обложечный вызов `exec-f3882dff-903b-4b57-ab1d-4b473d3f315d` содержал ошибочную подсказку о стороне тела в виде со спины; его геометрию нельзя копировать в будущие промпты. В финальном вызове `exec-eda4a3ca-1c71-496d-898b-dc156ea26331` сторона исправлена: при виде со спины правая сторона Сильвера находится справа от зрителя.

### Обложка: первый промежуточный проход

- Вызов: `exec-e419bb99-668e-49e3-b850-6a1466dcd8d0`

```prompt
Use case: precise-object-edit
Asset type: corrected text-free front-cover artwork, portrait 2:3
Input images: Image 1 is the edit target and must control the entire composition
Primary request: change only the tiny distant one-legged sailor on the road so his anatomy and support are unambiguous
Precise edit: the distant sailor is Long John Silver, a tall broad forty-eight-year-old man viewed from behind. His RIGHT lower leg is a stiff early prosthesis physically attached to his body and ending in an ordinary dark shoe on the road. He holds EXACTLY ONE plain wooden walking cane in his LEFT hand. The cane is the only separate stick in the entire silhouette.
Critical geometry: show one normal left leg, one visibly stiff right prosthetic lower leg, and one single cane on the left side. The prosthetic leg must read as a leg with a shoe, not as a second cane. Remove every second cane, crutch, pole, stick, doubled shadow, reflection, or vertical line beside him that could read as another support.
Invariants: preserve the sixteen-year-old boy in the foreground, motel, highway, wet reflections, tropical-sea suggestion, sky, negative space, lighting, palette, dry-brush and screenprint texture, exact framing, and every other object unchanged. Keep Silver equally small and distant; do not enlarge him or reveal his face.
Constraints: no second cane; no pair of crutches; no modern prosthesis; no new people, vehicles, signs, text, letters, logo, or watermark.
```

### Обложка: отвергнутая промежуточная геометрия

- Вызов: `exec-f3882dff-903b-4b57-ab1d-4b473d3f315d`
- Статус: не использовать как правило перспективы; в тексте промпта перепутана сторона тела при виде со спины.

```prompt
Use case: precise-object-edit
Asset type: corrected text-free front-cover artwork, portrait 2:3
Input image: preserve it exactly except for one tiny anatomical correction to the distant man.

Primary request: make Long John Silver's RIGHT lower-leg prosthesis unmistakable while preserving his size, pose, coat, route, lighting and single cane.

Rear-view geometry:
- Silver's anatomical RIGHT leg is the leg on the VIEWER'S LEFT.
- From just below the right knee to the shoe, replace the natural muscular calf and ankle with a visibly stiff, straight, narrow early-1950s wooden prosthetic lower leg: rigid shaft/socket silhouette, no calf bulge, no articulated ankle, ending in one ordinary dark shoe planted on the road.
- Silver's anatomical LEFT leg is the leg on the VIEWER'S RIGHT and remains a normal human leg.
- His LEFT hand, also on the VIEWER'S RIGHT, holds EXACTLY ONE plain wooden cane.
- The prosthesis must remain physically attached under his right trouser leg and must not resemble a second cane or crutch.

Invariants: preserve the boy, motel, road, sea, palms, snow/sleet, sky, reflections, palette, negative space, dry-brush/screenprint texture, exact framing and every other pixel-level narrative element. Keep Silver equally small and distant. Do not alter his head, torso, arms, normal left leg, single cane, or cast shadow.

Constraints: exactly one cane total; no second stick, crutch, pole, doubled shadow, text, letters, logo or watermark.
```

### Обложка: финальная точечная правка кандидата

- Вызов: `exec-eda4a3ca-1c71-496d-898b-dc156ea26331`

```prompt
Use case: precise-character-continuity edit
Asset type: portrait 2:3 text-free front-cover artwork
Input image: preserve the entire image, exact composition, scale, boy, motel, road, coast, palms, storm sky, wet reflections, negative space, palette, lighting and dry-brush/screenprint texture.

Edit only the tiny distant Long John Silver on the road:
- He is viewed FROM BEHIND, so his anatomical RIGHT side is also the VIEWER'S RIGHT.
- Add a plain dark-charcoal early-1950s flat cap to his head, low and simple.
- Make his RIGHT lower leg—the leg on the VIEWER'S RIGHT—read as a stiff straight early wooden prosthetic lower leg, attached under the trouser, with no natural calf bulge or articulated ankle, ending in the existing ordinary dark shoe.
- His LEFT leg on the VIEWER'S LEFT remains a normal human leg.
- Keep EXACTLY ONE plain wooden cane total in its current place. The prosthetic leg has a shoe and must never read as a second cane.

Keep Silver equally small and distant. Do not alter his coat, torso, pose, route, shadow, the foreground boy or any other element. No second cane, crutch, pole, extra leg, text, letters, logo, caption, border or watermark.
```

### Иллюстрация 1: замена трости слепого

- Вызов: `exec-06ab4c25-f44d-4f17-8337-46947261a9cf`

```prompt
Use case: precise-object-edit
Asset type: horizontal 3:2 text-free painterly book illustration
Input image: preserve the exact composition and all people, faces, hands, poses, clothing, motel interior, doorway, sleet, road, lighting, palette, anatomy, expressions and brush texture.

Change only one object: replace the older man's modern segmented white mobility cane with EXACTLY ONE single-piece plain dark-brown wooden walking stick appropriate to the early 1950s. It is old, solid, slightly battered wood, with no white paint, no red tip, no telescoping joints, no segmented sections, no rubberized modern grip and no reflective markings. Preserve its placement tucked securely under his raised arm and preserve the hand/wrist interaction exactly.

Do not add or remove any person or change the central wrist grip. Do not alter either face, glasses, doorway, weather, room, clothing, lighting or framing. No second cane, no text, letters, signage, logo, caption, border or watermark.
```

### Иллюстрация 3: живописная стилизация кабинета

- Вызов: `exec-1bd503d0-64cf-46e1-8d43-1279a6e5b8a5`

```prompt
Use case: style-and-character-continuity edit
Asset type: horizontal 3:2 text-free literary book illustration
Input image: preserve the exact study composition, camera, four-person arrangement, poses, furniture, bookcases, globe, model yacht, black rotary telephone, shaded lamps, winter windows, evidence papers, ordinary folded topographic map, clippings, photographs, Spanish forms and emotional focus.

Transform the rendering from glossy/photographic realism into the established visual language of the book: restrained mid-century adventure-novel painting, visible dry-brush and slightly screenprinted texture, simplified but natural modelling, rich dark wood, warm pools of lamplight, matte paper and fabric, cinematic yet clearly painted—not a photograph, not glossy concept art, not hyper-sharp digital realism.

Apply the approved character locks without changing their roles:
1) Jim Hawkins in the oversized chair: lean sixteen-year-old, about 170 cm, messy dark-chestnut hair, brown eyes, clean-shaven youthful face, coat still damp, sitting only on the front edge.
2) Doctor Livesey at the folder: about forty-five, lean, narrow intelligent face, dark hair graying at both temples, clean-shaven, thin metal reading glasses indoors, sober suit.
3) Squire Trelawney leaning over the map: fifty-two, conspicuously large and broad-shouldered, thick gray hair, full red-flushed clean-shaven face, wealthy but rumpled shirtsleeves. He must NOT have black or dark youthful hair.
4) Redruth with tray in back: around seventy, lean, dignified, tidy gray hair, formal old servant, clean-shaven.

Keep exactly four people. Keep the map ordinary, cheap and worn, with only tiny pencil markings and no pirate styling. No readable words, fantasy glow, gold, skull, treasure chest, new person, modern screen, caption, logo, border or watermark.
```

### Иллюстрация 3: финальная седина Трелони

- Вызов: `exec-7546a0d9-b487-45dc-b22c-d26459a31164`

```prompt
Use case: precise-character-detail edit
Asset type: horizontal 3:2 text-free painterly literary illustration
Input image: preserve every pixel-level narrative element, all four faces and bodies, the study, evidence, map, furniture, lighting, composition, dry-brush texture and framing.

Change only Squire Trelawney's hair. He is the very large broad man in rolled white shirtsleeves leaning over the map at the right. Keep the exact haircut, thickness, hairline, face, ruddy complexion and pose, but shift ALL of his hair from dark salt-and-pepper to unmistakable medium silver-gray with a few darker gray strands. It should read immediately as thick gray hair, not black, brown or youthful dark hair. Preserve natural shadow and painterly texture.

Do not change his face, eyebrows, skin, shirt, hands, any other person or any object. No text, letters, logo, caption, border or watermark.
```

### Иллюстрация 5: три пальца Смоллетта

- Вызов: `exec-691ad28a-cdc4-49e9-88e0-23cc22191ed3`

```prompt
Use case: precise-anatomy-edit
Asset type: horizontal 3:2 text-free painterly book illustration
Input image: preserve the entire cabin scene exactly: all four people, their identities, faces, bodies, clothes, poses, table, papers, cups, keys, port windows, Boston winter light, framing, palette, anatomy and painterly texture.

Change only Captain Smollett's raised hand. It must clearly and naturally display EXACTLY THREE extended fingers to enumerate three objections. Use the index, middle and ring fingers extended and separated enough to count; thumb folded across the curled little finger. The hand must have one thumb and four fingers total, anatomically natural, correctly attached to the existing wrist, with no extra digits, fused fingers or doubled hand.

Do not change Smollett's face, his other hand on the table, any other person, any object or any lighting. No text, letters, captions, logos, border or watermark.
```

### Иллюстрация 11: персонажи до первого выстрела

- Вызов: `exec-4bc962cf-9d14-41d7-8e61-ef64b9af436f`

```prompt
Use case: precise-character-and-continuity edit
Asset type: horizontal 3:2 text-free painterly book illustration
Input image: it controls the exact camera, shelter architecture, windows, bright tropical exterior, medium-dark interior exposure, ammunition boxes, loose cartridges and rigid clips, Jim's position, composition, palette and serious dry-brush literary style.

This moment is BEFORE the first shot of the siege. Preserve exactly THREE people total and correct the two adults:

1) Jim Hawkins remains the lean sixteen-year-old dark-chestnut-haired boy working with ammunition in the foreground. Preserve his pose and clothing.

2) The adult at the firing position/window is now Squire Trelawney: fifty-two, large and broad-shouldered, thick gray hair, clean-shaven, full red-flushed face, no cap or hat. He holds the existing rifle and watches the dazzling exterior. His scale and posture should feel big and wealthy but practical. No injury or bandage.

3) The rear-left adult is Redruth, an intact elderly formal servant, around seventy, lean and dignified, tidy gray hair, clean-shaven, in a sober old-fashioned shirt and waistcoat with sleeves neatly arranged. He is upright and quietly washing/arranging a few metal cups and a kettle on the existing surface, maintaining household order under pressure. He is NOT lying down, wounded, bandaged, bleeding, unconscious or being treated.

Critical continuity: no one has yet been wounded. Remove every injury, bandage, bloodstain, sling and prone/resting casualty. Exactly three people total; no extra silhouettes or reflections.

Invariants: preserve the existing readable middle lighting—the unfinished concrete interior remains cool, dim and oppressive, while outside is blazing tropical noon with turquoise water, sky and palms. Preserve Jim, ammunition, all architecture, camera, framing and painterly texture. Loose cartridges and rigid ammunition clips only; no flexible machine-gun belt. No text, letters, captions, logo, border or watermark.
```

### Иллюстрация 12: правая рука с ножом

- Вызов: `exec-6e766360-be25-4742-a5ed-2e77bb61cfdb`

```prompt
Use case: precise-anatomy-and-continuity edit
Asset type: horizontal 3:2 text-free painterly book illustration
Input image: preserve the exact night composition, tiny coracle, schooner, sea, moonlight, camera, Jim's face, body, clothing, pose, tension, knife, rope, palette and dry-brush literary style.

Correct only Jim Hawkins's bandages and hand/rope interaction:
- Jim's anatomical RIGHT hand is the hand holding the knife. Bandage ONLY this right knife hand, with a compact dirty cloth wrap around the palm and lower fingers; keep the knife grip secure and anatomically natural.
- Jim's anatomical LEFT hand and entire left forearm are completely bare, with visible skin and shirt sleeve only—no bandage, wrap, gauze or cloth on the left side.
- His bare LEFT elbow/forearm continues to pin and control the existing rope exactly as in the composition.
- Keep one knife only and preserve the existing rope path.
- Natural anatomy: two arms, two hands, five fingers per hand, no duplicated limbs.

Invariants: no change to Jim's age (lean sixteen-year-old), dark chestnut hair, face, boat, ship, water, moonlight, framing or objects. Do not add people, wounds, blood, text, letters, captions, logo, border or watermark.
```

### Иллюстрация 15: утверждённые лица и травмы

- Вызов: `exec-7dde56c6-124a-4444-a96d-b9d1e51badc5`

```prompt
Use case: precise-character-continuity edit
Asset type: horizontal 3:2 text-free painterly book illustration
Input image: preserve the exact small hand-dug cache pit, intact ground, five-person composition, camera, abandoned concrete theatre, red earth, boards, torn dark canvas, rope, tools, late-afternoon tropical light, poses and restrained literary painting style.

Keep EXACTLY FIVE people and correct only their locked identities and visible continuity:

1) Long John Silver at the rim: tall and broad/heavy, age forty-eight, short thinning dark-gray hair under a plain dark flat cap; pale/light-gray eyes; clean-shaven structure with only short island stubble, absolutely no moustache, beard, bandana or headscarf. His anatomical RIGHT lower leg is a stiff early prosthesis ending in an ordinary shoe. He has exactly ONE plain wooden cane, no crutch and no second stick.

2) Jim Hawkins beside him: lean sixteen-year-old, about 170 cm, messy dark-chestnut hair, brown eyes, clean-shaven. Keep both damaged hands compactly bandaged and keep the short rope tied loosely at his belt ending in Silver's fist.

3) Bobby standing inside the pit: approximately twenty, slim, light-brown hair, clean-shaven, youthful narrow face. He has frozen at the realization that the cache is empty.

4) Vince kneeling inside the pit at the old crate impression: approximately twenty-six, slim, narrow face, very dark neatly pomaded hair, clean-shaven. No cap or bandana.

5) Anderson alone in the rear: approximately forty-five, tall and broad. No bandana, headscarf or hat. His RIGHT arm is clearly immobilized and held against his torso under/inside his shirt because of a collarbone injury; he carries no tool or weapon.

Critical invariants: exact compact pit scale, exactly five humans, Silver's one right-leg prosthesis and exactly one cane, Jim's two bandaged hands, Bobby and Vince remain inside the pit, Anderson remains alone in back. No treasure, chest, gold, new people, extra limbs, added foreground objects, readable text, caption, logo, border or watermark.
```

### Иллюстрация 15: окончательная сторона протеза

Перед окончательной локальной правкой был сделан промежуточный проход, который дал верную кепку, лица и сторону задачи, но визуально восстановил обе естественные голени. Поэтому его нельзя считать финальным изображением, хотя именно он служит входом последнего вызова.

- Промежуточный вызов: `exec-50206c25-72c1-4fb5-9938-400db736ed85`

```prompt
Use case: precise-character-continuity edit
Asset type: horizontal 3:2 text-free painterly book illustration
Input image: preserve every person, face, expression, hand, pose, rope, cane, compact pit, soil, objects, architecture, lighting, camera, framing and painterly texture exactly.

Make only TWO corrections to Long John Silver, the large man standing at upper left:

A) Put the prosthesis on the correct leg. Silver faces toward the viewer, so:
- His anatomical RIGHT leg is on the VIEWER'S LEFT, next to his cane. Replace that right lower leg below the knee with the existing style of rigid early prosthesis, physically attached and ending in an ordinary dark shoe.
- His anatomical LEFT leg is on the VIEWER'S RIGHT. Remove the metal prosthesis currently on that viewer-right side and restore a normal human left lower leg in dark rolled trousers, with natural calf/ankle and matching dark work shoe.
- Preserve EXACTLY ONE wooden cane in its current place and hand. The prosthetic leg must not read as a second cane.

B) Add Silver's locked plain DARK CHARCOAL FLAT CAP, low on his short thinning dark-gray hair. It must be a simple early-1950s workingman's flat cap, not a bandana, headscarf, baseball cap, military cap or wide-brimmed hat. Preserve his face and short stubble.

Do not change Jim, Bobby, Vince, Anderson, the five-person count, Jim's bandages, rope, Anderson's immobilized right arm, or any other part of the image. No second cane, extra limbs, text, letters, logo, caption, border or watermark.
```

- Вызов: `exec-f9ca0ab1-e981-4e2b-a47e-770d33329ba9`

```prompt
Use case: precise-object-edit
Asset type: horizontal 3:2 text-free painterly book illustration
Input image: preserve it completely. Edit ONLY one small region: Long John Silver's correct right lower leg.

Target location: Silver is the large capped man at upper left. He faces toward the viewer. The target is the lower leg on the VIEWER'S LEFT, immediately beside the existing wooden cane—the leg whose dark shoe currently stands nearest the cane.

Replace that target lower leg from just below the knee to the top of its existing dark shoe with a clearly visible early prosthetic assembly:
- rigid straight dark-brown wooden shin/shaft;
- simple leather upper socket/cuff beneath the rolled trouser;
- no natural calf bulge, skin shin or articulated ankle;
- physically attached to Silver and ending in the same ordinary dark shoe on the ground.
This is his anatomical RIGHT prosthetic lower leg.

Keep his other lower leg on the VIEWER'S RIGHT entirely normal. Preserve exactly ONE wooden cane in its current position. Do not change Silver's flat cap, face, body, hands, rope, Jim, the other three men, pit, lighting or anything else.

No second cane, no crutch, no extra leg or foot, no modern metal sports prosthesis, no text, logo, caption, border or watermark.
```

## Дополнительный проход: телосложение Трелони

Первый согласованный набор признаков был сформулирован недостаточно жёстко: слова `large`, `broad` и `heavy` трижды превратились в выраженное ожирение. После авторского замечания замок уточнён: Трелони крупнокостный, широкоплечий и хорошо упитанный, но подвижный, с собранной талией и без шарообразного живота.

### Кабинет: новый основной якорь фигуры

- Вызов: `exec-6ee4cc93-9df5-4656-8813-cc0af46c1115`

```prompt
Use case: identity-preserve
Asset type: corrected horizontal 3:2 painterly literary book illustration
Input image: edit target; preserve the entire study scene and all four identities.

Primary request: correct ONLY Squire Trelawney's body build. He is the silver-haired man in rolled white shirtsleeves leaning over the map at the right.

Approved build:
- age fifty-two, about 183 cm;
- naturally large frame, broad shoulders, deep chest and strong thick forearms;
- sturdy, active, well-fed country gentleman and excellent shot;
- solid and imposing, but NOT obese, soft, bulbous or comically corpulent;
- clearly defined neck, contained waist, only a modest middle-aged belly;
- abdomen must not hang over the belt, shirt must not balloon around a huge stomach, hips and torso must not form a round barrel.

Precise edit: reduce his abdomen, waist, hips, back and overall torso volume by roughly one quarter while keeping his shoulder width and height. Make the white shirt fall more vertically from the chest to a visible waist. His body must plausibly ride, hike, kneel and handle a rifle without looking physically encumbered.

Identity invariants: preserve Trelawney's exact face, full ruddy cheeks, thick silver-gray hair, age, expression, hands, leaning pose and clothes. Preserve Jim, Livesey, Redruth, map, evidence, table, telephone, shelves, globe, model yacht, lighting, composition, dry-brush texture and every other object exactly. Keep exactly four people.

Constraints: no gaunt or athletic-young redesign; no obesity, giant belly, double chin, swollen neck or comic silhouette; no new people or objects; no text, logo, caption, border or watermark.
```

### Каюта: телосложение по новому якорю

- Вызов: `exec-2c84611d-05b6-43ce-a629-7b444145f217`

```prompt
Use case: identity-preserve
Asset type: corrected horizontal 3:2 painterly literary book illustration
Input images:
- Image 1 is the edit target and controls the exact schooner-cabin composition, every pose, face and object.
- Image 2 is a body-build reference ONLY for Squire Trelawney after correction; do not import its study, clothes, lighting, people or objects.

Primary request: in Image 1, correct ONLY Squire Trelawney's excessive body fat. Trelawney is the seated man in the left foreground facing Captain Smollett.

Match the approved build shown by Trelawney in Image 2:
- fifty-two, naturally large frame, broad shoulders, deep chest and strong build;
- sturdy, active, well-fed gentleman, but not obese or round-barrelled;
- visible neck, contained waist and only a modest middle-aged belly;
- reduce the thick neck, back, abdomen, waist and overall seated torso volume by roughly one quarter;
- keep him visibly bigger and broader than Livesey and Smollett, but make his well-tailored dark suit fit without bulging or stretching.

Identity invariants: preserve Trelawney's exact seated pose, ruddy profile, gray hair, hands, chair, suit and offended expression. Preserve Captain Smollett's face, body, table hand and EXACTLY THREE raised fingers. Preserve Livesey, Jim at the doorway, papers, cups, keys, cabin, ports, snowy Boston harbor, lighting, framing, palette and painterly texture exactly. Keep exactly four people.

Constraints: no thin or youthful redesign; no obesity, giant belly, double chin, swollen neck or comic silhouette; do not change Smollett's three-finger gesture; no new people, objects, text, logo, caption, border or watermark.
```

### Каюта: возврат седины после правки корпуса

- Вызов: `exec-9347b908-8b81-4300-8953-2baf92ddcb2b`

```prompt
Use case: precise-object-edit
Asset type: corrected horizontal 3:2 painterly literary book illustration
Input image: preserve the entire schooner-cabin image exactly.

Change ONLY Squire Trelawney's hair color. He is the large seated man in the left foreground, seen in ruddy profile. Keep his exact corrected body build, head shape, hairline, haircut, thickness, face, expression and pose, but change all of his currently dark hair to unmistakable thick medium silver-gray hair with a few darker gray strands. It must read immediately as gray, not brown or black.

Preserve Captain Smollett and EXACTLY THREE raised fingers, Livesey, Jim, every body, face, hand, chair, table, paper, cup, key, port, snowy harbor, light, framing and painterly texture. No other change. No text, logo, caption, border or watermark.
```

### Осада: подвижная крупная фигура

- Вызов: `exec-4d11f368-7a56-409f-af3f-163597f5cb7c`

```prompt
Use case: identity-preserve
Asset type: corrected horizontal 3:2 painterly literary book illustration
Input images:
- Image 1 is the edit target and controls the exact siege composition, architecture, people, poses, objects and lighting.
- Image 2 is a body-build reference ONLY for the corrected Squire Trelawney; do not import its study, clothes, people, furniture or lighting.

Primary request: in Image 1, correct ONLY Squire Trelawney's excessive obesity. He is the gray-haired rifleman kneeling at the right firing aperture.

Match the approved build shown in Image 2:
- fifty-two, about 183 cm, naturally large frame and broad shoulders;
- deep chest, strong arms and sturdy legs, an active country gentleman and excellent shot;
- solid, older and well-fed, but NOT obese, round, soft or physically encumbered;
- visible neck, contained waist and only a modest middle-aged belly.

Precise edit: reduce Trelawney's abdomen, waist, hips, buttocks and thighs by roughly one third, and reduce the swollen roundness of his upper back and neck. Keep his shoulders broad and his overall scale larger than Jim and Redruth. His light shirt should fall from chest to waist without wrapping around a huge sphere. His kneeling rifle posture must look balanced, capable and physically plausible.

Identity and scene invariants: preserve Trelawney's exact gray hair, ruddy face, age, rifle, hands, aim, kneeling pose and clothing. Preserve Jim crouched with loose cartridges and rigid clips. Preserve intact elderly Redruth arranging metal cups and the kettle. Preserve exactly three people, the pre-first-shot continuity, medium-dark concrete interior, dazzling tropical exterior, mesh, openings, water, palms, all ammunition, framing, palette and dry-brush texture.

Constraints: no thin, young or athletic-bodybuilder redesign; no obesity, giant belly, spherical torso, massive seat, double chin, swollen neck or comic silhouette; no wounds or bandages; no machine-gun belt; no extra person or object; no text, logo, caption, border or watermark.
```

### Осада: перенос действия в час ожидания

- Вызов: `exec-4801a4d5-bbb3-49e9-8981-729ad6a88375`
- SHA-256: `4e61871b78843205ac2d2be9b0f2c02ed69e6a80be4a638c8f436b0ec01dfdb1`
- Итоговый кандидат: `images/illustration-04-siege-candidate.png`
- Статус: выбран после авторского просмотра; отдельный платок читается яснее полы рубашки и точнее соответствует аккуратному характеру Трелони. Текст главы 21 приведён в соответствие.

```prompt
Use case: precise-object-edit
Asset type: corrected horizontal 3:2 painterly literary book illustration

Input images:
- Image 1 is the edit target.

Primary request:
Move this exact scene clearly to the quiet waiting hour BEFORE the first shot, as written in chapter 21. Change only Squire Trelawney's action and the placement of his rifle. Preserve the exact camera, composition, architecture, all three character identities, their faces and body builds, lighting, palette, ammunition, cups, tin coffee pot, window mesh, tropical exterior, and dry-brush painterly style.

Trelawney — change only his action:
- He is no longer aiming, shouldering, or holding the rifle.
- Keep him at the same right-hand defensive position and preserve his corrected large-boned, broad, strong but explicitly non-obese build, gray hair, ruddy face, clothing, identity, and scale.
- Turn him slightly inward toward the room, crouched or seated on one knee.
- In one hand he holds ONE ordinary brass rifle cartridge.
- With the loose hem of his own light shirt he is methodically wiping that cartridge. Make the interaction unmistakable: he is cleaning a brass cartridge with shirt fabric, not cleaning glasses, a cup, or the rifle.
- Move his existing rifle — exactly ONE rifle belonging to Trelawney — to rest safely within immediate reach along the concrete ledge or low wall beside him, muzzle pointing outward. It is not in his hands, not aimed, and not firing.

Redruth — preserve:
- Keep Redruth exactly as an intact elderly servant at rear-left.
- Keep all SIX metal mugs and the TIN COFFEE POT / tea service.
- He is calmly washing, arranging, or pouring the mugs before the attack.

Jim — preserve:
- Keep Jim exactly in the foreground sorting loose brass cartridges and rigid ammunition clips.

Story state and lighting:
- Exactly three people.
- This is before combat: no attackers, no wounds, no bandages, no casualties, no smoke, no muzzle flash, no active firing.
- Preserve the dim, cool defensive interior against the dazzling bright blue tropical day outside.
- Preserve all anatomy, hands, facial identities, spatial relationships, and the accepted non-obese Trelawney silhouette.

Constraints:
Exactly one visible Trelawney rifle, now resting nearby; no extra weapon; no machine-gun belt; no extra person; no text; no logo; no border; no watermark.
```

### Осада: пола собственной рубашки

- Вызов: `exec-6ebc0004-b75c-43c1-9794-72391a8aefc9`
- SHA-256: `0597767a2c293c6a89920520be36f3592252e5ca42b33bcc484f910e2cf23451`
- Статус: отвергнут после авторского просмотра: формально ткань соединена с рубашкой, но пола не считывается и жест выглядит менее естественным, чем работа отдельным платком.

```prompt
Use case: precise-object-edit
Asset type: corrected horizontal 3:2 painterly literary book illustration

Input images:
- Image 1 is the accepted near-final edit target.

Primary request:
Change ONLY the fabric in Squire Trelawney's hands so the manuscript action is exact. Preserve every other pixel-level story choice as closely as possible: exact camera and composition, architecture, all three character identities and builds, poses, hands, faces, lighting, colors, tropical exterior, ammunition, Redruth with mugs and tin coffee pot, Jim sorting cartridges, the resting rifles, and the dry-brush literary illustration style.

Required single correction:
- Remove the separate loose white rag from Trelawney's hands.
- Untuck one lower front shirttail / lower hem of Trelawney's own light shirt and have him pull that attached shirt hem upward with one hand.
- The fabric he uses must be visibly and anatomically continuous with the shirt he is wearing; it must clearly be his own shirt-tail, not a handkerchief, towel, napkin, bandage, or separate cloth.
- In his other hand preserve ONE ordinary brass rifle cartridge.
- Show him methodically wiping that brass cartridge with the raised hem of his own shirt.

Critical invariants:
Trelawney remains crouched at right, large-boned, broad, strong, explicitly non-obese, and is not aiming. His one rifle remains resting safely on the ledge beside him. Redruth remains intact at rear-left calmly handling the six metal mugs and tin coffee pot. Jim remains in the foreground sorting loose cartridges and rigid clips. Exactly three people. Quiet waiting hour before the attack.

Constraints:
No attackers, combat, wounds, smoke, muzzle flash, extra person, extra cartridge in Trelawney's hands, separate cleaning cloth, text, logo, border, or watermark.
```

Этот этап завершён: рабочие PNG подменены, пул расширен до двадцати пяти внутренних кадров, а обзорные листы собраны для общего авторского отбора.

## Финальный технический реестр пула из 25 кадров

Реестр ниже фиксирует точный итоговый вызов и контрольную сумму каждого PNG. Совпадение SHA-256 позволяет отличить выбранную версию от промежуточных генераций с похожим названием.

| № | Итоговый файл | Итоговый вызов | SHA-256 |
|---:|---|---|---|
| 1 | images/illustration-ch01-billy-bones-arrival.png | exec-e40d90a7-faf5-47f0-9390-87d6e29dffbc | 0fbc5c3f0a360ba41bb05d318bba548e202deaebc13053c4f501e20c014268a2 |
| 2 | images/illustration-ch03-blind-visitor.png | exec-a20c29c7-6e79-4e9f-a632-58bfc6d21ffd | 893df408fa3924c1b07743bb52072a7cd77fa38e03737c251d4813e1af5c9c0f |
| 3 | images/illustration-ch04-motel-coins.png | exec-5f27755d-34f5-49ed-8519-aea789997703 | 89175e6fec441bbb5a70f3fa097472be1941f7bea8a13d4051fcd183c90dff36 |
| 4 | images/illustration-ch06-trelawney-map.png | exec-6ee4cc93-9df5-4656-8813-cc0af46c1115 | 8be13510eeea73c5c09c4420e65d76d935757ebb6bfe7b23aa854a119e497b38 |
| 5 | images/illustration-ch07-boston-harbor.png | exec-921a92ee-c8d8-4049-8263-8560157e6745 | 0532559b47338319ae02ced589f0e2ab92a6c0f1249072a67a021d496383c235 |
| 6 | images/illustration-ch08-silver-meets-jim.png | exec-169a7b13-feae-446a-bda0-2e46ab84086c | b282a8389096e31fcf8d9da1594b26fe5a9f1a51e61bca0025a698a939a9398b |
| 7 | images/illustration-ch09-smollett-cabin.png | exec-094985a3-e524-4727-a4d1-b065a98f0e32 | 24871bbd1ebb58c213958935774d9a95cf5a9745639b06bd3f934f230c519b07 |
| 8 | images/illustration-ch11-apple-barrel.png | exec-ced537c5-1531-4861-b178-1bbc8d0afe9c | 3b18bb116123abd7cfa1ce75ff47199687c1c189b22d8a35c4c003adc4991885 |
| 9 | images/illustration-ch13-island-resort.png | exec-8926a921-f164-4140-b393-5ae0e0676c0d | e8c0c14bcaec695a9f6f0737f54e805017a9875047a6106f4ae69a43c814b6d9 |
| 10 | images/illustration-ch14-silver-and-tom.png | exec-8a5ca8a4-d379-400d-90e3-22b568b97797 | 5ce6cd2baa7622db442412521e08c3181c43308783720d08f44cad50bd124502 |
| 11 | images/illustration-ch15-ben-gunn.png | exec-13df0806-3d98-4438-a69b-ad567ac7e16d | 674dd454180b8c8b4e086e5891bd4f4a8b0c6b268e1ffd423e9aa7dfd9d23188 |
| 12 | images/illustration-ch17-overloaded-dinghy.png | exec-916f70d7-a523-42c1-b063-11656ecef0d3 | f73455ab276e72bb7a40d6a2104207ee5806a9886ba2528612b49a3ea7a6651a |
| 13 | images/illustration-ch18-raising-the-flag.png | exec-cecc382d-2dc2-43e7-b28d-57575f49d039 | 71faa3558f035e76dbd35599807b5ff6aaf31e9fc71782f90520ac245e8c7f0f |
| 14 | images/illustration-ch20-silver-smollett-parley.png | exec-a15cd3d5-9c43-4242-a646-028fc2ead41e | 835789fbfa8e0cfe5881a5c2633f901d8047dbb86fc8d58ecca3710dbb4dea6a |
| 15 | images/illustration-ch21-waiting-before-assault.png | exec-4801a4d5-bbb3-49e9-8981-729ad6a88375 | 4e61871b78843205ac2d2be9b0f2c02ed69e6a80be4a638c8f436b0ec01dfdb1 |
| 16 | images/illustration-ch22-ben-launches-coracle.png | exec-8bad8bb7-2fac-47d0-95ba-8dc1e8c7d810 | 1d275efcd4b635eceb9c9243056f9e659a79e9a35003e7ea834f23aa50c04b6b |
| 17 | images/illustration-ch23-coracle.png | exec-6e766360-be25-4742-a5ed-2e77bb61cfdb | c27446eceb7a5bdb04db197b5f63644ca0762ef9958d3807386c7861fa08ef69 |
| 18 | images/illustration-ch24-anchor-chain.png | exec-0718fcf3-ad99-4927-b8f8-feca14eb1cfd | cff05597840ad94adfbea9c50269eb83e0ce5be9d3e6db74363386e13be30846 |
| 19 | images/illustration-ch26-jim-and-hands.png | exec-d90d3cf9-1d3c-49ad-951c-66615a0b9522 | cb9df130ef94b274a1fe781fe96083948de75f4adc07fd349075e654bf4a9b1d |
| 20 | images/illustration-ch28-silver-protects-jim.png | exec-61cb3831-4492-4a5c-a9fa-02a3a820b117 | 19aa0148960798dd8a36edd2f6ce073b135d5da33a18f4de76d66bb76a32bf7e |
| 21 | images/illustration-ch29-black-mark.png | exec-c28a7e79-96e3-4ea0-8975-b9f4af67f5c2 | 2fa1a562aa424925cf3df852d91a5072cc6aae3f130ced1ccf7003a43107d332 |
| 22 | images/illustration-ch30-livesey-treats-jim.png | exec-e7eddde7-ae88-4172-b101-0d0a2fb86816 | 8d482474b452f8577a6b64081bbd0a0d92278b3a62092487aa0e177a14d7299b |
| 23 | images/illustration-ch32-flints-voice.png | exec-91f2a2be-cad7-4c97-883d-1d1b506fe484 | bf3705fca11894e0bd73e1c5db2b3aeb30e5a55293fbe693659dc7b9aaf721e7 |
| 24 | images/illustration-ch33-empty-cache.png | exec-f9ca0ab1-e981-4e2b-a47e-770d33329ba9 | f1508a56ae65d21d86995800c5976ddabf1d9836bfaec1822405c0693e08fafd |
| 25 | images/illustration-ch34-homecoming-hands.png | exec-8428be4b-35b9-4f51-9c32-cb84549f2b2e | 377a089470a612ddef3bab8fa35ef9f2e2800073b23d59af4fe29919e64a5c85 |

## Точные промпты новых и заново исправленных кадров

Промпты восьми сохранённых ранних кадров уже приведены выше в истории их правок. Ниже без сокращений сохранены итоговые revised_prompt для семнадцати сцен, созданных или существенно пересобранных при расширении пула до двадцати пяти.

### Глава 1: приход Билли Бонса

- Итоговый вызов: exec-e40d90a7-faf5-47f0-9390-87d6e29dffbc

~~~prompt
Use case: precise-object-edit
Asset type: corrected text-free interior book illustration for chapter 1, landscape 3:2
Input images: Image 1 is the edit target
Primary request: preserve the excellent Billy Bones and Jim exactly, but correct only the motel architecture, outdoor furniture and roadside sign to match the manuscript
Precise edit:
1. Replace the current one-story row of motel doors with a plausible poor, weathered TWO-STORY New England roadside motel/old motor inn of 1952. The ground floor contains the office/bar where Jim stands at the same lit window. Directly above it is a real second floor with several dark guest-room windows facing the road, because the father and Billy live upstairs and an interior staircase leads to a second-floor corridor. A modest attached lower wing may extend behind, but the clearly readable main building must have two full occupied stories. Keep the building small, shabby, white-painted clapboard, practical and unromantic.
2. Remove every chair from the exterior walkway and porch. The cold rain-soaked frontage is empty: only doors, windows, posts, puddles and perhaps one practical doormat. No outdoor seating in late-October bad weather.
3. Replace the unnatural hanging eighteenth-century tavern plaque with a believable freestanding early-1950s roadside motel sign on sturdy posts near the driveway: a faded rectangular painted metal or plywood panel, simple block lettering reading exactly "ADMIRAL BENBOW" once, plus a modest painted admiral looking through a spyglass, with one painted eye weathered away. It must look locally made and aged, not medieval, ornate, luxurious or neon.
Invariants: preserve Billy Bones pixel-for-pixel in identity, face, scar, body, coat, exact walking pose, both hands, duffel and metal suitcase; preserve Jim's identity, face, pose and the location of the warm office window; preserve the road, coast, utility poles, wet cold dusk, reflections, composition, viewpoint, palette and painterly texture. Do not add people, cars or luggage.
Constraints: two-story main motel building clearly visible; no exterior chairs; sign text exactly ADMIRAL BENBOW with no other lettering; historically plausible 1952 architecture and sign construction; no modern branding, neon, vacancy sign, logo or watermark
Avoid: one-story motel, exterior balcony with decorative railings, modern chain motel, saloon, tavern sign, ornate pub crest, porch furniture, extra windows floating without a second floor, misspelled lettering
~~~

### Глава 3: слепой у двери

- Итоговый вызов: exec-a20c29c7-6e79-4e9f-a632-58bfc6d21ffd

~~~prompt
Use case: historical-scene
Asset type: completely regenerated text-free literary book illustration, horizontal landscape 3:2

Input images:
- Image 1 is a CHARACTER, MOTEL, WEATHER, LIGHTING, PALETTE, and PAINTERLY-STYLE reference only. Preserve the established faces, ages, clothing, one dark wooden cane, wet winter motel atmosphere, and sophisticated dry-brush mid-century literary realism. ABSOLUTELY DO NOT COPY its composition, arm positions, grip, giant hand, hand scale, or overlapping-hand geometry.
- Image 2 is a secondary CHARACTER reference for sixteen-year-old Jim Hawkins's narrow teenage face, dark tousled hair, slim unfinished body, and correct age. Do not copy the mother, table, scene, or objects.

Primary request:
Regenerate from scratch the instant in chapter 3 when the blind visitor abruptly stops pretending to be helpless, grabs Jim by the WRIST, and pulls him through the partly opened motel-office door. The anatomy and forceful wrist grip are the central quality requirement.

New safer staging:
Use a wider side-on medium shot from approximately thigh height to head, with both bodies clearly separated and neither gripping hand close to the lens.
- Jim stands just inside the warm motel office at frame left, recoiling and twisting away. His RIGHT arm extends naturally down and slightly sideways at waist level, not toward the camera. His brown jacket sleeve ends in a clear cuff.
- The blind man stands upright at the threshold at frame right, suddenly precise and strong. In his LEFT hand, held well away from the contact point, he carries exactly ONE whole plain dark wooden cane vertically.
- With his free RIGHT hand he closes a normal-size human grip around Jim's RIGHT WRIST immediately below/beyond the jacket cuff.
- The two forearms meet side-on at roughly a right angle or shallow angle, with no foreshortening toward the viewer and no hands stacked directly over one another.

Exact grip anatomy:
- The blind man's right hand is lean, dry, and the SAME plausible adult scale as the rest of his body—not enlarged, monstrous, swollen, or foreground-distorted.
- Exactly four slender fingers curl around the far/outside half of Jim's narrow wrist; their four knuckles form one natural row.
- Exactly one thumb presses from the opposite near/inside half, visibly opposing the fingers and completing a real clamp.
- Jim's forearm remains continuous from his brown sleeve. Jim's own hand is entirely separate and hangs naturally BELOW the grip with exactly five relaxed fingers.
- Clear boundaries between black sleeve, brown jacket cuff, blind-man skin, Jim skin, and both separate wrists. No fused flesh, shared palm, interwoven fingers, duplicated hand, missing digit, extra digit, or impossible wrist rotation.
- The grip looks painfully strong because of posture and tension, not because the hand is huge.

Characters:
Exactly TWO people.
Jim is sixteen, thin, narrow-shouldered, dark tousled hair, no facial hair, worn brown work jacket over plaid shirt, frightened but not melodramatic.
The blind visitor is about fifty-five, tall, very thin and wiry, short wet gray hair, hollow cheeks, clean-shaven, dark wet wool coat. His dark glasses are pushed onto his forehead and the damaged eye area remains in natural shadow without graphic horror.

Scene and composition:
Run-down New England roadside motel office on a freezing rainy winter night in late 1952. Warm tungsten interior at left/right edge, cold wet road and motel rooms outside, rain slanting under wind, worn desk and kettle only as background. The open doorway separates warm interior from cold storm. Keep generous space around the wrist contact so anatomy reads cleanly.

Lighting/mood:
Warm motel light catches the side planes of faces, the single cane, jacket cuffs and grip; cold blue-black rain outside. Tense sudden reversal, not action-movie heroics. Important hands must be readable but not spotlighted or oversized.

Style/medium:
Sophisticated hand-painted mid-century literary book illustration, dry-brush and subtle screenprint grain, restrained realism, natural human anatomy, not photorealistic, glossy, cartoon, or horror art.

Critical constraints:
Brand-new composition. Do not copy the prior mutant hand. Exactly two people, exactly one normal-size gripping hand, exactly one separate Jim hand, exactly one dark wooden cane in the other hand. No second cane, no white modern mobility cane, no giant hand, no extra arm, no merged hands, no blood, weapon, attacker in background, car as focal subject, text, letters, readable sign, logo, caption, border, or watermark.
~~~

### Глава 8: первое рукопожатие

- Итоговый вызов: exec-169a7b13-feae-446a-bda0-2e46ab84086c

~~~prompt
Use case: precise-object-edit
Asset type: corrected text-free interior book illustration
Input images: Image 1 is the edit target
Primary request: change ONLY John Silver's malformed white garment into a historically ordinary 1952 cook's bib apron
Precise edit: replace the current hybrid apron-overalls shape with one conventional plain white cotton bib apron: a rectangular bib covering the shirt from upper chest to waist, simple neck loop, waist ties tied behind his body, and ONE single uninterrupted flat skirt panel hanging from the waist down the FRONT of his body to just below the knees. The apron skirt must be a single sheet of cloth, not split between the legs and not shaped like trousers. Silver's separate dark work trousers must remain clearly visible at both sides of the apron and below its hem. The apron should drape naturally across the front and may be lightly stained by kitchen work, but it has no trouser legs, crotch seam, suspenders, shoulder straps, boiler-suit body or wraparound bifurcation.
Invariants: preserve the exact composition, crop, diner, steam, all background patrons, lighting, color, dry-brush texture, Silver's approved face, hair, expression, age, powerful build, pale shirt, both arms and hands, exact natural handshake, Jim's approved face, clothes, pose and hands, Silver's LEFT natural leg, RIGHT wooden below-knee prosthesis, both shoes, floor and every object unchanged. Do not redraw, move or resize either person. Change only the white apron fabric.
Constraints: one normal single-panel cook's bib apron only; no overalls, no jumpsuit, no dress, no split skirt, no extra fabric between or around legs, no extra pockets, no text, logo or watermark
~~~

### Глава 11: разговор у яблочной бочки

- Итоговый вызов: exec-ced537c5-1531-4861-b178-1bbc8d0afe9c

~~~prompt
Use case: precise-object-edit
Asset type: corrected text-free horizontal 3:2 painterly literary book illustration

Input images:
- Image 1 is the near-final apple-barrel scene and edit target.

Primary request:
Change ONLY Long John Silver's visibly modern, diagonally protruding prosthetic lower leg at the LOWER LEFT of the image. Preserve every other element exactly: all three faces and identities, poses, bodies, barrel with the newly narrowed eye-slit, Jim's single hidden eye, Bobby and match, three apples, harmonica, night sea, stars, rigging, lighting, palette, anatomy, framing, and dry-brush painterly style.

Target and anatomy:
- The target is the exposed mechanical-looking lower limb below Silver's bent knee at the lower-left edge. It is Silver's anatomical RIGHT below-knee prosthesis.
- Remove the exposed modern modular metal tube, adjustable pylon, shock-absorber look, modern foot hardware, and the diagonal leg that juts toward the corner.
- Preserve Silver's real thigh and natural knee above it.
- Replace the target below-knee limb with a historically plausible late-1940s / early-1950s conventional prosthesis:
  - a simple worn brown leather upper socket/cuff partly hidden under the dark trouser hem;
  - a solid shaped dark-brown WOODEN shin and ankle with the mass and silhouette of an ordinary lower leg, not a bare rod;
  - one ordinary scuffed dark leather lace-up work shoe attached at the bottom.
- No visible modern joints, polished chrome, carbon fiber, telescoping hardware, sports blade, hydraulic part, or skeletal pylon.
- Repose only this lower limb: Silver's knee remains naturally bent while seated, but the wooden shin drops inward/near-vertical beneath the knee and the attached shoe rests flat on the deck close to Silver's body. It must not project diagonally toward the viewer or the lower-left corner.
- Keep the prosthesis clearly separate from Silver's normal LEFT leg. Exactly two legs total. Do not add a cane; aboard ship Silver uses no cane.

Critical invariants:
Do not change the barrel, tiny slit, hidden Jim, Silver's broad back, face, cap, hands or seated relationship to the barrel. Do not change Bobby's age, face, match, cigarette, posture, or harmonica. Do not alter ship geometry, sea, stars, ropes, colors, light, or composition.

Constraints:
Change only the lower-left prosthetic lower leg and its attached shoe. No modern prosthesis, diagonal projecting leg, extra leg, extra shoe, cane, crutch, stick, duplicated limb, text, logo, caption, border, or watermark.
~~~

### Глава 14: Сильвер и Том

- Итоговый вызов: exec-8a5ca8a4-d379-400d-90e3-22b568b97797

~~~prompt
Use case: historical-scene
Asset type: text-free literary book illustration, horizontal landscape 3:2

Input images:
- Image 1 is a CHARACTER reference only for Long John Silver's face, broad powerful build, dark flat cap, anatomical RIGHT below-knee prosthesis, and early-1950s island clothing. This scene is earlier and his stubble should be shorter.
- Image 2 is a STYLE, WORLD, COLOR, and TROPICAL-LIGHT reference only. Preserve bright physically beautiful Caribbean heat, abandoned resort concrete and pipe materials, and painterly dry-brush language; do not copy its composition.
- Image 3 is a CHARACTER reference only for sixteen-year-old Jim Hawkins's teenage face, dark unruly hair and narrow build.

Primary request:
Illustrate the tense conversation in chapter 14, seconds after the distant scream of Alan and BEFORE Silver attacks Tom. The scene must show persuasion failing, not the murder.

Scene/backdrop:
Harsh bright tropical afternoon beside an abandoned resort pump station. A thick rusted water pipe runs horizontally on waist-high concrete piers above a shallow green ravine with a narrow trickle of rusty water. Dense mangroves, roots, wet leaves, hot concrete, ruined pump house and water tower glimpsed through foliage. A burst of startled birds rises far over the beach after the scream.

Characters and exact staging:
Exactly THREE people.
1. Long John Silver sits on the rusted pipe, calm and nearly motionless, turned toward Tom. He is forty-eight, tall and broad with a heavy powerful torso, not obese; broad mobile face, very short island stubble, short receding dark-gray hair under one dark working flat cap. His normal LEFT leg and anatomical RIGHT below-knee early prosthesis must both read clearly. Across his knees lies exactly ONE broken half of a wooden oar with a heavy handle—the only walking support or stick in the scene. His hands rest on it for now; he has not thrown it, drawn a knife, or stood up.
2. Tom stands several paces away along the pipe, refusing Silver. About forty, taller and thin, long narrow face, light-brown hair, work shirt bleached white with salt across the back, neck sunburned in red patches, worn trousers and boots. His face has just gone gray with shock; his open empty hands are raised slightly as if pushing away an invisible table. He is frightened but morally decided.
3. Jim is hidden below them in the ravine at the water, lying on his stomach behind wet leaves. Only a small natural portion of his teenage face, dark hair and dirty faded shirt is visible from the reader's viewpoint. He must remain unseen by Silver and Tom. His left palm has a small raw coral cut, no bandage yet.

Composition/framing:
Layered horizontal composition: Jim low in humid leaf-shadow foreground; the rusted pipe forms a strong line above; Silver seated and Tom standing face each other in hard sunlight. Keep fifteen paces of implied space without making figures tiny. Emphasize the silent instant after the off-screen scream. No attack pose.

Lighting/mood:
Dazzling blue-white Caribbean daylight, rust orange, vivid wet greens, turquoise reflected water, crisp broken shadows. Beautiful heat and moral dread coexist. Important faces and the single half-oar must read clearly in print. No gloomy storm, night, sepia, or murky green-black wash.

Style/medium:
Approved sophisticated hand-painted mid-century literary book illustration, dry-brush and subtle screenprint grain, natural anatomy, restrained realism, not photorealistic or glossy concept art.

Critical constraints:
Exactly three people. No Alan, corpse, blood, stabbing, thrown weapon, attack action, extra pirate, extra leg, extra cane, full oar plus cane, second stick, modern prosthesis, pirate costume, red bandana, tricorn, treasure object, text, readable signage, letters, caption, logo, border, or watermark.
~~~

### Глава 15: Бен Ганн

- Итоговый вызов: exec-13df0806-3d98-4438-a69b-ad567ac7e16d

~~~prompt
Use case: historical-scene
Asset type: text-free literary book illustration, horizontal landscape 3:2

Input images:
- Image 1 is a STYLE, PALETTE, ISLAND-LIGHT, and WORLD reference only: preserve its sophisticated hand-painted mid-century dry-brush literary realism, tropical material language, and bright Caribbean daylight. Do not copy its composition.
- Image 2 is a CHARACTER reference only for sixteen-year-old Jim Hawkins: preserve his exact teenage age, narrow face, dark unruly hair, slim unfinished build, and painterly identity. Do not copy the study, other people, furniture, clothing, or composition.

Primary request:
Illustrate Ben Gunn's first appearance in chapter 15 of a 1953 Caribbean literary reimagining of Treasure Island. This must become the definitive visual anchor for Ben Gunn.

Scene/backdrop:
A hot, bright tropical clearing near the abandoned resort, with a barrier of sun-bleached fallen palm trunks and dense living green behind them. Small hints of decayed resort service structures can be visible deep through foliage, but the scene is natural and immediate, not an establishing shot.

Characters and exact action:
Exactly TWO people.
1. Ben Gunn dominates the frame, full body visible, three paces from Jim. He has just emerged from behind the fallen trunks and dropped awkwardly onto both knees. He reaches both empty hands forward with palms clearly turned upward, asking the boy to say anything because he has not heard a human answer in three years. The gesture is desperate, startling, and socially starved—not worshipful, saintly, theatrical, or comic.
2. Jim stands in the near foreground, partly from behind and in wary three-quarter profile, empty-handed, frightened but holding his ground. He is sixteen, about 170 cm, thin with narrow adolescent shoulders, dark-brown tousled hair, no facial hair, dirty faded light work shirt, dark trousers, ruined practical shoes. His left palm has a small untreated coral cut but no bandage yet.

Definitive Ben Gunn appearance:
- About fifty, severely lean and wiry, quick rather than frail.
- Skin burned to the rich brown of an old baseball glove; nearly black cracked lips.
- Extremely pale blue eyes, startling against the dark sun-burned face. Keep his eyes open and readable in this instant.
- Tangled dark-brown hair with sun-bleached strands.
- A long untrimmed beard down to his chest, the color of old black tar with faded brown highlights.
- Bare feet hardened by three years on coral; long dry fingers like wire; no shoes.
- Clothing: irregular pieces of weathered canvas tied with plain cords around his body, plus a torn dark-green jacket that is unmistakably the remnant of an early-1940s Caribbean resort employee uniform. The jacket has worn GOLD PIPING and one small EMBROIDERED PALM TREE on the breast pocket. It must not look military, ceremonial, pirate, fantasy, or decorative.
- No hat, bandana, jewelry, weapon, boots, or modern survival gear.

Composition/framing:
Eye-level horizontal full-width plate. Ben is the clear visual subject near center, kneeling but not tiny; his beard, pale eyes, palms, bare feet, canvas bindings, green jacket, gold piping and palm emblem all read clearly. Jim's wary silhouette frames one side and establishes scale and distance. Avoid centered religious iconography.

Lighting/mood:
Strong beautiful late-afternoon Caribbean sunlight broken by leaves, vivid warm skin and green foliage, blue tropical sky glimpsed above, clear readable faces and clothing. Beauty of the island and human strangeness coexist. No murky gloom, storm, night, sepia wash, horror lighting, or adventure glamour.

Style/medium:
Match the approved series: sophisticated hand-painted mid-century literary book illustration, dry-brush and subtle screenprint grain, natural anatomy and hands, restrained realism, visibly painterly rather than photorealistic or glossy concept art.

Constraints:
Historically plausible 1953 clothing and abandoned prewar resort context. Exactly two people. No extra castaway, pirate costume, pirate hat, tricorn, red bandana, parrot, treasure chest, skull, gun, knife, spear, modern object, religious halo, begging bowl, readable signage, text, letters, caption, logo, border, or watermark.
~~~

### Глава 17: перегруженный тузик

- Итоговый вызов: exec-916f70d7-a523-42c1-b063-11656ecef0d3

~~~prompt
Use case: identity-preserve
Asset type: text-free interior book illustration, landscape 3:2, a completely new composition for chapter 17
Input images: Image 1 is the approved identity reference for Captain Smollett (the short, very lean, straight older man standing at center with cropped steel-gray hair) and Doctor Livesey (the slim clean-shaven bespectacled man seated at right with dark hair graying at the temples). Preserve only those two identities; do not copy the cabin, other men, Jim, raised fingers, winter clothes, furniture, or snow.
Primary request: illustrate the dangerously overloaded final dinghy trip abandoning Hispaniola for the island
Scene/backdrop: bright Caribbean afternoon in a sheltered bay, blue-green water, tropical shoreline and old resort pilings ahead, the practical two-masted auxiliary schooner Hispaniola receding behind
Subject: exactly three men in a tiny overloaded wooden ship's dinghy. Abraham Grey, about thirty-five, wiry, short ash-blond hair, clean-shaven, fresh cut across one cheek and shirt torn half away at the shoulder, rows with short controlled strokes at the center. Captain Smollett, exactly the same face and very lean compact build from Image 1, sits upright in the stern in a plain dark naval jacket wet to the third button, a ship's journal open on his knees, chronometer wrapped safely under his jacket. Doctor Livesey, exactly the same face and slim build from Image 1 but without spectacles in active daylight, crouches low in the bow among one medical case, compact boxes and a sack of biscuits, holding cargo steady. The waterline is only about three inches below the gunwale; the boat visibly ships a little water but has not yet sunk.
Style/medium: same sophisticated hand-painted mid-century literary realism, dry brush and restrained screenprint grain, precise period detail, natural anatomy
Composition/framing: low waterline side view close enough to read all three men, full dinghy visible end to end, schooner and bright island layered behind; danger comes from scale and load, not a storm
Lighting/mood: harsh beautiful tropical afternoon, glare on water, quiet concentration and physical risk
Constraints: exactly three people and no Jim; preserve Smollett and Livesey identities; Grey has two natural legs and a single fresh cheek cut; no Silver, no prosthesis, no pirate clothes, no heroic action pose, no giant cargo mound, no modern life jackets, plastic containers, outboard motor, text, letters, logo or watermark
Avoid: ocean storm, capsizing, extra rowers, duplicate oars, fused limbs, oversized dinghy, luxury yacht
~~~

### Глава 18: подъём флага

- Итоговый вызов: exec-cecc382d-2dc2-43e7-b28d-57575f49d039

~~~prompt
Use case: identity-preserve
Asset type: text-free interior book illustration, landscape 3:2, a completely new composition for chapter 18
Input images: Image 1 is the approved identity reference for Captain Smollett, the short very lean straight older man with cropped steel-gray hair. Image 2 is the approved identity reference for John Trelawney, the broad strong silver-haired man kneeling with a rifle, and Thomas Redruth, the tall thin elderly steward in a dark vest at left. Preserve those three identities only; do not copy the cabin, siege pose, Jim, rifle action, tea table, snow, or ammunition.
Primary request: illustrate Captain Smollett personally raising Hispaniola's stern flag over the abandoned Caribbean resort enclosure
Scene/backdrop: an unfinished prewar resort service yard in 1953, low raw-concrete office, broken wire-mesh perimeter, improvised wooden flagpole, bright tropical vegetation and blue sky beyond
Subject: exactly three clearly readable men. Captain Smollett, exactly the same short, severe, very lean man from Image 1, in a plain dark naval jacket with no insignia, pulls the halyard hand over hand while a modest United States flag of the historical 48-star era reaches the top and unfolds. Trelawney, exactly the same large-boned but not obese silver-haired man from Image 2, stands nearby bareheaded in a good light shirt and dark trousers, watching. Redruth, exactly the same tall, thin, long-faced elderly steward from Image 2, carefully brushes dust from Trelawney's dark hat with his sleeve before returning it. All three are still uninjured; no cut above Trelawney's eye yet.
Style/medium: same sophisticated hand-painted mid-century literary realism as the references, dry brush and restrained screenprint grain, realistic anatomy and cloth
Composition/framing: medium-wide low-angle yard view, flag and pole rising diagonally without dominating the whole sky; Smollett's physical work central, Trelawney and Redruth's small formal ritual clear at one side
Lighting/mood: brilliant hard Caribbean morning, faded concrete and saturated natural greens, a grave practical ceremony rather than triumphalist propaganda
Constraints: preserve the three approved identities and proportions; exactly three people; historically plausible 1953 flag, clothing and resort infrastructure; Trelawney has no wound; no Jim, no Livesey, no Silver, no weapons in hands, no pirate flag, no modern flag hardware, no readable text, letters, logo or watermark
Avoid: heroic military tableau, saluting, battlefield smoke, giant flag, modern tactical clothing, extra fingers, duplicated hat
~~~

### Глава 20: переговоры

- Итоговый вызов: exec-a15cd3d5-9c43-4242-a646-028fc2ead41e

~~~prompt
Use case: identity-preserve
Asset type: text-free interior book illustration, landscape 3:2, a completely new composition for chapter 20
Input images: Image 1 is the PRIMARY approved identity reference for John Silver's exact face, age, powerful heavy build and attentive expression in Boston. Image 2 is only the approved reference for Silver's island clothing, dark flat cap, correct RIGHT below-knee prosthesis and single broken half-oar support. Image 3 is the approved identity reference for Captain Smollett, the short very lean severe man with cropped steel-gray hair, and for sixteen-year-old Jim Hawkins. Do not copy any reference composition, diner, tropical pipe, Tom, cabin, furniture, raised fingers, snow, or extra people.
Primary request: create a fresh illustration of Silver and Smollett's parley inside the unfinished Caribbean resort enclosure
Scene/backdrop: clear bright Caribbean morning after mist, raw-concrete service office opening to a fenced yard, stacked blocks and wire mesh, vivid sun outside and readable cool shade inside
Subject: exactly three readable people. Silver has exactly the same face, age and powerful non-obese body as Image 1, now sunburned with only short island stubble and wearing the worn pale work shirt and dark trousers of Image 2. He sits with effort on a low stack of concrete blocks, facing Smollett. His dark flat cap is unmistakably resting open-side-up on his knee. His LEFT natural leg and RIGHT below-knee early prosthesis are both fully visible and separated: the right lower leg is a conventional solid shaped dark-brown wooden shin attached to a leather socket/cuff and an ordinary dark lace-up shoe, with absolutely no exposed metal tube, modular pylon, mechanical joint or modern hardware. Exactly one broken wooden half-oar rests beside him as his only support, clearly separate from both legs. Captain Smollett, exactly the same compact lean man from Image 3, stands straight in the doorway in a plain dark naval jacket with BOTH HANDS CLASPED BEHIND HIS BACK, listening without gesture; he is uninjured. Jim, exactly the same slim sixteen-year-old from Image 3, is partly visible in profile at a firing slit, watchful, with a simple small bandage around his LEFT palm only.
Style/medium: same sophisticated hand-painted mid-century literary realism, dry brush and restrained screenprint texture, natural anatomy
Composition/framing: medium-wide eye-level view from inside; Silver seated at one side and Smollett standing across clear empty floor, Jim secondary at the slit; show Silver's two legs, right prosthesis, cap and single half-oar without overlap
Lighting/mood: hard beautiful tropical glare beyond the doorway, cool tense shade inside, formal hostility and calculation, Silver attentive rather than villainous
Constraints: preserve all three approved identities and ages; exactly three people; Silver has exactly one right prosthesis, one left natural leg, one half-oar and no other cane or crutch; cap on knee, not head; Smollett's hands both stay behind his back and no fingers are displayed; Jim's right hand unbandaged; no Trelawney, Livesey, Grey, Vince or background silhouettes; no modern prosthetic hardware, pirate clothing, muzzle flash, readable text, letters, logo or watermark
Avoid: modern metal pylon, extra legs, two sticks, standing Silver, obesity, moustache, beard, injured Smollett, hands in front, raised fingers, fused anatomy
~~~

### Глава 22: Бен спускает корытце

- Итоговый вызов: exec-8bad8bb7-2fac-47d0-95ba-8dc1e8c7d810

~~~prompt
Use case: identity-preserve
Asset type: text-free interior book illustration, landscape 3:2, a completely new composition for chapter 22
Input images: Image 1 is the approved identity reference for Ben Gunn and sixteen-year-old Jim Hawkins in the Caribbean. Preserve Ben's exact face, pale eyes, long tar-dark beard, wiry body, bare feet and ruined dark-green resort jacket with thin gold piping; preserve Jim's exact slim adolescent build, messy dark hair and face. Do not copy the kneeling pose, fallen palms, clearing, bright noon, logs, or ruins.
Primary request: illustrate Ben Gunn launching his handmade coracle for Jim at the start of the night mission
Scene/backdrop: sheltered tropical water behind a black tar-stained rock at the edge of an abandoned resort island just after sunset; luminous deep-blue twilight still reveals turquoise shallows, palms and the distant dark two-masted Hispaniola with one weak yellow cabin light
Subject: exactly two people. Ben, same identity as Image 1, stands barefoot knee-deep in the clear water, long beard and ragged green-gold resort jacket unmistakable, gripping the stern with both natural hands and pushing the tiny boat away. Jim, same sixteen-year-old identity as Image 1, sits low inside the crude tarred coracle with both hands still uninjured, one hand holding a simple tin bailer and the other ready at one short homemade paddle. The coracle is genuinely tiny and awkward, built from mismatched door planks and scrap boards sewn with wire and sealed by thick uneven tar; one short paddle only.
Style/medium: same sophisticated hand-painted mid-century literary realism as Image 1, dry brush and restrained screenprint grain, realistic anatomy
Composition/framing: low shoreline three-quarter view, Ben and boat fully visible, Jim small and low in the bowl, water opening toward the distant schooner; no close-up hand overlap
Lighting/mood: bright readable tropical blue hour, beauty and danger together, quiet practical farewell, not murky blackness
Constraints: preserve both identities; exactly two people; Ben has two natural bare feet and no weapons; Jim's hands have no bandages yet; one coracle, one short paddle, one tin bailer; no modern boat, outboard motor, life jacket, pirate costume, treasure imagery, readable text, letters, logo or watermark
Avoid: oversized canoe, round wicker coracle, duplicate paddle, extra arms, fused hands, storm, moonlit postcard glamour, pitch-black exposure
~~~

### Глава 24: якорная цепь

- Итоговый вызов: exec-0718fcf3-ad99-4927-b8f8-feca14eb1cfd

~~~prompt
Use case: precise-object-edit
Asset type: corrected text-free interior book illustration for chapter 24, landscape 3:2
Input images: Image 1 is the edit target
Primary request: correct ONLY Jim Hawkins's clothing while preserving the excellent chain-climbing composition and anatomy
Precise edit:
1. Put Jim's original old practical dark lace-up work boots back on BOTH feet. The boots are soaked, salt-stained and worn but intact. Preserve the exact positions of both feet: one boot braces against the sloping hull and the other braces against the chain. No bare feet or sandals.
2. Replace the sleeveless dark top with the remains of his sun-bleached LIGHT work shirt. The shirt is wet, dirty and badly torn from the ordeal; its lower hem and sleeve ends may be ragged because strips were torn off for bandages, but real cloth must still cover BOTH shoulders, upper back, chest and upper arms. Sleeves can end raggedly around the elbows or upper forearms so the forearms and bandaged hands remain unobstructed. Do not make it a vest, tank top or bare-shouldered garment.
Invariants: preserve Jim's approved face, exact sixteen-year-old age, hair, body proportions, pose, both arms, both naturally gripping bandaged hands, all fingers, chain, hull, hawsehole, frayed rope end, broken coracle boards, paddle, island, sea, sunlight, composition, crop, colors and painterly texture. Do not move, resize or redraw the hands, chain or face.
Constraints: two old dark lace-up boots; one torn light work shirt covering both shoulders; both hands remain bandaged; no shoulder wound yet; no extra clothing, life jacket, harness, text, logo or watermark
Avoid: bare feet, sleeveless vest, dark tank top, modern boots, extra fingers, altered grip, fused boot and chain
~~~

### Глава 26: Джим и Хэндс

- Итоговый вызов: exec-d90d3cf9-1d3c-49ad-951c-66615a0b9522

~~~prompt
Use case: identity-preserve
Asset type: text-free interior book illustration, landscape 3:2, a completely new composition for chapter 26
Input images: Image 1 is the approved identity and immediate-state reference for sixteen-year-old Jim Hawkins after climbing the anchor chain: preserve his exact adolescent face, messy dark hair, slim build, torn light shirt, dark trousers, old boots and both bandaged palms. Do not copy the anchor chain, hull exterior, broken boat, high midday light or pose.
Primary request: illustrate the final confrontation between Jim and Israel Hands on the beached Hispaniola at sunset
Scene/backdrop: deck and lower rigging of a practical two-masted auxiliary schooner sitting gently aground in shallow tea-colored tropical water near old pilings; low orange-green sunset, calm bay and palms beyond, no storm
Subject: exactly two people. Jim, same sixteen-year-old identity as Image 1, is high enough in the shrouds at the lower cross-trees to be out of reach, legs gripping the mast and one bandaged hand holding a ratline; the other bandaged hand holds an old wet revolver downward but not firing. A fresh shallow knife slash has opened the fabric over ONE shoulder and a small dark line of blood runs inside the shirt; no graphic gore. Below him on deck stands Israel Hands: about forty-two, stocky and wiry, heavy forearms, short dark oily hair, gray eyes, angular ordinary face with stubble, greasy work shirt and dark trousers. He holds one plain work knife blade-down and looks up without theatrical rage. Hands has TWO fully natural human legs; the outer side of his RIGHT thigh is tightly wrapped in a dark blood-stained cloth bandage, and that natural right leg trembles but supports him. No prosthesis, cane or crutch.
Style/medium: same sophisticated hand-painted mid-century literary realism as Image 1, dry brush and restrained screenprint grain, realistic rigging and anatomy
Composition/framing: low deck-level view looking up through diagonal shrouds, Jim small but clearly readable above, Hands full-body below; separate their silhouettes and hands; show both of Hands's natural boots and legs
Lighting/mood: beautiful low tropical sunset, long orange light on wet wood and rigging, exhausted calculation rather than swashbuckling heroism
Constraints: preserve Jim's approved identity and age; exactly two people; both Jim palms bandaged; one fresh shoulder slash; Hands has exactly two natural legs, one right-thigh bandage and one knife; no Silver, no wooden leg, no cap, no extra crew, no corpse or human-shaped tarp, no muzzle flash, pirate clothing, readable text, letters, logo or watermark
Avoid: prosthetic leg on Hands, amputee Hands, heroic sword duel, Jim older than sixteen, extra fingers, fused rigging and limbs, modern gun, storm, night-black exposure
~~~

### Глава 28: Сильвер объявляет Джима своим

- Итоговый вызов: exec-61cb3831-4492-4a5c-a9fa-02a3a820b117

~~~prompt
Use case: precise-object-edit
Asset type: corrected text-free interior book illustration for chapter 28, landscape 3:2
Input images: Image 1 is the edit target
Primary request: correct ONLY John Silver's lower-body anatomy and footwear while preserving the entire scene
Precise edit:
1. Silver's LEFT living leg is the long leg extended toward the center/right of the image. Put one ordinary worn dark lace-up work boot and dark sock on that natural left foot. Preserve the exact leg position. No bare foot.
2. Silver's RIGHT residual limb is the shorter limb toward the lower foreground. It must end naturally below the knee inside a short, soft, folded empty right trouser cuff over an anatomically plausible rounded residual limb. Remove the current hard brown log-like or wooden appearance from this attached limb. It must look like cloth and human anatomy, not wood, metal, a second prosthesis or a detached log.
3. Keep the ONE removed right prosthesis standing against the wall at far left exactly as the only wooden lower-leg object in the scene: leather socket, shaped wooden shin and ordinary attached lace-up shoe.
Invariants: preserve Silver's approved face, torso, arms, hands, gun held low, cap on lap, exact seated pose, all clothing above the knees, Jim, Vince, Anderson, their identities, wounds and poses, kerosene lamp, table, doorway, room, lighting, composition, crop, colors and dry-brush texture. Do not redraw any face, hand, weapon or other person.
Constraints: one natural left leg with one boot; one soft cloth-covered right residual limb; exactly one detached wooden prosthesis at the wall; no bare foot, no attached wooden stump, no extra leg, no modern metal pylon, no text, logo or watermark
Avoid: changing Silver's face, moving the gun, changing the detached prosthesis, adding another shoe or leg, graphic amputation detail
~~~

### Глава 29: чёрная метка

- Итоговый вызов: exec-c28a7e79-96e3-4ea0-8975-b9f4af67f5c2

~~~prompt
Use case: identity-preserve
Asset type: corrected text-free interior book illustration for chapter 29, landscape 3:2
Input images: Image 1 is the edit target. Image 2 is the approved identity reference for Bobby: he is the SHORT slim young man at right lighting a match beside the apple barrel, with light-brown hair falling over his forehead, an open boyish clean-shaven face and brown eyes. Use Image 2 only for Bobby's exact face, hair, age and small build; do not copy the ship, match, cigarette, harmonica, barrel, Silver, Jim or night lighting.
Primary request: change ONLY the central standing man who hands the soot-circle card to Silver so he is unmistakably the approved Bobby from Image 2, not a duplicate of wounded Jim
Precise edit: preserve the central figure's exact leaning pose, arms, hands, soot-black thumb and index finger, card, shirt, trousers and location. Replace only his face, head, hair and body scale enough to match Bobby: about twenty, short and slim, light-brown hair falling softly onto the forehead, clean-shaven, open still-boyish features. He should be visibly shorter and less broad than Vince and Anderson behind him. He must remain distinct from the seated sixteen-year-old wounded Jim at lower right.
Invariants: preserve Silver, his exact face, cap, attached right wooden prosthesis and pose; preserve seated wounded Jim at lower right pixel-for-pixel in identity, hair, face, wounds, bandages and pose; preserve Vince, Anderson, sling, lamp, table, card and soot circle, room, composition, lighting, crop, palette and painterly texture. Do not redraw any other face, hand, leg or object.
Constraints: exactly the same five people; only one Jim, seated at lower right; only one Bobby, central and handing the card; no facial hair on Bobby; no duplicate Jim face; no text, logo or watermark
Avoid: dark slick hair on Bobby, adult rugged face, broad shoulders, changing the card hand, moving anyone, adding a sixth person
~~~

### Глава 30: Ливси перевязывает Джима

- Итоговый вызов: exec-e7eddde7-ae88-4172-b101-0d0a2fb86816

~~~prompt
Use case: identity-preserve
Asset type: text-free interior book illustration, landscape 3:2, a completely new composition for chapter 30
Input images: Image 1 is the approved identity reference for Doctor Livesey: the slim clean-shaven man at center with dark-brown hair graying at the temples, narrow composed face and practical manner. Preserve Livesey only; do not copy Jim, Trelawney, Redruth, map, library, winter night, suits or furniture. Image 2 is the approved identity and wound-state reference for sixteen-year-old Jim Hawkins at lower right: preserve his exact adolescent face, messy dark hair, slim build, torn light shirt, dark trousers, old boots, both bandaged palms and shoulder wound. Do not copy Silver, Bobby, Vince, Anderson, card, office group, night or poses.
Primary request: illustrate Doctor Livesey privately treating Jim just outside the pirate-held enclosure
Scene/backdrop: bright clear Caribbean morning outside a raw-concrete resort service yard, sagging wire mesh fence and open gate behind, stacked sun-warmed concrete blocks, lush palms and pale blue sky; no other person visible
Subject: exactly two people. Jim, exact sixteen-year-old identity from Image 2, sits on the stacked concrete blocks turned into the morning light. His torn light shirt exposes only the medically necessary edge of a shallow dressed shoulder slash; both palms are damaged and wrapped in dirty strips. He rests his forearms separately on his knees with palms turned upward, not touching each other. Doctor Livesey, exact identity from Image 1, about forty-five, slim, sleeves rolled, no spectacles outdoors, kneels or sits beside him with an open dark medical bag. Livesey looks down at the hands and holds a fresh roll of gauze and a small packet of yellow antiseptic powder above them, not gripping or overlapping Jim's fingers; his own two hands remain clearly separate.
Style/medium: same sophisticated hand-painted mid-century literary realism, dry brush and restrained screenprint grain, realistic quiet anatomy
Composition/framing: intimate medium-wide side view, both full upper bodies and all four hands clearly separated, wire mesh and open gate giving depth; medical bag and concrete blocks anchor the scene
Lighting/mood: brilliant but gentle tropical morning, familiar medical smells and a hard private conversation, restraint rather than sentimentality
Constraints: preserve both approved identities and ages; exactly two people; Jim has two injured bandaged palms and one shoulder wound; Livesey has two natural hands and no glasses; no Silver or background silhouettes, no weapon, no modern medical plastics, no graphic blood, readable text, letters, logo or watermark
Avoid: fused hands, doctor gripping both wrists together, adult-looking Jim, hospital setting, dark bunker lighting, heroic embrace
~~~

### Глава 32: голос Флинта

- Итоговый вызов: exec-91f2a2be-cad7-4c97-883d-1d1b506fe484

~~~prompt
Use case: identity-preserve
Asset type: text-free interior book illustration, landscape 3:2, a completely new composition for chapter 32
Input images: Image 1 is the PRIMARY approved identity reference for John Silver's exact face, age and powerful non-obese build. Image 2 is the approved identity and late-island-state reference for Silver, sixteen-year-old Jim Hawkins, Bobby, Vince and Anderson together; preserve all five identities, Jim's wounds, Vince's brilliantined hair and comb, Bobby's young light-brown-haired profile and Anderson's right-arm sling. Do not copy the concrete office, soot card, lamp, seated poses, prosthesis exposure, dawn or composition.
Primary request: illustrate the instant an unseen voice from the vegetation sings like Flint and freezes the treasure party
Scene/backdrop: the ruined open-air theater of an abandoned Caribbean resort in late afternoon: weather-streaked white concrete stage shell with a black-green opening, cracked dance floor invaded by grass, bright palms and sea glare beyond
Subject: exactly five people, all the identities from Image 2. The hand-dug excavation is modest and physically plausible, roughly seven feet long, four feet wide and three to four feet deep, uneven and made by two men with shovels in a single day; NOT a giant quarry. Silver, exact face and build from Image 1 in sunburned late-island condition, stands at the edge with blood drained from his face, mouth slightly open, gripping exactly ONE plain wooden cane with BOTH hands while the cane visibly trembles. His RIGHT below-knee solid wooden prosthesis and LEFT natural leg are clearly separate; dark flat cap on his head. Jim stands near a small stone beside Silver, exact sixteen-year-old wounded identity, both palms bandaged and shoulder dressed; a slack eight-foot rope runs from Jim's belt to the stone because Silver has pinned the loose end there. Vince, exact slick-haired identity, backs slowly out of the pit without turning toward the black stage opening, holding one old revolver low and visibly trembling. Bobby, exact young identity, has climbed out on the opposite side and stands away from both pit and stage, one shovel abandoned near him. Anderson, exact broad older identity, stands from an empty metal water can; his RIGHT arm remains immobilized in a sling and his healthy left hand has moved under his shirt.
Style/medium: same sophisticated hand-painted mid-century literary realism, dry brush and restrained screenprint grain, realistic group anatomy
Composition/framing: wide but human-scale theater view, small pit in foreground/middle, five distinct silhouettes around it, black stage opening behind as the unseen source; no person or face visible in the vegetation
Lighting/mood: hot beautiful tropical late afternoon, long shadows and bright sea light, collective fear in full daylight rather than supernatural darkness
Constraints: preserve all five identities and injuries; exactly five people; one small hand-dug pit, two shovels at most, one revolver, one cane, one attached right wooden prosthesis; Anderson's right arm immobile; no Ben Gunn visible, no ghost, no skeleton foreground, no giant excavation, no heavy machinery, no pirate costumes, readable text, letters, logo or watermark
Avoid: extra people, apparition, transparent ghost, gigantic pit, excavator proportions, multiple canes, modern prosthesis, modern gun, night scene, horror gore
~~~

### Глава 34: руки покажи

- Итоговый вызов: exec-8428be4b-35b9-4f51-9c32-cb84549f2b2e

~~~prompt
Use case: identity-preserve
Asset type: text-free interior book illustration, landscape 3:2, a completely new composition for chapter 34
Input images: Image 1 is the approved architecture and atmosphere reference for the Admiral Benbow motel: preserve the same small poor TWO-STORY weathered white-clapboard New England motor inn, ground-floor office, upper guest-room windows facing the road and the freestanding faded "ADMIRAL BENBOW" sign with painted admiral. Do not copy Billy Bones, luggage, October storm, exact dusk lighting or walking pose. Image 2 is the approved identity reference for Jim's mother, the tired narrow-faced strong woman with dark-brown hair threaded with gray and pinned back, weathered red hands, plain dark dress and faded work apron. Preserve her exact face, age and build; do not copy the coin table, night interior or early Jim. Image 3 is the approved identity reference for sixteen-year-old Jim Hawkins's exact face, messy dark hair and slim adolescent build after the island. Preserve Jim only; do not copy Doctor Livesey, medical bag, blocks, tropical setting, shoulder exposure or bandages.
Primary request: illustrate Jim's return to his mother at the motel in late March, at the quiet instant she asks to see his hands
Scene/backdrop: the same two-story Admiral Benbow at the end of winter, wet thawed roadside, small dirty snow remnants in shade, some windows still badly patched with plywood, pale cold March daylight; the faded roadside sign is present in the background and may retain its exact existing lettering, no other text
Subject: exactly two people at the open office doorway. Jim's mother, exact identity from Image 2, has come out wiping work-wet hands on her faded apron; hair pinned, no makeup or decorative vintage styling. She stands close but controlled and looks down at Jim's hands. Jim, exact sixteen-year-old identity from Image 3, wears a worn brown work jacket over a faded shirt and dark trousers, thinner and weathered but still clearly adolescent. He holds BOTH bare hands separately at waist height, palms up: no bandages now, only healing pink scars crossing the palms and broken uneven nails. His mother does not clutch him; with two separate natural hands she lightly turns one wrist and inspects the other palm, a practical familiar gesture. All four hands must remain clearly distinct and anatomically natural.
Style/medium: same sophisticated hand-painted mid-century literary realism, dry brush and restrained screenprint grain, realistic skin and clothing
Composition/framing: medium-wide view from just inside or beside the doorway, mother and Jim central with all hands readable, two-story motel frontage and wet road receding behind; sign secondary, not oversized
Lighting/mood: pale clear post-rain March light with modest warm office light behind them, reunion expressed through inspection and work rather than melodramatic embrace
Constraints: preserve both approved identities and ages; exactly two people; same two-story motel architecture; no outside chairs; Jim has two bare scarred hands and no bandages, no open shoulder wound; mother wears apron; no Livesey, Silver, car, luggage, tropical elements, readable text beyond the preserved sign, logo or watermark
Avoid: hug, tears, theatrical pose, fused hands, mother gripping both wrists together, adult-looking Jim, one-story motel, ornate tavern sign, snowstorm, dark night
~~~
