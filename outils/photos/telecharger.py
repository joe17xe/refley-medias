"""Télécharge les photos publiques d'une édition et les range, recadrables, dans le dépôt.

Pourquoi ici : la session de Claude qui monte les vidéos n'a pas accès aux sites
des organisateurs ; les serveurs de GitHub, si. Chaque rendez-vous donne une ou
plusieurs adresses candidates ; on garde la plus grande image obtenue.
"""
import io
import json
import sys
import urllib.request
from pathlib import Path

from PIL import Image

AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
LARGEUR_MAX = 1600


def recuperer(url: str) -> Image.Image | None:
    req = urllib.request.Request(url, headers={"User-Agent": AGENT, "Accept": "image/avif,image/webp,image/*,*/*"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
        img = Image.open(io.BytesIO(data))
        img.load()
        return img
    except Exception as e:  # une adresse morte ne doit pas arrêter les autres
        print(f"  échec {url[:90]} : {e}")
        return None


def main(demande: Path) -> int:
    spec = json.loads(demande.read_text())
    dossier = demande.parent / "photos"
    dossier.mkdir(exist_ok=True)
    rapport = []
    for photo in spec["photos"]:
        cle = photo["cle"]
        print(cle)
        meilleure, source = None, None
        for url in photo["urls"]:
            img = recuperer(url)
            if img and (meilleure is None or img.width * img.height > meilleure.width * meilleure.height):
                meilleure, source = img, url
        if meilleure is None:
            rapport.append({"cle": cle, "ok": False})
            continue
        img = meilleure.convert("RGB")
        if img.width > LARGEUR_MAX:
            img = img.resize((LARGEUR_MAX, round(img.height * LARGEUR_MAX / img.width)), Image.LANCZOS)
        img.save(dossier / f"{cle}.jpg", "JPEG", quality=88, optimize=True)  # EXIF non recopié
        rapport.append({"cle": cle, "ok": True, "source": source, "taille": [img.width, img.height],
                        "credit": photo.get("credit", "")})
        print(f"  gardée {img.width}x{img.height}")
    (dossier / "rapport.json").write_text(json.dumps(rapport, ensure_ascii=False, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(Path(sys.argv[1])))
