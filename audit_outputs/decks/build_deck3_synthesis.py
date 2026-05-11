"""Deck 3 — Synthèse · 15 slides — workflow agence × dispositif agent."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from _framework import cover, section_slide, content_slide, build_deck

ROOT = "/home/user/Geopost/audit_outputs"
DECK = "SYNTHÈSE · 15 slides"
N = 15
S = []

# 1 Cover
S.append(cover(
    "Synthèse · Geopost",
    "Workflow agence × dispositif agent",
    "Comment on opère la production email de bout en bout",
    "11 mai 2026 · Geopost Lead CRM V1 + 7 sous-agents",
    1, N
))

# 2 Le constat
S.append(content_slide(
    "Slide 02 · Le constat",
    "L'email d'agence prend trop de temps, fait trop d'allers-retours",
    """
    <div class="layout-2col">
      <div>
        <h3>Production email classique</h3>
        <ul>
          <li>Brief client → strat → design → copy → HTML → QA → push</li>
          <li>5 à 8 personnes mobilisées par template</li>
          <li>2 à 4 semaines de cycle nominal</li>
          <li>Itérations × 3-5 par jalon</li>
          <li>Régression Outlook découverte tardivement</li>
          <li>Variations BU recodées à la main</li>
        </ul>
      </div>
      <div>
        <h3>Ce qui pose problème pour Geopost</h3>
        <ul>
          <li><strong>5 BUs × 6 templates = 30 emails</strong> en production</li>
          <li>3 fenêtres Peak / an</li>
          <li>Langue locale + légal local par BU</li>
          <li>Une seule QA centralisée Geopost</li>
          <li><strong>Le rythme classique ne tient pas</strong></li>
        </ul>
      </div>
    </div>
    """,
    2, N, DECK
))

# 3 La proposition
S.append(content_slide(
    "Slide 03 · Notre proposition",
    "Un dispositif multi-agents Claude orchestré par un Lead CRM",
    """
    <div style="background:#fafafa; border:1px solid var(--border); border-radius:8px; padding:24px; margin: 8px 0;">
      <h3 style="text-align:center; color:var(--red); margin-bottom:16px;">Lead CRM Geopost V1 — orchestrateur unique</h3>
      <div style="display:grid; grid-template-columns: repeat(7, 1fr); gap:8px;">
        <div style="background:#fff; border:1px solid var(--border); border-radius:6px; padding:10px; text-align:center; font-size:11px;"><strong>01</strong><br>Audit</div>
        <div style="background:#fff; border:1px solid var(--border); border-radius:6px; padding:10px; text-align:center; font-size:11px;"><strong>02</strong><br>CRO & UX Writing</div>
        <div style="background:#fff; border:1px solid var(--border); border-radius:6px; padding:10px; text-align:center; font-size:11px;"><strong>03</strong><br>Template Design</div>
        <div style="background:#fff; border:1px solid var(--border); border-radius:6px; padding:10px; text-align:center; font-size:11px;"><strong>04</strong><br>HTML Integration</div>
        <div style="background:#fff; border:1px solid var(--border); border-radius:6px; padding:10px; text-align:center; font-size:11px;"><strong>05</strong><br>Modular Library</div>
        <div style="background:#fff; border:1px solid var(--border); border-radius:6px; padding:10px; text-align:center; font-size:11px;"><strong>06</strong><br>Guidelines & Multi-Brand</div>
        <div style="background:#fff; border:1px solid var(--border); border-radius:6px; padding:10px; text-align:center; font-size:11px;"><strong>07</strong><br>Commercial RFP</div>
      </div>
    </div>
    <p style="text-align:center; font-size:18px; margin-top:24px;"><strong>1 chef de projet humain pilote 7 sous-agents spécialisés</strong>. Les sous-agents produisent. Le Lead CRM consolide.</p>
    """,
    3, N, DECK
))

# 4 Le flow type
S.append(content_slide(
    "Slide 04 · Le flow type — 1 template, end-to-end",
    "De la demande client à la mise en production",
    """
    <div class="flow">
      <div class="step"><div class="num">1</div><h4>Brief client</h4><p>Demande Geopost arrive au chef de projet</p></div>
      <div class="step"><div class="num">2</div><h4>Lead CRM qualifie</h4><p>Mode (Audit/Strat/Prod/Conso), BU, livrable</p></div>
      <div class="step"><div class="num">3</div><h4>Dispatch agents</h4><p>Briefs structurés vers 1 à 7 sous-agents</p></div>
      <div class="step"><div class="num">4</div><h4>Production</h4><p>Sous-agents délivrent en parallèle ou cascade</p></div>
      <div class="step"><div class="num">5</div><h4>Consolidation</h4><p>Lead CRM assemble en livrable cohérent</p></div>
      <div class="step"><div class="num">6</div><h4>QA + push</h4><p>Tests Litmus + déploiement imagino</p></div>
    </div>
    <h3 style="margin-top:24px;">Ce que ce flow change</h3>
    <ul>
      <li>Les <strong>aller-retours sont absorbés en heures</strong>, pas en jours (chaque sous-agent itère sur son périmètre sans réunion)</li>
      <li>Le <strong>chef de projet humain</strong> garde le contrôle stratégique (priorisation, arbitrages, validation Geopost)</li>
      <li>Les <strong>règles métier</strong> (a11y, Outlook, multi-brand) sont <em>codifiées</em> dans les system prompts → impossible de les oublier</li>
    </ul>
    """,
    4, N, DECK
))

# 5 Etape Audit
S.append(content_slide(
    "Slide 05 · Étape Audit · Agent 01",
    "Auditeur senior CRM/email automatisé",
    """
    <div class="layout-2col">
      <div>
        <h3>Ce que l'agent fait</h3>
        <ul>
          <li>Audit 6 dimensions (HTML, Outlook, a11y, design, copy, multi-brand)</li>
          <li>Captures multi-environnements (desktop, mobile, dark, images-off)</li>
          <li>Grille consolidée écarts numérotés + sévérité P0/P1/P2</li>
          <li>Plan d'action priorisé + estimation effort</li>
          <li>Dispatch vers sous-agents correctifs</li>
        </ul>
      </div>
      <div>
        <h3>Ce qu'on a déjà livré</h3>
        <ul>
          <li><strong>POC DPD FR audité</strong> en 1 itération</li>
          <li>36 écarts détectés · 5 captures annotées · scoring brief</li>
          <li>Itération V2 prête dès réception des 3 autres POC</li>
          <li>Format reproductible : script Python + Chromium headless</li>
        </ul>
        <p class="muted">⏱️ Cycle classique audit : 1-2 semaines · Cycle agent : <strong>2-4 heures</strong></p>
      </div>
    </div>
    """,
    5, N, DECK
))

# 6 Etape Copy
S.append(content_slide(
    "Slide 06 · Étape Copy · Agent 02 CRO & UX Writing",
    "Réécriture objet/preheader/H1/CTA, A/B variants",
    """
    <div class="layout-2col">
      <div>
        <h3>Ce que l'agent fait</h3>
        <ul>
          <li>Réécrit objet (≤50 car.), preheader (≤110), H1, body, CTA</li>
          <li>Produit 3 variantes A/B/C systématiquement</li>
          <li>Cohérence brand voice Geopost / BU</li>
          <li>Adapte le ton B2C vs B2B (Singular)</li>
          <li>Vérifie les mots interdits (révolutionnaire, ultime…)</li>
        </ul>
      </div>
      <div>
        <h3>Cadrage strict</h3>
        <ul>
          <li>≤4 mots CTA, casse normale</li>
          <li>1 seul CTA primaire par email</li>
          <li>Quantifier les durées (« 2 minutes » &gt; « quelques minutes »)</li>
          <li>Preheader teaser, jamais doublon H1</li>
          <li>Mention durée + bénéfice tangible</li>
        </ul>
        <p class="muted">Brand guidelines existantes Geopost respectées par le system prompt — pas d'évolution de tonalité non autorisée.</p>
      </div>
    </div>
    """,
    6, N, DECK
))

# 7 Etape Design
S.append(content_slide(
    "Slide 07 · Étape Design · Agent 03 Template Design",
    "Spec design : wireframe, hiérarchie, design system",
    """
    <div class="layout-2col">
      <div>
        <h3>Ce que l'agent fait</h3>
        <ul>
          <li>Spec design template (wireframe + tokens utilisés)</li>
          <li>Hiérarchie visuelle, échelle typo, espacements 4/8</li>
          <li>Bouton CTA bulletproof ≥44px tactile</li>
          <li>Adaptation dark mode (color-scheme)</li>
          <li>Brief image héro <em>décorative</em> (jamais porteuse de message)</li>
        </ul>
      </div>
      <div>
        <h3>Livrables techniques</h3>
        <ul>
          <li>Wireframes Figma annotés (par bloc)</li>
          <li>Specs tokens utilisés (couleur, typo, spacing)</li>
          <li>Variantes BU si tokens couleur impactants</li>
          <li>Spec image héro : ratio, poids, format optimal</li>
          <li>Cadrage taille mobile + spec responsive</li>
        </ul>
        <p class="muted">L'agent produit la spec → un designer humain finalise les visuels brand-aligned.</p>
      </div>
    </div>
    """,
    7, N, DECK
))

# 8 Etape HTML
S.append(content_slide(
    "Slide 08 · Étape HTML · Agent 04 HTML Integration",
    "Code email production-ready, Outlook + a11y compliant",
    """
    <div class="layout-2col">
      <div>
        <h3>Ce que l'agent fait</h3>
        <ul>
          <li>Intègre HTML XHTML email standard (head complet, charset, viewport, color-scheme)</li>
          <li>Tables imbriquées + <code>role="presentation"</code> partout</li>
          <li>Pack mso complet (lspace/rspace, line-height-rule, conditionals)</li>
          <li>Bulletproof button VML pour CTA</li>
          <li>Responsive <code>@media</code> + dark mode <code>prefers-color-scheme</code></li>
          <li>Inline CSS + fallback Arial sur toute stack typo</li>
        </ul>
      </div>
      <div>
        <h3>Tests automatisés</h3>
        <ul>
          <li>Validation HTML5 + WCAG axe-core</li>
          <li>Tests Litmus / Email on Acid (≥30 clients)</li>
          <li>Tests Outlook 2007, 2010, 2013, 2016+, M365, mobile, iOS, Android</li>
          <li>Dark mode Gmail Android + Outlook iOS</li>
          <li>Régression : snapshot pixel par client</li>
        </ul>
      </div>
    </div>
    """,
    8, N, DECK
))

# 9 Etape Library + Guidelines
S.append(content_slide(
    "Slide 09 · Étape Library + Guidelines · Agents 05 & 06",
    "Catalogue de blocs + formalisation des règles",
    """
    <div class="layout-2col">
      <div>
        <h3>Agent 05 — Modular Library</h3>
        <ul>
          <li>Extrait les blocs réutilisables après chaque template intégré</li>
          <li>Versionne le catalogue (~30 blocs cibles)</li>
          <li>Paramètres par bloc : tokens BU, slots de contenu</li>
          <li>Push vers librairie imagino (CDP)</li>
          <li>Garantit l'<strong>unicité du code</strong> entre les templates</li>
        </ul>
      </div>
      <div>
        <h3>Agent 06 — Guidelines & Multi-Brand</h3>
        <ul>
          <li>Formalise les règles (Outlook, a11y, design, copy)</li>
          <li>Table des tokens par BU (couleur, logo, légal, langue)</li>
          <li>RACI éditorial Geopost × BU locale</li>
          <li>Veille évolution des clients email majeurs (Apple Mail, Outlook 365)</li>
        </ul>
      </div>
    </div>
    <p class="muted" style="margin-top:14px;">→ Output combiné : <strong>1 référentiel Geopost</strong> qui survit aux rotations d'équipes agence.</p>
    """,
    9, N, DECK
))

# 10 RACI
S.append(content_slide(
    "Slide 10 · RACI — humains × agents",
    "Qui fait quoi, qui décide, qui valide",
    """
    <table>
      <thead><tr><th>Étape</th><th>Chef projet humain</th><th>Lead CRM Claude</th><th>Sous-agents</th><th>Geopost</th></tr></thead>
      <tbody>
        <tr><td>Qualification brief</td><td>A</td><td>R</td><td>—</td><td>C</td></tr>
        <tr><td>Audit POC</td><td>A</td><td>C</td><td><strong>R</strong> (01)</td><td>I</td></tr>
        <tr><td>Réécriture copy</td><td>A</td><td>C</td><td><strong>R</strong> (02)</td><td>C (validation locale)</td></tr>
        <tr><td>Spec design</td><td>A</td><td>C</td><td><strong>R</strong> (03)</td><td>C</td></tr>
        <tr><td>Visuels brand</td><td><strong>R</strong> (designer)</td><td>—</td><td>—</td><td>C</td></tr>
        <tr><td>Intégration HTML</td><td>A</td><td>C</td><td><strong>R</strong> (04)</td><td>I</td></tr>
        <tr><td>Tests Litmus</td><td><strong>R</strong></td><td>I</td><td>C (04)</td><td>I</td></tr>
        <tr><td>Push imagino</td><td><strong>R</strong></td><td>I</td><td>—</td><td>A</td></tr>
        <tr><td>Tracking KPIs</td><td>R</td><td>—</td><td>—</td><td><strong>A</strong></td></tr>
      </tbody>
    </table>
    <p class="muted" style="margin-top:8px;">R = Responsible · A = Accountable · C = Consulted · I = Informed</p>
    """,
    10, N, DECK
))

# 11 Gains chiffrés
S.append(content_slide(
    "Slide 11 · Gains chiffrés du dispositif",
    "Ce que l'agent fait gagner — par étape",
    """
    <table>
      <thead><tr><th>Étape</th><th>Cycle classique</th><th>Cycle agent</th><th>Gain</th></tr></thead>
      <tbody>
        <tr><td>Audit POC complet</td><td>1-2 semaines</td><td><strong>2-4 heures</strong></td><td>~20×</td></tr>
        <tr><td>Réécriture copy 3 variantes</td><td>3-5 jours</td><td><strong>1-2 heures</strong></td><td>~15×</td></tr>
        <tr><td>Spec design wireframe</td><td>3-5 jours</td><td><strong>4-6 heures</strong></td><td>~6×</td></tr>
        <tr><td>Intégration HTML + tests</td><td>1 semaine</td><td><strong>1-2 jours</strong></td><td>~3×</td></tr>
        <tr><td>Adaptation 5 BUs d'un template</td><td>2 semaines</td><td><strong>2 jours</strong></td><td>~5×</td></tr>
        <tr><td>Cycle complet 1 template prod</td><td>4-6 semaines</td><td><strong>1-2 semaines</strong></td><td><strong>~3×</strong></td></tr>
      </tbody>
    </table>
    <p class="muted" style="margin-top:8px;">Ordres de grandeur basés sur dispositif similaires WPP + benchmarks agences BtoB. À calibrer après 3 templates en prod.</p>
    """,
    11, N, DECK
))

# 12 Intégration imagino
S.append(content_slide(
    "Slide 12 · Intégration imagino",
    "Comment le dispositif se branche sur la plateforme CDP",
    """
    <div class="layout-2col">
      <div>
        <h3>Côté production (notre équipe)</h3>
        <ul>
          <li>Lead CRM + sous-agents tournent sur infra agence</li>
          <li>Outputs (HTML, blocs, tokens, copy) → <strong>repo Git versionné</strong></li>
          <li>CI : tests Litmus + WCAG automatisés sur PR</li>
          <li>Validation humaine sur PR avant merge</li>
        </ul>
      </div>
      <div>
        <h3>Côté imagino (CDP Geopost)</h3>
        <ul>
          <li>Templates HTML poussés via <strong>API imagino</strong> ou interface admin</li>
          <li>Blocs modulaires importés dans la librairie native imagino</li>
          <li>Tokens BU mappés aux <em>audience attributes</em> imagino</li>
          <li>Trigger règles configurées dans imagino (côté Geopost)</li>
          <li>Tracking ouvertures/clics renvoyé vers dashboard</li>
        </ul>
      </div>
    </div>
    <p class="muted" style="margin-top:14px;">⚠️ <strong>API imagino à confirmer</strong> Geopost (endpoints templates, format push, auth). À cadrer en kick-off semaine du 15 juin.</p>
    """,
    12, N, DECK
))

# 13 Governance
S.append(content_slide(
    "Slide 13 · Governance & sécurité",
    "Le cadre opérationnel agent",
    """
    <div class="layout-2col">
      <div>
        <h3>System prompts versionnés</h3>
        <ul>
          <li>Tous les system prompts (Lead CRM + 7 agents) sont <strong>fichiers .md versionnés Git</strong></li>
          <li>Toute évolution = PR + review humaine</li>
          <li>Audit trail complet de qui a changé quoi quand</li>
          <li>Rollback en 1 commande si dérive</li>
        </ul>
      </div>
      <div>
        <h3>Garde-fous métier</h3>
        <ul>
          <li>Sources autorisées limitées (URLs Geopost officielles)</li>
          <li>Aucun web search / scraping</li>
          <li>Pas de données client réelles dans les prompts</li>
          <li>RGPD : aucune PII passée aux agents en clair</li>
          <li>Règle « pas de chiffres inventés » → <code>[À CONFIRMER]</code> en clair si manque</li>
        </ul>
      </div>
    </div>
    <p class="muted" style="margin-top:14px;"><strong>Le dispositif n'envoie rien sans validation humaine.</strong> Les agents produisent → l'équipe agence valide → Geopost approuve → push imagino.</p>
    """,
    13, N, DECK
))

# 14 Roadmap intégration
S.append(content_slide(
    "Slide 14 · Roadmap intégration agent",
    "Comment on monte en charge sur 6 mois",
    """
    <div class="flow">
      <div class="step"><div class="num">M1</div><h4>Juin</h4><p>Kick-off + setup agents + audit V2 inter-BU</p></div>
      <div class="step"><div class="num">M2</div><h4>Juillet</h4><p>Welcome pilote BRT end-to-end avec dispositif</p></div>
      <div class="step"><div class="num">M3</div><h4>Août</h4><p>Réplication Welcome × 4 BUs (preuve scalabilité)</p></div>
      <div class="step"><div class="num">M4</div><h4>Sept</h4><p>Promote app + Boost sales × 5 BUs</p></div>
      <div class="step"><div class="num">M5</div><h4>Oct</h4><p>Peak Noël + Services + Singular × 5 BUs</p></div>
      <div class="step"><div class="num">M6</div><h4>Nov-Déc</h4><p>QA cross-BU + benchmarks 30j + itérations</p></div>
    </div>
    <h3 style="margin-top:24px;">Jalons clés</h3>
    <ul>
      <li><strong>S25-S26</strong> · Kick-off + accès imagino + brand guidelines BUs collectées</li>
      <li><strong>S30</strong> · Pilot Welcome BRT live en sandbox (validation Geopost)</li>
      <li><strong>S34</strong> · Welcome × 5 BUs en preprod (preuve réplication)</li>
      <li><strong>S44</strong> · Campagne Peak Noël en prod sur les 5 BUs</li>
      <li><strong>S52</strong> · Rétrospective 6 mois + benchmark vs POC</li>
    </ul>
    """,
    14, N, DECK
))

# 15 Closing
S.append(content_slide(
    "Slide 15 · Pourquoi nous, pourquoi maintenant",
    "Ce que cette approche change pour Geopost",
    """
    <div class="layout-2col">
      <div>
        <h3>3 différenciateurs</h3>
        <ul>
          <li><strong>1. Vitesse</strong> · cycle template ÷ 3 minimum, sans sacrifier la qualité technique</li>
          <li><strong>2. Cohérence</strong> · 1 codebase, 5 BUs, 0 dérive — règles codifiées dans les prompts</li>
          <li><strong>3. Scalabilité</strong> · ajouter une 6ème BU = ajouter des tokens, pas re-développer</li>
        </ul>
      </div>
      <div>
        <h3>Ce que l'on demande à Geopost</h3>
        <ul>
          <li>3 autres POC pour audit V2 inter-BU</li>
          <li>Brand guidelines détaillées par BU</li>
          <li>Accès imagino sandbox + doc API</li>
          <li>Référent éditorial par BU (RACI)</li>
          <li>Kick-off semaine du 15 juin</li>
        </ul>
      </div>
    </div>
    <div style="margin-top: auto; padding-top: 20px; border-top: 2px solid var(--red);">
      <h3 style="color:var(--red); text-align:center; margin:0;">Repository complet : Arnaud-ths/Geopost · branche claude/fix-bug-repush-3DPUw</h3>
      <p style="text-align:center; margin-top:8px;" class="muted">Lead CRM + 7 sous-agents · Audit POC livré · Decks 1+2+3 · Code reproductible</p>
    </div>
    """,
    15, N, DECK
))

build_deck("Synthèse — 15 slides", S, f"{ROOT}/decks/DECK_3_SYNTHESE.html")
print(f"OK Deck 3 ({len(S)} slides)")
