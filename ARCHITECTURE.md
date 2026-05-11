# Architecture — Lead CRM Geopost + sous-agents

## Vue d'ensemble

```
                        ┌──────────────────────────────┐
                        │   Lead CRM Geopost           │
                        │   (orchestrateur)            │
                        │                              │
                        │  • Audit CRM                 │
                        │  • Strat / cadrage           │
   demande utilisateur ─→  • Dispatch sous-agents      │
                        │  • Consolidation livrables   │
                        └──────────────┬───────────────┘
                                       │ brief structuré
                                       │ (Goal / Inputs / Constraints / Deliverable / Owner)
              ┌────────────────┬───────┴───────┬────────────────┬────────────────┬─────────────────┬─────────────────┐
              ▼                ▼               ▼                ▼                ▼                 ▼                 ▼
        ┌──────────┐    ┌──────────────┐  ┌───────────┐   ┌───────────────┐  ┌──────────────┐  ┌──────────────┐  ┌───────────┐
        │ 01 Audit │    │ 02 CRO & UX  │  │ 03 Template│  │ 04 HTML       │  │ 05 Modular   │  │ 06 Guidelines│  │ 07 Comm. │
        │  Agent   │    │  Writing     │  │   Design   │  │ Integration   │  │  Library     │  │  Multi-Brand │  │   RFP    │
        └──────────┘    └──────────────┘  └───────────┘   └───────────────┘  └──────────────┘  └──────────────┘  └───────────┘
```

---

## Logique d'orchestration

Le Lead CRM lit chaque demande entrante, la **qualifie** (audit ? strat ? prod ? commercial ?),
produit un **cadrage** en 5 puces max, puis dispatche vers le ou les sous-agents pertinents
avec un **brief structuré** :

```
Goal         : un objectif unique mesurable
Inputs       : sources, fichiers, contraintes connues
Constraints  : contraintes techniques / brand / légales
Deliverable  : format de sortie attendu
Owner        : sous-agent désigné
```

Le Lead CRM **ne produit jamais de HTML** ni de design lui-même. Il renvoie systématiquement
vers le sous-agent compétent. À la réception des outputs sous-agents, il **consolide** en un
livrable cohérent.

---

## Mapping scope brief Geopost → sous-agent

| Section brief Geopost                              | Sous-agent responsable                          |
|----------------------------------------------------|------------------------------------------------|
| §2 Key issues — layouts, a11y, UX writing          | 01 Audit + 02 CRO & UX Writing                 |
| §2 Key issues — limitations Outlook                | 01 Audit + 04 HTML Integration                 |
| §2 Key issues — variations visuelles               | 01 Audit + 06 Guidelines & Multi-Brand         |
| §2 Key issues — guidelines limitées                | 06 Guidelines & Multi-Brand                    |
| §2 Key issues — scalabilité multi-pays/brand       | 05 Modular Library + 06 Guidelines             |
| §3 Objectives — templates flexibles                | 03 Template Design + 05 Modular Library        |
| §3 Objectives — modular approach                   | 05 Modular Library                             |
| §3 Objectives — readability/a11y                   | 01 Audit + 04 HTML Integration                 |
| §3 Objectives — brand consistency                  | 06 Guidelines & Multi-Brand                    |
| §3 Objectives — performance (engagement, CTR)      | 02 CRO & UX Writing                            |
| §4.A Audit & Recommendations                       | 01 Audit + 02 CRO & UX Writing                 |
| §4.B Template Creation (3 triggers + 3 one-shot)   | 03 Template Design                             |
| §4.C HTML Integration                              | 04 HTML Integration                            |
| §4.C Modular content block library                 | 05 Modular Library                             |
| §5 Deliverables — Audit doc                        | 01 Audit                                       |
| §5 Deliverables — Email guidelines                 | 06 Guidelines & Multi-Brand                    |
| §5 Deliverables — Designed templates               | 03 Template Design                             |
| §5 Deliverables — Integrated HTML files            | 04 HTML Integration                            |
| §6 Budget & Planning                               | 07 Commercial RFP                              |

Chaque puce du brief est couverte par **au moins 1 sous-agent**.

---

## Table des sous-agents

| ID  | Nom                        | Rôle                                                                        | Output principal                                       |
|-----|-----------------------------|-----------------------------------------------------------------------------|--------------------------------------------------------|
| 01  | Audit Agent                 | Diagnostic HTML + design + a11y + UX writing + multi-brand                  | Grille d'audit numérotée + écarts + priorités P0/P1/P2 |
| 02  | CRO & UX Writing Agent      | Recos éditoriales, micro-copy, hiérarchie info, variantes A/B               | Recos rédactionnelles + variantes copy                 |
| 03  | Template Design Agent       | Spec design des 6 templates (3 triggers + 3 one-shot) — wireframes textuels | Spec design bloc-par-bloc, mobile/desktop/dark mode    |
| 04  | HTML Integration Agent      | Production HTML email Outlook 2016+ / a11y / imagino                        | HTML email production-ready                            |
| 05  | Modular Library Agent       | Conception librairie de blocs réutilisables                                 | Librairie HTML + nomenclature + doc d'assemblage       |
| 06  | Guidelines & Multi-Brand    | Formalisation guidelines CRM/email, règles 5 marques × N pays               | Email guidelines doc + QA checklist                    |
| 07  | Commercial RFP Agent        | Structure réponse AO Geopost                                                | Réponse AO structurée (exec summary, planning, budget) |

---

## Règles transverses

- **Langue par défaut** : français (cohérent avec usage interne agence et brief). Anglais sur
  demande explicite.
- **Sources externes** : interdites sauf URLs Geopost officielles (`geopost.com`, et URLs BU :
  `dpd.fr`, `dpd.ch`, `dpd.cz`, `dpd.sk`, `brt.it`, etc.). Aucun web search.
- **Outputs** : Markdown structuré par défaut, sauf §3 du prompt sous-agent qui spécifie un
  format dur (HTML pour 04, doc structurée pour 01, etc.).
- **Pas d'hallucination chiffrée** : si une donnée client manque (KPIs, références agence,
  pricing), signaler `[À COMPLÉTER AGENCE]` ou `[À CONFIRMER GEOPOST]` en clair.
- **Héritage Kia** : les sous-agents HTML (03, 04, 05) reprennent strictement la grammaire du
  prompt Kia (§4 reprise stricte librairie, §5 responsive, §6 contraintes email, §7 CTA, §9
  images/ALT, §10 footer). Les sous-agents non-HTML (01, 02, 06, 07) gardent l'ossature 17
  sections mais remplacent §4-§12 par leur propre cœur métier.

---

## Flux d'entrée / sortie typique

### Cas 1 — Audit complet

```
User : « Audit complet des 4 emails POC fournis »
  ↓
Lead CRM : qualifie « Audit CRM », dispatche → Audit Agent (01) + CRO Agent (02)
  ↓
01 : produit grille d'audit numérotée (HTML + design + a11y)
02 : produit recos UX writing + variantes copy
  ↓
Lead CRM : consolide en 1 document Markdown :
  • exec summary (5 puces)
  • grille d'audit fusionnée
  • plan d'action P0/P1/P2
  • next steps
```

### Cas 2 — Création template welcome multi-brand

```
User : « Conçois le template welcome pour BRT et DPD CH »
  ↓
Lead CRM : qualifie « Production template », dispatche en cascade :
  → Template Design Agent (03)  : spec design wireframée
  → Modular Library Agent (05)  : identifie blocs réutilisables
  → HTML Integration Agent (04) : intègre en HTML email
  → Guidelines Agent (06)       : valide cohérence brand par BU
  ↓
Lead CRM : retourne 1 livrable structuré + HTML × 2 BUs
```

### Cas 3 — Réponse AO

```
User : « Rédige la réponse AO Geopost »
  ↓
Lead CRM : qualifie « Commercial RFP », dispatche → Commercial RFP Agent (07)
  ↓
07 : produit la structure réponse (exec summary, méthodo, équipe, planning, budget)
     avec blocs [À COMPLÉTER AGENCE] sur les références clients / tarifs
  ↓
Lead CRM : retourne la trame, signale les blocs à compléter
```
