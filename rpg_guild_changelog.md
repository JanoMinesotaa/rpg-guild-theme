# Dziennik zmian - motyw RPG Guild

Motyw `RPG GUILD theme 2025`, ID `182160195850`, sklep `rpg-guild.myshopify.com`.

Zapis prowadzony dla dewelopera. Każdy wpis mówi **co**, **gdzie**, **dlaczego**
i **jak cofnąć**. Zmiany wykonane poza repozytorium - przez Admin API, MCP albo
ręcznie w panelu Shopify - są oznaczone `[poza repo]`, bo nie ma po nich commita.

Konwencja: najnowsze na górze.

---

## 2026-09-23

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
