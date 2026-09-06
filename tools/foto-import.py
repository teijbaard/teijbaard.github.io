#!/usr/bin/env python3
"""Importeer foto's naar assets/fotos/ en print kant-en-klare YAML.

Gebruik:  python3 tools/foto-import.py ~/Desktop/NieuweFotos

Zet HEIC/JPG/PNG om naar twee WebP-varianten (groot + thumbnail), draait ze
rechtop volgens de EXIF-orientatie en strípt alle metadata — dus ook de
GPS-coordinaten die in iPhone-foto's zitten. Video's (.mov) en .aae-bestanden
worden overgeslagen.

Vereist macOS (`sips`, voor HEIC) en Pillow (`pip3 install Pillow`).
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageOps

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "assets" / "fotos"

FULL_MAX, FULL_Q = 1800, 78
THUMB_MAX, THUMB_Q = 640, 75
EXTS = (".heic", ".heif", ".jpg", ".jpeg", ".png")


def creatiedatum(pad: Path) -> str:
    """YYYY-MM-DD uit de EXIF-opnamedatum, of leeg als die ontbreekt."""
    uit = subprocess.run(["sips", "-g", "creation", str(pad)],
                         capture_output=True, text=True).stdout
    m = re.search(r"creation:\s*(\d{4}):(\d{2}):(\d{2})", uit)
    return f"{m[1]}-{m[2]}-{m[3]}" if m else ""


def open_rechtop(pad: Path, tmpdir: str) -> Image.Image:
    if pad.suffix.lower() in (".heic", ".heif"):
        tmp = Path(tmpdir) / (pad.stem + ".jpg")
        subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "92",
                        "--resampleHeightWidthMax", "2600", str(pad), "--out", str(tmp)],
                       capture_output=True, check=True)
        pad = tmp
    return ImageOps.exif_transpose(Image.open(pad)).convert("RGB")


def passend(im: Image.Image, maxzijde: int) -> Image.Image:
    w, h = im.size
    if max(w, h) <= maxzijde:
        return im
    f = maxzijde / max(w, h)
    return im.resize((round(w * f), round(h * f)), Image.LANCZOS)


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    bron = Path(sys.argv[1]).expanduser()
    if not bron.is_dir():
        print(f"Map bestaat niet: {bron}")
        return 1

    OUT.mkdir(parents=True, exist_ok=True)
    bestanden = sorted(p for p in bron.iterdir() if p.suffix.lower() in EXTS)
    if not bestanden:
        print(f"Geen foto's gevonden in {bron}")
        return 1

    regels = []
    with tempfile.TemporaryDirectory() as td:
        for i, p in enumerate(bestanden, 1):
            datum = creatiedatum(p)
            nummer = re.sub(r"\D", "", p.stem) or f"{i:04d}"
            slug = f"{datum or '0000-00-00'}-img{nummer}"
            if (OUT / f"{slug}.webp").exists():
                print(f"[{i}/{len(bestanden)}] {p.name} — bestaat al, overgeslagen")
                continue

            im = open_rechtop(p, td)
            groot = passend(im, FULL_MAX)
            groot.save(OUT / f"{slug}.webp", "WEBP", quality=FULL_Q, method=5)
            passend(im, THUMB_MAX).save(OUT / f"{slug}-thumb.webp", "WEBP",
                                        quality=THUMB_Q, method=5)
            w, h = groot.size
            print(f"[{i}/{len(bestanden)}] {p.name} -> {slug}.webp  {w}x{h}")
            regels.append(f"""- bestand:      "{slug}.webp"
  titel:        ""
  vervoerder:   ""
  type:         ""
  land:         "nl"
  evenement:    ""
  locatie:      ""
  datum:        "{datum}"
  beschrijving: ""
  breedte:      {w}
  hoogte:       {h}
  hero:         {'true' if w >= h else 'false'}""")

    if regels:
        print("\n--- plak dit bovenaan _data/fotos.yml en vul de lege velden ---\n")
        print("\n".join(regels))
    return 0


if __name__ == "__main__":
    sys.exit(main())
