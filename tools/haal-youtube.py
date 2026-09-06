#!/usr/bin/env python3
"""Haalt de nieuwste video's van het YouTube-kanaal op en schrijft _data/youtube.yml.

    python3 tools/haal-youtube.py                      # kanaal-ID uit _config.yml
    python3 tools/haal-youtube.py --kanaal UCxxxxxxxx  # expliciet

Gebruikt de publieke Atom-feed van YouTube, dus geen API-sleutel nodig.
De feed geeft de laatste 15 uploads; hiervan bewaren we er MAX_VIDEOS.

Exit 0 = gelukt, exit 1 = fout (bestaande _data/youtube.yml blijft dan staan).
"""
import argparse
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONFIG = REPO / "_config.yml"
UIT = REPO / "_data" / "youtube.yml"
FEED = "https://www.youtube.com/feeds/videos.xml?channel_id={}"
MAX_VIDEOS = 4
NS = {"a": "http://www.w3.org/2005/Atom",
      "yt": "http://www.youtube.com/xml/schemas/2015",
      "media": "http://search.yahoo.com/mrss/"}


def kanaal_uit_config() -> str:
    m = re.search(r'youtube_channel_id:\s*"?(UC[\w-]{22})"?', CONFIG.read_text(encoding="utf-8"))
    return m[1] if m else ""


def q(s: str) -> str:
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--kanaal", default="")
    args = p.parse_args()

    kanaal = args.kanaal or kanaal_uit_config()
    if not re.fullmatch(r"UC[\w-]{22}", kanaal):
        print("Geen geldig kanaal-ID. Zet `youtube_channel_id: \"UC…\"` in _config.yml "
              "of geef --kanaal mee.", file=sys.stderr)
        return 1

    try:
        with urllib.request.urlopen(FEED.format(kanaal), timeout=30) as r:
            xml = r.read()
    except (urllib.error.URLError, TimeoutError) as e:
        print(f"Feed ophalen mislukt: {e}", file=sys.stderr)
        return 1

    try:
        wortel = ET.fromstring(xml)
    except ET.ParseError as e:
        print(f"Feed is geen geldige XML: {e}", file=sys.stderr)
        return 1

    kanaalnaam = wortel.findtext("a:title", default="", namespaces=NS)
    videos = []
    for e in wortel.findall("a:entry", NS)[:MAX_VIDEOS]:
        vid = e.findtext("yt:videoId", default="", namespaces=NS)
        if not re.fullmatch(r"[\w-]{11}", vid):
            continue
        videos.append({
            "id": vid,
            "titel": (e.findtext("a:title", default="", namespaces=NS) or "").strip(),
            "gepubliceerd": (e.findtext("a:published", default="", namespaces=NS) or "")[:10],
        })

    if not videos:
        print("Feed bevat geen video's — _data/youtube.yml ongewijzigd gelaten.",
              file=sys.stderr)
        return 1

    regels = [
        "# Automatisch bijgewerkt door tools/haal-youtube.py — niet met de hand aanpassen.",
        "# De GitHub Action draait dit dagelijks; de homepage toont `videos[0]`.",
        "",
        f"kanaal:     {q(kanaalnaam)}",
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
    print(f"_data/youtube.yml bijgewerkt: {len(videos)} video's, nieuwste = {videos[0]['titel']!r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
