# Dziennik zmian - motyw RPG Guild

Motyw `RPG GUILD theme 2025`, ID `182160195850`, sklep `rpg-guild.myshopify.com`.

Zapis prowadzony dla dewelopera. Każdy wpis mówi **co**, **gdzie**, **dlaczego**
i **jak cofnąć**. Zmiany wykonane poza repozytorium - przez Admin API, MCP albo
ręcznie w panelu Shopify - są oznaczone `[poza repo]`, bo nie ma po nich commita.

Konwencja: najnowsze na górze.

---

## 2026-10-06

### Sekcja The Long Night na wszystkich kolekcjach 5e (57 szablonów)
`4ef6c2b` · 55 kolejnych `templates/collection.*-5e.json` + tłumaczenia DE/FR `[poza repo]`

Po akceptacji testu na aarakocra-5e i aberration-5e (wpis niżej) Jan zlecił resztę: sekcja sezonu
stoi teraz na **wszystkich 57 szablonach kolekcji z „5e” w nazwie**, zawsze zaraz pod sekcją
„Guild” (w 40 szablonach nad „CTA”, w 17 nad „Headline + text + CTA”). Inne szablony kolekcji
(terrain, sale, spooky, bestsellers itd.) bez zmian.

Ta sama kopia `section_longNightSeason` z `product.json` (akt I, link do landingu sezonu, padding 40/40).
**Kod motywu bez zmian**, diff: +2805 / -0. Przed zmianą 55 szablonów pobranych z serwera
i porównanych z repo - identyczne, więc nic z edytora nie zostało nadpisane. Po pushu
wszystkie 57 pobrane ponownie: identyczne z repo, sekcja pod „Guild” w każdym.

Tłumaczenia: 1650 wpisów (55 szablonów × 15 pól × DE/FR) przez `translationsRegister`,
dopasowane po digeście EN, skryptem `shopify_tln_translations.py` (folder projektu, apka
`/rpg-movie`, tryby `plan` / `run` / `check`). Kontrola `check`: 57/57 kompletne.

Sprawdzone na żywo: sekcja w HTML wszystkich 57 kolekcji (EN). Pięć szablonów jest podpiętych
pod kolekcje o innym adresie niż nazwa szablonu: `bard-5e` → `/collections/5e-bard`,
`npcs-5e` → `dnd-5e-npcs`, `paladin-5e` → `5e-paladin`, `rogue-5e` → `5e-rogue`,
`terrain-5e` → `dnd-terrain-elements-miniatures`. DE/FR sprawdzone na próbce, także na
kolekcjach z przetłumaczonym adresem (`/de-de/collections/magier-5e`, `/fr-fr/collections/magicien-5e`
- stary adres odpowiada 301, to nie błąd).

**Uwaga przy pushu wielu plików z zsh:** lista `--only` sklejona w jedną zmienną idzie jako jeden
argument i CLI odrzuca polecenie (nic nie wysyła). Budować tablicę `args+=(--only plik)`.

**Jak cofnąć:** tag `przed-tln-kolekcje-5e` (stan sprzed obu etapów) i push tych 57 szablonów,
albo ukrycie sekcji „The Long Night · sezon” w edytorze danego szablonu.

### Sekcja The Long Night na kolekcjach 5e - test na dwóch szablonach
`60a5378` · `templates/collection.aarakocra-5e.json`, `templates/collection.aberration-5e.json`
+ tłumaczenia DE/FR `[poza repo]`

Pierwszy etap wdrożenia sekcji sezonu (`long-night-season`) na szablonach kolekcji z „5e”
w nazwie (57 szablonów). Decyzja Jana: najpierw dwa szablony na żywo do sprawdzenia, potem reszta.
Miejsce: **zaraz pod sekcją „Guild”**, nad CTA / „Headline + text + CTA”.

**Kod motywu bez zmian.** Do każdego szablonu doszedł jeden wpis `section_longNightSeason`
(kopia 1:1 z `product.json`: akt I podświetlony, link do landingu sezonu, padding 40/40)
i jedno miejsce w `order` po sekcji „Guild”. Diff: 51 dopisanych linii na plik, zero usuniętych.

Przed pushem: pull całego motywu z live (commit `955592b` - zmiany z panelu od 03.10),
sprawdzenie, że oba szablony na serwerze są identyczne z pullem, tag cofnięcia, push tylko tych
dwóch plików. Shopify CLI było uszkodzone (pakiet bez polecenia, poranny pull padał
„brak Shopify CLI”) - przeinstalowane, wersja 4.8.5.

Tłumaczenia: 15 pól na język na szablon (nadtytuł, hasło, napis przycisku, trzy akty),
przeniesione z `product.json` przez `translationsRegister`, dopasowane po digeście treści EN.

Sprawdzone na żywo: sekcja w HTML obu kolekcji na en, `/de-de/` i `/fr-fr/` (teksty w języku
rynku), zrzuty 1440 i 390 px - sekcja przylega do „Guild” i CTA.

**Jak cofnąć:** w edytorze obu szablonów ukryj albo usuń sekcję „The Long Night · sezon”.
Kod: tag `przed-tln-kolekcje-5e`.

---

## 2026-10-02

### Grafika kruka na czarnym tle do maili The Long Night w Plikach sklepu `[poza repo]`
Admin API, `stagedUploadsCreate` + `fileCreate` · Ustawienia → Pliki, `ln-ic-raven-night.png`

Sekcja maila „Kruk · pomoc” (pomoc w doborze rozmiaru i malowaniu) ma być zawsze na czarnym tle, a nie na
pergaminie (decyzja Jana, 02.10.2026). Nowa grafika kruka na nocy, adres dopisany do
`Black Friday 2026/11-edrone/obrazy/cdn.json`. Sprawdzone: adres zwraca 200. Przy okazji przebudowany mail
o sezonie w edrone i dwie nowe propozycje popupu sezonu - to pliki lokalne, sklepu nie dotyczą.

**Jak cofnąć:** Ustawienia → Pliki, `ln-ic-raven-night.png`, usuń (sekcja kruka w mailach straci obraz).

### 48 grafik do maili i popupów The Long Night w Plikach sklepu `[poza repo]`
Admin API, `stagedUploadsCreate` + `fileCreate` · Ustawienia → Pliki, nazwy `ln-*.jpg` / `ln-*.png`

Maile edrone wklejane jako HTML nie pokazywały obrazów, bo miały zastępczy adres `EDRONE-URL/...`
(zrzut Jana z edytora edrone, 02.10.2026). Wszystkie grafiki maili i popupów (hero, księżyce aktów,
ikony ofert, rwane krawędzie, ikony sociali, plansze z moodboardu TLN) są teraz w Plikach sklepu
i mają stałe adresy `cdn.shopify.com/.../files/ln-*`. Pliki są niewidoczne dla klientów, służą tylko
jako hosting obrazów. Mapa plik → adres: `Black Friday 2026/11-edrone/obrazy/cdn.json`.
Sprawdzone: wszystkie 48 adresów zwraca 200, w HTML maili nie został żaden `EDRONE-URL/`.

Dwie nowe ikony ofert (ruina wieży do DnD Terrain, zwój ze stalówką do Character Sheets)
wygenerowane w Recrafcie i wycięte lokalnie (`03-assets/elements/icons/ic-tower.png`, `ic-scroll.png`).

**Uwaga na przyszłość:** ponowne wgranie pliku o tej samej nazwie da w Plikach nową nazwę z sufiksem -
po zmianie grafiki trzeba odczytać nowy adres i zaktualizować `cdn.json`.

**Jak cofnąć:** Ustawienia → Pliki, filtr `ln-`, usuń zaznaczone (maile z tymi adresami przestaną
pokazywać obrazy).

## 2026-10-01

### Sekcja The Long Night na wszystkich stronach produktu
`6f1475d` · 10 szablonów `templates/product*.json` + tłumaczenia DE/FR `[poza repo]`

Sekcja sezonu (`long-night-season`, ta sama co na stronie bundli) stoi teraz na każdej stronie
produktu: pod ramą z zakładkami i paskiem „For DnD & Pathfinder Fans…”, nad „You may also like”
(w Character Sheet i Gift Card 2 nad „Explore our DnD Character Sheets 5e!”). Szablony:
domyślny, `dnd-dice`, `dnd-terrain`, `dnd-tiles`, `gift-card`, `gift-card-2`,
`mystery-box-product-page`, `pre-made-terrain-sets`, `starter-set-terrains`, `character-sheet`.

**Kod motywu bez zmian** - sekcja już była na sklepie, style ma zamknięte w ID sekcji. Do każdego
szablonu doszedł jeden wpis `section_longNightSeason` (kopia ze strony bundli) i jedno miejsce
w `order`, zaraz po `product_tabs_*`. Diff: same dopisania, zero usuniętych linii; każdy plik
po parsowaniu = stary + jedna sekcja.

Ustawienia: **akt I podświetlony** (decyzja Jana - październik), padding 40/40, link przycisku
pusty przy wdrożeniu - ustawia go Jan w edytorze (część szablonów ma już
`shopify://pages/the-long-night-rpg-guild-sale-season`, reszta czeka i do tego czasu ma `#`).

Tłumaczenia: 15 pól na język na szablon (nadtytuł, hasło, napis przycisku, trzy akty), przeniesione
ze strony bundli przez `translationsRegister`, dopasowane po digeście treści EN.

Sprawdzone na żywo w surowym HTML (`?view=<szablon>`): 10 szablonów × en, `/de-de/`, `/fr-fr/` -
miejsce, akt I, teksty w języku rynku. Odstępy na 390 i 1440 px identyczne z zaakceptowaną
wizualizacją (96 px od ramy do nadtytułu, sekcja 678 / 582 px).

**Na marginesie:** przy pullu wyszło, że szablony `t-character-sheet`, `test-2`
i `testowy-theme-product` zostały usunięte w panelu - zapisane w repo jako pull (`4b2d47b`).

**Uwaga przy testach:** `Accept-Language` w zapytaniu powoduje przekierowanie na rynek `en-pl` -
sprawdzając tłumaczenia przez `curl`/`urllib`, nie wysyłać tego nagłówka.

**Jak cofnąć:** w edytorze każdego szablonu produktu ukryj albo usuń sekcję
„The Long Night · sezon”. Kod: tag `przed-tln-produkty`.

### Kolekcja Spooky Miniatures po niemiecku i francusku `[poza repo]`
Admin API, `translationsRegister` · zasób `OnlineStoreThemeJsonTemplate/collection.spooky-collection`

Szablon kolekcji (sklonowany z Aarakocry) miał **zero** tłumaczeń DE i FR - cała strona poza
tytułem i opisem kolekcji szła po angielsku. Zarejestrowane 42 pola na język:
- 35 przejętych 1:1 z `collection.aarakocra-5e` (dopasowanie po digeście treści EN): FAQ,
  „Guild definition”, nagłówki listy produktów, promo Mystery Box, „Start your first quest”,
- 7 nowych: hero The Long Night (nadtytuł aktu I, opis, trzy USP, opis alternatywny figurki)
  i „All Spooky Miniatures:”. Terminy jak w Aarakocrze („Leicht zu bemalen”, „Facile à peindre”),
  nazwa aktu jak na landingu, nagłówek zgodny z istniejącym tytułem kolekcji
  („Gruselige Miniaturen”, „Miniatures effrayantes”).

Tytuł, opis i tytuł SEO samej kolekcji miały już tłumaczenia - bez zmian.
Sprawdzone na żywo w surowym HTML `/de-de/` i `/fr-fr/collections/spooky-miniatures`.

**Na przyszłość:** szablon sklonowany z innego nie dziedziczy tłumaczeń oryginału. Po każdym
klonie trzeba je przenieść (dopasowanie po digeście działa, bo klucze różnią się tylko nazwą szablonu).

**Jak cofnąć:** `translationsRemove` dla `de` i `fr` na tym zasobie albo w Translate & Adapt.

### Strona główna, hero: przycisk „The Long Night (Season SALE)”
`ef58fca` · `templates/index.json` (sekcja `section_mxgRNK`) + tłumaczenia DE/FR `[poza repo]`

Drugi przycisk obok „Your perfect miniature” (desktop od 1200 px), pod nim poniżej 1200 px,
pełna szerokość poniżej 480 px. Wygląd 1:1 z przyciskiem landingu sezonu (`.ln-cta`:
pergamin, srebrne okucie, Raleway wersalikami, hover w czerwieni księżyca), jedyna różnica:
zaokrąglenie 100px jak pierwszy przycisk. Link ustawia Jan.

**Zero zmian globalnych - żaden plik motywu nie był ruszany.**
- Przycisk to blok Jana `button_RKPYkx` (był wyłączony): włączony, `custom_class`
  `btn-2` → `ln-hero-cta`. `.btn-2` ma w `base.css` 10 właściwości z `!important`
  (bordowe tło, Rosarivo, `width:100%`), więc przycisk by je dziedziczył.
- Styl siedzi w bloku `custom_liquid_lnHeroCta` (typ `custom-liquid`) w tej samej kolumnie.
  Selektory przypięte do ID bloków (`__button_RKPYkx`, `__group_TGQ4iB`), nie do klas -
  ID nie podlega tłumaczeniu. Pusty kontener bloku chowa się sam (`:has`), więc nie dodaje odstępu.
- Układ obok siebie (grid) działa tylko w tej kolumnie i tylko gdy przycisk TLN jest włączony.
  Próg 1200 px, bo kolumna ma 55vw, a francuska etykieta potrzebuje 587 px obok pierwszego
  przycisku - przy 768 px przyciski rozpychały tytuł.
- Pierwszego przycisku celowo nie przeniesiono do nowej grupy: `base.css` (linie 177, 1578)
  celuje w pełną klasę `button--AZTUxMk5hbnNXQk1pW__button_TCN69m`, którą przeniesienie by zmieniło.

Sprawdzone przed wdrożeniem symulacją na żywej stronie (pomiar położenia wszystkich elementów
hero przed i po, 8 szerokości): od 1200 px nic poza nowym przyciskiem się nie przesuwa, poniżej
przesuwa się tylko „Main Collections” o wysokość przycisku. Po wdrożeniu: en, `/de-de/`,
`/fr-fr/` przy 1440 i 390 px.

Etykieta DE „Die Lange Nacht (Saison-SALE)”, FR „La Longue Nuit (Soldes de saison)”.

**Uwaga przy testach:** przeglądarka testowa z polskiego IP bywa przekierowywana na rynek
angielski i pokazuje angielskie etykiety także pod `/de-de/`. Tłumaczenia sprawdzać w surowym
HTML (`lang="de"`), nie po zrzucie.

**Jak cofnąć:** w edytorze wyłącz przycisk „The Long Night” i blok „The Long Night - styl
przycisku”. Kod: tag `przed-hero-tln-button`.

### Progi Custom Bundle 10 / 20 / 50 na stronie bundli
`6860568` · `templates/page.bundle.json` + tłumaczenia DE/FR `[poza repo]`

Decyzja Jana: obowiązują progi z landingu sezonu - 10 minis −10%, 20 −20%, 50 −30%.
Strona bundli mówiła co innego (5 / 10 / 20 za −10 / −15 / −30%), więc zmienione:
- baner: „Create a bundle of 20 and pay for 14!” → „Create a bundle of 50 and pay for 35!”,
- FAQ „How does the bundle discount work?”: nowe progi.

DE i FR obu pól odświeżone przez `translationsRegister` (stare tłumaczenia stały się nieaktualne
po zmianie EN). Copy baneru w warsztacie (`05-banners/app.js`) też poprawione, żeby kolejny
eksport nie przywrócił starej liczby. Sprawdzone na żywo na en, `/de-de/`, `/fr-fr/`.

**Poza motywem, po stronie Jana:** progi w aplikacji kreatora (EB Easy Bundle Builder) - to ona
liczy rabat i wyświetla „Add 5 product(s) to save 10%!”. Tekst strony i cena muszą się zgadzać.

**Jak cofnąć:** tag `przed-progi-bundle-10-20-50` + przywrócenie poprzednich tłumaczeń DE/FR.

### Landing The Long Night i marquee strony głównej po niemiecku i francusku `[poza repo]`
Admin API, `translationsRegister` · zasoby `OnlineStoreThemeJsonTemplate/page.long-night`,
`Page/165409587466` (tytuł landingu), `OnlineStoreThemeJsonTemplate/index` (marquee)

Landing sezonu nie miał żadnego tłumaczenia DE ani FR. Zarejestrowane 64 pola na język we
wszystkich czterech sekcjach: afisz, trzy akty, księga sezonu (daty, „Opens”, oferty, napisy
przycisków, opisy alternatywne ilustracji) i zapis na listy (etykiety, placeholdery, komunikaty,
zgoda z linkiem do Privacy Policy). Do tego tytuł strony. Pominięte celowo: `RPG Guild`, cyfry
rzymskie i linki `shopify://`. Nazwy aktów i zdania aktów identyczne jak na stronie bundli.

Marquee strony głównej: nowa pozycja `text_yiim4D` („100 $/€ = Free Character Sheets”, link
poprawiony przez Jana na `/products/dnd-character-sheets-all-13-in-color`) w formacie sąsiednich
pozycji: „100 $ oder € = Gratis-Charakterbögen”, „100 $ ou € = Fiches de personnage gratuites”.

Pełna lista tłumaczeń w trzech kolumnach: `Black Friday 2026/10-lp-sezon/tlumaczenia-de-fr.md`.

Sprawdzone na żywo: landing przez `/de-de/pages/cookies?view=long-night` i `/fr-fr/...`
(strona jest nieopublikowana), marquee na `/de-de/` i `/fr-fr/`.

Rozjazd progów Custom Bundle rozstrzygnięty tego samego dnia na 10 / 20 / 50 - patrz wpis wyżej.

**Jak cofnąć:** `translationsRemove` dla `de` i `fr` na tych zasobach albo ręcznie
w Translate & Adapt.

### Przecena Undead -5% i Spooky -10% `[poza repo]`

**Co:** dwie przeceny przez `compareAtPrice`, nalozone w kolejnosci Spooky -> Undead.

| Kolekcja | Rabat | Produkty | Warianty |
|---|---|---|---|
| `spooky-miniatures` | -10% | 12 | 210 |
| `undead-5e` | -5% | 628 z 637 | 9876 |

**Przeciecie:** 9 produktow nalezy do obu kolekcji. Decyzja Jana: wyzszy rabat wygrywa.
Zrealizowane przez kolejnosc - najpierw Spooky -10%, potem Undead -5%, ktory pominal
warianty majace juz `compareAtPrice`. Stad 628 zamiast 637 produktow w drugim przebiegu.

**Weryfikacja po operacji:** Undead 10086 wariantow - 9924 z -5%, 162 z -10%
(te 9 wspolnych), 0 bez przeceny. Spooky 210 wariantow - wszystkie -10%.

**Przerwanie w trakcie:** pierwszy przebieg Undead zatrzymal sie na 350/628. Wznowiony,
dokonczyl 228. UWAGA: ponowny `run` nadpisuje plik rollback wylacznie produktami jeszcze
nieprzecenionymi - przed wznowieniem zrobiono kopie i po zakonczeniu przywrocono pelna
liste 628 pozycji.

**Jak cofnac:** `shopify_discount_spooky.py rollback` i `shopify_discount_undead.py rollback`.
Pliki: `spooky_discount_rollback.jsonl`, `undead_discount_rollback.jsonl`. Nie kasowac.

---

### Przecena -15% na kolekcjach terrain `[poza repo]`

**Co:** 117 produktow, 1338 wariantow. `compareAtPrice` = dotychczasowa cena,
`price` = cena x 0,85. Suma cen 10 455,73 -> 8 886,68 (-15,01%).

**Zakres:** unia czterech kolekcji - `dnd-terrain` (117), `dnd-terrain-tiles` (100),
`modular-dnd-terrain-sets` (14), `modular-dnd-terrain-starter-sets` (3).
Kolekcja `dnd-terrain` pokrywa pozostale trzy, stad 117 unikalnych produktow.

**Swiadomie pominiete:** kolekcja `Terrain Elements` (`dnd-terrain-elements-miniatures`,
74 produkty / 1332 warianty) - na wyrazne zyczenie Jana. Przed operacja sprawdzono
przeciecie zbiorow: 0 wspolnych produktow. Po operacji potwierdzono: 0 wariantow
z `compareAtPrice`.

**Narzedzie:** `shopify_discount_terrain.py` - kopia sprawdzonego `shopify_discount_3pct.py`
ze zmieniona stawka (0.85), lista kolekcji i nazwami plikow.

**Weryfikacja:** probka 100 wariantow po operacji - 100/100 zgodnych z planem.

**Jak cofnac:** `python3 shopify_discount_terrain.py rollback`, czyta
`terrain_discount_rollback.jsonl`. NIE kasowac tego pliku.

**Skutek uboczny:** kolekcja "Miniatures on sale" filtruje po `Compare at price is set`,
wiec te 117 produktow sie w niej pojawi.

**Uwierzytelnianie:** apka `Price Manager` (`write_products`),
klucze w `~/.secrets/rpg-guild-shopify.env`.

---

### Podmiana filmow w banerze strony glownej - pazdziernik `[poza repo]`

**Co:** sekcja `hero_XFBPJU`, ustawienie `video_1`. Wrzesniowe filmy zastapione
pazdziernikowymi w trzech jezykach:

| Jezyk | Z | Na |
|---|---|---|
| EN | RPG Banner Film Sept 2026 ENG.mp4 | Stronka RPG Banner film 10_2026_ENG.mp4 |
| DE | RPG Banner Film Sept 2026 DE.mp4 | Stronka RPG Banner film 10_2026_DE.mp4 |
| FR | RPG Banner Film Sept 2026 FR.mp4 | Stronka RPG Banner film 10_2026_FR.mp4 |

**Gdzie:** EN w `templates/index.json` motywu live, DE i FR jako tlumaczenia zasobu
`OnlineStoreThemeJsonTemplate/index`. Skrypt `shopify_rpg_movie.py run`.

**Weryfikacja:** odczyt z API po operacji - wszystkie trzy wartosci wskazuja na wlasciwe
pliki, FR na plik z FR w nazwie (wrzesniowa pulapka nie wrocila).

**Uwaga o kluczu tlumaczenia:** pelny klucz ma sufiks digest, np.
`section.index.json.hero_XFBPJU.video_1:25npjs2877mvn`. Dopasowanie po samym
`section.index.json.hero_XFBPJU.video_1` nie zadziala - trzeba porownywac prefiksem.

**Cofniecie:** `rpg_movie_rollback.json` istnieje, ale wrzesniowe pliki zostaly
skasowane ze Shopify przez `run`. Powrot wymaga ponownego wgrania ich z dysku.

**Uwierzytelnianie:** apka dev `/rpg-movie`, scope `write_files, write_themes,
write_translations`. To NIE jest `Price Manager` (ten ma tylko `write_products`).

---

## 2026-09-30

### Strona bundli po niemiecku i francusku `[poza repo]`
Admin API, `translationsRegister` · zasób `OnlineStoreThemeJsonTemplate/page.bundle`
(motyw `182160195850`) i strona `gid://shopify/Page/165072371978`

Szablon strony bundli **nie miał żadnego tłumaczenia DE ani FR** - na `/de-de/` i `/fr-fr/`
cała strona szła po angielsku. Zarejestrowane 29 pól na język: baner (nadtytuł, hasło, dwa
rzędy wstępu - teksty zatwierdzone w `05-banners/app.js`), nagłówek i opis kreatora, cała
sekcja The Long Night (nadtytuł, hasło, przycisk, trzy akty), „Shop other:”, tytuł FAQ i trzy
pytania z odpowiedziami. Do tego tytuł strony (karta przeglądarki i Google). `handle` celowo
bez tłumaczenia, żeby nie zmieniać adresów.

Konwencja: DE na „du”, FR na „vous”, „Guild” zostaje jako nazwa. W FR twarde spacje przed
`? ! :` i w `5 000`, `38 mm`, `10 %`. Pominięte: wyłączony stary baner i pola techniczne
(`custom_class`, paddingi).

Sprawdzone na żywo: wszystkie nowe teksty obecne na `/de-de/` i `/fr-fr/`.

**Nie przetłumaczone i nie da się tego zrobić przez API Shopify:** aplikacja kreatora
(EB Easy Bundle Builder, Skai Lama). Jej napisy („Your Bundle:”, „Add To Cart”, „Choose the size
of your mini”) i nawet tytuły produktów idą po angielsku, choć produkty mają tłumaczenia DE/FR -
aplikacja ma wyłączony tryb wielojęzyczny. Włącza się go w panelu aplikacji:
Design Control Panel → Language → Multiple Language.

**Uwaga na przyszłość:** po zmianie tekstu EN w edytorze tłumaczenie nie aktualizuje się
samo - zostaje stara wersja oznaczona jako nieaktualna (`outdated`) i trzeba ją odświeżyć.

**Jak cofnąć:** `translationsRemove` z tymi kluczami dla `de` i `fr` albo ręcznie
w Translate & Adapt (Motyw → szablon `page.bundle`).

### Strona bundli: baner akt II z żywym tekstem, sekcja sezonu na mobile, przycisk z landingu
`9ab44c1` · `sections/long-night-hero.liquid`, `sections/long-night-season.liquid`,
`templates/page.bundle.json`

Makieta zaakceptowana przez Jana: `Black Friday 2026/05-banners/bundle-page-mobile.html`.

**Baner.** Obraz z wypalonym tekstem (`section_6kDNaa`, tło
`bundles-shop-rosarivo-en-alpha.webp`) jest w szablonie **wyłączony, nie usunięty**.
Na jego miejscu stoi `hero_longNightBundle` (sekcja `long-night-hero`): tekst w ustawieniach,
więc DE i FR idą przez Translate & Adapt zamiast przez osobne grafiki. Nadtytuł
„Act II · Blood Moon · Black Friday · November”, księżyc ociekający krwią na osi nad
nadtytułem, bez herbu. Na mobile rama pionowa `long-night-hero-frame-mobile.webp` - wcześniej
telefon dostawał szeroki obraz przycięty `cover`, który ucinał hasło z obu boków.
W „pre‑made” jest dywiz niełamiący (U+2011), inaczej wiersz łamał się na „pre-”.

Sekcja `long-night-hero` dostała trzy ustawienia: *Mobile: rama pionowa z motywu*,
*Układ znaków* (herb i księżyc w rogach / sam księżyc nad nadtytułem), *Faza księżyca*.
Domyślne wartości zachowują kadr wyjściowy. Sekcja nie była wcześniej użyta w żadnym szablonie.

**Sekcja The Long Night.** Desktop bez zmian poza przyciskiem. Przycisk jest 1:1 z landingu
sezonu (`.ln-cta`: pergamin, srebrne okucie z fazą, hover w czerwieni księżyca) na desktopie
i mobile. Bieżący akt: II. Mobile (poniżej 750 px) zamiast awaryjnego stosu kafli: oś pionowa,
księżyc 64 px po lewej, tekst po prawej, **bez plam krwi** (decyzja Jana). Wysokość sekcji
na telefonie spadła z ok. 1680 px do ok. 700 px.

Dwie rzeczy, które nie są oczywiste:
- **Oś biegnie pod księżycami, a nie przez nie.** Przygaszenie aktu idzie na tekst i sam
  księżyc, nie na cały kafel - półprzezroczysty kafel pokazywał linię osi przez tarczę.
  Pod tarczą leży krążek pergaminu, nad i pod nią 8 px przerwy. Pełne pole pergaminu
  wycinało prostokąt z tła, więc tylko krążek i wąski pasek.
- **Opakowanie `.ln__orb` na desktopie ma `display:contents`** - istnieje tylko dla osi mobilnej.

Pionowa nitka nad i pod księżycem zaćmienia jest w samym pliku
`long-night-moon-eclipse.webp`, nie w kodzie.

Szablon edytowany na wersji pobranej ze sklepu tego samego dnia (commit `9c6b21c`,
zdania aktów zmienione wcześniej w edytorze zachowane). Push: najpierw sekcje, potem szablon,
treść szablonu sprawdzona na serwerze. Zweryfikowane na żywo na en, `/de-de/` i `/fr-fr/`
(1440 px i 390 px).

Tłumaczenia DE i FR baneru zrobione tego samego dnia - patrz wpis „Strona bundli po niemiecku
i francusku”. CTA sekcji dalej celuje w Mystery Box, bo landing sezonu jest niepublikowany.

**Jak cofnąć:** w edytorze szablonu strony bundli włącz stary baner i wyłącz
„The Long Night · hero”; akt bieżący przestaw w sekcji sezonu. Kod: tag
`przed-bundle-mobile-akt2`.

### Tiamat - dokończenie cofnięcia przeceny `[poza repo]`

**Co:** produkt `Tiamat 5e | DnD Tiamat Queen of Dragons Miniature`
(`gid://shopify/Product/8539037827338`), 12 wariantów: `price` <- `compareAtPrice`,
`compareAtPrice` -> null. Przykład: 124,45 / 128,30 -> 128,30 / brak.

**Dlaczego osobno:** tego produktu NIE było w `discount_rollback.jsonl`, mimo że przecena
-3% go objęła (stosunki cen wynosiły dokładnie 0,97). Główny rollback go pominął, bo skrypt
cofa wyłącznie to, co znajdzie w pliku. Zgłoszone przez Jana po weryfikacji na sklepie.

**Jak cofnąć:** `tiamat_rollback.json` w katalogu projektu trzyma stan sprzed zmiany
(wszystkie 12 wariantów z cenami i compareAtPrice).

**Weryfikacja:** pełny skan katalogu po operacji - 6626 produktów, 0 z ustawionym
`compareAtPrice`. Kolekcja "Miniatures on sale" pokazywała jeszcze chwilę `1`,
bo smart collection przelicza się z opóźnieniem.

**Wniosek na przyszłość:** po każdej masowej operacji cenowej sprawdzać cały katalog
skanem, a nie ufać kompletności pliku rollback.

---

### Cofnięcie przeceny -3% na katalogu `[poza repo]`

**Co:** przywrócono ceny sprzed przeceny -3% z 2026-08-28 i wyczyszczono `compareAtPrice`.
634 produkty, 11 064 warianty. Suma cen 206 142,36 -> 212 507,50 (+3,09%).

**Gdzie:** Shopify Admin API, mutacja `productVariantsBulkUpdate`. Nie dotyczy kodu motywu.
Uruchomione skryptem `shopify_discount_3pct.py rollback` ze źródłem `discount_rollback.jsonl`.

**Dlaczego:** decyzja Jana - powrót do cen bazowych.

**Skutek uboczny:** kolekcja "Miniatures on sale" filtruje po `Compare at price is set`,
więc te 634 produkty z niej wypadły.

**Weryfikacja:** przed operacją 25 losowych wariantów zgadzało się co do grosza ze stanem
po przecenie (nikt ich nie ruszał od sierpnia). Po operacji 150 losowych wariantów: 150/150
z ceną bazową i pustym `compareAtPrice`. Skrypt: 634/634 produktów, 0 błędów.

**Uwaga:** pierwsze uruchomienie zostało przerwane po ~73% (110/150 w próbce). Skrypt jest
idempotentny, więc powtórzenie dokończyło resztę bez skutków ubocznych.

**Jak cofnąć:** `python3 shopify_discount_3pct.py run` nałoży przecenę od nowa
(pomija warianty, które już mają `compareAtPrice`, więc nie zrobi rabatu na rabat).

**Uwierzytelnianie:** nowa apka dev `Price Manager` (scope `write_products`),
dane w `~/.secrets/rpg-guild-shopify.env`. Stare wpisy w `~/.zshrc` wskazują na apkę
bez ważnej instalacji i dają HTTP 401 - do usunięcia.

---

## 2026-09-30

### Hero kolekcji Spooky Miniatures w stylu The Long Night
`sections/long-night-collection-hero.liquid` · `templates/collection.spooky-collection.json` ·
`assets/ln-mini-pumpkin-knight-duotone.webp` · `assets/long-night-hero-frame-mobile.webp`

Nowa sekcja hero dla kolekcji sezonu: rama rozbryzg / przełom z banneru bundli
(`long-night-hero-frame.webp`, już w motywie), tekst po lewej, figurka po prawej,
kości w jednym rzędzie - układ dotychczasowych hero kolekcji. Figurka (dyniowy
rycerz) wycięta z tła Recraftem i przepuszczona przez duotone TLN
(`03-assets/tools/texture.py`, gamma 1.8, lift .18). Za nią sierp księżyca aktu I
w lustrze i kałuża nocy. Tekst w ustawieniach (tłumaczalny), pusty nagłówek =
tytuł kolekcji. Skala w `cqw` z kanwy 1920 x 892, poniżej 750 px kolumna na ramie
mobilnej. Warsztat: `05-banners/spooky-collection.html`.

W szablonie kolekcji nowa sekcja stoi przed dotychczasowym hero, a stare hero
(`section_tJEjwT`, sklonowane z Aarakocry) jest **wyłączone, nie usunięte**.
Szablon edytowany na wersji pobranej ze sklepu 2026-09-30 (zmiany z panelu z tego
samego ranka zachowane).

**Poprawka tego samego dnia:** tło sekcji przezroczyste (poza rwanymi
krawędziami ramy widać stronę; ziarno zostaje w samej ramie). Mobile według
`05-banners/spooky-collection-mobile.html`: rama pionowa 750 x 1338, bez
nadtytułu, kości jako suwak w bok jak dotychczasowy `.kosci-slider`.

**Jak cofnąć:** w edytorze szablonu kolekcji włącz stare hero i wyłącz „The Long
Night · kolekcja". Kod: tag `przed-spooky-hero` (`adf049f`).

---

## 2026-09-24

### Automat raportowania nie wysyłał maili - naprawione `[poza repo]`
`.github/workflows/dziennik-zmian.yml`, hook `post-commit`

Kontrola wykazała dwie usterki, obie ciche.

**1. Harmonogram GitHuba nie trzyma godziny, a bramka to dusiła.**
Workflow miał dwa crony (06:00 i 07:00 UTC) i wysyłał tylko wtedy, gdy lokalna
godzina wynosiła równo 8 - po to, by nie wysłać dwóch maili dziennie. GitHub
odpalił oba przebiegi 23.09 dopiero o **12:00 i 14:00** czasu polskiego, więc
bramka uznała je za zdublowane i **nie wysłała nic**. Od uruchomienia automatu
nie poszedł ani jeden zaplanowany mail - wyszły tylko trzy ręczne testy z 22.09.

Poprawka: **jeden cron `7 6 * * *`, zero bramek**. Lepiej dostać raport
z opóźnieniem niż nie dostać go wcale. Minuta celowo nie jest równa - o pełnych
godzinach kolejka GitHuba jest najdłuższa.

Harmonogram GitHuba jest best-effort. Opóźnienie rzędu godzin jest normalne
i nie da się go wyeliminować na darmowym planie.

**2. Dziewięć commitów siedziało lokalnie i nigdy nie trafiło na GitHub.**
Prace nad landingiem The Long Night (23.09 19:08 → 24.09 10:46) były
zacommitowane, ale niewypchnięte. Workflow czyta historię **na GitHubie**, nie
na dysku - więc te zmiany nie istniały ani dla dewelopera, ani dla raportu.

Poprawka: hook `post-commit` w repozytorium pcha na `origin main` po każdym
commicie. Działa tylko na `main`, pomija stan rebase/merge/cherry-pick i nigdy
nie przerywa commita, nawet gdy push padnie. Hook jest lokalny (`.git/hooks/`),
więc nie wersjonuje się - przy klonowaniu repo na inną maszynę trzeba go założyć
ponownie.

**Dla dewelopera:** jeśli mail przyjdzie później niż rano, to jest kolejka
GitHuba, nie awaria. Jeśli nie przyjdzie wcale mimo commitów - sprawdź zakładkę
Actions.

---

## 2026-09-23

### Landing The Long Night - poprawki po przeglądzie Jana
`sections/long-night-lp-{doors,book,signal}.liquid` · `templates/page.long-night.json` ·
`assets/ln-lp-foot.webp`

- **Jaśniejszy pas pod kartami** - w miejscu, gdzie karty zachodzą na afisz,
  leżały dwie warstwy ziarna (afisza i kart). Ziarno kart zaczyna się teraz
  dopiero pod zakładem.
- **Formularz zbiera imię** (`contact[first_name]`) obok e-maila.
- **Zgoda z linkiem do Privacy Policy** włączona (wymagana), zastępuje notę pod
  formularzem.
- **„Send word when it opens" → „Get notified"** na przyciskach zamkniętych aktów.
- **Koniec strony: dół banneru bundli** (`04-export/banners/bundles-shop-rosarivo-en-alpha`,
  wycięty poniżej tekstu, wariant z kroplami). Maska chowa górę pasa, więc
  czerwień i krew są tylko przy rwanej krawędzi. Stary pas w kolorze stopki
  zostaje jako przełącznik, domyślnie wyłączony.

### Landing The Long Night bez menu i stopki sklepu
`sections/long-night-lp-poster.liquid` · `templates/page.long-night.json`

Afisz dostał przełącznik **„Ukryj menu i stopkę sklepu"** (domyślnie wyłączony,
włączony tylko w szablonie `page.long-night`). Chowa `display:none` trzy
elementy z `layout/theme.liquid`: `#header-group` (pasek promocji, menu,
separator), `.breadcrumbs` (pas „Home") i `.shopify-section-group-footer-group`
(rząd zaufania, stopka). Sprawdzone na żywym sklepie: selektory łapią tylko te
elementy, żadna sekcja landingu nie siedzi w środku.

**Nie jest to osobny layout**, celowo: skrypty z `theme.liquid` (cookies,
Edrone, analityka, aplikacje) ładują się bez zmian - chowamy wygląd, nie kod.
Reguła istnieje tylko na stronie, na której renderuje się afisz. Na landingu
włączona jest też górna belka afisza (herb + „Back to shop"), a rwana krawędź
na końcu zapisu jest wyłączona, bo bez stopki prowadziłaby do pustego pasa.

**Pułapka przy pushu:** sekcja i szablon poszły jednym pushem, szablon doszedł
pierwszy i Shopify sprawdził go względem STAREGO schematu afisza - nieznane
jeszcze `hide_shop_chrome` zostało po cichu wycięte, bez błędu. Pomógł drugi
push samego szablonu. Zasada: nowe ustawienie sekcji → najpierw sekcja, potem
szablon, i sprawdzenie treści szablonu na serwerze.

**Zweryfikowane na żywo:** na landingu menu, pas „Home" i stopka mają
`display:none`, Edrone się ładuje. Na stronie głównej i `/pages/cookies`
menu i stopka bez zmian, arkusz landingu nie jest tam w ogóle wczytywany.

**Jak cofnąć:** w edytorze, na afiszu, odznacz „Ukryj menu i stopkę sklepu".

### Strona „The Long Night" dostała szablon `long-night` `[poza repo]`
Admin API, `pageUpdate` · strona `gid://shopify/Page/165409587466`
(`/pages/the-long-night-rpg-guild-sale-season`)

`templateSuffix`: `page` → `long-night`. Strona **zostaje niepublikowana**,
publicznie zwraca 404. Ukrytej strony nie da się podejrzeć nawet zalogowanym,
więc do sprawdzania wyglądu służy dowolna opublikowana strona z parametrem
`?view=long-night`, np. `/pages/cookies?view=long-night`.

**Jak cofnąć:** w panelu przy stronie przestaw szablon na `page` albo
`pageUpdate` z `templateSuffix: "page"`.

### Landing sezonu The Long Night - cztery sekcje, arkusz, skrypt i szablon
`assets/long-night-lp.css` · `assets/long-night-lp.js` ·
`snippets/long-night-lp-base.liquid` ·
`sections/long-night-lp-{poster,doors,book,signal}.liquid` ·
`templates/page.long-night.json` · 12 assetów `assets/ln-lp-*.webp`

Przeniesienie zatwierdzonego prototypu landingu sezonu (październik - grudzień
2026) z warsztatu do motywu. **Same nowe pliki - żaden istniejący plik motywu
nie został ruszony.** `long-night-hero.liquid` i `long-night-season.liquid`
zostają nietknięte; ta druga dalej stoi na `templates/page.bundle.json`.

**Dlaczego cztery sekcje, a nie jedna.** Pod sekcją zapisu na listy ma usiąść
Edrone, więc ona ma się nie zmieniać. Afisz i księga zmieniają się co miesiąc,
gdy sezon przechodzi do następnego aktu. Osobne pliki znaczą, że podmiana
afisza nie dotyka formularza.

| Plik | Rola |
|---|---|
| `long-night-lp-poster` | afisz - kadr aktu, tytuł, zdanie wprowadzające |
| `long-night-lp-doors` | trzy karty aktów, podciągnięte na afisz |
| `long-night-lp-book` | księga - mechanika aktów, zamykanie nieruszonych |
| `long-night-lp-signal` | zapis na listy, natywny `form 'customer'` |

**Warstwa wspólna w jednym miejscu.** `long-night-lp.css` trzyma tokeny
kampanii i prymitywy (przycisk, miara strony, nadtytuł, wejście sekcji);
wstawia go snippet `long-night-lp-base`, renderowany przez każdą z czterech
sekcji. Zmiana przycisku to jedna edycja, nie cztery. Wszystko - łącznie
z tokenami - jest zamknięte w klasie `.ln-lp`, więc nic nie wychodzi poza
landing. Klasy dostały przedrostek `ln-`, bo `.wrap`, `.cta` czy `.form`
z prototypu zderzyłyby się z motywem.

**Akt liczy Liquid, nie JavaScript.** W prototypie stan sezonu jechał
z `?act=` i wyliczał go skrypt. Tutaj akt jest ustawieniem sekcji, więc
właściwy kadr i zamknięte wpisy są już w wyrenderowanym HTML-u: przeglądarka
pobiera jeden kadr afisza zamiast trzech (~0,8 MB mniej), nie ma mignięcia
odsłoniętej treści, a treść zamkniętego aktu nie jedzie do DOM-u jako
czytelny tekst.

**Formularz jest natywny** - `{% form 'customer' %}` z `contact[email]`
i tagiem `newsletter`, czyli droga, którą Shopify zapisuje subskrybenta
i z której bierze go Edrone. Skrypt nie przechwytuje submitu; dokłada tylko
podpowiedź przy literówce i napis "wysyłam". Gdy padnie, formularz działa.

**Tekst w ustawieniach, nie w markupie** - pola `text` / `inline_richtext`
Translate & Adapt wystawia jako treść motywu, więc rynki de i fr da się
obsłużyć bez przepisywania sekcji.

**Obrazy dwutorowo:** 12 plików `ln-lp-*.webp` (2,1 MB) leży w assetach
i renderuje się od razu po wgraniu, a każdy da się nadpisać `image_picker`-em
w edytorze bez pushu.

**Wejście sekcji nie zależy od skryptu.** Karty i księga pojawiają się
z krótkim wjazdem, ale ukrycie przed wjazdem działa tylko pod `html.ln-js`,
który snippet stawia inline przed treścią. Bez skryptu treść stoi widoczna
od początku, a po trzech sekundach bezpiecznik `ln-shown` pokazuje wszystko.
(W pierwszej wersji skrypt nie był nigdzie wstawiony, więc karty i księga
zostałyby niewidoczne - wyłapane przed pushem.)

**Pułapka przy pierwszym pushu:** serwer odrzucił `long-night-lp-signal`,
bo pole `text` miało `"default": ""` - Shopify nie przyjmuje pustego defaultu,
a lokalny `theme check` tego nie łapie. Szablon odpadł razem z nią, bo
odwoływał się do nieistniejącej sekcji. Pozostałe 18 plików weszło.

**Jak cofnąć:** wszystkie pliki są nowe, więc `git rm` tych ścieżek albo powrót
do tagu `przed-lp-long-night` (`ebf2d46`). Na sklepie: odepnij szablon
`long-night` od strony - sekcje przestają się renderować, nic innego nie zależy
od tych plików.

`theme check`: zero uwag na nowych plikach. Jedyne, co się odzywa, to
`OrphanedSnippet` na `long-night-lp-base` - fałszywy alarm, ta kontrola sypie
się w tym motywie na 109 snippetów, w tym na `add-to-cart-button`
i `breadcrumbs`.

---


### Rząd USP w koszyku - desktop przestał się łamać
`dbeb77f` · `assets/base.css`

Na desktopie tekst przy ikonach łamał się na dwie linie i rozjeżdżał układ.
Dwie niezależne przyczyny:

**1. Progi patrzyły na szerokość okna, a decyduje szerokość rzędu.**
Z produktami w koszyku strona przechodzi na dwie kolumny i rząd USP dostaje
znacznie mniej miejsca, niż sugeruje ekran:

| okno | szerokość rzędu |
|---|---|
| 1749px | 1012px |
| 1440px | 901px |
| 1200px | **681px** |
| 768px | **265px** |

Reguła „od 1200px cztery kolumny" wywalała się dokładnie przy 1200 i 768.

**2. Równe kolumny dawały każdemu USP tyle samo.** W koszyku zmieniono tekst -
`VAT incl.` ustąpiło `Free shipping over 60 $/€`, które potrzebuje 257px.
Przy kolumnie 232px łamało się na dwie linie, a `Made in EU` marnowało 100px.

**Rozwiązanie:** flex z zawijaniem i `space-between`, **bez ani jednego progu**.
Liczba USP w rzędzie wynika z realnie dostępnego miejsca, każdy zajmuje tyle,
ile potrzebuje.

Zmierzone na żywo z produktami w koszyku: rząd 1012 → 4 w rzędzie (odstępy
82/83/83), 901 → 4 (46/45/46), 681 → 3+1 (44/44), 265 → po jednym.
Wszędzie wysokość 25px, zero łamania, zero poziomego paska. Mobile nietknięte.

**Dla dewelopera:** jeśli kiedyś dojdzie piąty USP albo dłuższy tekst - nic nie
trzeba zmieniać. To był cały sens rezygnacji z progów.

**Cofnięcie:** `git checkout przed-usp-flex-fix -- assets/base.css`

---

## 2026-09-21

### Podmiana zdjęcia „Custom Production" na nową halę drukarek
`7f935fb` · 10 szablonów produktu

Stare zdjęcie występowało w **dwóch wariantach o niepowiązanych nazwach**:

| stary plik | wymiary | liczba szablonów |
|---|---|---|
| `Product_Page_Welcome_to_our_Guild_2.webp` | 1000×1000 | 6 |
| `Frame_1984077855.png` | 576×465 | 4 |

Drugi wariant nie ma w nazwie nic, co wiązałoby go z pierwszym. Znaleziony przez
mapowanie *obraz → najbliższy podpis pod nim*, nie po nazwie pliku. Szukanie po
nazwie znalazłoby połowę.

Nowe pliki w Shopify Files `[poza repo]`:
- `Product_Page_Custom_Production_2026.webp` - 1000×1000
- `Custom_Production_2026_landscape.webp` - 576×465

Stary plik mimo rozszerzenia `.webp` był w środku JPEG-iem 1000×1000, więc
proporcja się zgadza i layout się nie zmienił. Zaokrąglenie rogów robi CSS,
nie obraz.

Zweryfikowane na żywo: EN, DE, FR - zero wystąpień obu starych plików na całym
sklepie. Tłumaczenia nie miały nadpisań obrazu, więc podchwyciły nowe samo.

**Cofnięcie:** `git checkout przed-podmiana-foty-produkcja -- templates/` + push.
Stare pliki zostają w Shopify Files nietknięte.

**Uwaga dla dewelopera:** produkty z sufiksami `terrains`, `terrain-town-market`
i podobnymi renderują się przez **domyślny** `product.json`, bo pliki
`product.<sufiks>.json` dla nich nie istnieją. Te sufiksy są martwe.

---

## 2026-09-18

### Sekcja „The Long Night" na stronie bundli
`5442df5` `8144c85` `1df7907` `c909a09` · `sections/long-night-season.liquid`, `templates/page.bundle.json`

Nowa sekcja sezonu: oś trzech aktów, tekst w ustawieniach (tłumaczalny przez
Translate & Adapt), plamy krwi jako osobne assety bez tła.

Wstawiona między blok kreatora bundli a nagłówek „Shop other:". Padding 40/40.

Dwie pułapki, które kosztowały poprawkę:
- **Akty to bloki sekcji**, definiuje je `preset`. Instancja napisana ręcznie bez
  bloków renderuje sam nagłówek i CTA - oś aktów znika.
- **Dwa różne ustawienia paddingu o różnych typach.** `padding_top` jest typu
  `text` i wymaga stringa `"40"`; `padding-block-start` jest typu `range`
  i wymaga liczby `40`. Pomyłka psuje szablon.

CTA prowadzi na `shopify://pages/dnd-mystery-box` - tymczasowo, do czasu powstania
landingu sezonu. Forma `shopify://` jest obowiązkowa: adres względny nie dostaje
prefiksu rynku i klient z `/de-de/` ląduje na rynku amerykańskim.

**Cofnięcie:** tag `przed-long-night-bundle`.

### Nagłówek „Shop other:" na stronie bundli
`6cc81d0` · `templates/page.bundle.json`

Klon istniejącego nagłówka strony (`section_9DNaRd`), ta sama klasa
`title use-rosarivo`, preset `h2`, kolor `var(--color-foreground-heading)`.
Padding zmieniony ze 100/36 na 40/40, bo wzór stoi na górze strony.

**Cofnięcie:** tag `przed-shop-other`.

### Audyt spójności komunikacji - wysyłka, zwroty, cło
`fbc582d` `1f5569a` · `blocks/_product-details.liquid`, `templates/product*.json`, `templates/page.bundle.json`

Znalezione i naprawione sprzeczności między treścią na stronie a politykami:

| co | było | jest |
|---|---|---|
| próg darmowej wysyłki w `_product-details.liquid` | `$50` | `$60` |
| próg na karcie produktu | „**Global** free shipping over 60 $/€" | bez słowa „Global" |
| czasy wysyłki w FAQ strony bundli | „up to 10 business days" | per region: 5-8 UE, 10-14 USA |

Próg zweryfikowany w `deliveryProfiles`: 60 EUR / 60 USD, a w innych walutach
120 PLN, 53 GBP, 56 CHF, 90 AUD, 96 CAD. Słowo „Global" było nieprawdą.

**Ustalenia, które obowiązują w całej komunikacji:**
- produkcja: **5-7 dni roboczych** (nie 5-10)
- dostawa: osobno, per region - PL 2-4, UE 5-8, CH 8-10, USA 10-14, UK 10-15, AU 14-21, CA 21
- zwroty: **30 dni bez pytań**, obejmuje też produkty custom
- cło USA: **pokrywa RPG Guild**

### Polityki sklepu przepisane `[poza repo]`
Wklejone ręcznie w Shopify admin → Settings → Policies

Polityka wysyłki i zwrotów nie są w repozytorium - to ustawienia sklepu.
Konektor nie ma scope'a `write_legal_policies`, więc zmiana była ręczna.

Co się zmieniło: produkcja 5-10 → 5-7 dni; „Poczta Polska, do 10 dni" →
tabela per region; jeden przewoźnik → pełna lista (DHL, La Poste, Bpost,
PostNord, Posti, Hellenic Post, Canada Post, InPost, Poczta Polska); tracking
z `poczta-polska.pl` → `parcelsapp.com`; dopisany próg darmowej wysyłki;
usunięta sekcja „Import Tariffs & Customs Notice (USA)"; zwroty custom
i wyprzedażowych odblokowane, jedyny wyjątek to karty podarunkowe.

Źródło do ponownego wklejenia: `docs/polityki/*.html` w folderze projektu.

### Rząd USP w koszyku - mobile i desktop
`bac2a4d` `5d9df6e` `568bf9c` `eb3faae` `a225068` · `assets/base.css`, `templates/cart.json`

**Mobile:** cztery USP zawijały się do trzech rzędów (112px). Teraz jeden rząd
34px, przewijany palcem, ze `scroll-snap: x proximity` i automatycznym przesuwem
~21 px/s (skrypt w bloku `custom-liquid` w szablonie koszyka, pauzuje na dotknięcie,
respektuje `prefers-reduced-motion`).

**Desktop:** `display: grid` zamiast flexa - 4 równe kolumny od 1200px, 2 poniżej.
Próg 1200 jest dobrany **pod niemiecki**, nie pod angielski: najszerszy USP to
`30 Tage Rückgaberecht` (233px) wobec 205px w EN i FR. Przy progu 1024 niemiecki
się łamał.

**Nowe teksty:** Made in EU · Worldwide Shipping · 30 Days Returns · VAT incl.
Tłumaczenia DE i FR zarejestrowane przez `translationsRegister` `[poza repo]`.

> **PUŁAPKA, KTÓRA KOSZTOWAŁA CAŁY DEPLOY.** W `assets/base.css` linia ~12517
> otwiera `.swym-storefront-layout-notification-message {` i **nigdy jej nie
> zamyka** - od tej linii do końca pliku jest 16 `{` na 15 `}`. Wszystko dopisane
> na koniec pliku ląduje zagnieżdżone w tej regule i **nie działa**, mimo że plik
> poprawnie wjeżdża na CDN i widać go w źródle. Nowy CSS wstawiać **przed** tą
> linią. Numer linii dryfuje przy pullach - szukać po nazwie klasy.

**Cofnięcie:** tagi `przed-usp-slider-2`, `przed-usp-desktop`.

### Naprawa presetu blokującego push
`d861719` · `blocks/_product-details.liquid`

Push zwracał `Invalid preset "t:names.details": invalid block type "group":
undefined setting 'custom_width'`. Przyczyna: `blocks/group.liquid` definiuje
`custom_width_unit` i `custom_width_value`, ale nie samo `custom_width`.
Preset ustawiał je na trzech zagnieżdżonych blokach `group`.

Błąd był starszy niż zmiana, która go ujawniła - plik po prostu nie był
pushowany od czasu zmiany schematu bloku `group`.

### Hero „The Long Night"
`25418e9` `17e9402` `93d87db` · `sections/long-night-hero.liquid`

Sekcja hero z tekstem w ustawieniach zamiast wypalonego w grafice - trzy języki
to trzy zestawy tłumaczeń, a nie trzy komplety plików.

---

## Automatyzacja i środowisko `[poza repo]`

### Pull motywu przeniesiony z launchd do hooka sesji - 2026-09-18

Agent launchd `com.jan.rpg-guild.theme-pull` miał pullować motyw codziennie o 8:00.
**Nie zadziałał ani razu** od instalacji 16.09: `~/Documents` jest chronione przez
macOS TCC, agent launchd nie ma uprawnienia „Files and Folders" i padał z
`Operation not permitted` oraz kodem 126, zanim wykonał pierwszą linijkę.
W logu zero wpisów z godziny 08:0x.

Pull przeniesiony do hooka `~/.claude/hooks/rpg-guild-theme-freshness.sh`
(SessionStart), który przechodzi przez TCC jako proces potomny aplikacji.
Warunki: repo czyste **i** ostatni pull starszy niż 12h. Limit 120s.

Agent wyłączony, plist zarchiwizowany w `automation/wylaczone/` z opisem diagnozy.

**To jest ważne przy planowaniu czegokolwiek cyklicznego na tym Macu:**
launchd nie dosięgnie plików w `~/Documents` bez nadania Full Disk Access
dla `/bin/bash`.

---

## Znane, otwarte

1. **Czechy: próg darmowej wysyłki 740 CZK** (~30 EUR zamiast 60) i płatna
   stawka obowiązująca do 1450 CZK - zakres 740-1450 CZK łapie obie stawki.
   Do poprawy w ustawieniach wysyłki Shopify.
2. **Cło USA - DDP do potwierdzenia u przewoźnika.** Polityka obiecuje, że
   RPG Guild pokrywa cło i handling. Jeśli paczki nie jadą DDP, klient dostanie
   rachunek mimo tego zapisu.
3. **Autoplay USP w koszyku** - nigdy nie sprawdzony na fizycznym telefonie.
   Nie da się tego zweryfikować z panelu przeglądarki, bo `requestAnimationFrame`
   nie dostaje klatek w ukrytej karcie.
4. **Landing sezonu nie istnieje** - CTA sekcji The Long Night celuje tymczasowo
   w Mystery Box.
5. **Wariant poziomy nowego zdjęcia** (`Custom_Production_2026_landscape.webp`)
   jest podstawiony w czterech szablonach terenów, których nie używa żaden
   produkt. Dziś to martwy kod.

---

## Jak działa ten dziennik

**Repozytorium:** https://github.com/JanoMinesotaa/rpg-guild-theme
**Ten plik na surowo:** https://raw.githubusercontent.com/JanoMinesotaa/rpg-guild-theme/main/rpg_guild_changelog.md

Plik jest publiczny, więc można go wkleić do dowolnego czatu jako link - nie
wymaga logowania ani konta na GitHubie.

**Codzienny mail o 8:00** - workflow `.github/workflows/dziennik-zmian.yml`
zbiera commity z poprzedniego dnia kalendarzowego i wysyła je mailem.
Gdy zmian nie było, mail nie idzie w ogóle.

GitHub Actions zna tylko UTC, a 8:00 w Polsce to 06:00 UTC latem i 07:00 zimą.
Dlatego workflow odpala się dwa razy, a wysyłka jest bramkowana sprawdzeniem
lokalnej godziny w strefie `Europe/Warsaw` - mail wychodzi raz dziennie,
o 8:00 czasu polskiego, przez cały rok.

Wysyłka idzie przez `smtplib` w `.github/scripts/dziennik_maila.py`, bez
zewnętrznych akcji z marketplace'u - w publicznym repo cudza akcja miałaby
dostęp do sekretów skrzynki.

**Sekrety repo, które muszą być ustawione:** `MAIL_SERVER`, `MAIL_PORT`,
`MAIL_USERNAME`, `MAIL_PASSWORD`, `MAIL_TO`, opcjonalnie `MAIL_CC`.

**Test bez czekania do rana:** zakładka Actions → „Dzienny raport zmian" →
Run workflow. Ręczne uruchomienie omija bramkę godzinową.

### Ograniczenie, o którym trzeba wiedzieć

Mail czyta **wyłącznie `git log`**. Zmiana zrobiona przez Admin API, MCP albo
klikiem w panelu Shopify - polityki sklepu, tłumaczenia, pliki, ustawienia
wysyłki - nie zostawia commita, więc sama z siebie do maila nie trafi.

Dlatego obowiązuje zasada: **każda taka zmiana dostaje wpis w tym pliku,
oznaczony `[poza repo]`, i jest commitowana.** Commit z dopiskiem jest tym
śladem, który wpada do porannego maila.

Jeśli w dzienniku widzisz lukę - zmianę na sklepie, której tu nie ma - to znaczy,
że zasada została złamana, a nie że automat zawiódł.
