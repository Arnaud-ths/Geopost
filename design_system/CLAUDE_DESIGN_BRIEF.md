# Brief — Génération du design system email Geopost

> **Destinataire :** Claude Design (ou tout LLM design-aware capable de raisonner tokens +
> composants).
> **Mode d'emploi :** copier ce brief dans le chat, joindre le fichier source
> `geopost_corporate_homepage.html` (présent dans `design_system/_sources/`). Lancer.
> **Output attendu :** 4 fichiers générés (cf. §10).
> **Durée estimée :** 1 shot suffit pour le design system de base. Itérations possibles
> composant par composant (cf. §12).

---

## 1. Contexte

Le client **Geopost** (leader mondial livraison de colis et solutions e-commerce, +50 pays,
5 continents) lance le projet **Templates Revamp Project** dans le cadre de son Consumer
Relation and Acquisition Program.

Périmètre :
- 5 business units : **Geopost corporate, BRT (Italie), DPD CH (Suisse), DPD CZ (République
  tchèque), DPD SK (Slovaquie)** — autres BUs à venir.
- Plateforme d'envoi : **imagino** (Customer Data Platform).
- Kick-off : semaine du 15 juin 2026.
- 6 templates à produire à terme : 3 triggers (welcome, mobile app push, boost sales) + 3
  one-shot (commercial peak, services, Singular).

Mission de Claude Design : produire le **design system email Geopost**, en partant exclusivement
du HTML corporate `geopost.com/fr/entreprise/` (fourni en pièce jointe) et de ce brief.

---

## 2. Sources autorisées

**EXCLUSIVEMENT :**
1. Le fichier `geopost_corporate_homepage.html` joint à ce chat.
2. Les tokens chiffrés listés dans la section §4 ci-dessous (point de départ extrait du HTML).
3. Le contenu du présent brief.

**INTERDIT :**
- Web search, web scrape, fetch d'URL.
- Knowledge prior sur Geopost / DPD / BRT en dehors du HTML fourni.
- Inventer une couleur, une typographie, un logo absent du HTML.
- Proposer un framework email (MJML, Foundation, etc.) — l'intégration cible est HTML pur.

---

## 3. Mission précise

Produire un **design system email complet et cohérent**, structuré en 4 livrables (cf. §10),
couvrant :

- les **tokens** (couleurs, typographie, espacements, border-radius)
- les **composants email** (blocs réutilisables, anatomie, slots, variantes)
- les **templates dérivés** (mapping 1-pour-1 avec les 6 templates du scope brief)
- l'**adaptabilité multi-marque** (5 BUs)
- l'**accessibilité** WCAG AA non négociable
- les **contraintes email** (Outlook 2016+, tables imbriquées, styles inline, pas de JS)

---

## 4. Tokens de départ (extraits du HTML source)

### 4.1 Couleurs (occurrences dans le HTML)

| Hex        | Occurrences | Rôle observé                                |
|------------|-------------|---------------------------------------------|
| `#dc0032`  | 15          | **Rouge primaire Geopost** — CTA, accents   |
| `#a90034`  | 2           | Rouge sombre — hover/active                 |
| `#414042`  | 20          | Gris foncé — texte body                     |
| `#808285`  | 1           | Gris moyen — texte secondaire               |
| `#7e8993`  | 1           | Gris bleuté — texte tertiaire               |
| `#abb8c3`  | 1           | Gris clair — séparateurs, bordures          |
| `#ffffff`  | 13          | Blanc — fond                                |
| `#000000`  | 1           | Noir — exceptions ponctuelles               |

Couleurs résiduelles WordPress (à exclure) : `#1787bf, #ff6900, #ff253a, #fcb900, #f78da7,
#cf2e2e, #9b51e0, #8ed1fc, #7bdcb5, #0693e3, #00d084, #32373c`.

### 4.2 Typographie

- Polices natives site : **PlutoSansMedium** (titres), **PlutoSansRegular** (body).
- **Non web-safe** → fallback `Arial, Helvetica, sans-serif` OBLIGATOIRE pour email.
- Échelle observée :
  - **30px / weight 700 / line-height 1.23** — H1/H2 (en UPPERCASE sur le site)
  - **18px / weight 400 / line-height 27px** (~1.5) — body
  - **11px** — legal / fine print

### 4.3 Casse

- Titres en `UPPERCASE`
- Body en casse normale

---

## 5. Spec attendue — TOKENS À FORMALISER

### 5.1 Palette couleur (à compléter par toi)

Tu pars de §4.1 et tu produis une palette accessible WCAG AA structurée en :

- **Primary** : `#dc0032` (rouge Geopost) — proposer 1 nuance hover/active (`#a90034`).
- **Neutrals** : échelle de 5-6 greys cohérents (depuis `#414042` jusqu'au `#abb8c3`,
  combler les paliers manquants en respectant un step perceptuel régulier).
- **Semantic** (`success`, `warning`, `error`, `info`) — à proposer, en cohérence visuelle
  avec la palette, accessibles WCAG AA sur fond `#ffffff` et fond sombre dark mode.
- **Backgrounds** : light (`#ffffff`) + dark (proposer une valeur, ex. `#1a1a1a`).
- **Borders / dividers** : 1-2 valeurs.

Pour chaque couleur, vérifie le contraste WCAG AA contre le texte body et signale les paires
qui passent / échouent.

### 5.2 Typographie

- Stack final : `'PlutoSans', Arial, Helvetica, sans-serif` (avec note sur le chargement
  progressif Pluto Sans via `@font-face` — n'est rendu QUE sur Apple Mail / iOS Mail).
- Échelle email-safe (multiples utilisés en HTML email) :
  `12 / 14 / 16 / 18 / 24 / 30 / 36 px`.
- Poids : `400 / 500 / 700`.
- Line-heights : `1.2` (titres) / `1.5` (body) / `1.4` (intermédiaire).
- Tu mappes ces valeurs aux usages : H1, H2, H3, body, body small, legal, CTA label.

### 5.3 Espacements

- Système 4/8 : `4 / 8 / 12 / 16 / 24 / 32 / 48 / 64 px`.
- Tu mappes ces valeurs aux usages : padding bloc body, padding hero, padding CTA,
  marge entre blocs (NOTE : pas de margin entre tables en email — gérer par padding interne
  du bloc suivant).

### 5.4 Border-radius

- `0 / 4 / 8 / 9999` (rectangulaire / arrondi léger / arrondi prononcé / pill).
- Recommandation par défaut pour CTA Geopost : `0` (rectangulaire, conforme au site corporate
  observé).

### 5.5 Ombres

- **Pas d'ombre CSS3 en HTML email** (non supportée Outlook). Tu remplaces toute idée d'ombre
  par de l'espacement ou une bordure 1px.

---

## 6. Spec attendue — COMPOSANTS EMAIL

Tu produis l'anatomie de chacun des composants suivants, avec :
- description (à quoi sert le bloc)
- structure (HTML logique, pas le code de production)
- slots paramétrables (texte, image, lien, BU)
- variantes (par device, par dark mode, par BU)
- règles a11y (alts, role, contraste)
- exemple de code HTML email (table imbriquée + styles inline + classe responsive)

Liste des composants à spécifier :

1. **Header** — logo BU + lien "Voir la version en ligne" + (option) nav simple.
2. **Hero** — image full-width + titre + sous-titre + CTA primaire.
3. **Body text block** — H2 + paragraphe + CTA secondaire (optionnel).
4. **Body image + text** — image 1-col mobile, 2-col desktop (variante image gauche/droite).
5. **Cards grid** — 2 ou 3 cards (image + titre + lien).
6. **Promotional block** — visuel + label offre + CTA + mention "valable jusqu'au...".
7. **Services block** — grille 3 services (picto + label + lien).
8. **Social proof / KPI block** — 3 chiffres clés ou 3 logos clients ou témoignage court.
9. **CTA standalone** — primary (fond `#dc0032`) + secondary (contour `#dc0032`).
10. **Divider** — ligne séparatrice 1px.
11. **Footer** — mentions légales pays-spécifiques + désinscription + adresse + (option)
    réseaux sociaux.

Pour chaque composant, tu indiques :
- Dimensions desktop (wrapper 640px) et mobile (100% jusqu'à 360px).
- Variantes obligatoires : mobile (stack vertical), dark mode.
- Variantes optionnelles : par BU (logo, couleur si différente).

---

## 7. Templates à dériver (mapping scope brief)

Tu démontres l'usage des composants en assemblant 6 templates type :

| Template            | Composants assemblés (de haut en bas)                                  |
|---------------------|-------------------------------------------------------------------------|
| **welcome**         | header + hero + body text + services + CTA + footer                    |
| **mobile app push** | header + hero (mockup app) + body text (3 bénéfices) + double CTA (iOS+Android) + footer |
| **boost sales**     | header + hero + body text + social proof (3 KPIs) + CTA + footer       |
| **commercial peak** | header + hero (visuel saisonnier) + promotional block + CTA + footer   |
| **services**        | header + hero (carte) + body text + cards grid (3 étapes) + CTA + footer |
| **Singular**        | header + hero (mockup plateforme) + body text + social proof + double CTA + footer |

Tu ne produis PAS le HTML complet de chaque template — tu produis la séquence de composants
et les slots à remplir.

---

## 8. Adaptabilité multi-marque

Tu décris la stratégie de variation par BU, en t'appuyant sur la librairie modulaire :

- **Tokens marque-spécifiques injectables sur la même librairie de blocs** : logo (URL/path),
  primary color override (si la BU a une couleur différente de `#dc0032`), font (si la BU a
  une font différente de Pluto Sans).
- **Mode sombre (dark mode)** : règles de swap couleur (bg light → bg dark, texte foncé →
  texte clair) + contour CTA blanc 1px.

Tu ne crées PAS de variantes pour les 5 BUs spécifiquement (tu n'as pas les brand books). Tu
proposes le PATTERN d'injection (« comment varianter »).

---

## 9. Accessibilité — WCAG AA non négociable

- Contrastes ≥ 4.5:1 sur texte body, ≥ 3:1 sur texte large (≥18px ou ≥14px gras) et graphique
  fonctionnel (CTA fond).
- Alts descriptifs sur images porteuses de sens (≤80 caractères, sans ponctuation finale).
- `alt=""` sur images décoratives et pixel tracking (jamais omis).
- `role="presentation"` sur toutes les `<table>` de mise en page.
- `lang` attribut sur `<html>` (langue de l'email).
- Pas d'information transmise UNIQUEMENT par la couleur.
- Ordre de lecture cohérent (top-down).
- CTA label explicite (jamais "Cliquez ici" seul).

Pour chaque token couleur que tu proposes, tu vérifies les contrastes et tu signales les
combinaisons qui passent / échouent. Tu produis un livrable `accessibility-checklist.md`
documentant tout (cf. §10).

---

## 10. Format de sortie attendu

4 fichiers structurés :

### 10.1 `design-tokens.json`

Structure équivalente Style Dictionary, exemple de schéma :

```json
{
  "color": {
    "primary": { "value": "#dc0032", "type": "color" },
    "primary-dark": { "value": "#a90034", "type": "color" },
    "neutral-900": { "value": "#414042", "type": "color" },
    "neutral-600": { "value": "#808285", "type": "color" },
    "neutral-400": { "value": "#abb8c3", "type": "color" },
    "neutral-0": { "value": "#ffffff", "type": "color" },
    "semantic-success": { "value": "...", "type": "color" },
    "semantic-error": { "value": "...", "type": "color" }
  },
  "font": {
    "family-primary": { "value": "'PlutoSans', Arial, Helvetica, sans-serif", "type": "fontFamily" },
    "size-h1": { "value": "30px", "type": "fontSize" },
    "size-body": { "value": "18px", "type": "fontSize" },
    "weight-bold": { "value": "700", "type": "fontWeight" },
    "line-height-tight": { "value": "1.2", "type": "lineHeight" }
  },
  "spacing": {
    "xs": { "value": "4px" },
    "sm": { "value": "8px" },
    "md": { "value": "16px" },
    "lg": { "value": "32px" }
  }
}
```

### 10.2 `design-system.md`

Spec lisible humaine, organisée en :
1. Tokens (couleurs, typo, espacements, border-radius) — descriptions + valeurs + exemples.
2. Composants (les 11 composants §6) — pour chacun : anatomie + slots + variantes + code HTML email exemple.
3. Templates dérivés (les 6 §7) — séquence de composants par template.
4. Adaptabilité multi-brand — pattern d'injection.

### 10.3 `component-anatomy.md`

Anatomie détaillée de chaque composant :
- structure (arborescence HTML logique)
- slots (variables à remplir)
- états (default, hover, dark mode)
- variantes (par device, par BU)

### 10.4 `accessibility-checklist.md`

Check-list WCAG AA exhaustive :
- vérification contraste sur toutes les paires couleur du design system
- règles alt par type d'image
- règles sémantique tables
- règles dark mode
- règles ordre de lecture
- liste des contrôles à effectuer avant envoi

---

## 11. Interdictions

- ❌ Inventer une couleur / typo / logo absent du HTML source ou de ce brief.
- ❌ Supposer une charte non fournie.
- ❌ Proposer un framework email (MJML, Foundation for Emails, Stripo, Litmus Builder, etc.).
- ❌ Utiliser `box-shadow`, `text-shadow`, `transform`, `transition`, gradient CSS3.
- ❌ Utiliser des unités `rem`, `em`, `%` (sauf si pertinent, ex. `width: 100%` mobile).
- ❌ Proposer SVG inline (support Outlook insuffisant).
- ❌ Proposer JS, Web Components, custom elements.
- ❌ Inventer une BU autre que les 5 listées.
- ❌ Inventer des chiffres KPI pour les blocs social proof (laisser `{{ SLOT }}` vide).

---

## 12. Instructions de prompt itératif

Après la livraison du design system v1.0, l'opérateur peut relancer Claude Design pour des
modifications ciblées sans tout régénérer :

- **Zoom sur 1 composant** : « Donne-moi la spec détaillée du composant `Promotional block`
  avec 3 variantes layout. » → Claude Design produit uniquement la fiche composant, pas le
  reste du DS.
- **Ajout d'un nouveau composant** : « Ajoute le composant `tracking-status` (suivi colis
  avec étapes numérotées). » → Claude Design produit la fiche du nouveau composant + l'ajoute
  à l'index.
- **Variante BU spécifique** : « Décline le header pour la BU BRT avec logo brt et primary
  color `#xxxxxx`. » → Claude Design produit la variante uniquement (en s'appuyant sur le
  pattern §8).
- **Audit d'un design existant** : « Audite ce HTML (joint) contre le design system v1.0. »
  → Claude Design produit un tableau d'écarts numérotés.

---

## 13. Conclusion attendue de la livraison

Une fois les 4 fichiers livrés, l'opérateur peut :

1. Passer `design-tokens.json` à un développeur pour intégration Style Dictionary / variables CSS.
2. Passer `design-system.md` aux agents WPP `04 HTML Integration` et `05 Modular Library`
   comme source de référence pour la production HTML email.
3. Passer `component-anatomy.md` à l'agent `03 Template Design` pour produire les wireframes
   des 6 templates.
4. Passer `accessibility-checklist.md` à l'agent `06 Guidelines & Multi-Brand` pour
   intégration dans la check-list QA pré-envoi.
