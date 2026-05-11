# Brief — Génération du deck de pitch AO Geopost (PPT)

> **Destinataire :** Claude Design (ou tout LLM design-aware capable de produire une
> présentation structurée et un rendu visuel cohérent).
> **Mode d'emploi :** copier ce brief dans Claude Design, joindre en pièces jointes :
>   1. `geopost_corporate_homepage.html` (`design_system/_sources/`) — pour les tokens.
>   2. `Brief_TemplatesRevampProject.pdf` (`_brief/`) — pour la compréhension du périmètre.
>   3. (Optionnel) la sortie consolidée de l'agent WPP **Geopost Commercial RFP V1**
>      (`07_SYSTEM_PROMPT_commercial_rfp.md`) — pour le contenu rédactionnel.
> **Output attendu :** un deck de pitch en 15-20 slides, livré en 3 formats (cf. §11).
> **Cible de présentation :** comité décisionnel Geopost, semaine du 1er juin 2026 (shortlist
> agences). Format probable : présentation 30 minutes (20 min pitch + 10 min Q&R).

---

## 1. Contexte

L'agence répond à l'AO **Templates Revamp Project** de Geopost (Consumer Relation and
Acquisition Program). Calendrier clé :

- RFP launch : **4 mai 2026**
- Proposal submission deadline : **22 mai 2026**
- Shortlist : 28 mai 2026
- **Pitch presentations : semaine du 1er juin 2026** ← ce deck
- Notification : 5 juin 2026
- Kick-off : semaine du 15 juin 2026

Le deck a pour objectif de :
- démontrer la **compréhension fine du besoin Geopost**
- présenter une **approche méthodologique structurée et différenciante**
- prouver la **légitimité de l'agence** (track record, équipe)
- convaincre par la **clarté visuelle et la rigueur** (le client vend de la logistique
  rigoureuse — la présentation doit refléter cette même rigueur)

Mission de Claude Design : produire le deck complet en respectant la **brand voice Geopost**
(professionnel, factuel, fiable, accessible) et en s'appuyant sur les **tokens design Geopost**
(rouge `#dc0032`, gris `#414042`, Pluto Sans / Arial fallback, UPPERCASE titres).

---

## 2. Sources autorisées

**EXCLUSIVEMENT :**
1. Le fichier `geopost_corporate_homepage.html` joint (tokens design).
2. Le fichier `Brief_TemplatesRevampProject.pdf` joint (périmètre client).
3. (Optionnel) le contenu rédactionnel produit par l'agent WPP `Geopost Commercial RFP V1`.
4. Le contenu du présent brief.

**INTERDIT :**
- Web search, web scrape.
- Inventer une référence client, un KPI, un nom de partenaire, une certification.
- Inventer un visuel photographique Geopost — utiliser des placeholders ou des
  abstractions géométriques aux couleurs brand.
- Utiliser des photos stock non libres de droit.
- Inventer des prix / jours-hommes / durées de mission précises.

---

## 3. Tokens brand Geopost à appliquer dans le deck

### 3.1 Couleurs

| Token            | Hex        | Usage dans le deck                                |
|------------------|------------|---------------------------------------------------|
| `primary`        | `#dc0032`  | Accents, titres clés, CTA, lignes de progression  |
| `primary-dark`   | `#a90034`  | Hover/active états interactifs (cliquables PDF)   |
| `text-primary`   | `#414042`  | Texte body, sous-titres                           |
| `text-muted`     | `#808285`  | Métas, footnotes, page numbers                    |
| `divider`        | `#abb8c3`  | Séparateurs, bordures discrètes                   |
| `bg`             | `#ffffff`  | Fond principal des slides                         |
| `bg-accent`      | `#dc0032`  | Fond des slides de transition (sur lesquelles le titre est en blanc) |

### 3.2 Typographie

- Stack : **Pluto Sans** (titres) + **Arial** (body, fallback universel).
- Si Pluto Sans indisponible dans l'outil de production → utiliser **Arial Bold** pour les
  titres et **Arial Regular** pour le body. Pas de Comic Sans, pas de Calibri, pas de
  Times. Cohérence brand stricte.

### 3.3 Échelle typographique deck

| Usage             | Taille | Poids | Casse        |
|-------------------|--------|-------|--------------|
| Titre slide       | 36-40pt| 700   | UPPERCASE    |
| Sous-titre slide  | 20-24pt| 700   | UPPERCASE    |
| Body              | 14-18pt| 400   | normale      |
| Footnote / page # | 9-10pt | 400   | normale      |

### 3.4 Grille et composition

- Format slide : **16:9** (1920×1080 px).
- Grille : 12 colonnes, marges latérales 80px, marge top/bottom 60px.
- Espacement vertical entre éléments : multiples de 8 (8 / 16 / 24 / 32 / 48 / 64 / 80 px).
- 1 idée par slide. Si une slide contient plus de 3 niveaux d'information → la fractionner.

---

## 4. Mission précise

Produire un deck de **15 à 20 slides** structuré, visuellement cohérent, brand-fidèle, qui :

1. capte l'attention en 30 secondes (slide 1 + slide 2)
2. démontre la compréhension du brief (slides 3-5)
3. présente l'approche méthodologique en 3 phases (slides 6-12)
4. présente l'équipe et le track record (slides 13-15)
5. présente le planning et le budget de manière synthétique (slides 16-17)
6. ferme sur un appel à l'action clair (slides 18-19, + slide de conclusion)

---

## 5. Structure obligatoire du deck

### Slide 1 — Couverture
- Fond `#ffffff`.
- Logo agence (placeholder `[LOGO AGENCE]`) en haut à gauche.
- Titre central UPPERCASE : « Templates Revamp Project ».
- Sous-titre : « Réponse à l'appel d'offres — Geopost — Mai 2026 ».
- Bandeau bas `#dc0032` 8px d'épaisseur.

### Slide 2 — Pourquoi nous ? (3 raisons)
- Fond `#ffffff`.
- 3 colonnes égales avec icônes simples (placeholders géométriques).
- Chaque colonne : 1 chiffre clé en `#dc0032` + 1 phrase courte en `#414042`.
- Pas plus de 12 mots par colonne.

### Slide 3 — Compréhension du contexte Geopost
- Fond `#ffffff`.
- Rappel synthétique du brief : 5 BUs, programme CRM, plateforme imagino, phase POC → roll-out.
- Frise horizontale des 5 BUs : Geopost corporate / BRT / DPD CH / DPD CZ / DPD SK
  (logos en placeholders + nom dessous).

### Slide 4 — Les 5 issues identifiées
- Fond `#ffffff`.
- Grille 2×3 (5 issues + 1 case vide ou case « + autres écarts ») :
  1. Templates à optimiser (layouts, a11y, UX writing)
  2. HTML fragile sur Outlook anciens
  3. Variations visuelles cross-emails
  4. Guidelines CRM/email limitées
  5. Adaptation manuelle lourde multi-pays/marque
- Chaque case : titre court UPPERCASE en `#dc0032` + 1 phrase de constat en `#414042`.

### Slide 5 — Notre lecture des objectifs
- Fond `#ffffff`.
- Citation extraite du brief en grande typo (`24pt`, italique léger ou guillemets stylés).
- Sous la citation : 4 puces synthétiques sur la lecture de l'agence.

### Slide 6 — Vue d'ensemble de l'approche (3 phases)
- Fond `#dc0032`, texte en `#ffffff` — slide de **transition**.
- Titre central UPPERCASE : « Notre approche en 3 phases ».
- Frise horizontale des 3 phases avec durée approximative.

### Slide 7 — Phase 1 : Audit & Stratégie
- Fond `#ffffff`.
- Titre UPPERCASE + numéro de phase « 01 » en `#dc0032` énorme (60pt) à gauche.
- À droite : objectifs (3 puces) + livrables (3 puces) + durée + équipe mobilisée.

### Slide 8 — Phase 2 : Design system & Librairie modulaire
- Même template que slide 7, numéro « 02 ».
- Mention claire de la modularité (clé du brief Geopost).

### Slide 9 — Phase 3 : Production des 6 templates
- Même template que slide 7, numéro « 03 ».
- Visualisation simplifiée des 6 templates : 3 triggers (welcome, app, boost) + 3 one-shot
  (peak, services, Singular) — sous forme de mini-cartes avec icône stylisée.

### Slide 10 — Focus : la librairie modulaire
- Fond `#ffffff`.
- Schéma simple montrant : « 1 librairie de blocs réutilisables × 5 BUs × N langues =
  scalabilité ».
- Liste des blocs modulaires (header, hero, body text, cards grid, promo, services,
  social proof, CTA, divider, footer).

### Slide 11 — Focus : accessibilité & robustesse Outlook
- Fond `#ffffff`.
- 2 colonnes :
  - Gauche : WCAG AA (contraste, alts, sémantique tables, lang attribute).
  - Droite : Outlook 2016+ (tables imbriquées, mso conditionnels, bulletproof buttons,
    fallback fonts).
- En bas : check-list QA pré-envoi (7-8 items).

### Slide 12 — Focus : multi-brand & multi-pays
- Fond `#ffffff`.
- Matrice 5 BUs × 4 dimensions (logo, couleur, langue, mentions légales).
- Démonstration que la librairie modulaire absorbe les variations sans patch manuel.

### Slide 13 — L'équipe
- Fond `#ffffff`.
- 6-7 cartes membres équipe (placeholder photo ronde + nom + rôle + expérience clé).
- Tu utilises `[PHOTO]` + `[NOM]` + `[RÔLE]` comme placeholders si l'agence ne fournit pas
  les CVs.

### Slide 14 — Track record (3 cas clients)
- Fond `#ffffff`.
- 3 colonnes égales = 3 cas clients.
- Par colonne : nom client (ou placeholder `[CAS CLIENT 1]`) + secteur + brief en 1 phrase
  + 1 KPI résultat (placeholder `[+X% CTR]`) + durée.
- Tu N'INVENTES PAS de cas. Tu mets des placeholders explicites si l'agence n'a pas fourni
  les références.

### Slide 15 — Notre proposition de valeur
- Fond `#dc0032`, texte en `#ffffff` — slide de **transition**.
- Titre central UPPERCASE : « Ce que vous obtenez ».
- 4-5 puces courtes (livrables clés synthétiques).

### Slide 16 — Planning
- Fond `#ffffff`.
- Gantt simplifié horizontal des 3 phases sur 14-18 semaines, calé sur les jalons Geopost
  (kick-off semaine du 15 juin 2026 = S0).
- Jalons clés annotés (livraison audit S+3, livraison DS+librairie S+8, livraison templates
  S+14).

### Slide 17 — Budget
- Fond `#ffffff`.
- Tableau 4 lignes (3 phases + option phase 4) × 2 colonnes (jours-hommes / montant € HT).
- Total HT en bas en gros (`24pt`, `#dc0032`).
- Tous les chiffres en placeholders `[À COMPLÉTER AGENCE]` si non fournis.
- Note de bas de page : conditions de facturation, TVA.

### Slide 18 — Risques & mitigations
- Fond `#ffffff`.
- Tableau 3 colonnes : Risque / Probabilité (P/M/E) / Mitigation.
- 4-5 lignes maximum (risques principaux du projet).

### Slide 19 — Prochaines étapes
- Fond `#ffffff`.
- 3 étapes numérotées :
  1. Sélection finale (5 juin 2026)
  2. Contractualisation
  3. Kick-off (semaine du 15 juin 2026)

### Slide 20 — Merci + contact
- Fond `#dc0032`, texte en `#ffffff` — slide de **clôture**.
- Titre central UPPERCASE : « Merci ».
- Sous-titre : « Prêts à démarrer le 15 juin ».
- Contact : `[NOM CONTACT AGENCE]` / `[EMAIL]` / `[TÉLÉPHONE]`.

> Tu peux ajouter / retirer 1-2 slides selon le besoin, mais tu ne descends jamais sous
> 15 slides ni au-dessus de 22.

---

## 6. Règles visuelles transverses

### 6.1 Pas de remplissage gratuit

- 1 idée par slide.
- Pas plus de 30 mots par slide (sauf slides 7/8/9 qui peuvent monter à 60).
- Pas d'animation, pas de transition exotique.
- Pas de stock photo générique (« business handshake », « happy team »). Si tu veux du
  visuel, propose des **abstractions géométriques** aux couleurs brand (cercles, lignes,
  carrés) ou des **icônes line-art simples** monochromes.

### 6.2 Hiérarchie visuelle

- Titre de slide en haut à gauche, taille 36-40pt, UPPERCASE, `#414042` (ou `#ffffff` sur
  slide de transition rouge).
- Bandeau d'accent `#dc0032` 4px sous le titre.
- Body en `#414042`, 14-18pt, casse normale.
- Page number en bas à droite, `#808285`, 9pt.
- Logo agence en bas à gauche, taille discrète (12-15mm).

### 6.3 Conventions textuelles

- Casse titres : UPPERCASE (cohérence brand Geopost).
- Casse body : casse normale, vouvoiement.
- Chiffres : lockup tight (`6 templates`, `5 BUs`, `+50 pays`, `15/06/2026`).
- Pas d'emoji.
- Pas de point d'exclamation.
- Mots interdits (alignement transverse) : révolutionnaire, ultime, exceptionnel, magique,
  incroyable, partenaire de confiance, expérience inégalée, simplicité déconcertante.

### 6.4 Iconographie

- Style line-art (traits 2px), monochrome `#dc0032` ou `#414042`.
- Largeur d'icône : 48-64px desktop.
- Cohérence : toutes les icônes du deck partagent le même style (jamais un mix flat /
  line-art / 3D).

### 6.5 Iconographie suggérée (placeholders cohérents)

| Concept             | Icône suggérée (line-art)                              |
|---------------------|--------------------------------------------------------|
| Audit               | loupe sur document                                     |
| Stratégie           | échiquier ou flèches convergentes                      |
| Design system       | grille de carrés alignés                               |
| Librairie modulaire | blocs empilés style Lego                               |
| Production HTML     | balises `</>`                                          |
| Outlook robustesse  | bouclier                                               |
| Accessibilité       | symbole universel (cercle + personnage stylisé)        |
| Multi-brand         | 5 cercles connectés                                    |
| Performance / KPI   | graphique en hausse                                    |
| Planning            | calendrier                                             |
| Budget              | tirelire ou tableau de chiffres                        |
| Équipe              | groupe de cercles                                      |
| Track record        | médaille ou ruban                                      |

---

## 7. Tonalité éditoriale du contenu textuel

- Professionnelle, factuelle, crédible.
- Démontrer la compréhension du brief (citer 1-2 fois le brief Geopost directement).
- Bénéfices concrets pour Geopost dans chaque section.
- Pas de meta-commentaire (« Nous sommes ravis de... »).
- Pas de lyrisme.
- Mots préférés : expert, fiable, robuste, scalable, modulaire, mesurable, éprouvé,
  documenté, traçable, conforme.

---

## 8. Adaptabilité du deck

Le deck doit pouvoir être :
- **présenté en 30 minutes** (slides 1-20, 1-2 minutes par slide).
- **présenté en 15 minutes** (version courte : 1-5 + 6-11 + 16-17 + 20).
- **envoyé en PDF** (lecture autonome — donc chaque slide doit être lisible sans le
  speaker, et les titres + sous-titres doivent suffire à comprendre le message).

Tu produis donc le deck en pensant aux 2 modes d'usage (live + lecture autonome).

---

## 9. Placeholders à utiliser explicitement

Tu n'inventes JAMAIS de valeur. Pour chaque information manquante, tu utilises un
placeholder en clair :

- `[LOGO AGENCE]`
- `[NOM AGENCE]`
- `[NOM CONTACT]`
- `[EMAIL CONTACT]`
- `[TÉLÉPHONE]`
- `[PHOTO MEMBRE 1]`, `[NOM MEMBRE 1]`, `[RÔLE MEMBRE 1]`
- `[CAS CLIENT 1]`, `[SECTEUR]`, `[+X% CTR]`, `[DURÉE]`
- `[BUDGET PHASE 1]`, `[BUDGET PHASE 2]`, etc.
- `[J.H. PHASE 1]`, etc.
- `[CHIFFRE CLÉ 1]`
- `[À COMPLÉTER AGENCE]` (générique)

L'opérateur humain remplit ces placeholders avant la présentation.

---

## 10. Accessibilité du deck (WCAG AA — slides print + écran)

- Contrastes ≥ 4.5:1 sur tout texte body, ≥ 3:1 sur texte large.
- `#dc0032` sur `#ffffff` : OK pour large + graphique fonctionnel, MAIS LIMITE pour body
  (contraste 5.1:1). Privilégier `#a90034` pour texte body sur fond clair si besoin.
- Pas de texte uniquement en image (le PDF doit être searchable).
- Police taille minimum 12pt sur slides (idéalement 14pt+).
- Légendes sur images / graphiques (pas d'info par couleur seule).
- Hiérarchie titres claire (1 H1 par slide).

---

## 11. Format de sortie attendu

3 livrables :

### 11.1 `deck-content.md`

Document Markdown listant les 15-20 slides avec :
- Numéro slide
- Titre
- Sous-titre
- Body (texte de slide)
- Notes du speaker (3-5 phrases par slide, voix orale, ce que le présentateur dit)
- Visuels suggérés (icônes, schémas, placeholders)
- Layout suggéré (référence à la structure §5)

### 11.2 `deck-spec.md`

Spec design détaillée pour le designer / opérateur PowerPoint / Keynote :
- Format slides (16:9, 1920×1080)
- Tokens (couleurs, typo, espacements)
- Grille (12 colonnes, marges)
- Templates de slides (couverture / contenu / transition / clôture)
- Bibliothèque d'icônes (style line-art, 13 icônes §6.5)
- Règles transverses (hiérarchie, conventions, accessibilité)

### 11.3 `deck-html-preview.html` (optionnel mais recommandé)

Un fichier HTML self-contained avec les 15-20 slides rendues en HTML/CSS pur (1 div par
slide, 16:9 ratio, styles inline conformes aux tokens), navigable avec flèches clavier.
Sert d'aperçu visuel rapide avant transposition dans PowerPoint / Keynote / Google Slides.

> Si Claude Design n'est pas capable de produire un HTML preview correct, il livre
> uniquement §11.1 + §11.2.

---

## 12. Instructions de prompt itératif

Après livraison v1.0, l'opérateur peut relancer Claude Design pour :

- **Zoom slide unique** : « Re-conçois la slide 10 (librairie modulaire) avec un schéma plus
  visuel. »
- **Ajout de slide** : « Ajoute une slide entre 12 et 13 sur notre approche QA / tests. »
- **Variante de ton** : « Re-tonifie l'ensemble du deck pour un comité plus C-level (moins de
  technique, plus de business). »
- **Adaptation longueur** : « Produis la version 10 slides du deck pour un pitch raccourci. »
- **Localisation** : « Traduis le deck en anglais en gardant les tokens design. »

---

## 13. Interdictions (rappel)

- ❌ Inventer un cas client, un KPI, un partenaire, un award.
- ❌ Utiliser des photos stock génériques.
- ❌ Sortir de la palette `#dc0032` + neutres `#414042` / `#808285` / `#abb8c3` + `#ffffff`.
- ❌ Utiliser Calibri, Comic Sans, Times, Roboto ou toute police non-brand.
- ❌ Surcharger les slides (> 30 mots hors slides 7-8-9).
- ❌ Utiliser des effets 3D, ombres CSS3, gradients exotiques.
- ❌ Mettre des emojis.
- ❌ Inventer une BU autre que les 5 listées.
- ❌ Annoncer un chiffre d'affaires, un nombre d'employés, une certification agence sans
  fichier source.

---

## 14. Conclusion attendue de la livraison

Une fois les 3 fichiers livrés, l'opérateur peut :

1. Faire valider le contenu (`deck-content.md`) par le lead AO et la direction commerciale.
2. Passer `deck-spec.md` au designer PowerPoint / Keynote pour transposition pixel-perfect.
3. Utiliser `deck-html-preview.html` comme rendu intermédiaire validable avant produire le
   PPT final.
4. Compléter tous les placeholders `[...]` avec les vraies informations agence avant le
   pitch.
5. Répéter le pitch en 30 min puis en 15 min, vérifier que le deck supporte les deux modes.
