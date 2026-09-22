# Dziennik zmian - motyw RPG Guild

Motyw `RPG GUILD theme 2025`, ID `182160195850`, sklep `rpg-guild.myshopify.com`.

Zapis prowadzony dla dewelopera. Każdy wpis mówi **co**, **gdzie**, **dlaczego**
i **jak cofnąć**. Zmiany wykonane poza repozytorium - przez Admin API, MCP albo
ręcznie w panelu Shopify - są oznaczone `[poza repo]`, bo nie ma po nich commita.

Konwencja: najnowsze na górze.

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
