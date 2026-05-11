#!/usr/bin/env python3
"""Annote les captures avec cadres + numéros pour l'audit Geopost."""
from PIL import Image, ImageDraw, ImageFont
import os

SCREENS = "/home/user/Geopost-CRM-Agents/audit_outputs/screens"
OUT = "/home/user/Geopost-CRM-Agents/audit_outputs/annotated"
os.makedirs(OUT, exist_ok=True)

# Polices
def font(size, bold=False):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

RED = (220, 0, 50)
ORANGE = (255, 140, 0)
YELLOW = (255, 200, 0)

def annotate(src, dst, boxes, title=""):
    img = Image.open(src).convert("RGB")
    # Crop bottom padding
    bbox = img.getbbox()
    img = img.crop((0, 0, img.width, min(img.height, 1100)))
    # Add right gutter for legend
    gutter = 380
    canvas = Image.new("RGB", (img.width + gutter, img.height + 80), "white")
    canvas.paste(img, (0, 80))
    d = ImageDraw.Draw(canvas)
    # Title bar
    d.rectangle([0, 0, canvas.width, 70], fill=(30, 30, 30))
    d.text((20, 22), title, fill="white", font=font(22, bold=True))
    # Boxes
    for i, b in enumerate(boxes, 1):
        x1, y1, x2, y2 = b["box"]
        y1 += 80; y2 += 80
        color = b.get("color", RED)
        d.rectangle([x1, y1, x2, y2], outline=color, width=4)
        # Number badge — clamp inside canvas
        r = 18
        bx = max(r + 2, x1)
        by = max(r + 2, y1)
        d.ellipse([bx - r, by - r, bx + r, by + r], fill=color, outline="white", width=2)
        n = b.get("n", str(i))
        tx = bx - (6 if len(n) == 1 else 11)
        d.text((tx, by - 13), n, fill="white", font=font(18, bold=True))
    # Legend in gutter
    gx = img.width + 20
    d.text((gx, 100), "ÉCARTS RELEVÉS", fill="black", font=font(16, bold=True))
    y = 130
    for i, b in enumerate(boxes, 1):
        color = b.get("color", RED)
        n = b.get("n", str(i))
        r = 14
        d.ellipse([gx, y, gx + 2 * r, y + 2 * r], fill=color)
        d.text((gx + 4 if len(n) == 1 else gx, y + 4), n, fill="white", font=font(14, bold=True))
        d.text((gx + 40, y), b.get("sev", "P1"), fill=color, font=font(13, bold=True))
        # Wrap label
        label = b["label"]
        words = label.split()
        line = ""
        ly = y + 22
        for w in words:
            tw = d.textlength(line + " " + w, font=font(12))
            if tw > gutter - 50 and line:
                d.text((gx + 40, ly), line, fill="black", font=font(12))
                ly += 16
                line = w
            else:
                line = (line + " " + w).strip()
        if line:
            d.text((gx + 40, ly), line, fill="black", font=font(12))
            ly += 16
        y = ly + 12
    canvas.save(dst, "PNG", optimize=True)
    print("OK", dst)

# 01 as-is desktop — broken images, layout sans wrapper, footer cassé
annotate(
    f"{SCREENS}/01_as_is_desktop.png",
    f"{OUT}/A_as_is_desktop_annotated.png",
    title="A — Rendu brut Chromium (sans correction) — desktop 720px",
    boxes=[
        {"n": "1", "box": (260, 35, 420, 75), "sev": "P0",
         "label": "Logo cassé (URL gmail.com CID, inaccessible hors forward Gmail)."},
        {"n": "2", "box": (10, 90, 710, 110), "sev": "P0",
         "label": "Image héro cassée — la promesse principale est dans l'image, perdue si elle ne charge pas."},
        {"n": "3", "box": (10, 115, 710, 155), "sev": "P0",
         "label": "Triplon: même phrase 'Votre satisfaction…' en preheader masqué + alt image + bandeau rouge."},
        {"n": "4", "box": (240, 375, 450, 420), "sev": "P1",
         "label": "CTA ~40px de haut, sous la cible WCAG 44×44 tactile."},
        {"n": "5", "box": (10, 540, 710, 750), "sev": "P0",
         "label": "Footer rendu blanc alors que bgcolor HTML = #2e2e2f — CSS écrase l'attribut. Intention design cassée."},
    ],
)

# 02 with-images desktop
annotate(
    f"{SCREENS}/02_with_images_desktop.png",
    f"{OUT}/B_with_images_desktop_annotated.png",
    title="B — Rendu avec images simulées chargées — desktop 720px",
    boxes=[
        {"n": "6", "box": (260, 35, 420, 100), "sev": "P1",
         "label": "Logo: largeur 139px non standardisée — variante visuelle attendue entre BU non documentée."},
        {"n": "7", "box": (10, 150, 710, 320), "sev": "P0",
         "label": "Héro = image porteuse du H1. Échec total si images bloquées (cf. variante D)."},
        {"n": "8", "box": (10, 380, 710, 420), "sev": "P1",
         "label": "Bandeau titre dupliquant l'image héro — info redondante, occupe la 'fold'."},
        {"n": "9", "box": (40, 460, 700, 610), "sev": "P1",
         "label": "Body: 5 paragraphes pour 1 message. Verbeux, faible hiérarchie, pas d'estimation de temps réelle."},
        {"n": "10", "box": (235, 645, 450, 685), "sev": "P1",
         "label": "CTA en MAJUSCULES + sous-dimensionné. Label à remettre en casse normale."},
    ],
)

# 03 dark mode
annotate(
    f"{SCREENS}/03_dark_mode_desktop.png",
    f"{OUT}/C_dark_mode_annotated.png",
    title="C — Simulation dark mode (Gmail Android / Outlook iOS)",
    boxes=[
        {"n": "11", "box": (50, 25, 690, 120), "sev": "P0",
         "label": "Bloc email reste 100% blanc dans un client sombre — pas de meta name=color-scheme, pas de prefers-color-scheme."},
        {"n": "12", "box": (10, 380, 710, 420), "sev": "P1",
         "label": "Bandeau rouge #DC0032 sur fond sombre: contraste OK mais halo agressif, eye strain."},
        {"n": "13", "box": (10, 800, 710, 1020), "sev": "P1",
         "label": "Footer noir sur blanc dans contexte sombre = clignotement visuel à la lecture."},
    ],
)

# 04 images-off
annotate(
    f"{SCREENS}/04_images_off_desktop.png",
    f"{OUT}/D_images_off_annotated.png",
    title="D — Simulation 'images bloquées' (Outlook desktop par défaut)",
    boxes=[
        {"n": "14", "box": (260, 35, 480, 120), "sev": "P0",
         "label": "Logo absent — alt 'Logo DPD' OK mais aucune marque visible (perte ID brand à l'ouverture)."},
        {"n": "15", "box": (10, 130, 710, 180), "sev": "P0",
         "label": "H1 visuel absent — alt reproduit la phrase mais perte d'impact total. Le message principal doit être en TEXTE HTML."},
        {"n": "16", "box": (10, 200, 710, 250), "sev": "P0",
         "label": "Le bandeau rouge devient le seul 'titre' visible — encore une fois doublon avec l'alt image."},
    ],
)

# 05 mobile
annotate(
    f"{SCREENS}/05_mobile.png",
    f"{OUT}/E_mobile_375_annotated.png",
    title="E — Rendu mobile iPhone 375px — non responsive",
    boxes=[
        {"n": "17", "box": (0, 30, 375, 95), "sev": "P0",
         "label": "Largeur fixe 640px → débordement, logo tronqué à droite sur iPhone 375."},
        {"n": "18", "box": (0, 380, 375, 620), "sev": "P0",
         "label": "Corps de message coupé en fin de ligne — phrases illisibles sans scroll horizontal."},
        {"n": "19", "box": (220, 625, 375, 680), "sev": "P0",
         "label": "CTA 'JE DONNE MO…' tronqué. Conversion mobile impossible."},
    ],
)

print("DONE")
