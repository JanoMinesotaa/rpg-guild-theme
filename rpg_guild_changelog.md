# Dziennik zmian - motyw RPG Guild

Motyw `RPG GUILD theme 2025`, ID `182160195850`, sklep `rpg-guild.myshopify.com`.

Zapis prowadzony dla dewelopera. Każdy wpis mówi **co**, **gdzie**, **dlaczego**
i **jak cofnąć**. Zmiany wykonane poza repozytorium - przez Admin API, MCP albo
ręcznie w panelu Shopify - są oznaczone `[poza repo]`, bo nie ma po nich commita.

Konwencja: najnowsze na górze.

---

## 2026-10-31 (wieczor, 5)

### Kolekcja DnD Gifts: opis w hero nie wchodzi na skrzynie + tlumaczenia DE/FR
`templates/collection.gift-collection.json` · tlumaczenia `[poza repo]`

**Co:** blok opisu w hero (`text_9BHigY`, "Not sure what to get...") dostal
`custom_class: hero-guild-title2` (istniejaca klasa, `max-width: 700px`). Wczesniej
opis rozciagal sie do 60vw (`.home-hero-left`) i wchodzil na grafike skrzyni.

**Pulapka:** ustawienie "Max width" bloku tekstu w edytorze NIC nie robi -
`blocks/text.liquid` w tym motywie jest przerobiony i renderuje tylko tekst
i `custom_class`. Szerokosc zmienia sie wylacznie klasa.

**Skutek uboczny:** przy ~1700 px tytul "Perfect DnD Gift Ideas:" lamie sie
na dwie linie (potrzebuje 943,2 px, grupa dostaje 942,1 px - wczesniej maskowal
to szeroki opis). Na 1280/1440 lamal sie i tak. Na telefonie klasa dodaje 32 px
odstepu nad opisem.

**Tlumaczenia:** szablon mial 0 tlumaczen DE/FR (klon). Przez `translationsRegister`
wgrane 52 pola na jezyk: 47 przeniesionych po digescie z `collection.aarakocra-5e`
i `collection.75mm`, 5 nowych (hero, naglowek listy) przetlumaczonych. Kolekcja
(tytul, opis, SEO) miala juz tlumaczenia. Sprawdzone curlem na `/de-de/` i `/fr-fr/`.

**Jak cofnac:** klasa - `rollback/collection.gift-collection.2026-10-31-przed-opisem.json`;
tlumaczenia - `translationsRemove` dla zasobu
`OnlineStoreThemeJsonTemplate/collection.gift-collection`.

## 2026-10-31 (wieczor, 4)

### Kolekcja DnD Gifts: nowa grafika w hero (skrzynia)
`assets/base.css` · `templates/collection.gift-collection.json` · Files `[poza repo]`

**Co:** hero kolekcji `dnd-gifts` (szablon `collection.gift-collection.json`, sekcja
`section_tJEjwT`) dostaje `DnD_Gifts_Visual_Design.webp` (skrzynia z ciepla poswiata)
zamiast grafiki Aarakocry. Plik wgrany do Shopify Files przez Admin API (`fileCreate`).

**Jak:** ten sam mechanizm co 75mm - nowa klasa `hero-bg-103` w `base.css`, dopisana
we wszystkich trzech blokach responsywnych zaraz pod `hero-bg-102`, a w szablonie
`hero-bg-11` -> `hero-bg-103`. Regule `hero-bg-11` zostawiona, bo uzywaja jej
Aarakocra i Spooky.

**Do poprawy (nie ruszone):** tekst hero w Gifts to wciaz kopia z Aarakocry
("Soar through the skies...", "One Miniature - 18 variants"). Na telefonie `cover`
przycina grafike do lewej strony, wiec skrzyni nie widac - tak samo jak w innych hero.

**Jak cofnac:** w szablonie `hero-bg-103` -> `hero-bg-11` (kopia sprzed zmiany:
`rollback/collection.gift-collection.2026-10-31-przed-hero.json` w folderze projektu),
tag gita `przed-hero-gift-2026-10-31` dla `base.css`.

## 2026-10-31 (wieczor, 3)

### The Long Night (sezon): akt z daty - od 1.11 swieci akt II, we wszystkich miejscach i jezykach
`sections/long-night-season.liquid` (jedyny plik).

**Co:** dodany przelacznik `auto_act` (domyslnie wlaczony), ten sam wzorzec co
w `long-night-lp-book`: akt nigdy nie jest nizszy niz wynika z kalendarza - od
1.11 00:00 akt II, od 1.12 00:00 akt III (czas sklepu). Reczny `current_act`
w szablonie zostaje dolna granica. Liczy serwer Shopify przy renderze, wiec
nic nie trzeba przestawiac o polnocy.

**Dlaczego jedna zmiana w sekcji, a nie 72 szablony:** sekcja siedzi w 73
szablonach (kolekcje, produkty, `page.bundle`), w 72 z `current_act: 1`.
Zmiana w sekcji obejmuje wszystkie naraz oraz DE i FR - wybor aktu to ustawienie
liczbowe, nie tlumaczony tekst, wiec rynki de/fr czytaja ta sama wartosc.

**Sprawdzone:** logika Liquid przeliczona dla 31.10, 1.11, 15.11 i 1.12 przy
recznym akcie 1 i 2 (akt 1 -> 1 / 2 / 2 / 3). Przed 1.11 nic sie wizualnie nie zmienia.

**Jak cofnac:** `git revert` commita tej zmiany i push pliku, albo wylaczyc
`auto_act` w ustawieniach sekcji.

---

## 2026-10-31 (wieczor, 2) [poza repo]

### Zdjecie w produkcie FREE Mini of the Month na 1.11.2026, 01:02 CET - Val Town
val `janstarosta/rpg-guild-ceny-1-11`, nowy plik `foto.ts` (interval), cron
`2-30 0 1 11 *` (UTC) = 01:02-01:30 CET 1 listopada. Produkt
`free-dnd-mini-of-the-month` (ID 9772825706762).

**Co:** dodaje `BadgeListopad2026.webp` jako PIERWSZE zdjecie produktu i zdejmuje
`BadgePazdziernik2026.webp` (produkt zostaje z 4 zdjeciami). Nowy plik wgralem
wczesniej do Shopify Files (ID `gid://shopify/MediaImage/51484809855242`, READY,
na produkcie jeszcze nie widoczny). Alt nowego zdjecia: "FREE Mini of the Month November 2026".

**Okna w Val Town:** ceny 00:01-00:59 CET, to zadanie 01:02-01:30 CET, baner
01:05-01:59 CET, 75mm od 02:00 CET. Zadanie jest lekkie (kilka zapytan).

**Zabezpieczenia:** idempotentne (nie dubluje zdjecia), czeka az nowe zdjecie bedzie
READY, kontrola na koncu, stan w blobie `foto-state`, mail z wynikiem lub bledem.

**Sprawdzone:** uruchomienie na sucho przed 1.11 (uprawnienie write_products OK,
plik na CDN HTTP 200, stare zdjecie na produkcie znalezione). Sciezka zapisu NIE
byla przetestowana na zywo.

**Jak cofnac:** kopie obu zdjec sa w `Free-Mini-of-the-Month/`. Dodac stare zdjecie
z powrotem w panelu produktu i zdjac nowe.

---

## 2026-10-31 (wieczor) [poza repo]

### Podmiana filmow w banerze na 1.11.2026, 01:05 CET - Val Town
val `janstarosta/rpg-guild-baner-1-11`, plik `main.ts` (interval), cron
`5-59 0 1 11 *` (UTC) = 01:05-01:59 CET 1 listopada.

**Co:** o 1.11 podmienia wskazania filmu w banerze strony glownej: EN w
`templates/index.json` (`sections.hero_XFBPJU.settings.video_1`), DE i FR w
tlumaczeniach tego klucza. Pliki mp4 wgralem wczesniej do Shopify Files
(komenda `upload` w `shopify_rpg_movie.py`, status READY, baner bez zmian):
EN `RPG Banner Film Nov 2026 (1).mp4`, DE `RPG Banner Film Nov 2026.mp4`,
FR `RPG Banner Film Nov 2026 (2).mp4`.

**Okna w Val Town (zeby sie nie gryzly):** ceny 00:01-00:59 CET, ten val
01:05-01:59 CET, 75mm od 02:00 CET.

**Zabezpieczenia:** kolejnosc EN, potem digest i DE/FR; idempotentny; stan i
punkt cofniecia (poprzednie wskazania) w blobie `baner-state`; mail z wynikiem
albo z bledem. Starych filmow NIE kasuje, wiec cofniecie jest mozliwe.

**Sprawdzone:** uruchomienie na sucho przed 1.11 - uprawnienia
(write_files, write_themes, write_translations) OK, 3 pliki READY, obecne
wskazania odczytane (`Stronka RPG Banner film 10_2026_ENG/DE/FR.mp4`).
Sciezka zapisu NIE byla przetestowana na zywo.

**Jak cofnac:** przywrocic w motywie EN, DE i FR do wartosci z blobu
`baner-state` (pole `rollback.previous`) albo `python3 shopify_rpg_movie.py rollback`
nie zadziala (inny plik stanu) - wtedy recznie w edytorze motywu.

---

## 2026-10-31 (wieczorem)

### The Long Night: akt II swieci od 31.10, nie od 1.11
`sections/long-night-season.liquid`

**Co:** w sekcji sezonu prog aktu II przesuniety z `202611010000` na `202610310000`.
Od teraz os sezonu wszedzie na sklepie pokazuje zapalony ACT II / NOVEMBER.
Zmiana jednej liczby plus komentarz - 5 linii dodanych, 3 usuniete.

**Dlaczego w Liquidzie, a nie w szablonach:** sekcja stoi w **74 szablonach**.
Wszystkie maja `auto_act` nieustawione, czyli lapia domyslne `true` ze schematu,
73 maja `current_act: 1`, jeden ma `2`. Jedna linia w Liquidzie przestawia komplet;
edycja 74 plikow JSON byla by ta sama zmiana przepisana 74 razy.

**To nigdy nie bylo w Val Town.** Jan pytal, czy usunac to z vala - nie ma czego.
Przelaczanie aktu z daty liczy serwer Shopify przy renderze (commit `ed79872`),
zadne zadanie w chmurze go nie dotyka. Val `rpg-guild-baner-1-11` dotyczy filmow
w banerze strony glownej i zostaje nietkniety.

**Czego NIE zmienilem i dlaczego:** ta sama data siedzi jeszcze w trzech sekcjach
landingu sezonu (`long-night-lp-book`, `long-night-lp-doors`, `long-night-lp-poster`)
oraz w `assets/long-night-lp.js` jako bezpiecznik na cache. Tam akt **nie jest samym
podswietleniem** - steruje flaga `locked` na kartach aktow (`if no_i > act_i`), wiec
podniesienie go odslonilo by karte Black Friday dzien wczesniej. To decyzja handlowa,
nie kosmetyka. Landing przeskoczy sam 1.11 o polnocy. Zgloszone Janowi.

**Weryfikacja na zywym sklepie** (`/en-pl/collections/undead-5e`):
- desktop 1470 px: `aria-current="true"` na drugim akcie, ACT II / NOVEMBER,
  krwawa kreska pod nim, akty I i III przygaszone - zgodne ze zrzutem docelowym Jana,
- 375 px: ten sam wynik,
- konsola: 2 bledy, oba zewnetrzne (skrypt reklamowy Azure 429, Font Awesome z cdnjs),
  zadnego z motywu,
- `theme check`: 0 uwag dla tego pliku,
- bilans skladni policzony: `{%`/`%}` 31/31, `{{`/`}}` 83/83, `{`/`}` 290/290,
  schema parsuje sie jako JSON.

**Odczyt kontrolny po pushu:** md5 repo i LIVE identyczne
(`a365ef7a26807eb4b24d02e0f9942738`).

**Jak cofnac:** tag `przed-ln-akt2`, albo recznie `202610310000` -> `202611010000`
w linii 33. Kopia pliku sprzed zmiany byla pobrana z LIVE przed edycja
(md5 `10f360f0cbe1eb411d27100877ff46e5`).

**Przy okazji, do sprawdzenia przez Jana:** strona landingu
`/pages/the-long-night-rpg-guild-sale-season` jest opublikowana i na goly adres
oddaje 200, ale wersja `/en-pl/...` przekierowuje na `/collections/dnd-gifts`.
Nie dotykalem tego - zglaszam jako obserwacje.

---

## 2026-10-31 (korekta po poludniu) [poza repo]

### Lista 75mm przyciety z 593 do 503 - 90 produktow nie mialo ceny w Excelu

**Skad to wyszlo:** Jan poprosil o double check, czy w kolekcji sa naprawde te
produkty, ktore w arkuszu mialy ceny dla 75mm. Nie byly.

**Blad w zrodle planu:** `policz-ceny.py` dla kazdej z szesciu kolumn
`75 - Unassembled / Assembled / Drybrush / Primer Grey / Primer Black / Primer Red`
robil tak: jesli komorka ma wartosc i jest wieksza od progu 53.64 USD - polowa
tej ceny; **w kazdym innym przypadku stawka plaska**. "Kazdy inny przypadek"
obejmowal takze komorke pusta. Flaga `ma_ceny` sluzyla wylacznie do wyboru
miedzy zduplikowanymi wierszami tego samego SKU, nie do odsiewania wierszy.
Efekt: SKU bez ani jednej ceny 75mm dostawalo pelny cennik plaski i wchodzilo
do planu na rowni z resztą.

**Liczby z arkusza `Ceny wszystkie profile DM.csv` (759 SKU po deduplikacji):**
- 557 SKU ma wypelnione wszystkie szesc kolumn 75mm,
- 202 SKU ma wszystkie szesc pustych.
Podzial jest zero-jedynkowy, nie ma ani jednego SKU z czescia kolumn.

**Jak to wygladalo w planie 593:**
- 503 produkty z SKU, ktore ceny mialy,
- **90 produktow z SKU, ktore nie mialy zadnej** - do usuniecia,
- 0 produktow o SKU nieobecnym w arkuszu.

**Co zrobione:**
1. Kolekcja `75mm Miniatures` (`586086809866`): `collectionRemoveProducts`
   na 90 ID. Stan po: 503 produkty, zgodne z planem co do jednego.
2. `automation/backups/75mm/dane75.json` przebudowany na 503 produkty /
   3013 wariantow (bylo 593 / 3547).
3. Ten sam plik podmieniony w Val Town `janstarosta/rpg-guild-ceny-1-11`
   (`update_file` z `upload_id`, 67767 B). Suchy przebieg potwierdza:
   `503 produktow / 3013 wariantow do dodania`, companions-5e nadal 3 wspolne.
4. Komentarz naglowkowy `warianty75.ts` poprawiony z 593 na 503 wraz
   z powodem. Harmonogram nietkniety: cron `* 1-2 1 11 *`, aktywny.

**Druga strona kontroli - czego NIE naprawialem:** 55 SKU, ktore ceny 75mm
w arkuszu maja, nie weszlo do planu w ogole. Odrzucil je `dopasuj.py`: brak
produktu w sklepie, rozne SKU na wariantach jednego produktu, inny uklad opcji
niz Size/Treatment, nieznana obrobka. Czesc ma w nazwie `REVISIT`
(`Artizak REVISIT`, `Korgrin REVISIT`, `Tyria REVISIT`, `Varys REVISIT`,
`Virana REVISIT`, `Ninera REVISIT`, `Raiko REVISIT`). To jest otwarta luka,
nie regresja - zglaszona Janowi, decyzja po jego stronie.

**Jak cofnac:** pelna lista 90 odrzuconych rekordow z cenami leży w
`automation/backups/75mm/USUNIETE-90-bez-cen.json`, poprzedni plan w
`automation/backups/75mm/PRZED-dane75-593.json`, stan kolekcji przed calym
dodawaniem w `automation/backups/75mm/PRZED-kolekcja-75mm.json`.

---

## 2026-10-31 (po poludniu) [poza repo]

### Kolekcja 75mm: dodane 593 produkty

**Co:** do kolekcji `75mm Miniatures` (`75mm-miniature-big-scale`,
ID `586086809866`) dodane 593 produkty - dokladnie ta lista, dla ktorej
zadanie w Val Town zalozy 1.11.2026 o 02:00 CET wariant rozmiaru `75mm`.
Przed zmiana w kolekcji byl 1 produkt (`5e Bard`, ID `8544646562058`),
ktory na liscie tez jest, wiec nic nie wypadlo.

**Czym jest ta kolekcja:** w nowym modelu Shopify (`CollectionConditionsSource`)
ma zero warunkow i wylacznie recznie wskazane produkty. Nie jest automatyczna,
wiec nic sie samo nie dopisze ani nie wypadnie - lista jest statyczna.

**Jak zrobione:** Admin API `2025-07`, `collectionAddProductsV2` w paczkach po
100 (zwraca `job`, kazda paczka odczekana do `done`). Semantyka dodawania,
nie podmiany, wiec paczki sa bezpieczne. Skrypt: scratchpad sesji,
`dodaj75.py` + `kolekcja75.py`.

**Stan po zmianie (sprawdzony zapytaniem, nie zalozony):** 593 produkty
w kolekcji, z planu nie brakuje zadnego, nadmiarowych zero. 9 z nich ma status
`DRAFT`, wiec na sklepie pojawia sie dopiero po publikacji - to stan sprzed
tej zmiany, nie jej skutek.

**Weryfikacja na zywo:** `/en-pl/collections/75mm-miniature-big-scale` renderuje
siatke produktow, hero nadal `75mm_Visual_Design.png`.

**Uwaga na okno czasowe:** do 1.11 o 02:00 kolekcja pokazuje produkty, ktore
jeszcze nie maja opcji `75mm`. Po przejsciu zadania z Val Town opis kolekcji
i zawartosc sie zgadzaja. Czlonkostwo w kolekcji nie ma zadnego wplywu na to
zadanie - ono pracuje na ID produktow z `dane75.json`, kolekcji nie dotyka.

**Jak cofnac:** `collectionRemoveProducts` na 592 ID - stan przed zmiana lezy
w `automation/backups/75mm/PRZED-kolekcja-75mm.json`.

---

## 2026-10-31 (poludnie)

### Kolekcja 75mm: nowa grafika w hero
`assets/base.css` · `templates/collection.75mm.json`

**Co:** hero kolekcji `75mm-miniature-big-scale` (szablon `collection.75mm.json`,
sekcja `section_tJEjwT`) dostaje `75mm_Visual_Design.png` zamiast grafiki
pozyczonej od kolekcji Aberration.

**Dlaczego to nie jest zmiana jednego ustawienia:** szablon 75mm jest kopia
`collection.aberration-5e.json` i odziedziczyl po niej klase `hero-bg-15`.
Ustawienie `background_image` w sekcji nie ma tu nic do rzeczy - `base.css`
chowa ten obrazek regula
`.hero-spacer .custom-section-background img { display: none !important }`,
a tlo rysuja reguly `hero-bg-N`. Pierwsza probka (sama podmiana ustawienia)
nie zmienila na stronie nic.

**Jak dziala kaskada hero w base.css** - to jest pulapka, ktora kosztowala dwa
podejscia. Bloki `hero-bg-*` sa w pliku **trzy razy** i to nie jest duplikat
przez pomylke:

| blok | linie (po zmianie) | media query | dla kogo |
|---|---|---|---|
| 1 | ~326-831 | brak | telefon |
| 2 | ~1590-2101 | `min-width: 480px` | tablet |
| 3 | ~2177-2622 | `min-width: 768px` | desktop |

Miedzy blokami stoja ogolne reguly `.hero-spacer .custom-section-background > div`
(linie 1590 i 2106) z `home-hero-fix.png`. Maja **te sama szczegolowosc** co
reguly `hero-bg-N`, wiec kasuja wszystko, co stoi nad nimi. Regula dopisana
tylko do bloku 1 dziala wylacznie na telefonie, tylko do bloku 3 - wylacznie
na desktopie. `hero-bg-102` jest wiec w kazdym z trzech, dokladnie tak jak
`hero-bg-15`.

**Zmiana w base.css jest wylacznie dodaniem 15 linii** (3 x ta sama regula),
zero skasowanych - sprawdzone `diff` z kopia sprzed zmiany
(`automation/backups/75mm/PRZED-base.css`). Dopisane przy rodzenstwie, za
`hero-bg-101`, **nie na koncu pliku** - koniec `base.css` to znane miejsce,
gdzie dopiski gina.

**Sprawdzone na zywo:** 390, 600, 1024 i 1440 px - wszedzie
`75mm_Visual_Design.png`. EN, DE (`/de-de/`) i FR (`/fr-fr/`) - wszedzie nowa
grafika, klasa `hero-bg-102` dociera do przetlumaczonych storefrontow.
Kolekcja `aberration-5e` bez zmian, dalej `Aberration_5e_Miniatures.png`.
Na telefonie widac sam czerwony pas bez figurki, bo grafika jest szeroka
(1920x892) i `cover` ucina boki - dokladnie tak samo zachowuje sie hero
Aberration, wiec to nie regres, tylko sposob dzialania tego motywu.

**Jak cofnac:** tag `przed-hero-75mm` (stan sprzed calej zmiany) albo kopie
`automation/backups/75mm/PRZED-base.css` i `PRZED-collection.75mm.json`.
Mniejszym krokiem: wrocic w szablonie `custom_class` na `hero-bg-15`.

---

## 2026-10-31 (przed poludniem)

### Zadanie 75mm na 1.11.2026, 02:00 CET - Val Town `[poza repo]`
val `janstarosta/rpg-guild-ceny-1-11`, nowe pliki `warianty75.ts` (interval)
i `dane75.json` (dane, 80 KB)

**Co:** drugi plik w tym samym valu, w ktorym siedzi zmiana cen z 1.11. Dodaje
wartosc rozmiaru `75mm` i 3547 wariantow na 593 produktach DM Stash. Cron
`* 1-2 1 11 *` (UTC) = co minute 02:00-03:59 CET 1 listopada. Pierwsze
uruchomienie 2026-11-01T01:00:00Z, potwierdzone przez API.

Dlaczego 02:00, a nie o polnocy: `main.ts` w tym samym valu zajmuje okno
00:01-00:59 CET na ceny. Nie moga biec rownolegle.

**Jak dziala:** darmowy plan Val Town daje 1 minute na uruchomienie, wiec kazde
robi 40 s pracy i zapisuje pozycje w blobie `75mm-stan`; kolejne minuty koncza
reszte. Duplikat wariantu jest pomijany, nie liczony jako blad, wiec powtorzone
uruchomienie niczego nie psuje. Po 40 bledach zadanie sie zatrzymuje i wysyla
maila zamiast brnac dalej. Na koniec kontrola na probce 20 produktow plus
wszystkie z `companions-5e` i mail z podsumowaniem.

**Trzy produkty z dwoma mechanizmami naraz:** `Ervin`, `Jesmira`
i `Arkham_Ravenswood` leza i na liscie 75mm, i w kolekcji `companions-5e`,
ktora `main.ts` przecenia o 5% o 00:01. Ich nowe warianty 75mm dostaja to samo
przekreslenie zaraz po utworzeniu - inaczej karta mialaby polowe wariantow
w promocji, a polowe nie.

**Dane:** `dane75.json` to `do-wdrozenia.json` sciete do postaci
`[id produktu, id opcji rozmiaru, id opcji obrobki, SKU, [[indeks obrobki, cena]]]`
- 80 KB zamiast 307 KB. Ceny bez zmian: plaskie 26,95 / 28,96 / 23,98 / 34,99,
a tam gdzie cena z Excela przekraczala 53,64 USD - polowa ceny z Excela.
315 z 593 produktow ma przynajmniej jedna cene z tej drugiej reguly.

**Sprawdzone:** uruchomienie na sucho na `main` (przed START nic nie zapisuje)
- dane sie wczytuja, 593 produkty / 3547 wariantow, kolekcja `companions-5e`
ma 120 produktow i 3 wspolne z lista, opcja rozmiaru w probce znaleziona.
Osobno, na skasowanej juz galezi `proba75`, przeszla cala sciezka zapisu na
jednym produkcie: utworzenie 6 wariantow, zapis stanu w blobie, kontrola i mail
- wynik `OK`, warianty potem usuniete, produkt wrocil do 18 wariantow.

**Czego jeszcze nie sprawdzilem:** gałęzi z przecena dla tych trzech produktow
z `companions-5e`. Mutacja jest ta sama, ktorej `main.ts` uzywa od 27.10, ale
na zywo w tym pliku nie poszla.

**Czego zadanie NIE robi:** tlumaczen wartosci `75mm` na DE i FR. Apka ma tylko
`read_products` i `write_products`; `translatableResource` odbija sie o brak
`read_translations`. Na DE i FR pigulki rozmiarow maja tlumaczenia (`28 mm` ze
spacja), wiec `75mm` pokaze sie surowo. Do zrobienia po 1.11, gdy Jan dopisze
`read_translations` i `write_translations` do apki - wczesniej i tak sie nie da,
bo wartosc opcji nie istnieje, dopoki nie powstanie pierwszy wariant.

**Jak cofnac:** skasowac warianty 75mm (`productVariantsBulkDelete`) - wartosc
opcji znika sama razem z ostatnim z nich. Zadanie wylacza sie przez usuniecie
pliku `warianty75.ts` z vala albo zmiane crona; blob `75mm-stan` trzyma dokladna
pozycje, na ktorej skonczylo.

---

## 2026-10-31 (rano)

### 75mm: test na żywo na jednym produkcie, dwie poprawki po nim
`snippets/informacja-75mm.liquid` · `locales/en.default.json` · `locales/de.json` ·
`locales/fr.json` · warianty produktu `KadnaChosen` `[poza repo]`

**Co:** na produkcie `Sorcerer 5e | DnD Female Moon Goddess Miniature`
(`moon-goddess-sorcerer-5e-miniature`, SKU `KadnaChosen`) powstało na kilkanaście
minut 6 wariantów 75mm, żeby obejrzeć pigułkę, ikonkę i dymek na żywym sklepie.
Po testach warianty usunięte, wartość opcji `75mm` zniknęła razem z ostatnim
z nich - produkt wrócił do 18 wariantów i trzech rozmiarów.

Test wyłapał dwie rzeczy, których nie widać w makiecie:

1. **Link `mailto` renderował się jako tekst.** Shopify escapuje HTML w wartościach
   tłumaczeń, jeśli klucz nie kończy się na `_html`. Klucze `size_75_info`
   i `size_75_info_no_size` zmieniły nazwy na `size_75_info_html`
   i `size_75_info_no_size_html` w trzech plikach lokalizacji i w snippecie.
   Commit `3a56116`.
2. **Dymek wychodził poza kadr na telefonie.** Przy 390 px wyśrodkowany na ikonce
   dymek zaczynał się na -6 px; `body` ma `overflow-x: hidden`, więc tekst był
   przycięty. Pod 750 px `fieldset` z rozmiarami dostaje `position: relative`,
   a dymek `inset-inline: 0` - mieści się w kadrze niezależnie od tego, gdzie
   stoi ikonka. Strzałka na mobile ukryta, bo nie wskazywałaby już ikonki.
   Etykiety pigułek mają własne `position: relative`, więc nic się w nich
   nie przesunęło - sprawdzone na żywym DOM-ie przed zmianą. Commit `a1e95fd`.

**Sprawdzone na żywo** (playwright-cli, produkt z wariantem 75mm):
EN, DE i FR - dymek z właściwym tekstem i działającym `mailto`, przecinek
dziesiętny w DE i FR (`4,92` / `12,5`), angielska kropka w EN. Pigułka
niewybrana `#EFD4A4` z obwódką `#C58A30`, wybrana `#95500C` z tekstem `#F1E4D9`,
ikonka `#95500C` - zgodnie z zatwierdzoną wersją B. Cena wariantu 75mm
przeliczyła się normalnie przez Markets: 26,95 USD to 109,00 PLN i 24,95 EUR.
Desktop 1280 i telefon 390 - dymek w kadrze, brak poziomego przewijania.

**Do decyzji Jana:** na DE i FR pigułki rozmiarów mają tłumaczenia
(`28 mm` ze spacją), a nowa wartość `75mm` wyświetla się surowo, bo nikt jej
jeszcze nie przetłumaczył. Do zrobienia w Translate & Adapt albo przez
`translationsRegister` - na 593 produktach × 2 języki.

**Jak cofnąć:** motyw - tag `przed-75mm-html` wskazuje stan sprzed poprawki
kluczy `_html`; `git checkout przed-75mm-html -- snippets/informacja-75mm.liquid
locales/en.default.json locales/de.json locales/fr.json` i push tych plików.
Warianty testowe - już usunięte, log w `zrobione.jsonl.cofniete2` w scratchpadzie
sesji (ID 6 wariantów, gdyby trzeba było sprawdzić, co istniało).

---

## 2026-10-30 (noc)

### Rozmiar 75mm: pigułka, ikonka z wymiarami, tłumaczenia DE i FR
`snippets/informacja-75mm.liquid` (nowy) · `snippets/variant-main-picker.liquid` ·
`locales/en.default.json` · `locales/de.json` · `locales/fr.json`
oraz metapola produktów `[poza repo]`

**Co:** pigułka wariantu `75mm` dostaje ciepły bursztyn zamiast pergaminu i oksbloodu,
a obok niej staje ikonka informacji z dymkiem o wysokości miniatury.

| element | kolor |
|---|---|
| wybrana pigułka + ikonka | `#95500C` |
| obwódka | `#C58A30` |
| napis na niewybranej | `#884609` |
| tło niewybranej | `#EFD4A4` |

**Jak celowany jest 75mm.** Przez `input[value='75mm']`, a nie przez `nth-of-type`.
W `variant-main-picker.liquid` każdy `<input type="radio">` niesie `value` równe
nazwie wartości opcji, więc selektor trafia dokładnie w tę pigułkę i nie rozjedzie się,
gdy dojdzie piąty rozmiar albo zmieni się kolejność. Reguły z sekcji
„PRODUCT MAIN — VARIANTS" w `base.css` celują w `fieldset:last-of-type`, czyli obróbkę -
rozmiaru nie dotykają i nie ma kolizji.

**Skąd wymiar.** Dwa nowe metapola produktu, `custom.wysokosc_75_cal`
i `custom.wysokosc_75_cm`, wypełnione na 591 produktach ze źródła Jana
(arkusz DM Stash, kolumna J). Centymetry przeliczone z cali razy 2,54, a nie
z kolumny mm - arkusz ma tam wartości o około procent wyższe i dwie liczby
w jednym zdaniu by się nie zgadzały. `Tenagor` i `The Absolver` mają w arkuszu
`0,00` i `#ERROR!`, więc zostały bez metapola i dostaną dymek bez liczby.

**Tłumaczenia.** Trzy klucze w `products.product`: `size_75_label`, `size_75_info`,
`size_75_info_no_size`, w `en.default`, `de` i `fr`. Liczba wchodzi przez zmienne
`{{ inch }}` i `{{ cm }}`, więc tłumaczy się samo zdanie, a nie 591 osobnych tekstów.
Przecinek dziesiętny ustawia snippet: kropka po angielsku, przecinek po niemiecku
i francusku.

**Czemu CSS jest w snippecie, a nie w `base.css`.** Ma sens wyłącznie razem z tą
pigułką, a koniec `base.css` jest martwy - niedomknięta reguła Swyma połyka wszystko,
co się tam dopisze.

**Nic nie widać do 1.11.** Ikonka renderuje się tylko wtedy, gdy produkt ma wartość
opcji `75mm`, a dziś nie ma jej żaden produkt. Sprawdzone po wysyłce na
`/products/moon-goddess-sorcerer-5e-miniature` w trzech wersjach językowych:
selektor renderuje się normalnie (3 + 6 pigułek), `.rozmiar75` nie istnieje,
styl się nie wstrzykuje, przycisk zakupu działa, konsola czysta.

**Czego jeszcze nie widziałem na żywo:** samej pigułki 75mm i dymka na sklepie -
do tego potrzebny jest produkt z wariantem 75mm, a te powstają dopiero 1.11.

**Jak cofnąć:** `git checkout przed-75mm-motyw -- snippets/variant-main-picker.liquid
locales/en.default.json locales/de.json locales/fr.json` i push tych plików;
`snippets/informacja-75mm.liquid` usunąć z motywu. Metapola można zostawić -
bez snippetu nic ich nie czyta.

---

## 2026-10-30 (wieczorem)

### Cofnięcie 75mm z produktu testowego  `[poza repo]`
Shopify Admin API, bez zmian w motywie

**Co:** z produktu `Sorcerer 5e | DnD Female Moon Goddess Miniature`
(ID `9734318752010`, SKU `KadnaChosen`) usunięte 6 wariantów 75mm.
Produkt wrócił do 18 wariantów, rozmiary `28mm, 32mm, 38mm`.
Wartość opcji „75mm" zniknęła sama, gdy padł ostatni wariant, który jej używał -
nie trzeba było osobnego `productOptionUpdate`.

**Dlaczego:** decyzja Jana - całe wdrożenie 75mm (ceny, pigułka, ikonka, tłumaczenia)
ma wystartować dopiero 1.11.2026, więc produkt testowy nie może stać z 75mm przez
dwa dni jako jedyny w sklepie.

**Sprawdzone na żywo:** `/products/moon-goddess-sorcerer-5e-miniature.js` zwraca
18 wariantów i trzy rozmiary.

**Jak cofnąć cofnięcie:** nic nie trzeba - produkt wejdzie do wdrożenia masowego
1.11 na równi z pozostałymi 592. Ceny sprzed usunięcia leżą w
`automation/backups/75mm/PRZED-KadnaChosen-9734318752010.json`.

---

## 2026-10-30

### Rozmiar 75mm - test na jednym produkcie DM Stash  `[poza repo]`
Shopify Admin API (MCP), bez zmian w motywie

**Co:** do produktu `Sorcerer 5e | DnD Female Moon Goddess Miniature`
(ID `9734318752010`, SKU `KadnaChosen`) doszła czwarta wartość opcji
**„Choose the size of your mini" = 75mm** i 6 nowych wariantów:

| wariant | cena USD |
|---|---|
| 75mm / Unassembled | 39,64 |
| 75mm / Assembled | 43,64 |
| 75mm / Primer - Grey | 51,64 |
| 75mm / Primer - Black | 51,64 |
| 75mm / Primer - Red | 51,64 |
| 75mm / Drybrush | 51,64 |

Produkt ma teraz 24 warianty zamiast 18. Ceny z pliku `Ceny wszystkie profile DM.csv`
(kolumny W-AB). Nowe warianty dziedziczą ustawienia sąsiadów: `taxable: false`,
`inventoryPolicy: DENY`, `tracked: false`, `requiresShipping: true`, waga 0 kg,
bez ceny przekreślonej, SKU takie samo jak reszta produktu.

**Dlaczego:** pierwszy produkt z listy 759 SKU DM Stash - test przed wdrożeniem
masowym. Mutacja: `productVariantsBulkCreate`, wartość opcji 75mm tworzy się
automatycznie przy pierwszym wariancie, który jej używa.

**Motyw nietknięty.** Selektor wariantów renderuje opcje dynamicznie - jedyne
miejsca z „32mm" w motywie to tekst FAQ w szablonach, nie lista rozmiarów.

**Sprawdzone na żywo:** `rpgguild.shop/products/moon-goddess-sorcerer-5e-miniature`
pokazuje cztery pigułki rozmiaru (28/32/38/75), wybór 75mm ustawia wariant
`54030373388554` i cenę $39.64. Wszystkie 6 wariantów `available: true`
w `/products/<handle>.js`.

**Jak cofnąć:** `productVariantsBulkDelete` na sześciu ID
(`54030373388554`, `...421322`, `...454090`, `...486858`, `...519626`, `...552394`),
potem `productOptionUpdate` z `optionValuesToDelete` dla wartości 75mm.
Stan sprzed zmiany: `automation/backups/75mm/PRZED-KadnaChosen-9734318752010.json`.

---

## 2026-10-31

### [poza repo] Pliki do maila Mini of the Month (listopad) w Content > Files
- `motm-2026-11-hero.png`, `motm-2026-11-fire-elemental.png` - publiczne adresy obrazków do newslettera edrone (`Black Friday 2026/11-edrone/maile/motm-2026-11/`). Sklepu nie zmieniają. Cofnięcie: usunąć pliki w Files po wysyłce, jeśli nie są potrzebne.

## 2026-10-29

### Strzałki paska: większe i w kolorach przycisku wariantu
`sections/karuzela-sasiedzi.liquid` · szablon bez zmian

**Co:** 22 px → **32 px** (ikona 12 → 16 px), tło **`#5D1309`**, strzałka **`#F1E4D9`**,
bez obrysu, miękki cień pod spodem, widoczne cały czas zamiast przygaszenia do 55%.
Przy najechaniu tło delikatnie jaśnieje. Feedback: strzałki mają wyglądać jak przycisk
wariantu „28mm" na karcie produktu.

**Skąd dokładnie ten kolor.** `base.css` ustawia wybraną pigułkę wariantu na sztywno:
`.variant-option__button-label:has(:checked) { background-color: #5D1309 !important;
color: #F1E4D9 !important }`. Zmienna motywu `--color-primary-button-background` to
`#54130F`, czyli **inny odcień czerwieni** - użycie jej dałoby strzałki odstające kolorem
od przycisków obok. Dlatego w sekcji jest ten sam duet hexów co w `base.css`, z komentarzem
dlaczego. Jeśli kiedyś czerwień w `base.css` się zmieni, trzeba zmienić i tu.

Ikona dostała `--icon-stroke-width: 2px` lokalnie w przycisku - caret motywu jest przy
tej wielkości za cienki na pełnym tle.

**Zmierzone na żywo (desktop 1470 px):**

| | |
|---|---|
| rozmiar | 32 × 32 px, ikona 16 px |
| tło / ikona | `rgb(93, 19, 9)` / `rgb(241, 228, 217)` |
| zgodność z pigułką „28mm" | **identyczne**, oba kolory co do wartości |
| pozycja | lewy przy lewej krawędzi paska (0 px), prawy przy prawej (0 px), środek 1 px od środka zdjęcia |
| klik „dalej" / „wstecz" | przesuwa o jeden kafelek / wraca dokładnie do poprzedniego stanu |
| spoczynek paska | dalej równo na siatce (136 px) |
| telefon 375 px | oba przyciski `display: none` - bez zmian |

Wysokość sekcji bez zmian (przyciski dalej `position: absolute`), więc wyrównanie prawej
kolumny karty produktu nietknięte.

**Jak cofnąć:** `git checkout 32fbbd1 -- sections/karuzela-sasiedzi.liquid` (małe,
przygaszone strzałki) i push tego pliku.

---

## 2026-10-29

### Pasek sąsiadów: strzałki prawo-lewo, tylko desktop
`sections/karuzela-sasiedzi.liquid` · szablon bez zmian

**Co:** dwa małe przyciski (22 px) na krawędziach paska, w pionie na środku figurek.
Klik przesuwa pasek o jeden kafelek w swoją stronę, tą samą animacją co krok
automatyczny, i restartuje odliczanie, żeby automat nie dołożył kroku zaraz po kliknięciu.
Prośba Jana: „bardzo mała, minimalistyczna, ale funkcjonalna nawigacja".

**Tylko desktop** (`width >= 750px`) - na telefonie pasek przewija się palcem i strzałki
byłyby tylko zasłoną na figurkach. Na telefonie `display: none`.

**Wygląd:** okrąg 22 px, obrys `--color-border`, tło `--color-background` 88%, ikona 12 px.
W spoczynku `opacity: 0.55`, przy najechaniu na pasek albo focusie wewnątrz - pełna.
Ikona to **ten sam `icon-caret.svg`, którego motyw używa w swoich karuzelach**, obrócony
o 90°, a etykiety biorą się z gotowych tłumaczeń motywu (`accessibility.slideshow_previous`
i `_next`), więc DE i FR działają bez dokładania kluczy.

**Nie ruszają geometrii.** Przyciski są `position: absolute` w `.sasiedzi`, czyli poza
układem - wysokość sekcji bez zmian, więc wyliczenie podnoszące prawą kolumnę karty
produktu zostaje nietknięte. W pionie `top: 50%`: `.sasiedzi` to etykieta plus pasek,
więc środek wypada **1 px** od środka zdjęcia kafelka, niezależnie od szerokości ekranu.

**Krok wstecz to lustro kroku naprzód:** ostatni kafelek wraca na początek rzędu,
a pozycja przewinięcia rośnie w tej samej chwili o jego szerokość - jest dokąd cofać,
pętla działa w obie strony i nadal bez drugiej kopii listy.

**Przy `prefers-reduced-motion: reduce`** karuzela dalej nie rusza sama, ale strzałki
działają - z przeskokiem zamiast animacji. To ruch zamówiony klikiem, nie animacja tła.

**Zmierzone na żywo (desktop 1470 px):**

| | |
|---|---|
| przyciski | 22 × 22 px, lewy przy krawędzi paska (0 px), prawy przy prawej (0 px) |
| środek w pionie | 1 px od środka zdjęcia kafelka |
| klik „dalej" | kadr przesunięty dokładnie o jeden kafelek w lewo |
| klik „wstecz" | kadr wrócił dokładnie do poprzedniego stanu |
| automat po kliknięciu | odczekał pełne 3 s, nie dołożył kroku |
| klawiatura | przycisk łapie focus, obrys 1 px, Enter przesuwa pasek |
| telefon 375 px | oba przyciski `display: none` |
| hover | `opacity` 0,55 → 1 |

`theme check` 0 uwag.

**Zaobserwowane przy okazji, nie nasze:** po dłuższym staniu na karcie produktu edrone
montuje `#edrone-onsite-popup-iframe` na cały ekran (1470 × 900), który przejmuje
najazd myszą i kliknięcia na stronie. Przy świeżym wejściu go nie ma. Warto sprawdzić
w konfiguracji edrone, czy ta ramka ma prawo wisieć, gdy popup nic nie pokazuje.

**Jak cofnąć:** `git checkout 1a647b2 -- sections/karuzela-sasiedzi.liquid` (karuzela
krokowa bez strzałek) i push tego pliku.

---

## 2026-10-29

### Pasek sąsiadów: karuzela krokowa (poprawka po przenikaniu)
`sections/karuzela-sasiedzi.liquid` · szablon bez zmian

**Co było nie tak:** wersja z przenikaniem (wpis niżej) zmieniała figurkę **w miejscu** -
jedno zdjęcie wygasało, drugie się pojawiało. Jan: „to wygląda jak wygaszacz ekranu",
miał zostać ruch poziomy karuzeli, tylko spokojny.

**Co jest teraz:** co 3 sekundy pasek **przesuwa się płynnie o dokładnie jeden kafelek
w lewo** (650 ms, ease-in-out kubiczny), z prawej wjeżdża kolejna figurka. Między krokami
pasek stoi ~2,35 s.

**Pętla bez szwu i bez drugiej listy.** Kafelek, który wyjechał za lewą krawędź, wraca na
koniec rzędu, a `scrollLeft` maleje w tej samej chwili o jego szerokość. Operacja jest
wizualnie zerowa, więc pętla nie ma końca - stara karuzela potrzebowała do tego kopii
całej listy, ta nie potrzebuje. Kafelków tyle, ile mówi ustawienie (11 na tym produkcie),
obrazków tyle samo co wcześniej.

**Ruch idzie przez `scrollLeft` tego samego paska, który przewija palec**, więc gest
i karuzela nie walczą: dotknięcie, kółko albo swipe natychmiast przerywa przesuw
(`cancelAnimationFrame`) i wstrzymuje karuzelę na 1,2 s po ostatnim geście. Własna
animacja zamiast `scrollBy({ behavior: 'smooth' })`, bo natywna trwa ~300 ms i krok
wyglądał na szarpnięcie.

**Krok zawsze kończy na krawędzi kafelka.** Jeśli palec zostawi pasek w pół kafelka,
pierwszy krok po geście dociąga go do siatki - inaczej ucięty kafelek zostawałby przy
lewej krawędzi na zawsze.

**Usunięte:** zapas kafelków poza rzędem, klasy `--zapas` i `--gasnie`, całe przenikanie.
Plik schudł o 87 linii. Ustawienie w schemacie nazywa się teraz „Co ile sekund przesuwa
się o kafelek" (`interval`, 2-12 s, domyślnie 3).

**Zmierzone na żywo:**

| | desktop 1470 px | telefon 375 px |
|---|---|---|
| krok | zawsze dokładnie o jeden kafelek w lewo | to samo |
| rytm | ~3,0 s (2,35 s stoi + 0,65 s przesuw) | 3069 / 3086 / 3127 ms |
| krok w px | 136 (kafelek 127,8 + odstęp 8) | 69 (kafelek 60,6 + 8) |
| spoczynek | 136 px, odchyłka od siatki 0,0 px (4 pomiary) | 69 px, odchyłka 0,0 px (5 pomiarów) |
| po krzywym przewinięciu | 319 px → wraca na siatkę w jednym kroku | 185 px → 69 px |
| płynność | max 29 px na klatkę, **zero skoków > 60 px** w 260 próbkach | - |
| gest użytkownika | kółko w bok 136 → 386 px | swipe 69 → 270 px, strona nie drgnęła |
| obrazki | 11/11, zero pustych pól | 11/11, zero pustych pól |

Moment „kafelek wraca na koniec rzędu" jest niewidoczny: przy 260 próbkach co 50 ms żaden
kafelek w kadrze nie przeskoczył o więcej, niż wynosi sam płynny przesuw. `theme check`
0 uwag, konsola bez wzmianki o sekcji, zwykła karta produktu bez zmian (okruszki dalej
`16px 32px`, do prawej).

**Jak cofnąć:** `git checkout f187b73 -- sections/karuzela-sasiedzi.liquid` (wersja
z przenikaniem) albo `git checkout c55eeb4 -- …` (stara karuzela ciągła) i push tego pliku.

---

## 2026-10-29

### Pasek sąsiadów zamiast karuzeli: jeden kafelek zmienia się co 3 s
`sections/karuzela-sasiedzi.liquid` · szablon `product.test-default-product` bez zmian
> **Nieaktualne od tego samego dnia** - przenikanie w miejscu zastąpione krokiem
> karuzeli (wpis wyżej). Zostaje jako zapis, skąd wzięły się decyzje o siatce,
> przewijaniu i ukrytym pasku przewijania - te obowiązują dalej.

**Co:** pasek nad zdjęciem produktu przestał jeździć. Stoi, przewija się w bok palcem
albo gestem, a ruch to jedna podmiana - co 3 sekundy jeden kafelek **będący w kadrze**
przechodzi płynnie (260 ms) w inny produkt z tej samej kolekcji. Prośba Jana z 29.10.

**Co zostało bez zmian:** szerokość kafelka (pięć w kadrze, `calc((100cqw - 32px) / 5)`),
siatka, krawędź równa ze zdjęciem, wysokość paska - a więc i wyliczenie, które podnosi
prawą kolumnę karty produktu. Nagłówek, ceny, hover, maska na krawędziach też bez zmian.

**Jak to działa teraz:**

| | |
|---|---|
| ruch | `setInterval` co `interval` s (ustawienie w schemacie, domyślnie 3) |
| co się zmienia | jeden kafelek w kadrze, po kolei; kafelki poza kadrem pomijane |
| przejście | wygaszenie 260 ms → podmiana w DOM → wejście 260 ms |
| przewijanie | `overflow-x: auto` na oknie, 12 kafelków przy 5 w kadrze |
| zapas | 6 kafelków w tym samym `<ul>`, `position: absolute` + `visibility: hidden` |

**Dlaczego tylko kafelek w kadrze.** Pasek ma 12 kafelków, a w kadrze widać 5. Gdyby
podmiana szła po kolei przez cały rząd, 7 z 12 tyknięć zmieniałoby coś poza ekranem
i pasek wyglądałby na zepsuty. JS liczy więc `offsetLeft` względem `scrollLeft` i bierze
tylko te kafelki, które w całości mieszczą się w oknie.

**Zapas bywa pusty i to jest przewidziane.** Kolekcja Owlina (Aarakocra 5e) ma 12
produktów, więc po odjęciu bieżącego zostaje 11 kafelków i zapas wychodzi zerowy -
pierwsza wersja po prostu by nie ruszyła. Gdy zapasu nie ma, podmiana bierze kafelek,
który jest akurat **poza kadrem**, i zamienia się z nim miejscami: w kadrze widać nowy
produkt, ruch poza kadrem jest niewidoczny, nic się nie dubluje i nie dochodzi ani
jeden obrazek. Kafelek zdjęty w poprzednim tyknięciu jest pomijany, żeby ten sam
produkt nie wracał od razu.

**Dlaczego zapas siedzi w tym samym `<ul>`, nie w drugiej liście.** Podmiana to jeden
`insertBefore` - kafelek z zapasu wchodzi na miejsce starego, stary wraca na koniec
kolejki. Kafelki zapasu są wyjęte z układu przez `position: absolute`, więc nie zmieniają
szerokości rzędu ani pozycji przewinięcia, a `visibility: hidden` (nie `display: none`)
zostawia obrazek wczytany - w momencie podmiany nigdy nie ma pustego pola. To ta sama
pułapka, którą naprawialiśmy 28.10 przy `loading="lazy"`.

**Zapas ma 6 sztuk.** Kafelek zdjęty z paska wraca na koniec kolejki, więc pula krąży
i ten sam produkt wraca najwcześniej po szóstej podmianie. Koszt: 18 obrazków zamiast 11,
czyli ~69 KB więcej (po ~11,5 KB w 260 px).

**Kiedy pasek stoi:** karta w tle (`document.hidden`), kursor nad paskiem (tylko tam,
gdzie jest `hover: hover` - na telefonie `:hover` zostaje po tapnięciu i zamroziłoby
podmiany), focus w środku, oraz sekunda po ostatnim przewinięciu. Przy
`prefers-reduced-motion: reduce` skrypt nie startuje w ogóle i zostaje zwykły rząd
do przewinięcia.

**Paska przewijania nie pokazujemy** (`scrollbar-width: none` + `::-webkit-scrollbar`).
Na Windowsie zabrałby ~15 px wysokości, a od wysokości paska zależy wyrównanie prawej
kolumny. Że pasek idzie dalej, podpowiada maska wyciemniająca krawędzie.

**Schemat:** ustawienie „Czas pełnego obiegu" (`speed`) zniknęło, w jego miejsce
„Co ile sekund zmienia się kafelek" (`interval`, 2-12 s, domyślnie 3). W szablonie
na sklepie został nieużywany klucz `"speed": 110` - Shopify ignoruje nieznane klucze,
`interval` bierze się z domyślnej wartości schematu.

**Zmierzone na żywo po wdrożeniu** (Owlin, motyw live):

| | desktop 1470 px | telefon 375 px |
|---|---|---|
| podmiana | 4 na 13 s, odstępy 3010 / 3011 / 3008 ms | 4 na 13 s, odstępy 3016 / 3022 / 3009 ms |
| ile kafelków naraz | zawsze 1 | zawsze 1 |
| kafelek | 127,8 px, 5 w kadrze | 60,59 px, 5 w kadrze |
| pasek | lewa 40 px, szer. 671 px, wys. 150 px | lewa 20 px, szer. 335 px, wys. 82 px |
| przewijanie | 1494 / 671 px, gest w bok: 0 → 250 → 500 px | 755 / 335 px, swipe palcem: 0 → 179 px |
| strona przy przewijaniu paska | nie drgnęła (`scrollY` 0) | nie drgnęła (`scrollY` 0) |
| obrazki | 11/11 wczytanych, 0 pustych pól | 11/11 wczytanych, 0 pustych pól |
| duplikaty w kadrze | brak (11 kafelków, 11 unikalnych) | brak |
| kolejność | okruszki 158 → pasek 253 → zdjęcie 363 (telefon, bez zmian wobec 28.10) | |

Pozycja przewinięcia przy podmianie **nie drgnęła** - 24 próbki co 500 ms przy
`scrollLeft` 500 px dały stale 500. Pauza na hover działa: z kursorem nad paskiem
zero podmian przez 12 s. Przy `prefers-reduced-motion: reduce` zero podmian przez 8 s,
kafelek 76 px, pasek dalej przewijalny (924 / 671 px).

Konsola: 4 błędy na desktopie i 5 na telefonie, wszystkie cudze i sprzed zmiany
(gift-box-builder, dwa `cdnjs` font-awesome, `MissingRefError` w `header-menu`) -
żaden nie dotyczy sekcji. Zwykła karta produktu (`aarakocra-5e-rogue-miniature`)
bez paska, okruszki dalej `16px 32px` i do prawej - bez zmian.

**Jak cofnąć:** `git checkout c55eeb4 -- sections/karuzela-sasiedzi.liquid` i push tego
jednego pliku. Szablon nietknięty, więc nic poza tym nie trzeba ruszać. Kopia wersji
sprzed zmiany (pobrana z live) leży też w scratchpadzie sesji.

---

## 2026-10-29

### [poza repo] Nowa mapa korzyści (treasure map) na stronach produktu: EN, DE, FR
- **Co:** w bloku obrazka 9 szablonów produktu (`product`, `dnd-dice`, `dnd-terrain`, `dnd-tiles`, `gift-card`, `mystery-box-product-page`, `pre-made-terrain-sets`, `starter-set-terrains`, `test-default-product`) obraz `Obszar_roboczy_14_od_Janek_via_Slack_1.webp` (stara mapa, 60$ Free Delivery) zamieniony na `treasure-map-2026-en.png` (z „Over 100$/€ Spent, Free Character Sheet”). Tłumaczenia tego obrazka (Translate & Adapt): DE `treasure-map-2026-de.png`, FR `treasure-map-2026-fr.png` (wcześniej `Mapa_DE.png` / `Mapa_FR.png`).
- **Jak:** pliki przez stagedUploads + fileCreate; szablony przez Asset API (Theme Access), podmiana jednej nazwy pliku; tłumaczenia przez `translationsRegister` z nowym digestem.
- **Sprawdzone na żywo:** en-pl, /products (terrains), de-de, de-ch, fr-fr pokazują właściwą mapę.
- **Jak cofnąć:** kopie szablonów i tłumaczeń sprzed zmiany w `automation/backups/2026-10-29-treasure-map/przed/` (wgrać z powrotem pliki szablonów, a w tłumaczeniach DE/FR wpisać `Mapa_DE.png` / `Mapa_FR.png`). Stare pliki zostały w Content > Files.
- **Pułapka:** strony DE i FR to `/de-de/`, `/de-at/`, `/de-ch/`, `/fr-fr/`, `/fr-ch/` (nie `/de/`); z polskiego IP sklep przekierowuje na `/en-pl/`, więc do testów trzeba ustawić ciasteczko `localization=DE`/`FR`.

## 2026-10-27

### [poza repo] Plik `rpg-guild-logo-mail.png` w Content > Files (logo do maili)
- **Co:** logo RPG Guild 219x240 px, `gid://shopify/MediaImage/51420845572362`, adres `https://cdn.shopify.com/s/files/1/0689/3204/3018/files/rpg-guild-logo-mail.png`.
- **Dlaczego:** publiczny adres logo do maila edrone po SPIEL Essen (`Black Friday 2026/11-edrone/maile/essen-2026/`).
- **Jak cofnąć:** usunąć plik w Content > Files (najpierw z maili, które go używają).

### [poza repo] Zaplanowana zmiana cen na 1.11.2026 (Val Town `janstarosta/rpg-guild-ceny-1-11`)
- **Co:** 1.11 od 00:01 zdejmuje przeceny (dragon-5e, spooky, terrain) i daje `companions-5e` -5%. Zapas: launchd `pl.rpgguild.ceny-1-11` na Macu Jana.
- **Jak cofnąć:** zrzuty w blobach vala (`snap-restore`, `snap-companions`) i w `~/.local/share/rpg-guild-1-11/` (`job.py undo`).

### Landing The Long Night: akt przełącza się sam z daty (1.11 akt II, 1.12 akt III)
Pliki: `sections/long-night-lp-poster.liquid`, `sections/long-night-lp-doors.liquid`,
`sections/long-night-lp-book.liquid`, `assets/long-night-lp.js`. Szablon `page.long-night.json` bez zmian.

**Co:** afisz, drzwi i księga liczą akt z daty serwera (czas sklepu, CET): od 1.11 00:00
co najmniej akt II, od 1.12 00:00 akt III. Ręczne ustawienie „Bieżący akt” jest dolną granicą.
Nowy przełącznik w każdej z trzech sekcji: „Przełączaj akt automatycznie wg daty”, domyślnie włączony.
W `long-night-lp.js` bezpiecznik: gdy strona przyjdzie z cache wyrenderowana przed północą,
przeładowuje się RAZ z parametrem `?ln=<akt>` (z parametrem nie próbuje drugi raz - zero pętli).

**Dlaczego:** przejście aktu o północy bez ręcznego przestawiania i bez działającego komputera.
Wpis aktu II w księdze przestaje być rozmyty i zamknięty o 00:00 1.11.

**Testy (27.10):** kopia motywu 195810165002 - z progiem przestawionym na dziś akt II we wszystkich
sekcjach (wpis III jedyny zamknięty, kadr afisza 2); z prawdziwymi datami akt I jak na live;
bezpiecznik JS 7/7 przypadków w Node (granica 23:59:59/00:00, brak pętli, UTM zachowane).

**Jak cofnąć:** w edytorze wyłączyć „Przełączaj akt automatycznie wg daty” w trzech sekcjach
(natychmiast, bez kodu) albo przywrócić pliki z poprzedniego commita. Kopia plików sprzed zmiany:
`Black Friday 2026/13-social/auto-akt/live-przed-zmiana-27-10/` w katalogu projektu.

---

## 2026-10-29 (druga tura)

### Karuzela na telefonie: kafelki nie znikają, pętla policzona
`sections/karuzela-sasiedzi.liquid`, dalej tylko szablon `test-default-product`

Jan poprosił o upewnienie się, że na telefonie produkty nie znikają i że pętla
jest nieskończona. Sprawdzone pomiarem na żywo, nie na oko.

**Pętla.** Przy 320 px okna: kafelek 58 px, 22 kafelki, lista 721,53 px, tor
1443,06 px, połowa toru 721,53 px - **szew wypada co do setnej piksela**.
`animation-iteration-count` to `Infinity`, stan `running`. Tor próbkowany 24 razy
co 500 ms: przesuwał się w każdej próbce (-313 → -389 px), czyli 6,3 px/s przy
721,53 px na 110 s.

**Znikające kafelki - znalezione i naprawione.** W ustalonym ruchu było czysto,
ale przy pierwszym obiegu jeden kafelek pokazywał się jako puste pole: miał
`loading="lazy"` i doczytywał się dopiero w momencie wjazdu w kadr. W karuzeli
każdy kafelek prędzej czy później wjeżdża w kadr, więc leniwe ładowanie nie ma
tu sensu - **wszystkie kafelki dostały `loading="eager"`**.

Koszt okazał się mniejszy, niż się wydaje: **11 zapytań, nie 22**. Druga lista
ma te same adresy, więc przeglądarka bierze ją z cache. Razem 126 KB, średnio
11,5 KB na kafelek. Dla porównania pozostałe obrazy tej karty to 19 zapytań
i 2187 KB - karuzela to około 5% wagi zdjęć na stronie. Wszystkie mają
`fetchpriority="low"`, więc nie konkurują ze zdjęciem produktu.

**Po zmianie, od pierwszej sekundy po załadowaniu:** 22 z 22 kafelków wczytane,
0 kafelków z `loading="lazy"`, i w 20 próbkach co 500 ms **ani razu żadne puste
pole w kadrze**.

---

## 2026-10-29

### Dolne krawędzie kolumn hero wyrównane - desktop
`sections/karuzela-sasiedzi.liquid`, dalej tylko szablon `test-default-product`

Po podniesieniu prawej kolumny jej dół kończył się **48 px wyżej** niż miniatury
galerii po lewej. Jan poprosił o delikatne zwiększenie wszystkich odstępów, żeby
obie kolumny kończyły się równo.

Kolumna zakupowa to flex w pionie z `row-gap: 24px` i ośmioma przerwami między
blokami. 48 / 8 = 6 px na przerwę, więc `row-gap: 30px`.

**Pierwsze podejście przestrzeliło o 20 px.** Selektor `.group-block-content`
łapał nie tylko kontener najwyższego poziomu, ale też sześć zagnieżdżonych
wewnątrz bloków - odstęp urósł dwa razy, 96 px zamiast 48. Poprawione na
`.product-details > .group-block > .group-block-content`.

**Zmierzone na żywo przy 1440 px:** dół lewej kolumny 1277 px, prawej 1271 px -
różnica 6 px. Góra: etykieta paska i prawa kolumna rozjechane o 3 px. Jedno i drugie
w granicach zaokrąglenia line-heightów.

**Uwaga:** 6 px na przerwę jest dobrane do tego produktu. Przy produkcie z inną
liczbą wariantów luz będzie inny - przy rozszerzaniu na kolejne szablony trzeba
policzyć od nowa albo rozdzielać luz automatycznie.

**Jak cofnąć:** usunąć regułę `row-gap: 30px` z sekcji.

---

## 2026-10-28 (trzecia tura)

### Prawa kolumna hero wyrównana do karuzeli - desktop
`sections/karuzela-sasiedzi.liquid`, dalej tylko szablon `test-default-product`

Po pokazaniu Janowi sześciu wariantów układu na makiecie wybrał ten: ocena i tytuł
startują na tej samej wysokości co pasek rekomendacji po lewej, zamiast czekać na
górną krawędź zdjęcia. Pustka w prawym górnym rogu hero znika.

Prawa kolumna podnosi się ujemnym marginesem o wysokość paska. **Wysokość liczona,
nie wpisana na sztywno:**

```
margin-block-start: calc(-1 * (70px + (100% - 56px) / 5))
```

70 px to części stałe (odstępy sekcji 16 + 14, etykieta 17 + 6, cena 12 + 5),
a `(100% - 56px) / 5` to kafelek: procent w marginesie liczy się od szerokości
kolumny, pasek jest od niej węższy o 24 px, do tego cztery odstępy po 8 px.
Dzięki temu wyrównanie trzyma się na każdej szerokości ekranu, nie tylko na 1440.

Reguła siedzi w `@media screen and (width >= 750px)` - **telefon bez zmian**,
zgodnie z decyzją Jana.

**Zmierzone na żywo przy 1440 px:** etykieta paska 262 px od góry strony, prawa
kolumna 264 px - różnica 3 px, w granicach zaokrąglenia line-heightów.

**Jak cofnąć:** usunąć blok `@media` z sekcji. Reszta układu zostaje bez zmian.

**Uwaga na przyszłość:** gdyby etykieta paska kiedyś złamała się na dwie linie
(dłuższa nazwa kolekcji przy wąskim oknie), stałe 70 px przestanie się zgadzać
i prawa kolumna podniesie się o kilkanaście pikseli za mało.

---

## 2026-10-28 (druga tura)

### Karuzela sąsiadów - pięć poprawek po pierwszym teście
`sections/karuzela-sasiedzi.liquid` · `templates/product.test-default-product.json`

Uwagi Jana po obejrzeniu wdrożenia. Wszystko dalej tylko na szablonie
`test-default-product`.

| co | przed | po |
|---|---|---|
| kafelków w oknie | 8,6 (stałe 76 px) | **dokładnie 5** (125 px desktop, 61 px telefon) |
| czas obiegu | 56 s | **110 s** |
| start ruchu | od razu przy ładowaniu | po 0,9 s, pasek wchodzi płynnie |
| pierwsze 5 obrazków | `loading="lazy"` | `loading="eager"` |
| okruszki | po prawej, 57 px wysokości | **do lewej, w linii ze zdjęciem**, 39 px |
| odstęp menu → zdjęcie | 291 px | **270 px** |

**Szerokość kafelka liczona od okna, nie od toru.** `container-type: inline-size`
na oknie plus `flex: 0 0 calc((100cqw - 32px) / 5)` daje zawsze pięć sztuk,
niezależnie od szerokości ekranu. Pętla zostaje bez szwu, bo jedna lista to
zawsze `N * (kafelek + 8 px)`, a tor przesuwa się o `-50%`.

**Dziwna animacja przy ładowaniu** brała się z leniwych obrazków nad zgięciem -
wskakiwały pojedynczo już w ruchu. Teraz pierwsza piątka ładuje się zwykle,
a cały pasek pojawia się z 450 ms opóźnieniem, gdy jest już czym wypełnić kadr.

**Okruszki** nie były wyrównane przez `text-align` tylko przez `display: flex`
z `justify-content: flex-end` - stąd `justify-content: flex-start` w nadpisaniu.
Dalej tylko na stronach z tą sekcją (`body:has(.sasiedzi-sekcja)`).

**Pustka nad zdjęciem** pochodziła z reguły
`.shopify-section[id$="__main"]:has(.product-information)`, która ustawia
`padding-block-start: 80px` z `!important`. Przy karuzeli ten odstęp lądował pod
nią zamiast pod okruszkami. Nadpisany na 14 px selektorem o wyższej
szczegółowości, oddech daje teraz `padding-block-start: 16px` samej karuzeli.

**Zmierzone na żywo po poprawkach:** okruszki, karuzela i zdjęcie na jednej
krawędzi (40 px desktop, 20 px telefon), kolejność na telefonie okruszki (158) →
karuzela (253) → zdjęcie (363), 22 z 22 obrazków wczytane, zero przewijania
w bok, animacja `running` 110 s.

**Zostaje do decyzji:** 270 px od menu do zdjęcia to w większości sam pasek
(~170 px). Przy pięciu kafelkach na szerokości 656 px kafelek ma 125 px i to jest
geometryczne minimum. Mniej miejsca = więcej kafelków w rzędzie: 6 daje 104 px,
7 daje 89 px. Na telefonie pięć sztuk to 61 px na kafelek - dość mało.

---

## 2026-10-28

### Karuzela „sąsiadów z kolekcji" nad zdjęciem - test na jednym szablonie
`sections/karuzela-sasiedzi.liquid` (nowy plik) · `templates/product.test-default-product.json`

Pasek innych miniatur z tej samej kolekcji, nad głównym zdjęciem na karcie produktu.
Na razie **tylko szablon `test-default-product`**, czyli jeden produkt:
[Owlin 5e | DnD Owlin Archer Miniature](https://rpgguild.shop/products/owlin-5e-archer-fighter-miniature).
Pozostałe karty produktów bez zmian.

**Bez JavaScriptu.** Ruch robi jedna animacja CSS na torze złożonym z dwóch identycznych
list. Przesunięcie o `-50%` to dokładnie szerokość jednej listy, więc pętla nie ma szwu.
Druga lista ma `aria-hidden="true"`, żeby czytnik ekranu czytał produkty raz. Najazd myszą
i `:focus-within` zatrzymują ruch. Przy `prefers-reduced-motion: reduce` animacja znika,
duplikat się chowa, a karuzela staje się zwykłym paskiem do przewinięcia.

Zdjęcia kafelków w 200 px (kafelek ma 76 px), z `loading="lazy"` i `fetchpriority="low"` -
nie konkurują z głównym zdjęciem produktu przy pierwszym renderze.

**Skąd produkty:** `product.collections.first`, z pominięciem bieżącego produktu.
Decyzja Jana - `complementary_products` i `related_products` są w tym sklepie puste
(0 na 300 sprawdzonych produktów), więc kurowane powiązania renderowałyby się puste.
W schemacie jest pole „Kolekcja" - puste znaczy „pierwsza kolekcja produktu".

**Dlaczego nowa sekcja, a nie blok w `product-information`:** schemat tamtej sekcji
przyjmuje wyłącznie bloki aplikacji (`blocks: [{"type": "@app"}]`), a `_product-media-gallery`
nie przyjmuje bloków potomnych. Wstawienie tam własnego bloku wymagałoby edycji pliku
wspólnego dla wszystkich szablonów produktu. Osobna sekcja tego nie wymaga - kod wspólny
nietknięty.

**Dlaczego własny kontener zamiast `section--page-width`:** `base.css` ma globalne
`.section--page-width { grid-template-columns: 1fr !important }`, a szerokość kontenera
hero jest tam wpisana twardo pod konkretne ID sekcji. Sekcja powtarza więc te same wymiary
u siebie: `max-width: 1540px`, `padding-inline: 40px`, a pasek `calc(50% - 24px)` - te 24 px
to `padding-inline-end` kolumny media, czyli połowa odstępu 48 px z `product-information`.

**Okruszki na telefonie** równane do krawędzi treści (20 px zamiast 32 px), ale **tylko
na stronach z tą sekcją** - selektor `body:has(.sasiedzi-sekcja)`. Sprawdzone: na zwykłej
karcie produktu padding dalej wynosi 32 px.

**Zmierzone na żywo** (Owlin, po wdrożeniu):

| | |
|---|---|
| karuzela desktop | lewa 40 px, szerokość 656 px |
| zdjęcie produktu | lewa 40 px, szerokość 656 px - równo co do piksela |
| telefon 375 px | okruszki, etykieta i zdjęcie wszystkie na 20 px |
| kolejność na telefonie | okruszki (158) → karuzela (259) → zdjęcie (403) |
| animacja | `running`, 56 s na obieg |
| przewijanie w bok | brak |
| zwykła karta produktu | bez sekcji, padding okruszków 32 px, hero 1360/656 - bez zmian |

`theme check` na nowym pliku czysto (jedna poprawka po drodze: tag `doc` działa tylko
w snippetach i blokach, nie w sekcjach - zamieniony na `comment`).

**Jak cofnąć:** usunąć sekcję `sasiedzi_karuzela` z szablonu albo wgrać kopię
`rollback/product.test-default-product.PRZED-karuzela.json` z katalogu projektu.
Plik sekcji można zostawić - bez wpisu w szablonie nic nie renderuje.

**Do decyzji:** nagłówek mówi „More Aarakocra 5e", a okruszki nad nim „Humanoid 5e".
Obie kolekcje są poprawne, ale biorą się z innej logiki - `collections.first` w Liquid
kontra reguła okruszków. Jeśli mają być zgodne, trzeba wskazać, która wygrywa.

---

## 2026-10-18

### Ceny: zdjęta przecena z Undead 5e, nałożona -5% na Dragon 5e `[poza repo]`
Zmiany przez Admin API (`productVariantsBulkUpdate`), kod motywu bez zmian.
Skrypty i pliki cofnięcia w katalogu projektu, nie w repo.

| Kolekcja | Produkty | Warianty | Co się stało |
|---|---|---|---|
| Undead 5e | 637 | 10 086 | zdjęta przecena: `price = compareAtPrice`, przekreślenie usunięte |
| Dragon 5e | 337 | 2 306 | przecena **-5%**: `compareAtPrice` = stara cena, `price` = stara × 0,95 |

Rabat -5% to ta sama wartość, co w `shopify_discount_undead.py` (`DISCOUNT = 0.95`).
Uwaga dla czytającego: docstring tamtego skryptu mówi „-3%", ale stała w kodzie to 0,95
i ceny na sklepie też pokazywały -5% (9,50 → 9,03). Nowy `shopify_discount_dragon.py`
ma docstring poprawiony.

**Dlaczego powrót z `compareAtPrice`, a nie z `undead_discount_rollback.jsonl`:**
plik znał 9 924 warianty, a kolekcja ma ich 10 086 - 162 doszły po 1 października.
Przed zapisem sprawdzone, że dla wszystkich 9 924 znanych `compareAtPrice` był
identyczny z ceną zapisaną w pliku (0 rozjechanych), więc nic nie zostało utracone,
a te 162 też wróciły.

71 wariantów leży w obu kolekcjach („Undead 5e | DnD Undead Pope of the Damned" i inne).
Najpierw wróciły do ceny bazowej, potem dostały -5% z Dragona. To jest zamierzone -
Jan prosił o -5% na wszystkich produktach Dragon 5e.

**Pliki cofnięcia:**

- `undead_5e_restore_rollback.jsonl` - stan Undead sprzed zdjęcia przeceny (`price` + `compareAtPrice`).
  Powrót: `shopify_restore_from_compare_at.py undo undead-5e`.
- `dragon_discount_rollback.jsonl` - ceny Dragona sprzed -5%.
  Powrót: `shopify_discount_dragon.py rollback`.

**Nowe skrypty:** `shopify_restore_from_compare_at.py` (ogólny, bierze handle kolekcji
jako argument; plumbing API importuje z `shopify_discount_undead.py`, nie kopiuje)
oraz `shopify_discount_dragon.py` (kopia skryptu undead, zmienione: kolekcja, nazwy
plików, docstring).

### ZAMKNIĘTE: 9 produktów chwilowo straciło przecenę spooky -10%

Zdjęcie przeceny z Undead 5e ruszyło **wszystkie** warianty tej kolekcji, a 9 produktów
miało w niej nie rabat undead -5%, tylko spooky -10%. Te **162 warianty** stoją teraz na
cenie sprzed spooky, bez przekreślenia - czyli są **droższe** niż przed 18.10.

Dotknięte: Undead Knight, Undead Dragon Rider, Cursed Tombs Ghost, Skeleton King,
Pumpkinhead, Skeleton Riders, Spooky Ghosts Set, Skeleton Dragon, Vampire Baron.

Dwa z nich (Undead Dragon Rider, Skeleton Dragon) są też w Dragon 5e - zostały
**wyłączone** z przeceny -5% przez `SKIP_PRODUCT_IDS` w `shopify_discount_dragon.py`,
żeby nie zabetonować złej ceny. Dlatego Dragon ma 2 306, a nie 2 342 przecenionych wariantów.

Naprawa jest gotowa i przetestowana na podglądzie, ale **zapis został zablokowany**
przez tryb auto Claude Code. Do uruchomienia ręcznie:

```
cd ~/Documents/Claude\ ✴️/Projects/RPG\ Guild\ 🛡️
set -a && . ~/.secrets/rpg-guild-shopify.env && set +a
python3 shopify_przywroc_spooky.py run
```

Skrypt nie liczy cen - wpisuje z powrotem dokładnie to, co było w
`undead_5e_restore_rollback.jsonl`. Po tym Undead Dragon Rider i Skeleton Dragon
znów mają przekreślenie, więc przy ewentualnym ponownym `shopify_discount_dragon.py run`
zabezpieczenie skryptu pominie je samo.

**Naprawione tego samego dnia.** Pierwsze uruchomienie padło na `HTTP 401: Invalid API key`
- w shellu Jana siedział stary `SHOPIFY_ACCESS_TOKEN`, a `get_token()` bierze go przed
`SHOPIFY_CLIENT_ID`/`SECRET`. Zapis nie przeszedł w ogóle (sprawdzone: 0 ze 162 wariantów).
`shopify_przywroc_spooky.py` usuwa teraz tę zmienną, gdy ma klucze aplikacji.
Drugie uruchomienie: 162 ze 162 wariantów przywrócone, 0 braków.

**Stan końcowy, sprawdzony na żywo wariant po wariancie - 0 rozjechanych:**

| Kolekcja | Warianty | Rozkład |
|---|---|---|
| Undead 5e | 10 086 | 9 853 bez przeceny · 162 spooky -10% · 71 Dragon -5% |
| Dragon 5e | 2 372 | 2 306 Dragon -5% · 66 spooky -10% |

---

## 2026-10-11

### Linia zaufania na B2B: 300,000+ → 500,000+ miniatures (EN + DE + FR)
`templates/page.b2b-wholesale.json` + tłumaczenia DE/FR `[poza repo]`

Domknięcie sprzeczności zgłoszonej dzień wcześniej: nagłówek mówił
`500,000 minis forged in just 3 years`, a linia zaufania niżej `300,000+ miniatures produced`.
Jan zdecydował podbić niższą liczbę.

| Gdzie | Język | Było | Jest |
|---|---|---|---|
| B2B, linia zaufania | EN | 300,000+ miniatures produced | **500,000+ miniatures produced** |
| B2B, linia zaufania | DE | Über 300.000 produzierte Miniaturen | **Über 500.000 produzierte Miniaturen** |
| B2B, linia zaufania | FR | Plus de 300 000 figurines produites | **Plus de 500 000 figurines produites** |

Angielski wszedł przez `themeFilesUpsert` na jednym ciągu znaków - **bez pushowania
lokalnej kopii szablonu**, bo push nadpisuje zmiany z edytora. Przed podmianą pobrany
żywy plik i porównany z repo: jedyną różnicą było `300,000 → 500,000` w nagłówku
(podbite kiedyś w edytorze). JSON zwalidowany przed wysyłką, długość pliku bez zmian.

Po zmianie EN zmienił się `translatableContentDigest`, więc DE/FR zostały wpisane
na nowo nowym digestem - nie są `outdated`.

Repo zrównane z produkcją: `templates/index.json` i `templates/page.b2b-wholesale.json`
zapisane z żywego sklepu (diff: po jednej linii w każdym - liczba w nagłówku).
Wcześniej repo mówiło 300,000, a sklep 500,000 - przy następnym pushu szablonu
sklep cofnąłby się do 300,000.

Weryfikacja na żywo - `/pages/b2b-wholesale`, `/de-de/pages/b2b-wholesale`,
`/fr-fr/pages/b2b-wholesale`, `/de-de`, `/fr-fr`: nigdzie nie ma już 300,000.

**Jak cofnąć:** EN - podmienić ciąg `500,000+ miniatures produced` z powrotem
w pliku szablonu (albo `git revert` tego commita i push samego szablonu, gdy repo
jest świeże). DE/FR - wartości przed zmianą w `rpg_tln_500k_rollback.json`
w katalogu projektu, klucz `przed_po_podbiciu_en`.

---

## 2026-10-10

### Tłumaczenia DE/FR akapitu „500,000 minis forged" - homepage i B2B `[poza repo]`
`templates/index.json`, `templates/page.b2b-wholesale.json` - tylko tłumaczenia, kod motywu i angielski bez zmian

Angielski na żywym sklepie mówi od jakiegoś czasu **500,000 minis forged in just 3 years**
(podbite w edytorze, lokalna kopia repo ma tu jeszcze 300,000). Tłumaczenia zostały z tyłu
i Shopify trzymał je jako `outdated`, ale dalej je wyświetlał - czyli klient niemiecki
i francuski widział inną liczbę niż angielski.

| Gdzie | Język | Było | Jest |
|---|---|---|---|
| Homepage (`index`) | DE | 150.000 | **500.000** |
| Homepage (`index`) | FR | 300 000 | **500 000** |
| B2B Wholesale | DE | 300.000 | **500.000** |
| B2B Wholesale | FR | 300 000 | **500 000** |

Poza liczbą, w tym samym przebiegu:

- **FR na B2B był ucięty** - brakowało całego bloku zaufania („Trusted by tabletop
  businesses worldwide" + linia z liczbami). Dopisany po francusku.
- **DE na homepage** miał zepsute odstępy (`<p> Mit`, `</strong> ,`, `lassen</strong> .`) - wyczyszczone.

Klucze (zasób `OnlineStoreThemeJsonTemplate`, motyw `182160195850`):

- `section.index.json.section_WMcpBJ.group_KzPg9U__group_GjUFif__text_T6MgGR.text:14r9gq3pvd2v9`
- `section.page.b2b-wholesale.json.section_eBAPy.group_WMyYJT__text_A4eaJ7.text:37gz0ar88k22j`

Wpisane przez `translationsRegister` z aktualnym `translatableContentDigest`, więc pola
nie są już `outdated`. Zweryfikowane na żywo: `/de-de`, `/fr-fr`, `/de-de/pages/b2b-wholesale`,
`/fr-fr/pages/b2b-wholesale`.

**Jak cofnąć:** poprzednie wartości leżą w `rpg_tln_500k_rollback.json` w katalogu projektu
(`~/Documents/Claude ✴️/Projects/RPG Guild 🛡️/`) - wpisać je z powrotem tym samym
`translationsRegister` albo wkleić w Translate & Adapt.

### Do decyzji Jana - nie zmienione *(rozstrzygnięte 2026-10-11, patrz wpis wyżej)*

Angielski na B2B sam sobie przeczy: nagłówek mówi `500,000 minis forged in just 3 years`,
a linia zaufania dwa akapity niżej `300,000+ miniatures produced`. Tłumaczenia trzymają się
angielskiego (DE `Über 300.000 produzierte Miniaturen`, FR `Plus de 300 000 figurines produites`),
bo zmiana tej liczby to zmiana obietnicy marketingowej, nie tłumaczenia. Jeśli ma być 500,000+ -
trzeba podbić angielski w edytorze i te dwa tłumaczenia razem z nim.

---

## 2026-10-06

### Sekcja The Long Night na kolekcjach terrain (4 szablony)
`e1a10da` · `templates/collection.dnd-terrain-master.json`, `collection.dnd-terrain-pre-made-sets.json`,
`collection.dnd-terrain-tiles.json`, `collection.dnd.terrain-starter-set.json` + tłumaczenia DE/FR `[poza repo]`

Po kolekcjach 5e Jan zlecił to samo dla terrain. Sekcja sezonu stoi zaraz pod „Guild”:

| Szablon | Kolekcja | Pod sekcją |
|---|---|---|
| `dnd-terrain-master` | `/collections/dnd-terrain` | Guild, nad filmem „Movie” |
| `dnd-terrain-pre-made-sets` | `/collections/modular-dnd-terrain-sets` | Guild, nad CTA |
| `dnd-terrain-tiles` | `/collections/dnd-terrain-tiles` | Guild, nad „Sign Up” |
| `dnd.terrain-starter-set` | `/collections/modular-dnd-terrain-starter-sets` | Guild, nad CTA |

Piąty szablon terrain (`terrain-5e` → Terrain Elements) dostał sekcję wcześniej, razem z kolekcjami 5e.

Ta sama kopia `section_longNightSeason` z `product.json`, kod motywu bez zmian, diff +204 / -0.
Szablony na serwerze sprawdzone przed zmianą (= repo). Wstawienie skryptem `shopify_tln_insert.py`
(folder projektu), tłumaczenia `shopify_tln_translations.py` - 120 wpisów, kontrola 4/4 kompletne.
Sprawdzone na żywo: wszystkie 4 kolekcje × en, `/de-de/`, `/fr-fr/` - sekcja jest, tekst w języku
rynku. `dnd-terrain` ma inny układ niż reszta (strona-wizytówka z filmem) - zrzuty 1440 i 390 px OK.

**Jak cofnąć:** tag `przed-tln-kolekcje-terrain` i push tych 4 szablonów albo ukrycie sekcji
„The Long Night · sezon” w edytorze.

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
