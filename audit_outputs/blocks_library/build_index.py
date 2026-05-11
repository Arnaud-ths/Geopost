"""Build the visual index of blocks: each block rendered with default tokens + doc."""
import os, re, html

ROOT = "/home/user/Geopost/audit_outputs/blocks_library"
OUT = f"{ROOT}/_index.html"

# Default tokens — Geopost corporate visual baseline
TOKENS = {
    "LANG": "fr-FR",
    "EMAIL_TITLE": "Geopost — Email Preview",
    "COLOR_PRIMARY": "#DC0032",
    "COLOR_PRIMARY_DARK": "#a8002a",
    "COLOR_SECONDARY": "#2e2e2f",
    "COLOR_POSITIVE": "#16a34a",
    "COLOR_NEGATIVE": "#dc2626",
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
    "APP_STORE_URL": "https://apps.apple.com/preview",
    "GOOGLE_PLAY_URL": "https://play.google.com/preview",
    "APP_STORE_BADGE_URL": "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='140' height='48' viewBox='0 0 140 48'><rect width='140' height='48' rx='6' fill='%23000'/><text x='12' y='20' font-family='Arial,Helvetica,sans-serif' font-size='9' fill='%23fff'>Télécharger dans</text><text x='12' y='36' font-family='Arial,Helvetica,sans-serif' font-size='14' font-weight='700' fill='%23fff'>App Store</text></svg>",
    "GOOGLE_PLAY_BADGE_URL": "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='140' height='48' viewBox='0 0 140 48'><rect width='140' height='48' rx='6' fill='%23000'/><text x='12' y='20' font-family='Arial,Helvetica,sans-serif' font-size='9' fill='%23fff'>Disponible sur</text><text x='12' y='36' font-family='Arial,Helvetica,sans-serif' font-size='14' font-weight='700' fill='%23fff'>Google Play</text></svg>",
    "BODY_TEXT": "Bonjour, vous venez de créer votre compte Geopost. Nous sommes prêts à vous aider à envoyer ou suivre vos colis. Voici les <strong>3 actions clés</strong> à effectuer dans les prochaines minutes.",
    "CARD_1_ICON": "📍", "CARD_1_TITLE": "Tracking temps réel", "CARD_1_TEXT": "Suivez vos colis à la minute près, où qu'ils soient.",
    "CARD_2_ICON": "🔔", "CARD_2_TITLE": "Notifications push", "CARD_2_TEXT": "Avertissement à chaque étape, sans email parasite.",
    "CARD_3_ICON": "⚙️", "CARD_3_TITLE": "Modifier en 1 tap", "CARD_3_TEXT": "Reporter, dévier, choisir un point relais — instantané.",
    "STEP_1_TITLE": "Confirmer votre adresse", "STEP_1_TEXT": "Vérifiez vos coordonnées postales pour des livraisons sans erreur.",
    "STEP_2_TITLE": "Télécharger l'application", "STEP_2_TEXT": "Tracking temps réel et notifications push depuis votre mobile.",
    "STEP_3_TITLE": "Envoyer ou recevoir un colis", "STEP_3_TEXT": "Vous êtes prêt. Lancez votre premier envoi en moins de 3 minutes.",
    "IMAGE_URL": "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='260' height='180' viewBox='0 0 260 180'><rect width='260' height='180' fill='%23f5f5f4'/><rect x='80' y='40' width='100' height='100' fill='%23DC0032' opacity='0.2' rx='8'/><text x='130' y='100' text-anchor='middle' font-family='Arial' font-size='12' fill='%23666'>Service visuel</text></svg>",
    "IMAGE_ALT": "Service Point Relais",
    "IMAGE_WIDTH": "260",
    "SUBTITLE": "Nouveau service",
    "TITLE": "Le point relais qui vous arrange.",
    "TEXT": "5 000 points relais Geopost partout en France. Le plus proche est peut-être à 3 minutes.",
    "LINK_URL": "https://geopost.com/points-relais",
    "LINK_LABEL": "Trouver mon point relais",
    "PROMO_HEADLINE": "-20% sur votre prochain envoi",
    "PROMO_CODE": "BOOST20",
    "PROMO_EXPIRES": "31 août 2026",
    "PROMO_CONDITIONS_URL": "https://geopost.com/conditions-promo",
    "METRIC_1_VALUE": "1 247", "METRIC_1_LABEL": "Colis envoyés", "METRIC_1_DELTA": "+12% vs nov.", "METRIC_1_DELTA_POSITIVE": "true",
    "METRIC_2_VALUE": "98,3%", "METRIC_2_LABEL": "Livraisons à temps", "METRIC_2_DELTA": "+0,8 pts", "METRIC_2_DELTA_POSITIVE": "true",
    "METRIC_3_VALUE": "3,2j", "METRIC_3_LABEL": "Délai moyen", "METRIC_3_DELTA": "-0,3j vs nov.", "METRIC_3_DELTA_POSITIVE": "false",
    "AM_PHOTO_URL": "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='80' height='80' viewBox='0 0 80 80'><circle cx='40' cy='40' r='40' fill='%23f5f5f4'/><circle cx='40' cy='32' r='14' fill='%23ccc'/><path d='M16 72 Q40 56 64 72 L64 80 L16 80 Z' fill='%23ccc'/></svg>",
    "AM_NAME": "Marie Dupont",
    "AM_ROLE": "Account Manager Singular",
    "AM_PHONE": "+33 1 23 45 67 89",
    "AM_EMAIL": "marie.dupont@geopost.com",
    "HEIGHT": "24",
    "DIVIDER": "false",
    "TRACKING_PIXEL_URL": "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7",
    "CONTENT": "<!-- Bloc démo -->",
}

# Block manifest with metadata
BLOCKS = [
    ("01_wrapper", "Wrapper email + reset", "Base à utiliser pour TOUT email. Inclut head complet, dark mode, responsive, pack mso.", ["LANG", "EMAIL_TITLE", "COLOR_PRIMARY"], True),
    ("02_preheader", "Preheader masqué", "Texte invisible mais lu par l'aperçu inbox. ≤110 caractères.", ["PREHEADER_TEXT"], False),
    ("03_header_logo", "Header logo simple", "Logo BU centré, sous le preheader, en haut de l'email.", ["LOGO_URL", "LOGO_ALT", "LOGO_WIDTH", "BU_HOMEPAGE"], False),
    ("04_hero_text_image", "Hero texte + visuel décoratif", "H1 PORTÉ PAR LE TEXTE (jamais l'image). Image décorative alt vide.", ["H1_TEXT", "HERO_IMAGE_URL", "HERO_IMAGE_ALT", "HERO_IMAGE_WIDTH"], False),
    ("05_sub_hero", "Sub-héro", "1 phrase bénéfice + durée. ≤20 mots.", ["SUB_HERO_TEXT"], False),
    ("06_cta_primary", "CTA primaire bulletproof", "1 CTA principal. VML Outlook + fallback table. ≥44px tactile.", ["CTA_URL", "CTA_LABEL", "COLOR_PRIMARY"], False),
    ("07_cta_double_apps", "CTA double App Store + Google Play", "Promote app uniquement. Badges officiels obligatoires.", ["APP_STORE_URL", "GOOGLE_PLAY_URL", "APP_STORE_BADGE_URL", "GOOGLE_PLAY_BADGE_URL"], False),
    ("08_body_1col", "Body 1 colonne", "Paragraphe texte. 1 idée. Empilable.", ["BODY_TEXT"], False),
    ("09_body_3cards", "Body 3 cards horizontales", "3 bénéfices côte à côte. Stack vertical mobile.", ["CARD_1_*", "CARD_2_*", "CARD_3_*"], False),
    ("10_body_3steps", "Body 3 étapes verticales", "Onboarding, mode d'emploi. Numérotation typo (pas image).", ["STEP_1_*", "STEP_2_*", "STEP_3_*", "COLOR_PRIMARY"], False),
    ("11_image_text_right", "Image + texte (responsive stack)", "Bloc service / nouveauté. Image gauche, texte droite, stack mobile.", ["IMAGE_URL", "IMAGE_ALT", "SUBTITLE", "TITLE", "TEXT", "LINK_URL", "LINK_LABEL"], False),
    ("12_banner_promo", "Bannière promo (code)", "Boost sales variante prix. Code, date, conditions visibles.", ["PROMO_HEADLINE", "PROMO_CODE", "PROMO_EXPIRES", "PROMO_CONDITIONS_URL", "COLOR_PRIMARY"], False),
    ("13_metric_data", "Data metric (B2B Singular)", "3 chiffres + variation. Pas d'info via couleur seule.", ["METRIC_1_*", "METRIC_2_*", "METRIC_3_*", "COLOR_POSITIVE", "COLOR_NEGATIVE"], False),
    ("14_signature_am", "Signature manuelle AM (B2B)", "Singular only. Photo + nom + rôle + tel + email.", ["AM_PHOTO_URL", "AM_NAME", "AM_ROLE", "AM_PHONE", "AM_EMAIL", "BU_NAME"], False),
    ("15_footer_legal", "Footer légal RGPD", "Adresse + RGPD + désabonnement + DPO. Pays-spécifique.", ["BU_NAME", "LEGAL_ADDRESS", "LEGAL_RGPD_TEXT", "UNSUB_URL", "PREFS_URL", "CONTACT_DPO_EMAIL"], False),
    ("16_spacer", "Spacer / divider", "Espacement vertical ou ligne. Table-based.", ["HEIGHT", "DIVIDER"], False),
    ("17_tracking_pixel", "Tracking pixel", "1×1 transparent en fin d'email pour tracking ouvertures imagino.", ["TRACKING_PIXEL_URL"], False),
]

def render(text):
    """Replace {{TOKEN}} with TOKENS[TOKEN]."""
    def repl(m):
        k = m.group(1).strip()
        return TOKENS.get(k, f"{{{{{k}}}}}")
    return re.sub(r"\{\{([A-Z0-9_]+)\}\}", repl, text)

# Build the index
INDEX_CSS = """
* { box-sizing: border-box; }
body { margin: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif; background: #f4f4f4; color: #1a1a1a; line-height: 1.6; }
header { background: linear-gradient(135deg, #1a1a1a 0%, #2e2e2f 100%); color: #fff; padding: 48px 32px; }
header .inner { max-width: 1200px; margin: 0 auto; }
header .eyebrow { display:inline-block; background: #DC0032; color:#fff; padding:4px 12px; font-size: 11px; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; border-radius:2px; margin-bottom: 16px; }
header h1 { font-size: 36px; margin: 0 0 8px; font-weight: 800; letter-spacing: -0.5px; }
header p { margin: 4px 0; color: rgba(255,255,255,0.7); font-size: 14px; }
.wrap { max-width: 1200px; margin: 32px auto; padding: 0 32px 80px; }
.intro { background: #fff; border-radius: 8px; padding: 24px 28px; margin-bottom: 32px; border-left: 4px solid #DC0032; }
.intro h2 { margin: 0 0 8px; font-size: 18px; }
.intro p { margin: 0; font-size: 14px; color: #555; }
.block-card { background: #fff; border-radius: 12px; margin-bottom: 32px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.04); }
.block-header { padding: 20px 24px; border-bottom: 1px solid #e5e5e5; display: flex; justify-content: space-between; align-items: flex-start; gap: 20px; }
.block-header .left { flex: 1; }
.block-header h2 { margin: 0 0 4px; font-size: 18px; }
.block-header .num { display:inline-block; background:#1a1a1a; color:#fff; padding:2px 8px; border-radius:4px; font-size:12px; font-family: monospace; margin-right: 8px; }
.block-header p.desc { margin: 0; color: #666; font-size: 13px; }
.block-header .tokens { font-family: monospace; font-size: 11px; color: #888; padding: 8px 12px; background: #f9f9f9; border-radius: 4px; max-width: 320px; }
.block-render { background: #f4f4f4; padding: 24px; }
.block-render-inner { max-width: 640px; margin: 0 auto; background: #fff; box-shadow: 0 4px 16px rgba(0,0,0,0.06); }
.block-source { padding: 16px 24px; border-top: 1px solid #e5e5e5; background: #fafafa; }
.block-source summary { cursor: pointer; font-size: 13px; font-weight: 600; color: #666; user-select: none; }
.block-source pre { background: #1a1a1a; color: #e5e5e5; padding: 16px; border-radius: 6px; overflow-x: auto; font-size: 11px; line-height: 1.4; margin: 12px 0 0; }
.block-source code { font-family: "SF Mono", Monaco, monospace; }
.note { font-size: 12px; color: #999; margin-top: 8px; }
.toc { background: #fff; border-radius: 8px; padding: 20px 24px; margin-bottom: 32px; }
.toc h2 { margin: 0 0 12px; font-size: 16px; }
.toc ol { margin: 0; padding-left: 20px; column-count: 2; column-gap: 40px; }
.toc li { margin: 4px 0; font-size: 13px; }
.toc a { color: #1a1a1a; text-decoration: none; border-bottom: 1px solid transparent; }
.toc a:hover { border-color: #DC0032; }
@media (max-width: 720px) {
  .block-header { flex-direction: column; }
  .toc ol { column-count: 1; }
}
"""

# TOC items
toc = "\n".join(f'    <li><a href="#block-{slug}">{slug.split("_",1)[0]}. {name}</a></li>' for slug, name, _, _, _ in BLOCKS)

# Block sections
sections = []
for slug, name, desc, tokens_list, is_wrapper in BLOCKS:
    path = f"{ROOT}/{slug}.html"
    with open(path) as f:
        src = f.read()
    rendered = render(src)
    # If it's the wrapper, simulate by injecting a placeholder content
    if is_wrapper:
        rendered = rendered.replace("<!-- {{CONTENT}} -->", '<div style="padding:60px 32px; text-align:center; color:#999; font-style:italic;">(Le wrapper enveloppe les autres blocs)</div>')
    # Strip the HTML comment block at top for the rendered preview
    # but keep it in the source
    iframe_src = rendered
    # Wrap non-full-page blocks in a minimal preview shell
    if not is_wrapper:
        iframe_src = f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><style>body{{margin:0;background:#fff;font-family:Arial,sans-serif;}}</style></head><body>{rendered}</body></html>"""

    # Escape src for srcdoc
    srcdoc = html.escape(iframe_src, quote=True)

    tokens_html = "<br>".join(f"<code>{{{{<wbr>{t}}}}}</code>" for t in tokens_list)
    sections.append(f"""
<section class="block-card" id="block-{slug}">
  <div class="block-header">
    <div class="left">
      <h2><span class="num">{slug.split('_',1)[0]}</span>{name}</h2>
      <p class="desc">{desc}</p>
    </div>
    <div class="tokens">
      <strong style="color:#1a1a1a;">Tokens :</strong><br>{tokens_html}
    </div>
  </div>
  <div class="block-render">
    <div class="block-render-inner">
      <iframe srcdoc="{srcdoc}" style="width:100%; min-height:300px; border:0; display:block;" loading="lazy" onload="this.style.height = this.contentDocument.body.scrollHeight + 'px';"></iframe>
    </div>
  </div>
  <details class="block-source">
    <summary>Voir le code HTML source</summary>
    <pre><code>{html.escape(src)}</code></pre>
  </details>
</section>""")

FULL = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Geopost — Blocks Library v1</title>
<style>{INDEX_CSS}</style>
</head>
<body>
<header>
  <div class="inner">
    <span class="eyebrow">Geopost · Blocks Library v1</span>
    <h1>Librairie de blocs email</h1>
    <p>17 blocs conformes — Outlook 2007 → M365 · WCAG 2.1 AA · Dark mode · Mobile responsive · Multi-brand tokens</p>
    <p>11 mai 2026 · Geopost Lead CRM V1</p>
  </div>
</header>
<div class="wrap">

  <div class="intro">
    <h2>Comment utiliser cette librairie</h2>
    <p>Chaque bloc est <strong>standalone</strong> et paramétrable via tokens <code>{{<wbr>{{TOKEN}}<wbr>}}</code>. Le wrapper (01) enveloppe les autres blocs. La composition d'un email = wrapper + preheader + header + héro + (1-3 blocs body) + CTA + footer + tracking pixel. Aperçus ci-dessous rendus avec les <strong>valeurs par défaut Geopost corporate</strong> — à substituer par les tokens BU réels en production.</p>
  </div>

  <div class="toc">
    <h2>Sommaire</h2>
    <ol>
{toc}
    </ol>
  </div>

  {''.join(sections)}

</div>
</body>
</html>
"""

with open(OUT, "w") as f:
    f.write(FULL)

print(f"OK {OUT} ({os.path.getsize(OUT)//1024} KB)")
