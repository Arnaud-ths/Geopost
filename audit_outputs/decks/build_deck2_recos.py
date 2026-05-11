"""Deck 2 — Recos CRM · 40 slides — focus parcours par BU + templatisation."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from _framework import cover, section_slide, content_slide, build_deck

ROOT = "/home/user/Geopost/audit_outputs"
DECK = "RECOS CRM · 40 slides"
N = 40
S = []

# ============ SECTION 1 — Cadre (slides 1-4) ============

# 1 Cover
S.append(cover(
    "Recommandations CRM · Geopost",
    "Parcours, templatisation & méthode email",
    "Phase 2 — Roll-out 6 templates × 5 BUs",
    "11 mai 2026 · Geopost Lead CRM V1",
    1, N
))

# 2 Section divider Partie 01 — Cadre
S.append(section_slide(1, "Cadre & ambition", "Ce que la Phase 2 doit délivrer", 2, N))

# 3 Ambition
S.append(content_slide(
    "Slide 03 · Ambition Phase 2",
    "De 1 POC fragile à une fabrique scalable",
    """
    <div class="layout-2col">
      <div>
        <h3>Constat Phase 1 (POC)</h3>
        <ul>
          <li>Templates legacy, code Outlook fragile</li>
          <li>Variations visuelles d'un email à l'autre</li>
          <li>Adaptation manuelle lourde par BU</li>
          <li>Guidelines peu formalisées</li>
          <li>POC noté <strong>1.3 / 5</strong> dans l'audit</li>
        </ul>
      </div>
      <div>
        <h3>Ambition Phase 2</h3>
        <ul>
          <li><strong>Templates clean</strong>, simples, flexibles, réutilisables</li>
          <li><strong>Architecture modulaire</strong> : core + blocs + tokens BU</li>
          <li><strong>Lisibilité &amp; a11y</strong> WCAG AA strict</li>
          <li><strong>Multi-pays / multi-brand</strong> sans recompilation</li>
          <li><strong>Performance</strong> : +30% click rate cible <span class="muted">[à confirmer Geopost]</span></li>
        </ul>
      </div>
    </div>
    <div class="kpi" style="margin-top:20px;">
      <div class="item"><div class="v">6</div><div class="l">Templates à refondre</div></div>
      <div class="item"><div class="v">5</div><div class="l">BUs au lancement</div></div>
      <div class="item"><div class="v">~30</div><div class="l">Blocs modulaires cibles</div></div>
      <div class="item"><div class="v">1</div><div class="l">Librairie unique imagino</div></div>
    </div>
    """,
    3, N, DECK
))

# 4 Périmètre 6 templates × 5 BU
S.append(content_slide(
    "Slide 04 · Périmètre",
    "6 templates × 5 BUs = 30 livrables, 1 librairie",
    """
    <table>
      <thead><tr><th>Famille</th><th>Template</th><th>Type</th><th>Trigger</th></tr></thead>
      <tbody>
        <tr><td rowspan="3"><strong>Trigger automatisés</strong></td><td>Welcome</td><td>Onboarding</td><td>Création compte</td></tr>
        <tr><td>Promote app</td><td>Acquisition</td><td>J+7 après création</td></tr>
        <tr><td>Boost sales</td><td>Réactivation</td><td>30j d'inactivité</td></tr>
        <tr><td rowspan="3"><strong>One-shot</strong></td><td>Commercial peak</td><td>Campagne</td><td>Noël / BF / Saint-Valentin</td></tr>
        <tr><td>Services</td><td>Information</td><td>Sortie offre out-of-home</td></tr>
        <tr><td>Singular</td><td>B2B SME</td><td>Boost ventes plateforme</td></tr>
      </tbody>
    </table>
    <div style="margin-top:20px;">
      <span class="tag">Geopost corporate</span>
      <span class="tag">BRT (Italie)</span>
      <span class="tag">DPD CH</span>
      <span class="tag">DPD CZ</span>
      <span class="tag">DPD SK</span>
      <span class="tag" style="background:#fef3c7;color:#92400e;">+ DPD FR à confirmer scope</span>
    </div>
    """,
    4, N, DECK
))

# ============ SECTION 2 — Méthode email-making (slides 5-7) ============

# 5 Section
S.append(section_slide(2, "Méthode email-making", "La grille de fabrication d'un email Geopost", 5, N))

# 6 Anatomie d'un email
S.append(content_slide(
    "Slide 06 · Anatomie d'un email Geopost",
    "8 zones, 1 grille, 0 surprise",
    """
    <div class="layout-2col">
      <div>
        <ul>
          <li><strong>1. Préheader</strong> (≤110 car.) — teaser, jamais doublon</li>
          <li><strong>2. Header</strong> — logo BU + nav optionnelle</li>
          <li><strong>3. Héro</strong> — H1 texte + visuel décoratif <code>alt=""</code></li>
          <li><strong>4. Sub-héro</strong> — 1 phrase bénéfice + temps requis</li>
          <li><strong>5. CTA primaire</strong> — bulletproof ≥44px tactile</li>
          <li><strong>6. Body modulaire</strong> — 1 à 3 blocs réutilisables max</li>
          <li><strong>7. CTA secondaire</strong> — optionnel, lien texte</li>
          <li><strong>8. Footer légal</strong> — adresse + désinscription + RGPD par pays</li>
        </ul>
      </div>
      <div style="background:#fafafa; border:1px solid var(--border); border-radius:8px; padding:16px;">
        <div style="background:#f1f5f9; padding:6px; margin-bottom:6px; font-size:11px; color:#475569; text-align:center;">1 · Préheader</div>
        <div style="background:#fff; padding:14px; margin-bottom:6px; border:1px solid var(--border); text-align:center; font-size:13px;">2 · Header / Logo</div>
        <div style="background:#DC0032; color:#fff; padding:24px; margin-bottom:6px; text-align:center; font-weight:700;">3 · Héro H1 TEXTE<br><span style="font-size:11px; opacity:0.8; font-weight:400;">+ visuel décoratif</span></div>
        <div style="background:#fff; padding:10px; margin-bottom:6px; border:1px solid var(--border); text-align:center; font-size:13px;">4 · Sub-héro 1 phrase</div>
        <div style="background:#1a1a1a; color:#fff; padding:14px; margin-bottom:6px; text-align:center; font-size:13px; font-weight:700; border-radius:4px;">5 · CTA primaire</div>
        <div style="background:#fff; padding:14px; margin-bottom:6px; border:1px solid var(--border); text-align:center; font-size:13px;">6 · Body modulaire</div>
        <div style="background:#2e2e2f; color:#fff; padding:10px; text-align:center; font-size:11px;">8 · Footer légal</div>
      </div>
    </div>
    """,
    6, N, DECK
))

# 7 Règles d'or
S.append(content_slide(
    "Slide 07 · Règles d'or non négociables",
    "Ce qu'on ne fait jamais, ce qu'on fait toujours",
    """
    <div class="layout-2col">
      <div>
        <h3 style="color:#c00021;">❌ Jamais</h3>
        <ul>
          <li>Mettre le H1 dans une image</li>
          <li>Largeur fixe sans <code>@media</code></li>
          <li>Bouton CTA sans VML/bulletproof</li>
          <li>Tables sans <code>role="presentation"</code></li>
          <li><code>&lt;div&gt;</code> en structure principale</li>
          <li>Padding sur <code>&lt;table&gt;</code> (Outlook l'ignore)</li>
          <li>Plus de 3 tailles de typo par email</li>
          <li>CTA en MAJUSCULES (TTS variable)</li>
          <li>Préheader = doublon du H1</li>
        </ul>
      </div>
      <div>
        <h3 style="color:#16a34a;">✓ Toujours</h3>
        <ul>
          <li><code>&lt;head&gt;</code> standard XHTML email complet</li>
          <li><code>meta viewport</code> + <code>color-scheme</code></li>
          <li>Pack mso : <code>lspace</code>, <code>rspace</code>, <code>line-height-rule</code></li>
          <li><code>role="presentation"</code> sur tables layout</li>
          <li>Fallback Arial dans toute stack typo</li>
          <li>Espacements multiples de 4 ou 8</li>
          <li>1 seul CTA primaire, ≤4 mots, casse normale</li>
          <li>Preheader teaser unique (durée, bénéfice)</li>
          <li>Mentions légales pays-spécifiques complètes</li>
        </ul>
      </div>
    </div>
    """,
    7, N, DECK
))

# ============ SECTION 3 — Architecture parcours (slides 8-11) ============

# 8 Section
S.append(section_slide(3, "Architecture parcours", "Customer journey CRM Geopost", 8, N))

# 9 Vision parcours
S.append(content_slide(
    "Slide 09 · Vue d'ensemble parcours",
    "5 moments de vie destinataire × 5 BUs",
    """
    <div class="flow">
      <div class="step"><div class="num">1</div><h4>Acquisition</h4><p>Welcome onboarding<br>+ promote app</p></div>
      <div class="step"><div class="num">2</div><h4>Activation</h4><p>Première utilisation<br>tracking colis</p></div>
      <div class="step"><div class="num">3</div><h4>Engagement</h4><p>Services contextuels<br>out-of-home, options</p></div>
      <div class="step"><div class="num">4</div><h4>Rétention</h4><p>Boost sales<br>réactivation 30j+</p></div>
      <div class="step"><div class="num">5</div><h4>Advocacy</h4><p>Enquête satisfaction<br>parrainage</p></div>
    </div>
    <h3 style="margin-top:24px;">Moments saisonniers superposés</h3>
    <div style="display:flex; gap:12px; margin-top:8px;">
      <span class="tag" style="background:#fee2e2;color:#c00021;">🎄 Peak Noël (nov-déc)</span>
      <span class="tag" style="background:#fef3c7;color:#92400e;">Black Friday (nov)</span>
      <span class="tag" style="background:#fce7f3;color:#be185d;">💝 Saint-Valentin (fév)</span>
      <span class="tag" style="background:#dbeafe;color:#1e40af;">Singular B2B (continu)</span>
    </div>
    <p class="muted" style="margin-top:20px;">Chaque parcours est <strong>déclinable</strong> sur les 5 BUs avec mêmes blocs, tokens BU différents (couleur, logo, langue, devise, mention légale).</p>
    """,
    9, N, DECK
))

# 10 Triggers
S.append(content_slide(
    "Slide 10 · Triggers & règles de déclenchement",
    "Quand chaque email part de imagino",
    """
    <table>
      <thead><tr><th>Template</th><th>Trigger</th><th>Délai</th><th>Fréquence cap</th><th>KPI primaire</th></tr></thead>
      <tbody>
        <tr><td><strong>Welcome</strong></td><td>Création compte CDP</td><td>Immédiat</td><td>1 / compte</td><td>Activation J+7</td></tr>
        <tr><td><strong>Promote app</strong></td><td>Compte créé + pas d'app</td><td>J+7</td><td>1 / compte / 90j</td><td>Install / open</td></tr>
        <tr><td><strong>Boost sales</strong></td><td>30j sans envoi colis</td><td>J+30 inactivité</td><td>Max 3 / an</td><td>Réactivation J+14</td></tr>
        <tr><td><strong>Peak commercial</strong></td><td>Date fenêtre marketing</td><td>J-7 avant pic</td><td>Max 2 / fenêtre</td><td>Click-to-open</td></tr>
        <tr><td><strong>Services</strong></td><td>Sortie offre / change life event</td><td>J+1</td><td>1 / offre</td><td>Awareness + click</td></tr>
        <tr><td><strong>Singular</strong></td><td>Engagement compte B2B SME</td><td>Variable</td><td>Lifecycle</td><td>MRR / revenu</td></tr>
      </tbody>
    </table>
    <p class="muted" style="margin-top:16px;">Tous les triggers sont câblés dans imagino (CDP). Le contenu est <em>rendu côté serveur</em> avec tokens BU + tokens destinataire.</p>
    """,
    10, N, DECK
))

# 11 KPI matrix
S.append(content_slide(
    "Slide 11 · KPIs par parcours",
    "Ce qu'on mesure, ce qu'on optimise",
    """
    <div class="layout-3col">
      <div class="card">
        <h3>Délivrabilité</h3>
        <p><strong>Cible :</strong> ≥97% inbox<br><strong>Diag :</strong> bounce, spam, soft bounce</p>
      </div>
      <div class="card">
        <h3>Ouverture</h3>
        <p><strong>Cible :</strong> 25-35% open<br><strong>Diag :</strong> objet, preheader, sender name</p>
      </div>
      <div class="card">
        <h3>Engagement</h3>
        <p><strong>Cible :</strong> 4-8% CTR<br><strong>Diag :</strong> H1, CTA, hiérarchie</p>
      </div>
      <div class="card">
        <h3>Conversion</h3>
        <p><strong>Cible :</strong> dépend trigger<br><strong>Diag :</strong> CTA, landing align</p>
      </div>
      <div class="card">
        <h3>Désabonnement</h3>
        <p><strong>Cible :</strong> &lt;0.2% / envoi<br><strong>Diag :</strong> fréquence, pertinence</p>
      </div>
      <div class="card">
        <h3>Rendu cross-client</h3>
        <p><strong>Cible :</strong> 0 régression<br><strong>Outil :</strong> Litmus / Email on Acid</p>
      </div>
    </div>
    <p class="muted" style="margin-top:16px;">Tous chiffres cibles à confirmer Geopost. Benchmark secteur logistique/services 2025.</p>
    """,
    11, N, DECK
))

# ============ SECTION 4 — Les 6 templates (slides 12-30) ============

# 12 Section
S.append(section_slide(4, "Les 6 templates", "Anatomie, copy framework, KPIs par template", 12, N))

# Template Welcome (slides 13-16)
def template_intro(name, mission, when_to_send, audience, kpi, page):
    return content_slide(
        f"Slide {page:02d} · Template {name}",
        f"Vision — {name}",
        f"""
        <div class="layout-2col">
          <div>
            <h3>Mission</h3>
            <p>{mission}</p>
            <h3 style="margin-top:18px;">Quand envoyer</h3>
            <p>{when_to_send}</p>
          </div>
          <div>
            <h3>Audience</h3>
            <p>{audience}</p>
            <h3 style="margin-top:18px;">KPI primaire</h3>
            <p><strong>{kpi}</strong></p>
          </div>
        </div>
        """,
        page, N, DECK
    )

def template_seq(name, seq_html, page):
    return content_slide(
        f"Slide {page:02d} · Template {name}",
        f"Séquence — {name}",
        f"""
        <div class="flow">
        {seq_html}
        </div>
        """,
        page, N, DECK
    )

def template_copy(name, copy_html, page):
    return content_slide(
        f"Slide {page:02d} · Template {name}",
        f"Copy framework — {name}",
        copy_html,
        page, N, DECK
    )

# 13-16 Welcome
S.append(template_intro(
    "Welcome",
    "Onboarder le destinataire après création de compte. <strong>Confirmer la promesse, donner les 3 actions clés à faire dans les 7 prochains jours</strong>, créer le réflexe d'usage.",
    "Trigger immédiat à la création du compte CDP imagino. 1 envoi unique, jamais ré-envoyé.",
    "Tout nouveau compte (B2C + SME B2B). Segmentation BU par localisation + langue.",
    "Taux d'activation J+7 (≥1 colis envoyé OU app installée)",
    13
))

S.append(template_seq(
    "Welcome",
    """
    <div class="step"><div class="num">1</div><h4>Email Welcome (J0)</h4><p>Confirme compte + 3 actions</p></div>
    <div class="step"><div class="num">2</div><h4>Reminder soft (J+3)</h4><p>Si aucune action — push 1 action prioritaire</p></div>
    <div class="step"><div class="num">3</div><h4>Push app (J+7)</h4><p>Voir template <strong>Promote app</strong></p></div>
    <div class="step"><div class="num">4</div><h4>Sortie séquence</h4><p>Sinon → parcours engagement standard</p></div>
    """,
    14
))

S.append(template_copy(
    "Welcome",
    """
    <div class="layout-2col">
      <div>
        <h3>Objet (3 variantes A/B/C)</h3>
        <ul>
          <li>« Bienvenue chez {BU}, voici vos 3 prochaines étapes »</li>
          <li>« Votre compte {BU} est prêt — 2 minutes pour démarrer »</li>
          <li>« {Prénom}, bienvenue. On commence par où ? »</li>
        </ul>
        <h3 style="margin-top:14px;">Preheader (≤110)</h3>
        <p>« Activez votre compte en 3 étapes simples. Comptez 2 minutes maximum. »</p>
      </div>
      <div>
        <h3>H1 (texte HTML, jamais image)</h3>
        <p><strong>« Bienvenue chez {BU}. »</strong></p>
        <h3 style="margin-top:14px;">Sub-héro</h3>
        <p>« 3 actions pour démarrer. <strong>2 minutes</strong> chrono. »</p>
        <h3 style="margin-top:14px;">CTA primaire</h3>
        <p>« <strong>Activer mon compte</strong> » (1 seul, ≥44px tactile)</p>
        <h3 style="margin-top:14px;">Body</h3>
        <p>3 cards verticales : ① Confirmer adresse · ② Télécharger l'app · ③ Envoyer un premier colis. Chacune 1 phrase max + lien.</p>
      </div>
    </div>
    """,
    15
))

S.append(content_slide(
    "Slide 16 · Template Welcome",
    "Variations BU & KPIs cibles",
    """
    <div class="layout-2col">
      <div>
        <h3>Tokens BU à substituer</h3>
        <table>
          <thead><tr><th>Token</th><th>Exemple BRT</th><th>Exemple DPD CH</th></tr></thead>
          <tbody>
            <tr><td><code>{BU}</code></td><td>BRT</td><td>DPD Suisse</td></tr>
            <tr><td><code>{COLOR_PRIMARY}</code></td><td>#E32119</td><td>#DC0032</td></tr>
            <tr><td><code>{LANGUE}</code></td><td>it-IT</td><td>fr-CH</td></tr>
            <tr><td><code>{DEVISE}</code></td><td>EUR</td><td>CHF</td></tr>
            <tr><td><code>{LEGAL_BU}</code></td><td>Adresse BRT IT + RGPD IT</td><td>Adresse DPD CH + RGPD CH/FADP</td></tr>
          </tbody>
        </table>
      </div>
      <div>
        <h3>KPIs cibles Welcome</h3>
        <div class="kpi" style="grid-template-columns: 1fr 1fr;">
          <div class="item"><div class="v">≥35%</div><div class="l">Open rate</div></div>
          <div class="item"><div class="v">≥12%</div><div class="l">CTR</div></div>
          <div class="item"><div class="v">≥40%</div><div class="l">Activation J+7</div></div>
          <div class="item"><div class="v">&lt;0.1%</div><div class="l">Désabonnement</div></div>
        </div>
        <p class="muted" style="margin-top:8px;">Benchmarks logistique 2025. À calibrer après 30j de prod.</p>
      </div>
    </div>
    """,
    16, N, DECK
))

# 17-19 Promote app
S.append(template_intro(
    "Promote app",
    "Convertir l'inscription web en <strong>install mobile</strong>. Vendre les 3 avantages app : tracking temps réel, notifications push, gestion livraison à domicile.",
    "J+7 après création de compte si app non installée. 1 relance max à J+21 si non-install.",
    "Comptes sans installation app détectée (lien CDP × Firebase / AppsFlyer).",
    "Install rate + first open dans les 48h post-clic",
    17
))

S.append(template_copy(
    "Promote app",
    """
    <div class="layout-2col">
      <div>
        <h3>Objet</h3>
        <ul>
          <li>« Suivez vos colis en temps réel. L'app {BU}. »</li>
          <li>« {Prénom}, ne ratez plus jamais une livraison »</li>
        </ul>
        <h3 style="margin-top:14px;">Preheader</h3>
        <p>« Notifications, tracking, modifications de dernière minute — tout depuis votre mobile. »</p>
      </div>
      <div>
        <h3>H1</h3>
        <p><strong>« Vos colis, dans votre poche. »</strong></p>
        <h3 style="margin-top:14px;">3 bénéfices (cards)</h3>
        <ul>
          <li>📍 Tracking temps réel</li>
          <li>🔔 Notifications push</li>
          <li>⚙️ Modifier livraison en 1 tap</li>
        </ul>
        <h3 style="margin-top:14px;">CTA</h3>
        <p>2 boutons : « <strong>App Store</strong> » + « <strong>Google Play</strong> » (deep links).</p>
      </div>
    </div>
    """,
    18
))

S.append(content_slide(
    "Slide 19 · Template Promote app",
    "Particularités techniques & déclinaison BU",
    """
    <div class="layout-2col">
      <div>
        <h3>Particularités HTML</h3>
        <ul>
          <li><strong>Deep links</strong> par OS : iOS Universal Link + Android App Link</li>
          <li><strong>UTM standardisés</strong> : <code>utm_source=email&amp;utm_medium=trigger&amp;utm_campaign=promoteapp&amp;utm_content={BU}</code></li>
          <li><strong>QR code de secours</strong> (desktop) — image décorative + alt explicite</li>
          <li><strong>Fallback Outlook</strong> : badges App/Play en images optimisées + lien texte</li>
        </ul>
      </div>
      <div>
        <h3>Déclinaison BU</h3>
        <ul>
          <li><strong>BRT</strong> — app BRT MyDelivery (IT)</li>
          <li><strong>DPD CH</strong> — app DPD Switzerland</li>
          <li><strong>DPD CZ / SK</strong> — app DPD Online</li>
          <li><strong>Geopost corp</strong> — pas d'app utilisateur final, non applicable</li>
        </ul>
        <p class="muted" style="margin-top:14px;">Le template <em>ne s'envoie pas</em> pour les BUs sans app — la modularité doit absorber l'exclusion via condition CDP.</p>
      </div>
    </div>
    """,
    19, N, DECK
))

# 20-22 Boost sales
S.append(template_intro(
    "Boost sales",
    "Réactiver un destinataire inactif depuis 30j. <strong>Rappeler la valeur</strong> du service + lever un frein perçu (prix, complexité) via <em>1 promo ou 1 simplification</em>.",
    "J+30 d'inactivité (pas d'envoi de colis). Max 3 envois / an / compte, 90j de gap minimum.",
    "Comptes inactifs 30-180j. Au-delà de 180j → parcours dédié re-engagement.",
    "Taux de réactivation J+14 (≥1 colis envoyé)",
    20
))

S.append(template_copy(
    "Boost sales",
    """
    <div class="layout-2col">
      <div>
        <h3>Objet (variant levier promo / utilité)</h3>
        <ul>
          <li>Levier <strong>prix</strong> : « -20% sur votre prochain envoi {BU} »</li>
          <li>Levier <strong>simplicité</strong> : « Envoyer un colis n'a jamais été aussi rapide »</li>
          <li>Levier <strong>nouveauté</strong> : « 3 nouveautés {BU} à découvrir »</li>
        </ul>
      </div>
      <div>
        <h3>Structure</h3>
        <ul>
          <li><strong>H1</strong> bénéfice tangible (« Économisez 20% »)</li>
          <li><strong>Sub-héro</strong> rappel ancienneté (« Cela fait un mois… »)</li>
          <li><strong>Bloc levier</strong> : promo OU 3 nouveautés OU tutoriel</li>
          <li><strong>CTA primaire</strong> orienté action (« Profiter de l'offre »)</li>
          <li><strong>CTA secondaire</strong> faible-engagement (« Voir les options »)</li>
        </ul>
      </div>
    </div>
    """,
    21
))

S.append(content_slide(
    "Slide 22 · Template Boost sales",
    "Personnalisation & règles d'arrêt",
    """
    <div class="layout-2col">
      <div>
        <h3>Variables de personnalisation</h3>
        <ul>
          <li><code>{Prénom}</code> dans objet (boost open +5-8%)</li>
          <li><code>{Dernier_envoi}</code> dans sub-héro (« cela fait 32 jours… »)</li>
          <li><code>{Préférence_destination}</code> si connue (« vers {Pays} »)</li>
          <li><code>{Code_promo}</code> + <code>{Date_expiration}</code> dans bloc levier</li>
        </ul>
      </div>
      <div>
        <h3>Règles d'arrêt</h3>
        <ul>
          <li>Si destinataire désabonne après envoi 1 ou 2 → stop</li>
          <li>Si pas d'open après 3 envois → freeze 6 mois</li>
          <li>Si conversion après 1 envoi → exit séquence boost</li>
          <li>Si peak commercial en cours → priorité peak, boost reporté</li>
        </ul>
      </div>
    </div>
    """,
    22, N, DECK
))

# 23-25 Peak commercial
S.append(template_intro(
    "Peak commercial",
    "Capitaliser sur les <strong>3 moments forts de l'année</strong> (Noël, Black Friday, Saint-Valentin). Vendre la <em>tranquillité</em> : « Vos cadeaux livrés à temps, sans stress. »",
    "Fenêtre marketing fixe annuelle : Noël (mi-nov → 22 déc), BF (semaine BF), Saint-Valentin (1-13 fév).",
    "Base active 12 mois. Exclure inactifs &gt;180j. Possibilité segmentation B2C vs B2B SME.",
    "Volume d'expéditions sur la fenêtre vs N-1",
    23
))

S.append(template_copy(
    "Peak commercial",
    """
    <div class="layout-2col">
      <div>
        <h3>Architecture campagne Noël (exemple)</h3>
        <ul>
          <li><strong>J-21</strong> Email 1 — anticipation (« Pensez à vos colis Noël »)</li>
          <li><strong>J-14</strong> Email 2 — last-call délais (« Plus que X jours »)</li>
          <li><strong>J-7</strong> Email 3 — urgence + alternatives (« Express disponible »)</li>
        </ul>
        <h3 style="margin-top:14px;">Tonalité</h3>
        <p>Bienveillante, rassurante. Pas de FOMO agressif. Geopost garantit la livraison, pas la peur.</p>
      </div>
      <div>
        <h3>H1 variantes</h3>
        <ul>
          <li>« Vos cadeaux à temps. C'est promis. »</li>
          <li>« Encore 21 jours. Largement le temps de bien faire. »</li>
        </ul>
        <h3 style="margin-top:14px;">CTA primaire</h3>
        <p>« <strong>Voir les délais garantis</strong> » → landing page délais par destination</p>
        <h3 style="margin-top:14px;">Visuel héro</h3>
        <p>Décoratif uniquement (paquet emballé, mains, neige). Jamais porteur du H1.</p>
      </div>
    </div>
    """,
    24
))

S.append(content_slide(
    "Slide 25 · Template Peak commercial",
    "Adaptation par BU & timing local",
    """
    <table>
      <thead><tr><th>BU</th><th>Noël</th><th>Black Friday</th><th>Saint-Valentin</th><th>Particularités locales</th></tr></thead>
      <tbody>
        <tr><td><strong>Geopost corp</strong></td><td>✓ B2B</td><td>—</td><td>—</td><td>Communication corporate, jamais retail</td></tr>
        <tr><td><strong>BRT IT</strong></td><td>✓</td><td>✓</td><td>✓</td><td>Befana (6 jan) à ajouter — campagne locale IT</td></tr>
        <tr><td><strong>DPD CH</strong></td><td>✓</td><td>✓</td><td>✓</td><td>Fête nationale 1er août — moment alternatif</td></tr>
        <tr><td><strong>DPD CZ</strong></td><td>✓</td><td>✓</td><td>✓</td><td>Mikuláš (5 déc) — pré-Noël CZ spécifique</td></tr>
        <tr><td><strong>DPD SK</strong></td><td>✓</td><td>✓</td><td>✓</td><td>Mikuláš (6 déc) — pré-Noël SK</td></tr>
      </tbody>
    </table>
    <p class="muted" style="margin-top:14px;">⚠️ <strong>Coordination calendrier</strong> : la modularité doit gérer plusieurs fenêtres simultanées par BU. Conflit BF + Noël en novembre → règle de priorité dans imagino.</p>
    """,
    25, N, DECK
))

# 26-28 Services
S.append(template_intro(
    "Services",
    "Annoncer une <strong>nouvelle offre ou un changement d'usage</strong> (point relais, consigne, livraison hors domicile). Pédagogie + bénéfice utilisateur, pas argumentaire commercial.",
    "Au lancement d'une offre OU sur change life event (déménagement, premier colis hors zone). One-shot ou trigger ponctuel.",
    "Base active OU sous-segment géo selon disponibilité du service.",
    "Awareness (open) + adoption (1ère utilisation du service)",
    26
))

S.append(template_copy(
    "Services",
    """
    <div class="layout-2col">
      <div>
        <h3>Exemple : Out-of-home (point relais)</h3>
        <p><strong>Objet :</strong> « Recevez vos colis quand <em>vous</em> voulez, où <em>vous</em> voulez »</p>
        <p><strong>Preheader :</strong> « 5 000 points relais {BU}. Le plus proche est peut-être à 3 minutes. »</p>
        <p><strong>H1 :</strong> « Le point relais qui vous arrange. »</p>
        <p><strong>Sub-héro :</strong> « Activez l'option en 1 clic dans votre prochain envoi. »</p>
      </div>
      <div>
        <h3>Body modulaire</h3>
        <ul>
          <li>1 bloc <em>« Comment ça marche »</em> en 3 étapes (icônes décoratives + texte HTML)</li>
          <li>1 bloc <em>« Cas d'usage »</em> (« vous voyagez », « vous travaillez tard »)</li>
          <li>1 bloc CTA + lien <em>« Trouver mon point relais »</em></li>
        </ul>
        <h3 style="margin-top:14px;">Ton</h3>
        <p>Pédagogique, jamais survendeur. On explique, on n'argumente pas.</p>
      </div>
    </div>
    """,
    27
))

S.append(content_slide(
    "Slide 28 · Template Services",
    "Réutilisable pour toute nouvelle offre",
    """
    <div class="layout-2col">
      <div>
        <h3>Cas d'usage du template Services</h3>
        <ul>
          <li><strong>Point relais / consigne</strong> — out-of-home delivery</li>
          <li><strong>Livraison sur RDV</strong> — créneau choisi</li>
          <li><strong>Retour de colis</strong> — process & options</li>
          <li><strong>Assurance colis</strong> — protection valeur</li>
          <li><strong>Suivi avancé</strong> — notifications enrichies</li>
          <li><strong>Tout nouveau service</strong> — slots futurs</li>
        </ul>
      </div>
      <div>
        <h3>Architecture pour reuse</h3>
        <ul>
          <li>Bloc « héro » paramétrable : <code>{SERVICE_NAME}</code>, <code>{H1}</code>, <code>{IMAGE_ALT}</code></li>
          <li>Bloc « comment ça marche » : 3 slots paramétrables <code>{ETAPE_N_TITRE}</code> + <code>{ETAPE_N_TEXTE}</code></li>
          <li>Bloc « cas d'usage » : tableau 2 colonnes paramétrable</li>
          <li>Bloc CTA : <code>{CTA_LABEL}</code> + <code>{CTA_URL}</code></li>
        </ul>
        <p class="muted">→ template Services = blueprint réutilisable, jamais re-développé pour chaque offre.</p>
      </div>
    </div>
    """,
    28, N, DECK
))

# 29-30 Singular
S.append(template_intro(
    "Singular",
    "Email B2B pour la plateforme Singular (boost des ventes SME). <strong>Ton plus pro</strong>, plus orienté ROI, données chiffrées. Pas de tutoiement, pas de promo grand public.",
    "Lifecycle B2B : onboarding compte SME, milestones d'usage, opportunités revenue. Cadence à définir avec Sales.",
    "Comptes Singular SME. Segmentation par taille (TPE/PME), secteur, ARR.",
    "MRR / revenu généré + adoption features avancées",
    29
))

S.append(content_slide(
    "Slide 30 · Template Singular",
    "Différenciation B2B vs B2C",
    """
    <div class="layout-2col">
      <div>
        <h3>Ce qui change vs templates B2C</h3>
        <ul>
          <li><strong>Tonalité</strong> : vouvoiement, sobriété, pas d'emoji</li>
          <li><strong>Sender name</strong> : « {Nom Account Manager} — Geopost Singular »</li>
          <li><strong>Visuel héro</strong> : data / dashboards / outils, jamais lifestyle</li>
          <li><strong>Body</strong> : metrics, ROI, témoignages chiffrés</li>
          <li><strong>CTA</strong> : « Demander une démo », « Voir le rapport », jamais « Profiter »</li>
          <li><strong>Footer</strong> : signature manuelle Account Manager + téléphone direct</li>
        </ul>
      </div>
      <div>
        <h3>KPIs Singular</h3>
        <div class="kpi" style="grid-template-columns: 1fr 1fr;">
          <div class="item"><div class="v">≥45%</div><div class="l">Open rate B2B</div></div>
          <div class="item"><div class="v">≥18%</div><div class="l">CTR</div></div>
          <div class="item"><div class="v">≥8%</div><div class="l">Reply / meeting</div></div>
          <div class="item"><div class="v">&lt;0.05%</div><div class="l">Désabo (compte stratégique)</div></div>
        </div>
        <p class="muted">B2B : engagement individuel &gt; volume.</p>
      </div>
    </div>
    """,
    30, N, DECK
))

# ============ SECTION 5 — Déclinaison BU (slides 31-33) ============

S.append(section_slide(5, "Déclinaison multi-BU", "Les 5 marques avec un seul moteur", 31, N))

S.append(content_slide(
    "Slide 32 · Tokens BU — le moteur de la multi-brand",
    "Un seul HTML, 5 brand-faces",
    """
    <table>
      <thead><tr><th>Token</th><th>Geopost corp</th><th>BRT</th><th>DPD CH</th><th>DPD CZ</th><th>DPD SK</th></tr></thead>
      <tbody>
        <tr><td><code>{COLOR_PRIMARY}</code></td><td>#DC0032</td><td>#E32119 <span class="muted">[à valider]</span></td><td>#DC0032 <span class="muted">[à valider]</span></td><td>#DC0032 <span class="muted">[à valider]</span></td><td>#DC0032 <span class="muted">[à valider]</span></td></tr>
        <tr><td><code>{COLOR_SECONDARY}</code></td><td>#2e2e2f</td><td>#1a1a1a</td><td>#2e2e2f</td><td>#2e2e2f</td><td>#2e2e2f</td></tr>
        <tr><td><code>{LOGO_URL}</code></td><td>logo-geopost.svg</td><td>logo-brt.svg</td><td>logo-dpd-ch.svg</td><td>logo-dpd-cz.svg</td><td>logo-dpd-sk.svg</td></tr>
        <tr><td><code>{LOGO_WIDTH}</code></td><td>140</td><td>140</td><td>140</td><td>140</td><td>140</td></tr>
        <tr><td><code>{LANGUE}</code></td><td>en-EU</td><td>it-IT</td><td>fr-CH / de-CH</td><td>cs-CZ</td><td>sk-SK</td></tr>
        <tr><td><code>{DEVISE}</code></td><td>—</td><td>EUR</td><td>CHF</td><td>CZK</td><td>EUR</td></tr>
        <tr><td><code>{LEGAL_ADDR}</code></td><td>Geopost HQ</td><td>BRT Milan</td><td>DPD CH Buchs</td><td>DPD CZ Praha</td><td>DPD SK Bratislava</td></tr>
        <tr><td><code>{LEGAL_RGPD}</code></td><td>EU general</td><td>RGPD + privacy IT</td><td>FADP (CH)</td><td>GDPR + CZ act</td><td>GDPR + SK act</td></tr>
        <tr><td><code>{UNSUB_URL}</code></td><td>geopost.com/...</td><td>brt.it/unsub</td><td>dpd.ch/unsub</td><td>dpd.cz/unsub</td><td>dpd.sk/unsub</td></tr>
      </tbody>
    </table>
    <p class="muted" style="margin-top:8px;">Les valeurs <code>[à valider]</code> doivent être confirmées vs charte officielle de chaque BU avant production.</p>
    """,
    32, N, DECK
))

S.append(content_slide(
    "Slide 33 · Règles de gouvernance multi-BU",
    "Qui décide quoi, qui peut modifier quoi",
    """
    <div class="layout-2col">
      <div>
        <h3>Couche corporate (Geopost)</h3>
        <ul>
          <li>Architecture template + librairie blocs</li>
          <li>Règles techniques (Outlook, a11y, mso)</li>
          <li>Structure parcours CRM</li>
          <li>KPIs cadre + benchmarks</li>
          <li><strong>Non modifiable par BU</strong></li>
        </ul>
      </div>
      <div>
        <h3>Couche BU</h3>
        <ul>
          <li>Tokens couleur, logo, langue, devise</li>
          <li>Mentions légales pays</li>
          <li>Calendrier campagnes locales (Mikuláš, Befana…)</li>
          <li>Copy / wording dans la langue locale</li>
          <li>Sender name + adresse expéditeur</li>
          <li><strong>Modifiable par BU dans imagino</strong></li>
        </ul>
      </div>
    </div>
    <h3 style="margin-top:20px;">Process modification template</h3>
    <p>Toute évolution de la <em>structure</em> ou des <em>règles techniques</em> → demande au Lead CRM Geopost → audit impact 5 BUs → release versionnée. <strong>Aucune BU ne modifie le HTML core.</strong></p>
    """,
    33, N, DECK
))

# ============ SECTION 6 — Modularité & templatisation (slides 34-36) ============

S.append(section_slide(6, "Templatisation", "L'architecture modulaire de production", 34, N))

S.append(content_slide(
    "Slide 35 · Architecture modulaire",
    "Core + Blocs + Tokens = scalabilité",
    """
    <div class="layout-2col">
      <div>
        <h3>3 couches</h3>
        <ul>
          <li><strong>1. Core templates (6)</strong> — squelette HTML par type (welcome, app, boost, peak, services, singular)</li>
          <li><strong>2. Blocs réutilisables (~30)</strong> — header, héro, sub-héro, CTA, body 1-col, body 2-col, body 3-cards, image-text, banner promo, footer, etc.</li>
          <li><strong>3. Tokens (~20 / BU)</strong> — couleur, logo, langue, légal, etc.</li>
        </ul>
      </div>
      <div style="background:#fafafa; border:1px solid var(--border); border-radius:8px; padding:16px;">
        <div style="background:#1a1a1a; color:#fff; padding:10px; margin-bottom:6px; font-size:12px; text-align:center; border-radius:4px;">📐 Core template (1 / parcours)</div>
        <div style="text-align:center; color:#999; font-size:14px;">↓ assemble</div>
        <div style="background:#DC0032; color:#fff; padding:10px; margin: 6px 0; font-size:12px; text-align:center; border-radius:4px;">🧱 Blocs réutilisables (~30)</div>
        <div style="text-align:center; color:#999; font-size:14px;">↓ injecte</div>
        <div style="background:#f1f5f9; color:#475569; padding:10px; margin-top:6px; font-size:12px; text-align:center; border-radius:4px; border:1px solid #cbd5e1;">🏷️ Tokens BU (~20 / marque)</div>
        <p class="muted" style="text-align:center; margin-top:10px; font-size:11px;">= 30 emails distincts en production sans 30 codebases</p>
      </div>
    </div>
    """,
    35, N, DECK
))

S.append(content_slide(
    "Slide 36 · Librairie de blocs cibles (~30)",
    "Le catalogue à construire",
    """
    <div class="layout-3col">
      <div class="card">
        <h3>Structure (5)</h3>
        <ul style="font-size:13px;">
          <li>Wrapper 640px + reset</li>
          <li>Header logo (1 ligne)</li>
          <li>Header logo + nav (option)</li>
          <li>Footer légal complet</li>
          <li>Spacer / divider</li>
        </ul>
      </div>
      <div class="card">
        <h3>Héro & titres (4)</h3>
        <ul style="font-size:13px;">
          <li>Héro texte + visuel</li>
          <li>Héro texte plein</li>
          <li>Bannière promo</li>
          <li>Section heading</li>
        </ul>
      </div>
      <div class="card">
        <h3>Body (7)</h3>
        <ul style="font-size:13px;">
          <li>Texte 1 colonne</li>
          <li>Texte 2 colonnes</li>
          <li>3 cards horizontales</li>
          <li>3 étapes verticales</li>
          <li>Image + texte droite</li>
          <li>Image + texte gauche</li>
          <li>Quote / témoignage</li>
        </ul>
      </div>
      <div class="card">
        <h3>CTA (4)</h3>
        <ul style="font-size:13px;">
          <li>CTA bulletproof primary</li>
          <li>CTA bulletproof secondary</li>
          <li>2 CTA juxtaposés (App+Play)</li>
          <li>Lien texte simple</li>
        </ul>
      </div>
      <div class="card">
        <h3>Spéciaux (6)</h3>
        <ul style="font-size:13px;">
          <li>Tracking colis (data dyn.)</li>
          <li>Point relais carte</li>
          <li>Code promo bloc</li>
          <li>Compteur Noël J-X</li>
          <li>Témoignage Singular B2B</li>
          <li>QR code app store</li>
        </ul>
      </div>
      <div class="card">
        <h3>Conformité (4)</h3>
        <ul style="font-size:13px;">
          <li>Mention RGPD FR/IT/CH/CZ/SK</li>
          <li>Désabonnement 1-clic</li>
          <li>Adresse postale BU</li>
          <li>Preheader masqué</li>
        </ul>
      </div>
    </div>
    """,
    36, N, DECK
))

# ============ SECTION 7 — Roadmap industrialisation (slides 37-39) ============

S.append(section_slide(7, "Roadmap industrialisation", "Comment on déploie sur 6 mois", 37, N))

S.append(content_slide(
    "Slide 38 · Roadmap 6 mois",
    "Du kick-off à la prod 5 BUs",
    """
    <table>
      <thead><tr><th>Phase</th><th>Période</th><th>Livrables</th><th>BUs concernées</th></tr></thead>
      <tbody>
        <tr><td><strong>1. Fondations</strong></td><td>Juin 2026 (S25-S26)</td><td>Guidelines email + tokens + audit V2 inter-BU</td><td>Cross-BU</td></tr>
        <tr><td><strong>2. Pilot template</strong></td><td>Juillet 2026 (S27-S30)</td><td>Welcome end-to-end (design + HTML + tests Litmus) sur 1 BU pilote</td><td>BRT (pilote)</td></tr>
        <tr><td><strong>3. Réplication</strong></td><td>Août 2026 (S31-S34)</td><td>Welcome répliqué sur 4 autres BUs via tokens</td><td>+ DPD CH, CZ, SK, Geopost</td></tr>
        <tr><td><strong>4. Vague trigger</strong></td><td>Sept 2026 (S35-S38)</td><td>Promote app + Boost sales sur les 5 BUs</td><td>5 BUs</td></tr>
        <tr><td><strong>5. Vague one-shot</strong></td><td>Oct 2026 (S39-S42)</td><td>Peak commercial Noël + Services + Singular</td><td>5 BUs</td></tr>
        <tr><td><strong>6. Stabilisation</strong></td><td>Nov 2026 (S43-S46)</td><td>QA cross-BU + benchmarks 30j prod + retours équipes locales</td><td>5 BUs</td></tr>
        <tr><td><strong>7. Run &amp; iterate</strong></td><td>Déc 2026 +</td><td>Itérations data-driven + nouveaux services</td><td>5+ BUs</td></tr>
      </tbody>
    </table>
    <p class="muted" style="margin-top:8px;">⚠️ <strong>Vague 5 démarre AVANT Noël</strong> pour test campagne Peak en conditions réelles.</p>
    """,
    38, N, DECK
))

S.append(content_slide(
    "Slide 39 · Dépendances & risques",
    "Ce qui peut faire dérailler le planning",
    """
    <div class="layout-2col">
      <div>
        <h3>Dépendances bloquantes Geopost</h3>
        <ul>
          <li><strong>Brand guidelines par BU</strong> — palette, logo, ton — à fournir S25</li>
          <li><strong>3 autres emails POC</strong> — pour audit V2 inter-BU</li>
          <li><strong>Accès imagino sandbox</strong> par BU pour tests CDP</li>
          <li><strong>RACI éditorial</strong> par BU — qui valide le copy local ?</li>
          <li><strong>CDN imagino</strong> pour assets emails (images + fonts)</li>
        </ul>
      </div>
      <div>
        <h3>Risques majeurs identifiés</h3>
        <ul>
          <li><strong>R1</strong> · Palette non confirmée → blocage design</li>
          <li><strong>R2</strong> · Validation BU locale longue → retard prod</li>
          <li><strong>R3</strong> · Conflit calendrier Peak + Trigger en nov</li>
          <li><strong>R4</strong> · Régression Outlook sur nouveau client (versions futures)</li>
          <li><strong>R5</strong> · Désaccord copy local (legal + marketing BU)</li>
        </ul>
        <p class="muted">Mitigation : workflow Lead CRM + sous-agents permet audit/itération en heures plutôt qu'en jours (cf. deck 3).</p>
      </div>
    </div>
    """,
    39, N, DECK
))

# 40 Conclusion
S.append(content_slide(
    "Slide 40 · Synthèse Recos",
    "Ce qu'on livre, ce qu'on gagne",
    """
    <div class="layout-2col">
      <div>
        <h3>Livrables Phase 2</h3>
        <ul>
          <li>6 core templates HTML production-ready</li>
          <li>~30 blocs modulaires de librairie imagino</li>
          <li>~20 tokens BU par marque (5 BUs)</li>
          <li>Guidelines email Geopost v1 (formalisées)</li>
          <li>Audit cross-BU inter-marque</li>
          <li>Suite Litmus / EoA de tests automatisés</li>
        </ul>
      </div>
      <div>
        <h3>Gains attendus</h3>
        <div class="kpi" style="grid-template-columns: 1fr 1fr;">
          <div class="item"><div class="v">5×</div><div class="l">BUs servies par 1 codebase</div></div>
          <div class="item"><div class="v">-70%</div><div class="l">Temps de lancement campagne <span class="muted">[à valider]</span></div></div>
          <div class="item"><div class="v">+25%</div><div class="l">Click rate vs POC <span class="muted">[hypothèse]</span></div></div>
          <div class="item"><div class="v">0</div><div class="l">Régression Outlook tolérée</div></div>
        </div>
      </div>
    </div>
    <div style="margin-top: auto; padding-top: 16px; border-top: 2px solid var(--red); text-align:center;">
      <h3 style="color:var(--red); margin:0;">→ Voir Deck 3 — Synthèse workflow agence × agents Claude</h3>
    </div>
    """,
    40, N, DECK
))

build_deck("Recos CRM — 40 slides", S, f"{ROOT}/decks/DECK_2_RECOS.html")
print(f"OK Deck 2 ({len(S)} slides)")
