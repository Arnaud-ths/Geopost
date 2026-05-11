"""Deck 1 — Audit DPD FR · 10 slides."""
import base64, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from _framework import cover, content_slide, build_deck

ROOT = "/home/user/Geopost/audit_outputs"
DECK = "AUDIT · 10 slides"
N = 10

def img64(rel):
    with open(os.path.join(ROOT, rel), "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()

S = []

# 1 — Cover
S.append(cover(
    "Audit CRM · Geopost",
    "Templates Revamp Project",
    "Audit POC #1 — DPD France · Enquête satisfaction",
    "11 mai 2026 · Geopost Lead CRM V1 + Audit Agent V1",
    1, N
))

# 2 — Cadre & méthode
S.append(content_slide(
    "Slide 02 · Méthode",
    "Comment on a auditté",
    """
    <div class="layout-2col">
      <div>
        <h3>Périmètre</h3>
        <ul>
          <li><strong>1 email POC</strong> — DPD FR enquête satisfaction post-livraison</li>
          <li>Source : <code>sample_existing_dpd_email.html</code> (124 lignes)</li>
          <li>Langue : FR · Plateforme : imagino</li>
          <li><strong>Hypothèse traçable :</strong> DPD FR pas listée dans les 4 BUs du brief, à confirmer</li>
        </ul>
        <h3 style="margin-top:18px;">6 dimensions auditées</h3>
        <ul>
          <li>Structure HTML · Compatibilité Outlook · Accessibilité WCAG AA</li>
          <li>Design system · UX writing · Cohérence multi-brand</li>
        </ul>
      </div>
      <div>
        <h3>5 environnements simulés (Chromium)</h3>
        <table>
          <thead><tr><th>Variante</th><th>Environnement</th></tr></thead>
          <tbody>
            <tr><td><strong>A</strong></td><td>Desktop 720px brut</td></tr>
            <tr><td><strong>B</strong></td><td>Desktop avec images</td></tr>
            <tr><td><strong>C</strong></td><td>Dark mode Gmail / Outlook iOS</td></tr>
            <tr><td><strong>D</strong></td><td>Images bloquées Outlook</td></tr>
            <tr><td><strong>E</strong></td><td>Mobile iPhone 375px</td></tr>
          </tbody>
        </table>
      </div>
    </div>
    """,
    2, N, DECK
))

# 3 — Synthèse exécutive
S.append(content_slide(
    "Slide 03 · Synthèse exécutive",
    "5 constats P0 qui plombent le POC",
    """
    <div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px;">
      <div class="card accent">
        <h3><span class="badge p0">P0</span> Non-responsive</h3>
        <p>Largeur fixe 640px, aucune <code>@media</code>, pas de <code>meta viewport</code>. CTA tronqué sur iPhone → <strong>conversion mobile impossible</strong>.</p>
      </div>
      <div class="card accent">
        <h3><span class="badge p0">P0</span> H1 dans une image</h3>
        <p>Le message principal est porté par l'image héro. Outlook bloque les images par défaut → <strong>promesse de marque invisible</strong>.</p>
      </div>
      <div class="card accent">
        <h3><span class="badge p0">P0</span> Robustesse Outlook nulle</h3>
        <p><code>&lt;head&gt;</code> vide, <code>&lt;tbody&gt;</code> orphelin, pas de mso conditionals, CTA non bulletproof, pas de <code>role="presentation"</code>.</p>
      </div>
      <div class="card accent">
        <h3><span class="badge p1">P1</span> Triplon éditorial</h3>
        <p>« Votre satisfaction… » répété 3 fois (preheader + alt image + bandeau). <strong>Preheader gaspillé</strong>.</p>
      </div>
      <div class="card accent" style="grid-column: span 2;">
        <h3><span class="badge p1">P1</span> UX writing verbeux + CTA sous-dimensionné</h3>
        <p>5 paragraphes pour porter 1 message. CTA en MAJUSCULES, hauteur ~40px (sous cible WCAG 44×44 tactile). Pas d'estimation de temps réelle (« quelques minutes » → quantifier <em>« 2 minutes »</em>).</p>
      </div>
    </div>
    """,
    3, N, DECK
))

# 4 — Capture A
S.append(content_slide(
    "Slide 04 · Variante A",
    "Rendu brut — desktop sans correction",
    f"""
    <div class="layout-img-right">
      <div>
        <h3>5 écarts visibles à l'œil nu</h3>
        <ul>
          <li><span class="badge p0">1</span> Logo cassé (URL CID Gmail inaccessible)</li>
          <li><span class="badge p0">2</span> Image héro cassée — même cause</li>
          <li><span class="badge p0">3</span> Triplon du slogan « Votre satisfaction… »</li>
          <li><span class="badge p1">4</span> CTA ~40px &lt; cible WCAG 44×44</li>
          <li><span class="badge p0">5</span> Footer rendu blanc — <code>bgcolor</code> écrasé par CSS</li>
        </ul>
        <p class="muted" style="margin-top:18px;">C'est ce que voit un destinataire qui ouvre l'email aujourd'hui hors du contexte Gmail forward d'origine.</p>
      </div>
      <img src="{img64('annotated/A_as_is_desktop_annotated.png')}" alt="Capture A annotée">
    </div>
    """,
    4, N, DECK
))

# 5 — Capture D — images bloquées
S.append(content_slide(
    "Slide 05 · Variante D — la plus critique",
    "Outlook desktop bloque les images par défaut",
    f"""
    <div class="layout-img-right">
      <div>
        <h3>Sans les images, l'email perd son sens</h3>
        <ul>
          <li><span class="badge p0">14</span> Logo absent — identité de marque invisible</li>
          <li><span class="badge p0">15</span> H1 visuel absent — message principal perdu</li>
          <li><span class="badge p0">16</span> Bandeau rouge devient le seul « titre » — doublon avec alt</li>
        </ul>
        <p style="margin-top:18px;"><strong>Règle d'or :</strong> le message principal d'un email <em>ne doit jamais</em> être porté uniquement par une image. Texte HTML en H1 + image décorative <code>alt=""</code>.</p>
      </div>
      <img src="{img64('annotated/D_images_off_annotated.png')}" alt="Capture D annotée">
    </div>
    """,
    5, N, DECK
))

# 6 — Capture E mobile
S.append(content_slide(
    "Slide 06 · Variante E",
    "Mobile 375px — conversion impossible",
    f"""
    <div class="layout-img-right">
      <div>
        <h3>L'email n'est pas responsive</h3>
        <ul>
          <li><span class="badge p0">17</span> Largeur 640px débordée → logo tronqué</li>
          <li><span class="badge p0">18</span> Body coupé en fin de ligne → illisible</li>
          <li><span class="badge p0">19</span> CTA « JE DONNE MO… » tronqué → conversion impossible</li>
        </ul>
        <p style="margin-top:18px;"><strong>Impact :</strong> sur ~60% d'ouvertures mobile dans le secteur, c'est <em>l'écart qui coûte le plus au POC</em>.</p>
        <p class="muted">Fix : <code>meta viewport</code> + <code>@media (max-width:480)</code> + <code>width:100%</code> mobile + images fluides.</p>
      </div>
      <img src="{img64('annotated/E_mobile_375_annotated.png')}" alt="Capture E mobile annotée">
    </div>
    """,
    6, N, DECK
))

# 7 — Capture C dark + B
S.append(content_slide(
    "Slide 07 · Variantes C & B",
    "Dark mode et rendu idéal",
    f"""
    <div class="layout-2col" style="align-items:start;">
      <div>
        <h3>C · Dark mode (Gmail Android / Outlook iOS)</h3>
        <img src="{img64('annotated/C_dark_mode_annotated.png')}" alt="Dark mode" style="max-height:360px; width:100%; object-fit:contain; border-radius:6px; border:1px solid var(--border); box-shadow:0 4px 12px rgba(0,0,0,0.06);">
        <ul style="margin-top:8px; font-size:14px;">
          <li><span class="badge p0">11</span> Bloc 100% blanc dans client sombre</li>
          <li><span class="badge p1">12</span> Halo agressif du bandeau rouge</li>
        </ul>
      </div>
      <div>
        <h3>B · Cas idéal (images chargées)</h3>
        <img src="{img64('annotated/B_with_images_desktop_annotated.png')}" alt="Cas idéal" style="max-height:360px; width:100%; object-fit:contain; border-radius:6px; border:1px solid var(--border); box-shadow:0 4px 12px rgba(0,0,0,0.06);">
        <ul style="margin-top:8px; font-size:14px;">
          <li><span class="badge p1">8</span> Bandeau dupliquant l'image héro</li>
          <li><span class="badge p1">9</span> Body 5 paragraphes pour 1 message</li>
        </ul>
      </div>
    </div>
    """,
    7, N, DECK
))

# 8 — Grille consolidée (top écarts)
S.append(content_slide(
    "Slide 08 · Grille consolidée",
    "36 écarts détectés — top 12",
    """
    <table>
      <thead><tr><th style="width:30px;">#</th><th>Dimension</th><th>Constat</th><th>Sév.</th><th>Dispatch</th></tr></thead>
      <tbody>
        <tr><td>1</td><td>Structure</td><td><code>&lt;head&gt;</code> vide : pas de DOCTYPE, charset, viewport, title</td><td><span class="badge p0">P0</span></td><td>04</td></tr>
        <tr><td>4</td><td>Structure</td><td>Images pointant vers <code>mail.google.com</code> (CID Gmail)</td><td><span class="badge p0">P0</span></td><td>04</td></tr>
        <tr><td>5</td><td>Structure</td><td>Pas de <code>meta viewport</code> → non responsive</td><td><span class="badge p0">P0</span></td><td>04</td></tr>
        <tr><td>7</td><td>Outlook</td><td>CTA <code>border-radius</code> CSS sans fallback VML bulletproof</td><td><span class="badge p0">P0</span></td><td>04</td></tr>
        <tr><td>11</td><td>a11y</td><td><code>role="presentation"</code> absent sur tables layout</td><td><span class="badge p0">P0</span></td><td>04</td></tr>
        <tr><td>13</td><td>a11y</td><td>H1 porté par image — perdu si images bloquées</td><td><span class="badge p0">P0</span></td><td>03+04</td></tr>
        <tr><td>16</td><td>a11y</td><td>CTA sans <code>aria-label</code>, sans focus, en MAJUSCULES</td><td><span class="badge p0">P0</span></td><td>02+04</td></tr>
        <tr><td>19</td><td>a11y</td><td>Aucune adaptation dark mode</td><td><span class="badge p0">P0</span></td><td>04</td></tr>
        <tr><td>26</td><td>Design</td><td>Conflit bgcolor footer #2e2e2f vs CSS inline #fff</td><td><span class="badge p0">P0</span></td><td>03+04</td></tr>
        <tr><td>27</td><td>Copy</td><td>Preheader = duplique H1 + alt image</td><td><span class="badge p1">P1</span></td><td>02</td></tr>
        <tr><td>30</td><td>Copy</td><td>Body 5 paragraphes pour 1 message</td><td><span class="badge p1">P1</span></td><td>02</td></tr>
        <tr><td>33</td><td>Brand</td><td>#DC0032 (rouge Geopost) appliqué à DPD FR à valider</td><td><span class="badge p1">P1</span></td><td>06</td></tr>
      </tbody>
    </table>
    <p class="muted" style="margin-top:8px;">+ 24 autres écarts dans le rapport complet — voir <code>AUDIT_DPD_FR_v1.md</code></p>
    """,
    8, N, DECK
))

# 9 — Scoring + plan
S.append(content_slide(
    "Slide 09 · Scoring vs brief & plan d'action",
    "POC = 1.3 / 5 — non production-ready",
    """
    <div class="layout-2col">
      <div>
        <h3>Score par issue du brief §2</h3>
        <table>
          <thead><tr><th>Issue brief</th><th>Score</th></tr></thead>
          <tbody>
            <tr><td>Layouts à optimiser</td><td><strong>1 / 5</strong></td></tr>
            <tr><td>Accessibilité</td><td><strong>2 / 5</strong></td></tr>
            <tr><td>Impact visuel</td><td><strong>1 / 5</strong></td></tr>
            <tr><td>UX writing</td><td><strong>2 / 5</strong></td></tr>
            <tr><td>Robustesse Outlook</td><td><strong>1 / 5</strong></td></tr>
            <tr><td>Scalabilité multi-pays</td><td><strong>1 / 5</strong></td></tr>
          </tbody>
        </table>
      </div>
      <div>
        <h3>Plan d'action</h3>
        <ul>
          <li><span class="badge p0">P0</span> 8 actions bloquantes — <em>avant pitch shortlist</em><br><span class="muted">Head email, wrapper table, héro texte, bulletproof CTA, responsive, role=presentation, focus, footer</span></li>
          <li style="margin-top:10px;"><span class="badge p1">P1</span> 7 actions importantes — <em>avant production</em><br><span class="muted">Pack mso, preheader, H1 actionnable, body compressé, dark mode, palette par BU</span></li>
          <li style="margin-top:10px;"><span class="badge p2">P2</span> 4 actions cosmétiques — <em>post-MVP</em><br><span class="muted">Logo standardisé, tokens documentés, liens maps, contraste AAA</span></li>
        </ul>
      </div>
    </div>
    """,
    9, N, DECK
))

# 10 — Dispatch + next steps
S.append(content_slide(
    "Slide 10 · Dispatch & next steps",
    "6 briefs sous-agents prêts à exécuter",
    """
    <div class="flow">
      <div class="step"><div class="num">02</div><h4>CRO & UX Writing</h4><p>Réécrire objet + preheader + H1 + body + CTA</p></div>
      <div class="step"><div class="num">03</div><h4>Template Design</h4><p>Spec héro texte + CTA ≥44px + footer</p></div>
      <div class="step"><div class="num">04</div><h4>HTML Integration</h4><p>Head, mso, responsive, dark mode, bulletproof</p></div>
      <div class="step"><div class="num">05</div><h4>Modular Library</h4><p>4 blocs réutilisables (header, héro, CTA, footer)</p></div>
      <div class="step"><div class="num">06</div><h4>Guidelines</h4><p>Palette BU, échelle typo, taille CTA tactile</p></div>
      <div class="step"><div class="num">01</div><h4>Audit V2</h4><p>3 autres POC inter-BU à fournir par Geopost</p></div>
    </div>
    <h3 style="margin-top:24px;">À débloquer côté Geopost</h3>
    <ul>
      <li>3 autres emails POC (BRT IT, DPD CH, DPD CZ/SK) — indispensable pour audit comparatif inter-BU</li>
      <li>Objet email du POC DPD FR (manquant dans l'export)</li>
      <li>Confirmation DPD FR dans le scope revamp Phase 2</li>
      <li>Confirmation conformité palette #DC0032 vs charte DPD FR officielle</li>
    </ul>
    <div style="margin-top: auto; padding-top: 20px; border-top: 1px solid var(--border); font-size:13px; color:var(--muted);">
      <strong>Prochain jalon :</strong> pitch shortlist semaine du 1er juin 2026 · deadline RFP 22 mai 2026
    </div>
    """,
    10, N, DECK
))

build_deck("Audit DPD FR — 10 slides", S, f"{ROOT}/decks/DECK_1_AUDIT.html")
print(f"OK Deck 1 ({len(S)} slides)")
