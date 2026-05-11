# Geopost CRM Agents

Dispositif multi-agents WPP Creative Studio pour répondre à l'AO **Templates Revamp Project**
de Geopost (Consumer Relation and Acquisition Program — RFP du 4 mai 2026, deadline 22 mai).

Contrairement à l'agent `kia Dev V4` (mono-agent, purement HTML email), Geopost demande un
dispositif plus large : audit, stratégie CRM, design, copywriting/CRO, intégration HTML
robuste, librairie modulaire, guidelines multi-brand/multi-country (5 marques : BRT,
DPD CH, DPD CZ, DPD SK, autres à venir), et réponse commerciale.

D'où l'architecture **Lead CRM orchestrateur + 7 sous-agents spécialisés**.

---

## Structure

```
Geopost-CRM-Agents/
├── README.md                                  ← ce fichier
├── ARCHITECTURE.md                            schéma d'orchestration Lead CRM ↔ sous-agents
├── PLAYBOOK_replication_geopost.md            playbook de réplication WPP (calque du Kia)
│
├── _brief/
│   ├── Brief_TemplatesRevampProject.pdf       brief Geopost original
│   ├── Brief_TemplatesRevampProject.txt       extraction texte (lisible)
│   └── sample_existing_dpd_email.html         exemple email DPD existant (état actuel)
│
├── _references_kia/                           références de production (NE PAS coller dans WPP Geopost)
│   ├── SYSTEM_PROMPT_agent_email.md           prompt 17 sections Kia (squelette à dériver)
│   └── PLAYBOOK_agent_email_dev_scalable.md   playbook scalable Kia
│
├── lead_crm/
│   └── SYSTEM_PROMPT_lead_crm_geopost.md      Lead CRM (audit + strat + dispatch)
│
├── sub_agents/
│   ├── 01_SYSTEM_PROMPT_audit.md
│   ├── 02_SYSTEM_PROMPT_cro_ux_writing.md
│   ├── 03_SYSTEM_PROMPT_template_design.md
│   ├── 04_SYSTEM_PROMPT_html_integration.md
│   ├── 05_SYSTEM_PROMPT_modular_library.md
│   ├── 06_SYSTEM_PROMPT_guidelines_multibrand.md
│   └── 07_SYSTEM_PROMPT_commercial_rfp.md
│
└── design_system/
    ├── CLAUDE_DESIGN_BRIEF.md                 brief Claude Design — design system email
    ├── CLAUDE_DESIGN_BRIEF_PPT.md             brief Claude Design — deck pitch AO (15-20 slides)
    └── _sources/
        ├── geopost_corporate_homepage.html    HTML source (geopost.com/fr/entreprise/)
        └── extracted_tokens.md                tokens extraits (point de départ chiffré)
```

---

## Comment utiliser

### 1. Production opérationnelle CRM (Lead CRM + sous-agents)

Chaque fichier dans `lead_crm/` et `sub_agents/` est un **System prompt self-contained** au
format WPP Creative Studio (`imagine.wpp.ai`).

Pour chacun :

1. Ouvrir le fichier.
2. Faire un **Find & Replace global** des placeholders entre crochets (cf. §0 de chaque prompt).
3. Coller le bloc `MISSION ... OBJECTIF FINAL` dans le champ **System prompt** WPP.
4. Renseigner les onglets **Profile / Sources / Instructions / Learning** selon
   `PLAYBOOK_replication_geopost.md`.
5. Tester avec les **tests d'acceptance** documentés dans le playbook.
6. Publish.

**Important :** le Lead CRM est l'interlocuteur unique de l'équipe pitch / lead AO.
Les sous-agents ne sont jamais sollicités directement par l'équipe — ils reçoivent un brief
formaté par le Lead CRM (cf. `ARCHITECTURE.md`).

### 2. Génération du design system Geopost (track parallèle)

Coller `design_system/CLAUDE_DESIGN_BRIEF.md` dans Claude Design (ou tout LLM design-aware)
avec en pièce jointe `design_system/_sources/geopost_corporate_homepage.html`.

Output attendu : `design-tokens.json`, `design-system.md`, `component-anatomy.md`,
`accessibility-checklist.md`.

### 2 bis. Génération du deck pitch AO (PPT)

Coller `design_system/CLAUDE_DESIGN_BRIEF_PPT.md` dans Claude Design, avec en pièces jointes :
`geopost_corporate_homepage.html` (tokens), `Brief_TemplatesRevampProject.pdf` (périmètre),
et optionnellement la sortie consolidée de l'agent `Geopost Commercial RFP V1`.

Output attendu : `deck-content.md`, `deck-spec.md`, et optionnellement
`deck-html-preview.html` (preview navigable).

### 3. Réponse à l'AO Geopost

Utiliser le sous-agent `07_SYSTEM_PROMPT_commercial_rfp.md` pour structurer la réponse
écrite (résumé exécutif, méthodologie, équipe, planning, budget, deliverables).
Les blocs `[À COMPLÉTER AGENCE]` doivent être renseignés avec les vraies infos agence
(références clients, tarifs, CVs équipe) avant envoi.

---

## Plateforme cible

- **WPP Creative Studio** (`imagine.wpp.ai`) — modèle Gemini 3.1 Pro, mode Medium,
  Seed 0, Temperature Predictable, Top P Focused, Max Tokens & Top K Diverse.
- **imagino** (Customer Data Platform) côté Geopost — plateforme d'envoi.

---

## Repo local — pas de push automatique

Ce repo est en `git init` local uniquement. Le push vers un remote distant est à faire
manuellement (le user pousse depuis sa machine vers le remote agence à créer).
