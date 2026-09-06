#!/usr/bin/env python3
"""Kiest elke week een nieuwe headerfoto voor de homepage.

Draait wekelijks vanuit de GitHub Action, maar je kunt hem ook lokaal draaien:

    python3 tools/roteer-hero.py            # rouleer als de week om is
    python3 tools/roteer-hero.py --forceer  # rouleer sowieso
    python3 tools/roteer-hero.py --toon     # laat alleen zien wat er nu staat

Regels
  * `vast: true` in _data/hero.yml  -> nooit automatisch wisselen
  * handmatig gekozen foto          -> blijft minimaal 7 dagen staan
  * daarna                          -> willekeurige foto met `hero: true`,
                                       waarbij de laatste 8 keuzes worden
                                       overgeslagen zodat je niet snel herhaalt

Exit 0 = klaar (of niets te doen), exit 1 = fout.
"""
import argparse
import random
import re
import sys
from datetime import date, timedelta
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
FOTOS = REPO / "_data" / "fotos.yml"
HERO = REPO / "_data" / "hero.yml"
VASTE_PERIODE = timedelta(days=7)
GESCHIEDENIS_MAX = 8


def lees_hero() -> dict:
    """Minimale YAML-lezer voor _data/hero.yml — geen externe afhankelijkheden."""
    d = {"bestand": "", "ingesteld_op": "", "bron": "automatisch",
         "vast": False, "geschiedenis": []}
    if not HERO.exists():
        return d
    for regel in HERO.read_text(encoding="utf-8").splitlines():
        regel = "" if regel.lstrip().startswith("#") else regel.split("#")[0].rstrip()
        if not regel.strip():
            continue
        if m := re.match(r'\s*-\s*"?([^"]+?)"?\s*$', regel):
            d["geschiedenis"].append(m[1])
            continue
        m = re.match(r'(\w+):\s*"?([^"]*?)"?\s*$', regel)
        if not m:
            continue
        sleutel, waarde = m[1], m[2].strip()
        if sleutel == "vast":
            d["vast"] = waarde.lower() == "true"
        elif sleutel == "geschiedenis":
            pass          # de lijst zelf staat op de volgende regels
        elif sleutel in d:
            d[sleutel] = waarde
    return d


def lees_kandidaten() -> list[str]:
    """Alle bestanden uit fotos.yml met hero: true."""
    kandidaten, huidig = [], None
    for regel in FOTOS.read_text(encoding="utf-8").splitlines():
        if m := re.match(r'-\s*bestand:\s*"([^"]+)"', regel):
            huidig = m[1]
        elif huidig and re.match(r'\s+hero:\s*true\s*$', regel):
            kandidaten.append(huidig)
            huidig = None
    return kandidaten


def schrijf_hero(bestand: str, bron: str, vast: bool, geschiedenis: list[str]) -> None:
    regels = [
        "# Headerfoto van de homepage.",
        "#",
        "# Zelf kiezen? Zet hieronder de bestandsnaam uit _data/fotos.yml neer en",
        "# vul de datum van vandaag in bij `ingesteld_op`. Op /fotos/?beheer=1 staat",
        "# bij elke liggende foto een knop die dit blokje voor je klaarzet.",
        "#",
        "#   vast: true   de foto blijft staan tot je hem zelf weer wisselt",
        "#   vast: false  na een week kiest tools/roteer-hero.py willekeurig een andere",
        "",
        f'bestand:      "{bestand}"',
        f'ingesteld_op: "{date.today().isoformat()}"',
        f'bron:         "{bron}"',
        f"vast:         {'true' if vast else 'false'}",
        "",
        "# Laatst getoond, nieuwste eerst — wordt gebruikt om herhaling te voorkomen.",
        "geschiedenis:",
    ]
    regels += [f'  - "{g}"' for g in geschiedenis[:GESCHIEDENIS_MAX]]
    HERO.write_text("\n".join(regels) + "\n", encoding="utf-8")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--forceer", action="store_true")
    p.add_argument("--toon", action="store_true")
    args = p.parse_args()

    hero = lees_hero()
    kandidaten = lees_kandidaten()

    if args.toon:
        print(f"nu:          {hero['bestand'] or '(geen)'}")
        print(f"ingesteld:   {hero['ingesteld_op'] or '(onbekend)'} ({hero['bron']})")
        print(f"vast:        {hero['vast']}")
        print(f"kandidaten:  {len(kandidaten)}")
        return 0

    if not kandidaten:
        print("Geen foto's met hero: true in _data/fotos.yml — niets te kiezen.")
        return 1

    if hero["vast"] and not args.forceer:
        print(f"vast: true — {hero['bestand']} blijft staan.")
        return 0

    if not args.forceer and hero["ingesteld_op"]:
        try:
            leeftijd = date.today() - date.fromisoformat(hero["ingesteld_op"])
        except ValueError:
            leeftijd = VASTE_PERIODE
        if leeftijd < VASTE_PERIODE:
            resterend = (VASTE_PERIODE - leeftijd).days
            print(f"{hero['bestand']} staat er pas {leeftijd.days} dag(en) — "
                  f"nog {resterend} te gaan.")
            return 0

    recent = set(hero["geschiedenis"][:GESCHIEDENIS_MAX - 1]) | {hero["bestand"]}
    pool = [k for k in kandidaten if k not in recent] or \
           [k for k in kandidaten if k != hero["bestand"]] or kandidaten
    nieuw = random.choice(pool)

    geschiedenis = [nieuw] + [g for g in hero["geschiedenis"] if g != nieuw]
    schrijf_hero(nieuw, "automatisch", False, geschiedenis)
    print(f"Nieuwe headerfoto: {nieuw}  (uit {len(pool)} kandidaten)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
