# Playbook — Réplication du dispositif Lead CRM Geopost dans WPP Creative Studio

> **Objet :** déployer les 8 agents (1 Lead CRM + 7 sous-agents) sur WPP Creative Studio
> (`imagine.wpp.ai`), en suivant la même méthode que celle utilisée pour `kia Dev V4`.
> **Calque :** ce playbook est dérivé de `_references_kia/PLAYBOOK_agent_email_dev_scalable.md`
> et adapté au périmètre Geopost (multi-agents, multi-BUs, plateforme imagino).

---

## 0. Brief Geopost — checklist d'entrée

Avant d'ouvrir WPP, rassembler ces actifs. Sans eux les agents ne peuvent pas être conformes.

- [ ] **Brief Geopost** (présent dans `_brief/Brief_TemplatesRevampProject.pdf`).
- [ ] **HTML source Geopost corporate** (présent dans `design_system/_sources/`).
- [ ] **Exemples emails actuels (POC imagino)** — à demander à Geopost (au moins 4 emails :
      welcome, app, boost sales, peak commercial). Un exemple existant DPD France est fourni
      dans `_brief/sample_existing_dpd_email.html` à titre indicatif.
- [ ] **Brand guidelines officielles** par BU (BRT, DPD CH, DPD CZ, DPD SK, Geopost corporate).
- [ ] **Charte rédactionnelle** : tonalité, vocabulaire imposé, vocabulaire interdit, par langue.
- [ ] **Header officiel email** par BU = `<doctype>` + `<head>` + media queries + bloc `<section>`
      du header marque (à coller à l'identique dans le prompt 04 HTML Integration).
- [ ] **Liste des URLs officielles autorisées** : `geopost.com`, `brt.it`, `dpd.ch`, `dpd.cz`,
      `dpd.sk`, plus les URLs de campagne fournies par Geopost.
- [ ] **Documentation imagino** : variables propriétaires (`##VARIABLE##`, `{{ var }}`, etc.),
      contraintes routeur, formats acceptés.
- [ ] **Contraintes légales** récurrentes par pays (RGPD, mentions désinscription, adresse
      postale légale).

---

## 1. Variables à remplacer (Find & Replace global par agent)

Chaque system prompt utilise des placeholders entre crochets. Avant Publish, faire un
Find & Replace global sur le fichier prompt.

### Placeholders communs aux 8 agents

| Placeholder              | Valeur Geopost                                            |
|--------------------------|-----------------------------------------------------------|
| `[CLIENT]`               | Geopost                                                   |
| `[CLIENT_LOWER]`         | geopost                                                   |
| `[PROGRAMME]`            | Consumer Relation and Acquisition Program                 |
| `[LANGUE]`               | français                                                  |
| `[PLATEFORME_EMAIL]`     | imagino                                                   |
| `[URLS_OFFICIELLES]`     | geopost.com, brt.it, dpd.ch, dpd.cz, dpd.sk, dpd.fr       |
| `[LISTE_BU]`             | Geopost corporate / BRT (IT) / DPD CH / DPD CZ / DPD SK   |
| `[DATE_RFP]`             | 4 mai 2026                                                |
| `[DATE_DEADLINE]`        | 22 mai 2026                                               |
| `[DATE_KICKOFF]`         | semaine du 15 juin 2026                                   |

### Placeholders spécifiques aux sous-agents HTML (03, 04, 05)

| Placeholder              | Valeur cible (à confirmer Geopost)                        |
|--------------------------|-----------------------------------------------------------|
| `[BREAKPOINT]`           | 640 (px) — à valider sur templates POC                    |
| `[WRAPPER_DESKTOP]`      | 640                                                       |
| `[WRAPPER_MOBILE]`       | 360                                                       |
| `[WRAPPER_MOBILE_SUB]`   | 320                                                       |
| `[COLOR_PRIMARY]`        | `#dc0032` (rouge Geopost)                                 |
| `[COLOR_PRIMARY_DARK]`   | `#a90034`                                                 |
| `[COLOR_TEXT]`           | `#414042`                                                 |
| `[COLOR_BG]`             | `#ffffff`                                                 |
| `[FONT_STACK]`           | `Arial, Helvetica, sans-serif`                            |
| `[CLASSES_RESPONSIVE]`   | `[À CONFIRMER après réception templates POC imagino]`     |

### Placeholders spécifiques au Commercial RFP (07)

| Placeholder              | Valeur                                                    |
|--------------------------|-----------------------------------------------------------|
| `[NOM_AGENCE]`           | `[À COMPLÉTER AGENCE]`                                    |
| `[TRACK_RECORD]`         | `[À COMPLÉTER AGENCE]` (références clients similaires)    |
| `[EQUIPE_PITCH]`         | `[À COMPLÉTER AGENCE]` (CVs / rôles équipe pitch)         |
| `[GRILLE_TARIFS]`        | `[À COMPLÉTER AGENCE]`                                    |

---

## 2. Onglet **Profile** (commun aux 8 agents)

```
Name        : [voir tableau ci-dessous, un par agent]
Description : voir §2.1 par agent
Personality : (laisser vide)
Role        : Expert  ← TOUJOURS Expert
```

### Nom à donner à chaque agent dans WPP

| Fichier prompt                                 | Name WPP                      |
|------------------------------------------------|-------------------------------|
| `lead_crm/SYSTEM_PROMPT_lead_crm_geopost.md`   | Geopost Lead CRM V1           |
| `sub_agents/01_SYSTEM_PROMPT_audit.md`          | Geopost Audit V1              |
| `sub_agents/02_SYSTEM_PROMPT_cro_ux_writing.md` | Geopost CRO & UX Writing V1   |
| `sub_agents/03_SYSTEM_PROMPT_template_design.md`| Geopost Template Design V1    |
| `sub_agents/04_SYSTEM_PROMPT_html_integration.md`| Geopost HTML Integration V1  |
| `sub_agents/05_SYSTEM_PROMPT_modular_library.md`| Geopost Modular Library V1    |
| `sub_agents/06_SYSTEM_PROMPT_guidelines_multibrand.md`| Geopost Guidelines V1   |
| `sub_agents/07_SYSTEM_PROMPT_commercial_rfp.md` | Geopost Commercial RFP V1     |

### 2.2 Advanced settings (commun aux 8 agents)

| Paramètre    | Valeur            | Pourquoi                                          |
|--------------|-------------------|---------------------------------------------------|
| Model        | Gemini 3.1 Pro    | Meilleure qualité sur long contexte structuré     |
| Mode         | Medium            | Privilégie qualité sur vitesse                    |
| Seed         | 0                 | Reproductibilité entre runs                       |
| Temperature  | Predictable       | Pas de créativité, reproduction stricte           |
| Top P        | Focused           | Tokens haute confiance uniquement                 |
| Max Tokens   | Diverse           | Budget large pour livrables complets              |
| Top K        | Diverse           | Élargit les candidats avant filtrage              |

---

## 3. Onglet **Sources** (datasets par agent)

> ⚠️ **Architecture critique :** créer plusieurs datasets séparés (Context window pour les
> sources critiques, Automatic pour les sources volumineuses servant d'exemple).

### 3.1 Lead CRM Geopost

| Dataset                       | Type            | Contenu                                                  |
|-------------------------------|-----------------|----------------------------------------------------------|
| Brief Geopost                 | Context window  | `Brief_TemplatesRevampProject.pdf` + `.txt`              |
| Outputs sous-agents (cache)   | Automatic       | À alimenter au fur et à mesure des livraisons sous-agents|

### 3.2 Sous-agents — datasets par agent

| Agent                          | Dataset principal (Context window)                     | Dataset secondaire (Automatic)                |
|--------------------------------|--------------------------------------------------------|----------------------------------------------|
| 01 Audit                       | Emails POC actuels Geopost (HTML)                      | Brief + tokens extraits                       |
| 02 CRO & UX Writing            | Charte éditoriale Geopost + tonalité par BU            | Benchmark concurrents (si fourni)             |
| 03 Template Design             | `extracted_tokens.md` + design system Geopost          | Templates POC actuels (RAG)                   |
| 04 HTML Integration            | Librairie modulaire Geopost (output de l'agent 05)     | Templates index POC (RAG) + doc imagino       |
| 05 Modular Library             | Spec design (output agent 03) + audit (output 01)      | Librairie Kia (`_references_kia/`) en référence|
| 06 Guidelines & Multi-Brand    | Brand books 5 BUs + contraintes légales par pays       | Brief + audit                                 |
| 07 Commercial RFP              | Brief Geopost + track record agence                    | Réponses AO historiques agence                |

---

## 4. Onglet **Instructions**

### 4.1 Tools (panneau de droite)

| Toggle                | État | Pourquoi                                                            |
|-----------------------|------|---------------------------------------------------------------------|
| Web search            | Off  | Seules les URLs `[URLS_OFFICIELLES]` sont autorisées (citées prompt)|
| Web scrape            | Off  | idem                                                                |
| Web search & scrape   | Off  | idem                                                                |
| YouTube analyser      | Off  | Pas pertinent                                                       |
| GPT Code Interpreter  | Off  | Le HTML email s'écrit, ne s'exécute pas                             |
| Gemini Code Interpreter| Off | idem                                                                |
| GitHub Subscriptions  | Off  | Hors périmètre                                                      |
| Signal AI             | Off  | Hors périmètre                                                      |
| Predict HQ            | Off  | Hors périmètre                                                      |

### 4.2 Settings

| Setting               | État | Pourquoi                                                            |
|-----------------------|------|---------------------------------------------------------------------|
| Artifact generation   | Off  | Sortie en Markdown ou HTML brut copiable                            |
| Agent team            | Off  | Chaque agent fonctionne en mono-agent. **L'orchestration humaine    |
|                       |      | (ou Lead CRM) appelle les sous-agents séquentiellement.**           |

> **Note importante.** WPP ne permet pas (à date) une orchestration multi-agents automatique
> robuste. Le « Lead CRM » est donc soit un humain qui dispatche manuellement les briefs aux
> sous-agents WPP, soit un agent WPP unique qui produit le cadrage et indique à l'utilisateur
> quel sous-agent solliciter ensuite. La V1 retient le mode **humain dispatcheur** pour la
> fiabilité.

### 4.3 Conversation starters

`Off` — l'utilisateur cible (chef de projet expérimenté) sait formuler ses demandes.

### 4.4 Required information

`Off` — chaque agent accepte indifféremment image / PDF / texte / HTML brut.

### 4.5 Steps

**No steps.** Toute la logique est dans le system prompt en un seul shot.

### 4.6 System prompt

Coller le bloc `MISSION ... OBJECTIF FINAL` du fichier prompt correspondant, après
Find & Replace des placeholders.

---

## 5. Onglet **Learning** (commun aux 8 agents)

| Paramètre      | État au lancement | Quand activer                                |
|----------------|-------------------|----------------------------------------------|
| Learning mode  | Off               | Après 2-3 semaines d'usage stable            |
| User feedback  | Off               | Après validation par l'équipe créa           |
| Guardrails     | 0                 | Si exigences brand safety spécifiques        |
| User memories  | (auto)            | Se construisent à l'usage                    |

---

## 6. Tests d'acceptance par agent (à passer avant Publish)

### 6.1 Lead CRM Geopost
1. **Audit.** Input : « audit complet 4 emails POC fournis ». Output attendu : cadrage 5 puces
   + dispatch vers Audit Agent + CRO Agent, avec briefs structurés (Goal/Inputs/Constraints/
   Deliverable/Owner).
2. **Strat.** Input : « stratégie modularité multi-BU ». Output : recommandation stratégique
   + dispatch vers Modular Library + Guidelines.
3. **Production template.** Input : « conçois welcome BRT + DPD CH ». Output : cascade
   dispatch design → library → integration → guidelines.
4. **Commercial.** Input : « rédige la réponse AO ». Output : dispatch vers Commercial RFP
   uniquement.
5. **Pas de HTML auto-produit.** Vérifier que le Lead CRM **ne produit jamais de HTML**
   directement (renvoie systématiquement vers HTML Integration ou Template Design).

### 6.2 Audit Agent (01)
1. Output structuré en grille (Structure HTML / Compat Outlook / a11y WCAG AA / Design system
   / UX writing / Cohérence multi-brand).
2. Écarts numérotés avec priorité P0/P1/P2.
3. Pas de HTML inventé.

### 6.3 CRO & UX Writing Agent (02)
1. Variantes A/B produites avec rationale.
2. Aucun mot interdit (lyrisme, superlatifs vides).
3. Respect de la longueur objet/préheader (max 50/110 caractères).

### 6.4 Template Design Agent (03)
1. Spec bloc-par-bloc (jamais d'HTML, jamais d'image générée).
2. Variantes mobile/desktop/dark mode explicites.
3. Brand variants pour les 5 BUs listées.

### 6.5 HTML Integration Agent (04)
1. HTML email tables imbriquées, Outlook 2016+ compatible.
2. WCAG AA respecté (alts descriptifs, contrastes ≥ 4.5:1).
3. Zéro classe inventée hors librairie modulaire.
4. Variables imagino conservées intactes si présentes.

### 6.6 Modular Library Agent (05)
1. Librairie de blocs documentée bloc-par-bloc.
2. Nomenclature classes cohérente, namespace `gp-` ou équivalent.
3. Doc d'assemblage : comment combiner les blocs pour produire un template.

### 6.7 Guidelines & Multi-Brand Agent (06)
1. Règles par BU (5 marques) explicitées.
2. Règles par pays (langue, devise, mentions légales) explicitées.
3. QA checklist pré-envoi.

### 6.8 Commercial RFP Agent (07)
1. Structure de réponse complète (exec summary, méthodologie, équipe, planning, budget,
   deliverables, track record, milestones, risques).
2. Aucune référence client inventée — blocs `[À COMPLÉTER AGENCE]` clairs.
3. Planning aligné sur le calendrier brief Geopost (deadline 22 mai, kick-off 15 juin 2026).

---

## 7. Versionning et maintenance

| Action                                    | Quand                              | Qui                |
|-------------------------------------------|------------------------------------|--------------------|
| Bump version (V1 → V2) dans Name          | À chaque modif majeure du prompt   | Créa lead          |
| Update du dataset Librairie modulaire     | Quand la base de blocs Geopost évolue | Dev référent    |
| Update du dataset Brand guidelines        | À chaque nouvelle BU intégrée      | Créa lead          |
| Audit memories Learning                   | Trimestriel                        | Project owner      |
| Re-test des tests d'acceptance par agent  | Après chaque update                | Créa lead          |

---

## 8. Différences vs. `kia Dev V4`

| Aspect                  | kia Dev V4                       | Geopost CRM Agents                                |
|-------------------------|----------------------------------|---------------------------------------------------|
| Architecture            | Mono-agent                       | Lead CRM + 7 sous-agents                          |
| Périmètre               | Production HTML email            | Audit, strat, design, prod, guidelines, commercial|
| Plateforme cible        | Actito                           | imagino                                           |
| BUs                     | 1 (Kia FR)                       | 5+ (Geopost corp + BRT + DPD CH/CZ/SK + autres)   |
| Tonalité éditoriale     | 1 charte (Kia FR)                | N chartes (1 par BU × langue)                     |
| Liste produits + genres | Critique (modèles auto)          | Non applicable (livraison de colis = services)    |
| Librairie modulaire     | Existante (`librairie_kia/`)     | À produire (output sous-agent 05)                 |
| Sortie principale       | HTML brut                        | Markdown structuré (Lead CRM) + HTML (agent 04)   |

---

*Playbook v1 — généré le 11 mai 2026. Calque dérivé de `kia Dev V4`.*
