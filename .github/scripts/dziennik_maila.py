#!/usr/bin/env python3
"""
Dzienny raport zmian w motywie RPG Guild.

Zbiera commity z POPRZEDNIEGO dnia kalendarzowego (strefa Europe/Warsaw)
i wysyla je mailem do dewelopera. Gdy zmian nie bylo - nie wysyla nic,
zeby nie zasmiecac skrzynki codziennym "brak zmian".

Uruchamiany przez .github/workflows/dziennik-zmian.yml
Konfiguracja idzie przez zmienne srodowiskowe (sekrety repo).
"""
import os
import smtplib
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from email.message import EmailMessage

WARSZAWA = timezone(timedelta(hours=2))  # nadpisywane przez TZ w workflow

def polecenie(*args):
    return subprocess.run(args, capture_output=True, text=True, check=True).stdout

def zakres_wczoraj():
    """Poczatek i koniec poprzedniego dnia w czasie lokalnym runnera (TZ=Europe/Warsaw)."""
    teraz = datetime.now()
    dzis = teraz.replace(hour=0, minute=0, second=0, microsecond=0)
    wczoraj = dzis - timedelta(days=1)
    return wczoraj, dzis

def commity(od, do):
    surowe = polecenie(
        "git", "log",
        f"--since={od:%Y-%m-%d %H:%M:%S}",
        f"--until={do:%Y-%m-%d %H:%M:%S}",
        "--pretty=format:%H%x1f%h%x1f%ad%x1f%s%x1f%b%x1e",
        "--date=format:%H:%M",
    )
    wynik = []
    for blok in surowe.split("\x1e"):
        blok = blok.strip("\n")
        if not blok:
            continue
        pelny, krotki, godzina, temat, tresc = blok.split("\x1f")
        pliki = polecenie("git", "show", "--pretty=format:", "--name-only", pelny)
        pliki = [p for p in pliki.strip().split("\n") if p]
        wynik.append(
            {"krotki": krotki, "godzina": godzina, "temat": temat,
             "tresc": tresc.strip(), "pliki": pliki}
        )
    return wynik

def zbuduj_tresc(lista, od, repo):
    naglowek = f"Zmiany w motywie RPG Guild - {od:%d.%m.%Y}"
    linie = [naglowek, "=" * len(naglowek), ""]
    linie.append(f"Commitow: {len(lista)}")
    linie.append(f"Repozytorium: https://github.com/{repo}")
    linie.append(f"Pelny dziennik: https://github.com/{repo}/blob/main/rpg_guild_changelog.md")
    linie.append("")
    for c in lista:
        linie.append(f"--- {c['godzina']}  [{c['krotki']}]  {c['temat']}")
        if c["tresc"]:
            for w in c["tresc"].splitlines():
                if w.strip().startswith("Co-Authored-By:"):
                    continue
                linie.append(f"    {w}")
        if c["pliki"]:
            linie.append("")
            linie.append(f"    Pliki ({len(c['pliki'])}):")
            for p in c["pliki"][:25]:
                linie.append(f"      - {p}")
            if len(c["pliki"]) > 25:
                linie.append(f"      ... i jeszcze {len(c['pliki']) - 25}")
        linie.append("")
        linie.append(f"    Diff: https://github.com/{repo}/commit/{c['krotki']}")
        linie.append("")

    surowy = f"https://raw.githubusercontent.com/{repo}/main/rpg_guild_changelog.md"
    linie += [
        "",
        "=" * 64,
        "JAK PODPIAC SWOJEGO CHATA POD TEN DZIENNIK",
        "=" * 64,
        "",
        "Pelny dziennik jest publiczny, wiec kazdy chat z dostepem do sieci",
        "(ChatGPT, Claude, Gemini) przeczyta go z tego adresu:",
        "",
        f"  {surowy}",
        "",
        "SPOSOB 1 - doraznie, bez konfiguracji",
        "Wklej powyzszy link do czatu i dopisz pytanie, np.:",
        "",
        '  "Przeczytaj ten plik i powiedz, co zmienilo sie w ostatnim tygodniu"',
        '  "Z tego dziennika: jakie sa znane, otwarte problemy?"',
        '  "Czy w tym motywie sa jakies pulapki, o ktorych powinienem wiedziec',
        '   zanim dotkne pliku assets/base.css?"',
        "",
        "SPOSOB 2 - na stale, wlasny GPT (ChatGPT Plus)",
        "ChatGPT -> Explore GPTs -> Create -> w polu Instructions wklej:",
        "",
        f'  "Zrodlem prawdy o motywie Shopify RPG Guild jest {surowy}',
        '   Przed kazda odpowiedzia pobierz ten plik i opieraj sie na nim.',
        '   Odpowiadaj po polsku, konkretnie, z numerami commitow."',
        "",
        "Wlacz w nim Web Browsing. Od tego momentu pytasz go normalnie,",
        "a on sam siega po aktualna wersje dziennika.",
        "",
        "UWAGA: GitHub cache'uje surowe pliki okolo 5 minut. Jesli commit",
        "wlasnie poszedl, a chat go nie widzi - odczekaj chwile i powtorz.",
        "",
        "Kod motywu w calosci: https://github.com/" + repo,
    ]
    return "\n".join(linie)

def main():
    od, do = zakres_wczoraj()
    lista = commity(od, do)
    if not lista:
        print(f"Brak commitow z {od:%Y-%m-%d} - nie wysylam maila.")
        return 0

    wymagane = ["MAIL_SERVER", "MAIL_PORT", "MAIL_USERNAME", "MAIL_PASSWORD", "MAIL_TO"]
    braki = [k for k in wymagane if not os.environ.get(k)]
    if braki:
        print(f"BLAD: brakuje sekretow repo: {', '.join(braki)}", file=sys.stderr)
        return 1

    repo = os.environ.get("GITHUB_REPOSITORY", "JanoMinesotaa/rpg-guild-theme")
    tresc = zbuduj_tresc(lista, od, repo)

    wiadomosc = EmailMessage()
    wiadomosc["Subject"] = f"RPG Guild - zmiany w motywie {od:%d.%m.%Y} ({len(lista)} commitow)"
    wiadomosc["From"] = os.environ["MAIL_USERNAME"]
    wiadomosc["To"] = os.environ["MAIL_TO"]
    if os.environ.get("MAIL_CC"):
        wiadomosc["Cc"] = os.environ["MAIL_CC"]
    wiadomosc.set_content(tresc)

    port = int(os.environ["MAIL_PORT"])
    if port == 465:
        with smtplib.SMTP_SSL(os.environ["MAIL_SERVER"], port) as s:
            s.login(os.environ["MAIL_USERNAME"], os.environ["MAIL_PASSWORD"])
            s.send_message(wiadomosc)
    else:
        with smtplib.SMTP(os.environ["MAIL_SERVER"], port) as s:
            s.starttls()
            s.login(os.environ["MAIL_USERNAME"], os.environ["MAIL_PASSWORD"])
            s.send_message(wiadomosc)

    print(f"Wyslano raport za {od:%Y-%m-%d}: {len(lista)} commitow -> {os.environ['MAIL_TO']}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
