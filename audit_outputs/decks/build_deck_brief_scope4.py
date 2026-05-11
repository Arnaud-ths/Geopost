"""Deck scope brief §4 — recentré strict sur A. Audit & Reco / B. Templates / C. HTML Integration."""
import base64, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from _framework import cover, section_slide, content_slide, build_deck

ROOT = "/home/user/Geopost/audit_outputs"
DECK = "RÉPONSE BRIEF §4"
S = []

def img64(rel):
    with open(os.path.join(ROOT, rel), "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()

# 1 Cover
S.append(cover(
    "Réponse RFP · Geopost",
    "Templates Revamp Project",
    "Notre approche sur le scope §4 du brief",
    "11 mai 2026 · Geopost Lead CRM V1",
    1, 18
))

# 2 Compréhension du brief §4
S.append(content_slide(
    "Slide 02 · Compréhension du brief",
    "Scope §4 — 3 buckets, on adresse les 3",
    """
    <table>
      <thead><tr><th>§4</th><th>Bucket</th><th>Ce que demande le brief</th><th>Notre réponse</th></tr></thead>
      <tbody>
        <tr>
          <td><strong>A</strong></td>
          <td>Audit &amp; Recommendations <em>(optionnel)</em></td>
          <td>Audit graphique et HTML existant · Recos contenu éditorial UX/CRO · Best practices Outlook / dark mode / a11y</td>
          <td>Slides 03-05 — POC DPD FR déjà audité, méthode reproductible</td>
        </tr>
        <tr>
          <td><strong>B</strong></td>
          <td>Template Creation</td>
          <td>Refonte de <strong>6 templates</strong> : 3 trigger (welcome, app, boost) + 3 one-shot (peak, services, singular) · Design aligné brand guidelines existantes</td>
          <td>Slides 06-13 — un slide par template, design framework</td>
        </tr>
        <tr>
          <td><strong>C</strong></td>
          <td>HTML Integration</td>
          <td>Intégration HTML robuste des templates · Focus Outlook + a11y + maintenabilité · Possibilité librairie modulaire</td>
          <td>Slides 14-17 — règles Outlook, a11y, modularité</td>
        </tr>
      </tbody>
    </table>
    <p class="muted" style="margin-top:14px;">→ Pas de tonalité ni positionnement modifiés (cf. brief §3 « conformité brand guidelines existantes »).</p>
    """,
    2, 18, DECK
))

# ============ SECTION A — Audit & Recommendations (3 slides) ============

# 3 — A.1 Audit graphique et HTML
S.append(content_slide(
    "Slide 03 · §4-A.1",
    "Audit graphique et HTML des emails existants",
    f"""
    <div class="layout-img-right">
      <div>
        <h3>Ce qu'on a déjà livré sur le POC</h3>
        <ul>
          <li><strong>1 email POC audité</strong> (DPD FR — enquête satisfaction)</li>
          <li>5 environnements simulés (desktop, mobile 375, dark mode, images bloquées, cas idéal)</li>
          <li><strong>36 écarts détectés</strong> · 5 captures annotées · scoring brief 1.3/5</li>
          <li>Plan d'action P0/P1/P2 et dispatch agents</li>
        </ul>
        <h3 style="margin-top:14px;">Itération V2 prête</h3>
        <p>Dès réception des 3 autres POC (BRT, DPD CH, + 1 BU), audit comparatif inter-BU livré sous 48h.</p>
        <p class="muted">Méthode reproductible : Chromium headless + Python — auditable, versionnable.</p>
      </div>
      <img src="{img64('annotated/A_as_is_desktop_annotated.png')}" alt="Audit POC DPD FR">
    </div>
    """,
    3, 18, DECK
))

# 4 — A.2 Recos contenu éditorial UX/CRO
S.append(content_slide(
    "Slide 04 · §4-A.2",
    "Recommandations contenu éditorial & UX / CRO",
    """
    <div class="layout-2col">
      <div>
        <h3>Cadre éditorial</h3>
        <ul>
          <li><strong>Objet</strong> ≤50 car., 3 variantes A/B systématiques</li>
          <li><strong>Preheader</strong> ≤110 car., teaser unique (jamais doublon du H1)</li>
          <li><strong>H1 en texte HTML</strong> — jamais dans une image</li>
          <li><strong>Body</strong> phrases ≤20 mots, bénéfices concrets, durée quantifiée</li>
          <li><strong>CTA</strong> 1 seul primaire, ≤4 mots, casse normale, verbe d'action</li>
        </ul>
      </div>
      <div>
        <h3>Recos CRO observées sur le POC</h3>
        <ul>
          <li>Compresser le body — POC actuel : 5 paragraphes pour 1 message</li>
          <li>Quantifier (« 2 minutes » &gt; « quelques minutes »)</li>
          <li>Différencier preheader / H1 / image héro (POC actuel : triplon)</li>
          <li>Mettre le CTA dans la fold sur mobile</li>
          <li>Sur Welcome / Boost : personnalisation <code>{Prénom}</code> dans objet</li>
        </ul>
      </div>
    </div>
    <p class="muted" style="margin-top:14px;">Brand voice et tonalité Geopost <strong>non modifiées</strong> — uniquement la mise en forme et la structure éditoriale.</p>
    """,
    4, 18, DECK
))

# 5 — A.3 Best practices environnements dégradés
S.append(content_slide(
    "Slide 05 · §4-A.3",
    "Best practices en environnements dégradés",
    f"""
    <div class="layout-2col">
      <div>
        <h3>Outlook (2007 → M365)</h3>
        <ul style="font-size:14px;">
          <li>Mise en page <strong>tables imbriquées</strong>, jamais <code>&lt;div&gt;</code></li>
          <li><code>role="presentation"</code> sur toutes les tables layout</li>
          <li>Pack mso : <code>lspace</code>, <code>rspace</code>, <code>line-height-rule:exactly</code>, conditionals</li>
          <li>CTA <strong>bulletproof VML</strong>, jamais border-radius CSS isolé</li>
          <li>Padding sur <code>&lt;td&gt;</code>, jamais sur <code>&lt;table&gt;</code></li>
        </ul>
        <h3 style="margin-top:14px;">Dark mode</h3>
        <ul style="font-size:14px;">
          <li><code>&lt;meta name="color-scheme" content="light dark"&gt;</code></li>
          <li><code>@media (prefers-color-scheme: dark)</code> avec variantes couleur</li>
          <li>Logos avec versions claire / sombre quand brand le permet</li>
        </ul>
      </div>
      <div>
        <h3>Accessibilité WCAG AA</h3>
        <ul style="font-size:14px;">
          <li>Contraste body ≥4.5:1, large texte ≥3:1</li>
          <li><code>alt</code> descriptif ≤80 car. sur images sens, <code>alt=""</code> sur décoratifs</li>
          <li><code>lang</code> attribut sur <code>&lt;html&gt;</code></li>
          <li>CTA labels explicites (« Découvrir l'offre » &gt; « Cliquez ici »)</li>
          <li>CTA hauteur tactile ≥44×44px</li>
          <li>Jamais d'info transmise par la couleur seule</li>
        </ul>
        <h3 style="margin-top:14px;">Images bloquées (Outlook par défaut)</h3>
        <ul style="font-size:14px;">
          <li>Message principal en texte HTML, jamais en image</li>
          <li>Alt explicites + structure intelligible sans images</li>
        </ul>
      </div>
    </div>
    """,
    5, 18, DECK
))

# ============ SECTION B — Template Creation (8 slides) ============

# 6 — B intro
S.append(content_slide(
    "Slide 06 · §4-B",
    "Template Creation — refonte des 6 templates",
    """
    <table>
      <thead><tr><th>#</th><th>Famille</th><th>Template</th><th>Mission éditoriale</th></tr></thead>
      <tbody>
        <tr><td>1</td><td rowspan="3"><strong>Trigger automatisés</strong></td><td>Welcome</td><td>Onboarder après création de compte — confirmer la promesse, 3 actions à faire</td></tr>
        <tr><td>2</td><td>Promote mobile app download</td><td>Convertir l'inscription web en install mobile — tracking + notifications + gestion</td></tr>
        <tr><td>3</td><td>Boost sales</td><td>Réactiver un destinataire inactif — rappeler la valeur, lever un frein</td></tr>
        <tr><td>4</td><td rowspan="3"><strong>One-shot</strong></td><td>Commercial peak (Noël / BF / Saint-Valentin)</td><td>Capitaliser sur les fenêtres marketing — vendre la tranquillité</td></tr>
        <tr><td>5</td><td>Services (out-of-home, etc.)</td><td>Annoncer une nouvelle offre — pédagogie, jamais argumentaire</td></tr>
        <tr><td>6</td><td>Singular (plateforme boost ventes SME)</td><td>B2B — ton pro, ROI chiffré, signature Account Manager</td></tr>
      </tbody>
    </table>
    <p class="muted" style="margin-top:14px;">Tous les templates respectent les 5 règles d'or du framework (slide 04) et sont alignés sur les brand guidelines existantes Geopost.</p>
    """,
    6, 18, DECK
))

# 7-12 — 6 templates (1 slide chacun)
def template_card(name, mission, when, audience, copy_examples, page):
    return content_slide(
        f"Slide {page:02d} · §4-B · Template {name}",
        name,
        f"""
        <div class="layout-2col">
          <div>
            <h3>Mission</h3>
            <p style="font-size:15px;">{mission}</p>
            <h3 style="margin-top:14px;">Quand envoyer</h3>
            <p style="font-size:15px;">{when}</p>
            <h3 style="margin-top:14px;">Audience</h3>
            <p style="font-size:15px;">{audience}</p>
          </div>
          <div>
            <h3>Exemples de copy (1 variante)</h3>
            {copy_examples}
          </div>
        </div>
        """,
        page, 18, DECK
    )

S.append(template_card(
    "Welcome",
    "Onboarder le destinataire après création de compte. Confirmer la promesse + donner les <strong>3 actions clés</strong> à faire dans la 1ère semaine.",
    "Trigger immédiat à la création du compte CDP imagino. Envoi unique.",
    "Tout nouveau compte (B2C + SME B2B).",
    """
    <p><strong>Objet :</strong> « Bienvenue chez Geopost, voici vos 3 prochaines étapes »</p>
    <p><strong>Preheader :</strong> « Activez votre compte en 3 étapes simples. 2 minutes. »</p>
    <p><strong>H1 :</strong> « Bienvenue chez Geopost. »</p>
    <p><strong>Body :</strong> 3 cards verticales — ① Confirmer adresse · ② Télécharger l'app · ③ Envoyer un premier colis</p>
    <p><strong>CTA :</strong> « Activer mon compte »</p>
    """,
    7
))

S.append(template_card(
    "Promote mobile app download",
    "Convertir l'inscription web en <strong>install mobile</strong>. Vendre les 3 avantages app : tracking, notifications push, modifications.",
    "J+7 après création si app non installée. 1 relance max à J+21.",
    "Comptes sans installation app détectée (CDP × Firebase / AppsFlyer).",
    """
    <p><strong>Objet :</strong> « Suivez vos colis en temps réel. L'app Geopost. »</p>
    <p><strong>Preheader :</strong> « Notifications, tracking, modifications — depuis votre mobile. »</p>
    <p><strong>H1 :</strong> « Vos colis, dans votre poche. »</p>
    <p><strong>Body :</strong> 3 bénéfices (cards) — 📍 Tracking · 🔔 Notifications · ⚙️ Modifier en 1 tap</p>
    <p><strong>CTA :</strong> 2 boutons — « App Store » + « Google Play » (deep links)</p>
    """,
    8
))

S.append(template_card(
    "Boost sales",
    "Réactiver un destinataire inactif depuis 30j. Rappeler la valeur + lever un frein perçu via <strong>1 promo OU 1 simplification</strong>.",
    "J+30 d'inactivité. Max 3 envois / an / compte. Stop si désabo après 1-2 envois.",
    "Comptes inactifs 30-180j. Au-delà : parcours dédié re-engagement.",
    """
    <p><strong>Objet :</strong> « -20% sur votre prochain envoi Geopost »</p>
    <p><strong>Preheader :</strong> « Cela fait un mois… on vous facilite le retour. »</p>
    <p><strong>H1 :</strong> « Économisez 20% sur votre prochain envoi. »</p>
    <p><strong>Body :</strong> Rappel ancienneté · Bloc levier (promo OU 3 nouveautés OU tutoriel)</p>
    <p><strong>CTA :</strong> « Profiter de l'offre » (+ CTA secondaire texte)</p>
    """,
    9
))

S.append(template_card(
    "Commercial peak",
    "Capitaliser sur Noël / Black Friday / Saint-Valentin. Vendre la <strong>tranquillité</strong> : « Vos cadeaux livrés à temps, sans stress. »",
    "Fenêtres fixes : Noël (mi-nov → 22 déc), BF (semaine BF), Saint-Valentin (1-13 fév).",
    "Base active 12 mois. Exclure inactifs &gt;180j.",
    """
    <p><strong>Objet :</strong> « Vos cadeaux à temps. C'est promis. »</p>
    <p><strong>Preheader :</strong> « 21 jours avant Noël. Largement le temps de bien faire. »</p>
    <p><strong>H1 :</strong> « Encore 21 jours. Largement le temps. »</p>
    <p><strong>Body :</strong> Délais garantis par destination · Options express si retard</p>
    <p><strong>CTA :</strong> « Voir les délais garantis »</p>
    """,
    10
))

S.append(template_card(
    "Services",
    "Annoncer une nouvelle offre ou un changement d'usage (point relais, consigne, livraison hors domicile). <strong>Pédagogie</strong>, pas argumentaire.",
    "Au lancement d'une offre OU sur change life event (déménagement, premier colis hors zone).",
    "Base active OU sous-segment géo selon disponibilité du service.",
    """
    <p><strong>Objet :</strong> « Recevez vos colis quand vous voulez, où vous voulez »</p>
    <p><strong>Preheader :</strong> « 5 000 points relais. Le plus proche est peut-être à 3 minutes. »</p>
    <p><strong>H1 :</strong> « Le point relais qui vous arrange. »</p>
    <p><strong>Body :</strong> « Comment ça marche » en 3 étapes + 2 cas d'usage</p>
    <p><strong>CTA :</strong> « Trouver mon point relais »</p>
    """,
    11
))

S.append(template_card(
    "Singular (B2B SME)",
    "Email B2B pour la plateforme Singular. <strong>Ton pro</strong>, ROI chiffré, signature Account Manager. Pas de promo grand public.",
    "Lifecycle B2B : onboarding compte SME, milestones d'usage, opportunités revenue.",
    "Comptes Singular SME. Segmentation par taille (TPE/PME), secteur, ARR.",
    """
    <p><strong>Sender :</strong> « {Nom AM} — Geopost Singular »</p>
    <p><strong>Objet :</strong> « Votre rapport ventes Singular est disponible »</p>
    <p><strong>H1 :</strong> « Vos 3 leviers d'optimisation ce mois. »</p>
    <p><strong>Body :</strong> Metrics + ROI chiffré + 1 témoignage SME</p>
    <p><strong>CTA :</strong> « Demander une démo » ou « Voir le rapport » (jamais « Profiter »)</p>
    """,
    12
))

# 13 — Design framework
S.append(content_slide(
    "Slide 13 · §4-B",
    "Design aligné sur brand guidelines existantes",
    """
    <div class="layout-2col">
      <div>
        <h3>Anatomie commune des 6 templates</h3>
        <ul>
          <li>Préheader (≤110 car.)</li>
          <li>Header — logo brand + nav optionnelle</li>
          <li>Héro — H1 texte + visuel décoratif <code>alt=""</code></li>
          <li>Sub-héro — 1 phrase bénéfice + temps requis</li>
          <li>CTA primaire bulletproof ≥44px tactile</li>
          <li>Body modulaire — 1 à 3 blocs réutilisables max</li>
          <li>CTA secondaire (optionnel)</li>
          <li>Footer légal — adresse + désabo + RGPD pays-spécifique</li>
        </ul>
      </div>
      <div>
        <h3>Règles design strictes</h3>
        <ul>
          <li>Wrapper 640px desktop / 100% mobile</li>
          <li>Échelle typo ≤3 tailles par email</li>
          <li>Espacements multiples de 4 ou 8</li>
          <li>1 ou 2 polices max, fallback Arial obligatoire</li>
          <li>Border-radius cohérent (0 ou valeur unique)</li>
          <li>Pas d'ombre CSS3 (non supportée Outlook)</li>
          <li>Logo taille et position constantes</li>
        </ul>
        <p class="muted" style="margin-top:10px;">→ Brand guidelines Geopost respectées strictement. Aucune évolution de tonalité ni positionnement.</p>
      </div>
    </div>
    """,
    13, 18, DECK
))

# ============ SECTION C — HTML Integration (4 slides) ============

# 14 — C intro
S.append(content_slide(
    "Slide 14 · §4-C",
    "HTML Integration — robustesse, a11y, maintenabilité",
    """
    <table>
      <thead><tr><th>Périmètre</th><th>Templates concernés</th><th>Tests automatisés</th></tr></thead>
      <tbody>
        <tr><td><strong>Trigger email templates</strong></td><td>Welcome · Promote app · Boost sales</td><td>Litmus / EoA · WCAG axe-core · Outlook 2007→M365 · iOS/Android · dark mode</td></tr>
        <tr><td><strong>One-shot templates</strong></td><td>Commercial peak · Services · Singular</td><td>Idem + tests campagne saisonnière sur sandbox imagino</td></tr>
      </tbody>
    </table>
    <h3 style="margin-top:24px;">3 focus du brief</h3>
    <div class="layout-3col">
      <div class="card accent"><h3>Compatibilité Outlook</h3><p>Slide 15 — head standard, pack mso, bulletproof button, role=presentation</p></div>
      <div class="card accent"><h3>Standards a11y</h3><p>Slide 16 — WCAG AA, focus visible, alt explicites, color-scheme, taille tactile</p></div>
      <div class="card accent"><h3>Maintenabilité</h3><p>Slide 17 — librairie modulaire, versioning, doc, tests automatisés</p></div>
    </div>
    """,
    14, 18, DECK
))

# 15 — C.1 Outlook compat
S.append(content_slide(
    "Slide 15 · §4-C · Compatibilité Outlook",
    "Ce qu'on garantit (2007 → M365)",
    """
    <div class="layout-2col">
      <div>
        <h3>Head email standard</h3>
        <ul style="font-size:14px;">
          <li><code>&lt;!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"&gt;</code></li>
          <li><code>&lt;meta charset="utf-8"&gt;</code></li>
          <li><code>&lt;meta name="viewport" content="width=device-width"&gt;</code></li>
          <li><code>&lt;meta http-equiv="X-UA-Compatible" content="IE=edge"&gt;</code></li>
          <li><code>&lt;meta name="color-scheme" content="light dark"&gt;</code></li>
          <li><code>&lt;title&gt;</code> non vide</li>
        </ul>
        <h3 style="margin-top:14px;">Pack mso obligatoire</h3>
        <ul style="font-size:14px;">
          <li><code>mso-table-lspace: 0pt; mso-table-rspace: 0pt;</code></li>
          <li><code>mso-line-height-rule: exactly;</code></li>
          <li>Conditional comments <code>&lt;!--[if mso]&gt; ... &lt;![endif]--&gt;</code></li>
        </ul>
      </div>
      <div>
        <h3>Structure HTML</h3>
        <ul style="font-size:14px;">
          <li>Tables imbriquées exclusives (pas de <code>&lt;div&gt;</code> en structure)</li>
          <li><code>width</code> en HTML attribut <em>ET</em> en CSS</li>
          <li><code>height</code> en HTML attribut sur images</li>
          <li><code>border="0" cellpadding="0" cellspacing="0"</code> systématique</li>
          <li>Pas de <code>padding</code> sur <code>&lt;table&gt;</code> — sur <code>&lt;td&gt;</code> uniquement</li>
          <li>Aucun JavaScript, iframe, <code>@import</code>, framework</li>
        </ul>
        <h3 style="margin-top:14px;">Bouton CTA</h3>
        <ul style="font-size:14px;">
          <li><strong>Bulletproof VML</strong> + fallback <code>&lt;td bgcolor&gt;</code></li>
          <li>Jamais de <code>border-radius</code> CSS isolé sur table</li>
          <li>Jamais de <code>box-shadow</code></li>
        </ul>
      </div>
    </div>
    """,
    15, 18, DECK
))

# 16 — C.2 a11y
S.append(content_slide(
    "Slide 16 · §4-C · Standards d'accessibilité",
    "WCAG AA strict + dark mode",
    """
    <div class="layout-2col">
      <div>
        <h3>WCAG AA — checklist exécutée à l'intégration</h3>
        <ul style="font-size:14px;">
          <li>Contraste body ≥4.5:1, texte large ≥3:1</li>
          <li>Contraste graphique fonctionnel ≥3:1</li>
          <li><code>alt</code> descriptif ≤80 car. sur images sens</li>
          <li><code>alt=""</code> sur décoratifs et pixel tracking</li>
          <li><code>role="presentation"</code> sur tables layout</li>
          <li><code>lang</code> sur <code>&lt;html&gt;</code></li>
          <li>Ordre de lecture top-down / left-right LTR</li>
          <li>CTA labels explicites, jamais « Cliquez ici »</li>
          <li>Pas d'info via couleur seule</li>
          <li><code>:focus</code> visible sur tous liens et CTA</li>
        </ul>
      </div>
      <div>
        <h3>Dark mode</h3>
        <ul style="font-size:14px;">
          <li><code>&lt;meta name="color-scheme" content="light dark"&gt;</code></li>
          <li><code>@media (prefers-color-scheme: dark)</code></li>
          <li>Variantes couleur fond/texte/CTA</li>
          <li>Logos avec versions si brand le permet</li>
        </ul>
        <h3 style="margin-top:14px;">Cible tactile</h3>
        <ul style="font-size:14px;">
          <li>CTA hauteur ≥44px</li>
          <li>Largeur clic ≥44px</li>
          <li>Espacement entre liens cliquables ≥8px</li>
        </ul>
        <h3 style="margin-top:14px;">Tests automatisés</h3>
        <ul style="font-size:14px;">
          <li>WCAG axe-core en CI sur chaque PR</li>
          <li>Litmus screenshot ≥30 clients</li>
        </ul>
      </div>
    </div>
    """,
    16, 18, DECK
))

# 17 — C.3 Librairie modulaire
S.append(content_slide(
    "Slide 17 · §4-C · Librairie modulaire de blocs",
    "« Bloc promo intégrable dans n'importe quel email » — cf. brief",
    """
    <div class="layout-2col">
      <div>
        <h3>Architecture proposée</h3>
        <ul>
          <li><strong>1 core template par parcours</strong> (×6)</li>
          <li><strong>Catalogue de blocs réutilisables</strong> partagé entre tous les templates</li>
          <li>Chaque bloc est <strong>autonome, testé, versionné</strong></li>
          <li>Assemblage par référence dans imagino (pas par copier-coller)</li>
        </ul>
        <h3 style="margin-top:14px;">Maintenabilité</h3>
        <ul>
          <li>Repo Git versionné agence</li>
          <li>PR avec tests Litmus + WCAG en CI</li>
          <li>Doc Markdown par bloc (paramètres, slots)</li>
          <li>Releases versionnées</li>
        </ul>
      </div>
      <div>
        <h3>Familles de blocs candidates</h3>
        <ul style="font-size:14px;">
          <li><strong>Structure</strong> — wrapper, header, footer, spacer</li>
          <li><strong>Héros &amp; titres</strong> — héro texte+visuel, héro plein, bannière promo</li>
          <li><strong>Body</strong> — texte 1col, 2col, 3 cards, 3 étapes, image+texte, quote</li>
          <li><strong>CTA</strong> — primary, secondary, double, lien texte</li>
          <li><strong>Spéciaux</strong> — tracking colis, code promo, QR app store</li>
          <li><strong>Conformité</strong> — mentions RGPD, désabo, adresse</li>
        </ul>
        <p class="muted" style="margin-top:10px;">→ Le bloc promo cité au brief est traité comme bloc Spéciaux, intégrable dans n'importe quel template.</p>
      </div>
    </div>
    """,
    17, 18, DECK
))

# 18 — Closing — jalons brief
S.append(content_slide(
    "Slide 18 · Synthèse",
    "Ce qu'on livre, alignement jalons brief §7",
    """
    <div class="layout-2col">
      <div>
        <h3>Livrables (cf. brief §5)</h3>
        <ul>
          <li>Documentation audit &amp; recommandations <em>(§4-A)</em></li>
          <li>Email guidelines Geopost</li>
          <li>6 templates email designés <em>(§4-B)</em></li>
          <li>Fichiers HTML intégrés et entièrement testés <em>(§4-C)</em></li>
          <li>Librairie modulaire de blocs <em>(§4-C, optionnel brief)</em></li>
        </ul>
      </div>
      <div>
        <h3>Jalons brief §7</h3>
        <ul style="font-size:14px;">
          <li><strong>22 mai 2026</strong> — Proposal submission</li>
          <li><strong>28 mai 2026</strong> — Review &amp; shortlist</li>
          <li><strong>S1 juin</strong> — Pitch presentations</li>
          <li><strong>5 juin</strong> — Final selection</li>
          <li><strong>15 juin</strong> — Kick-off meeting</li>
        </ul>
      </div>
    </div>
    <div style="margin-top: auto; padding-top: 20px; border-top: 2px solid var(--red);">
      <h3 style="color:var(--red); text-align:center; margin:0;">Track record, budget &amp; planning détaillé en annexe commerciale</h3>
      <p style="text-align:center; margin-top:8px;" class="muted">cf. Agent 07 — Commercial RFP · livré séparément avec composition équipe + expérience CRM emailing</p>
    </div>
    """,
    18, 18, DECK
))

build_deck("Réponse Brief §4 — Templates Revamp Geopost", S, f"{ROOT}/decks/DECK_BRIEF_SCOPE4.html")
print(f"OK Deck Brief §4 ({len(S)} slides)")
