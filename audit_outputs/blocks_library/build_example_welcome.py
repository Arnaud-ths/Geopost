"""Assemble a full Welcome email using the blocks library — proof of composition."""
import os, re

ROOT = "/home/user/Geopost/audit_outputs/blocks_library"
OUT = f"{ROOT}/_example_welcome_assembled.html"

# Tokens — Welcome email for BRT BU (italian SME e-commerce founder onboarding)
TOKENS = {
    "LANG": "fr-FR",
    "EMAIL_TITLE": "Bienvenue chez Geopost",
    "COLOR_PRIMARY": "#DC0032",
    "COLOR_PRIMARY_DARK": "#a8002a",
    "COLOR_SECONDARY": "#2e2e2f",
    "LOGO_URL": "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='140' height='40' viewBox='0 0 140 40'><rect width='140' height='40' fill='%23fff'/><text x='0' y='30' font-family='Arial,Helvetica,sans-serif' font-size='28' font-weight='900' fill='%23DC0032'>geopost</text></svg>",
    "LOGO_ALT": "Geopost",
    "LOGO_WIDTH": "140",
    "BU_NAME": "Geopost France",
    "BU_HOMEPAGE": "https://geopost.com",
    "UNSUB_URL": "https://geopost.com/unsub?token=preview",
    "PREFS_URL": "https://geopost.com/preferences?token=preview",
    "LEGAL_ADDRESS": "26 rue des Bons Enfants, 92500 Rueil-Malmaison, France",
    "LEGAL_RGPD_TEXT": "En application du Règlement Général sur la Protection des Données (RGPD) et de la loi Informatique et Libertés du 6 janvier 1978 modifiée, vos données personnelles sont traitées par Geopost dans le cadre de la relation client.",
    "CONTACT_DPO_EMAIL": "dpo@geopost.com",
    "LINK_LEGAL_NOTICE_URL": "https://geopost.com/mentions-legales",
    "LINK_PRIVACY_URL": "https://geopost.com/confidentialite",
    "PREHEADER_TEXT": "Activez votre compte en 3 étapes simples. 2 minutes maximum.",
    "H1_TEXT": "Bienvenue chez Geopost.",
    "HERO_IMAGE_URL": "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='640' height='280' viewBox='0 0 640 280'><defs><linearGradient id='g' x1='0' x2='1' y1='0' y2='1'><stop offset='0' stop-color='%23fafafa'/><stop offset='1' stop-color='%23e5e5e5'/></linearGradient></defs><rect width='640' height='280' fill='url(%23g)'/><circle cx='200' cy='140' r='80' fill='%23DC0032' opacity='0.1'/><rect x='280' y='100' width='160' height='100' fill='%23fff' stroke='%23DC0032' stroke-width='3' rx='8'/><text x='320' y='240' font-family='Arial,Helvetica,sans-serif' font-size='14' fill='%23999'>Image décorative</text></svg>",
    "HERO_IMAGE_ALT": "",
    "HERO_IMAGE_WIDTH": "640",
    "SUB_HERO_TEXT": "3 actions pour bien démarrer. <strong>2 minutes</strong> chrono.",
    "CTA_URL": "https://geopost.com/activate",
    "CTA_LABEL": "Activer mon compte",
    "STEP_1_TITLE": "Confirmer votre adresse", "STEP_1_TEXT": "Vérifiez vos coordonnées postales pour des livraisons sans erreur.",
    "STEP_2_TITLE": "Télécharger l'application", "STEP_2_TEXT": "Tracking temps réel et notifications push depuis votre mobile.",
    "STEP_3_TITLE": "Envoyer ou recevoir un colis", "STEP_3_TEXT": "Lancez votre premier envoi en moins de 3 minutes.",
    "BODY_TEXT": "Bonjour, vous venez de créer votre compte. Voici les <strong>3 actions clés</strong> à effectuer dans les prochaines minutes pour bien démarrer.",
    "HEIGHT": "24",
    "TRACKING_PIXEL_URL": "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7",
}

def render(text):
    def repl(m):
        k = m.group(1).strip()
        return TOKENS.get(k, "")
    return re.sub(r"\{\{([A-Z0-9_]+)\}\}", repl, text)

def read_block(slug):
    with open(f"{ROOT}/{slug}.html") as f:
        return f.read()

# Compose the Welcome email
# 1. Open wrapper (replace its <!-- {{CONTENT}} --> with the inner content)
wrapper = read_block("01_wrapper")

preheader = read_block("02_preheader")
header_logo = read_block("03_header_logo")
hero = read_block("04_hero_text_image")
sub_hero = read_block("05_sub_hero")
body_intro = read_block("08_body_1col")
steps = read_block("10_body_3steps")
cta = read_block("06_cta_primary")
spacer = read_block("16_spacer")
footer = read_block("15_footer_legal")
pixel = read_block("17_tracking_pixel")

inner_content = (
    preheader +
    header_logo +
    hero +
    sub_hero +
    body_intro +
    steps +
    spacer +
    cta +
    footer +
    pixel
)

assembled = wrapper.replace("<!-- {{CONTENT}} -->", inner_content)
final = render(assembled)

with open(OUT, "w") as f:
    f.write(final)

print(f"OK {OUT} ({os.path.getsize(OUT)//1024} KB)")
