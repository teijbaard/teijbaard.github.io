#!/usr/bin/env python3
"""Haalt de nieuwste video's van het YouTube-kanaal op en schrijft _data/youtube.yml.

    python3 tools/haal-youtube.py                      # kanaal-ID uit _config.yml
    python3 tools/haal-youtube.py --kanaal UCxxxxxxxx  # expliciet

Geen API-sleutel nodig. Er zijn twee bronnen, in deze volgorde:

  1. De publieke Atom-feed. Geeft de laatste uploads met titel én datum.
     YouTube knijpt dit endpoint af bij veel verkeer vanaf één IP en geeft dan
     een generieke 404 terug — vandaar drie pogingen met oplopende wachttijd.

  2. Lukt dat niet, dan de uploads-tab van het kanaal: daar staat de nieuwste
     video als eerste videoId in de HTML. De titel komt vervolgens van het
     oEmbed-endpoint. Deze route levert één video en geen publicatiedatum.

Zijn beide bronnen onbereikbaar, dan blijft _data/youtube.yml staan zoals hij
is en eindigt het script met code 0: de site toont dan gewoon de vorige video.
Alleen echte fouten (geen geldig kanaal-ID) geven exit 1.
"""
import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONFIG = REPO / "_config.yml"
UIT = REPO / "_data" / "youtube.yml"

FEED = "https://www.youtube.com/feeds/videos.xml?channel_id={}"
UPLOADS = "https://www.youtube.com/channel/{}/videos"
OEMBED = "https://www.youtube.com/oembed?url=https%3A//www.youtube.com/watch%3Fv%3D{}&format=json"

MAX_VIDEOS = 4
POGINGEN = 3
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/122.0 Safari/537.36")
NS = {"a": "http://www.w3.org/2005/Atom",
      "yt": "http://www.youtube.com/xml/schemas/2015"}


def haal(url: str, timeout: int = 30) -> bytes:
    verzoek = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept-Language": "nl,en;q=0.8",
    })
    with urllib.request.urlopen(verzoek, timeout=timeout) as r:
        return r.read()


def kanaal_uit_config() -> str:
    m = re.search(r'youtube_channel_id:\s*"?(UC[\w-]{22})"?',
                  CONFIG.read_text(encoding="utf-8"))
    return m[1] if m else ""


def via_feed(kanaal: str) -> list[dict]:
    """Bron 1 — de Atom-feed. Geeft [] als YouTube niet meewerkt."""
    for poging in range(1, POGINGEN + 1):
        try:
            xml = haal(FEED.format(kanaal))
            break
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            reden = getattr(e, "code", e)
            if poging == POGINGEN:
                print(f"Feed niet beschikbaar na {POGINGEN} pogingen ({reden}).",
                      file=sys.stderr)
                return []
            wacht = 2 * poging
            print(f"Feed gaf {reden}; nieuwe poging over {wacht}s "
                  f"({poging}/{POGINGEN - 1}).", file=sys.stderr)
            time.sleep(wacht)

    try:
        wortel = ET.fromstring(xml)
    except ET.ParseError as e:
        print(f"Feed is geen geldige XML: {e}", file=sys.stderr)
        return []

    videos = []
    for e in wortel.findall("a:entry", NS)[:MAX_VIDEOS]:
        vid = e.findtext("yt:videoId", default="", namespaces=NS)
        if re.fullmatch(r"[\w-]{11}", vid):
            videos.append({
                "id": vid,
                "titel": (e.findtext("a:title", default="", namespaces=NS) or "").strip(),
                "gepubliceerd": (e.findtext("a:published", default="", namespaces=NS) or "")[:10],
            })
    return videos


def via_uploadspagina(kanaal: str) -> list[dict]:
    """Bron 2 — de uploads-tab plus oEmbed. Eén video, zonder datum."""
    try:
        html = haal(UPLOADS.format(kanaal)).decode("utf-8", "replace")
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        print(f"Uploads-pagina niet bereikbaar: {getattr(e, 'code', e)}", file=sys.stderr)
        return []

    m = re.search(r'"videoId":"([\w-]{11})"', html)
    if not m:
        print("Geen videoId gevonden op de uploads-pagina.", file=sys.stderr)
        return []
    vid = m[1]

    try:
        meta = json.loads(haal(OEMBED.format(vid), timeout=20))
        titel = (meta.get("title") or "").strip()
    except (urllib.error.URLError, TimeoutError, OSError, ValueError) as e:
        print(f"oEmbed gaf geen titel ({getattr(e, 'code', e)}); id wel gevonden.",
              file=sys.stderr)
        titel = ""

    if not titel:
        return []
    print(f"Teruggevallen op de uploads-pagina — alleen de nieuwste video, "
          f"zonder publicatiedatum.", file=sys.stderr)
    return [{"id": vid, "titel": titel, "gepubliceerd": ""}]


def huidige_eerste_id() -> str:
    """Het id van de video die nu in _data/youtube.yml bovenaan staat."""
    if not UIT.exists():
        return ""
    m = re.search(r'^\s*-\s*id:\s*"([\w-]{11})"', UIT.read_text(encoding="utf-8"), re.M)
    return m[1] if m else ""


def q(s: str) -> str:
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--kanaal", default="")
    args = p.parse_args()

    kanaal = args.kanaal or kanaal_uit_config()
    if not re.fullmatch(r"UC[\w-]{22}", kanaal):
        print('Geen geldig kanaal-ID. Zet `youtube_channel_id: "UC…"` in '
              "_config.yml of geef --kanaal mee.", file=sys.stderr)
        return 1

    videos = via_feed(kanaal)
    terugval = False
    if not videos:
        videos = via_uploadspagina(kanaal)
        terugval = True

    if not videos:
        print("Geen enkele bron gaf video's terug — _data/youtube.yml "
              "ongewijzigd gelaten.")
        return 0

    # De terugval kent maar één video en geen datum. Is dat dezelfde video als
    # er al staat, laat het bestand dan met rust: anders ruilen we de complete
    # gegevens van de feed in voor een armere versie van hetzelfde.
    if terugval and huidige_eerste_id() == videos[0]["id"]:
        print("Nieuwste video is ongewijzigd — bestaande gegevens blijven staan.")
        return 0

    regels = [
        "# Automatisch bijgewerkt door tools/haal-youtube.py — niet met de hand aanpassen.",
        "# De GitHub Action draait dit dagelijks; de homepage toont `videos[0]`.",
        "",
        f"kanaal_id:  {q(kanaal)}",
        f"bijgewerkt: {q(datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'))}",
        "",
        "videos:",
    ]
    for v in videos:
        regels += [f"  - id:           {q(v['id'])}",
                   f"    titel:        {q(v['titel'])}",
                   f"    gepubliceerd: {q(v['gepubliceerd'])}"]
    nieuw = "\n".join(regels) + "\n"

    # Alleen wegschrijven als er echt iets veranderd is; anders levert de dagelijkse
    # Action elke dag een commit op waarin alleen de tijdstempel verschilt.
    def zonder_tijdstempel(tekst: str) -> str:
        return "\n".join(r for r in tekst.splitlines() if not r.startswith("bijgewerkt:"))

    if UIT.exists() and zonder_tijdstempel(UIT.read_text(encoding="utf-8")) == zonder_tijdstempel(nieuw):
        print("Geen nieuwe video's — _data/youtube.yml ongewijzigd.")
        return 0

    UIT.write_text(nieuw, encoding="utf-8")
    print(f"_data/youtube.yml bijgewerkt: {len(videos)} video's, "
          f"nieuwste = {videos[0]['titel']!r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
