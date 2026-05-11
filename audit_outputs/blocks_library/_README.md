# Geopost Email Blocks Library v1

Librairie de blocs HTML email **conformes aux normes** du brief Geopost Templates Revamp.

## Conformité — chaque bloc respecte

| Norme | Détail |
|---|---|
| **Outlook 2007 → M365** | Tables imbriquées, `role="presentation"`, pack mso (lspace/rspace/line-height-rule), bulletproof button VML, padding sur `<td>` jamais `<table>` |
| **WCAG 2.1 AA** | Contrastes ≥4.5:1 body / ≥3:1 large, alts descriptifs, focus visible, taille tactile ≥44×44, ordre de lecture cohérent |
| **Dark mode** | `<meta name="color-scheme">` + `@media (prefers-color-scheme: dark)` quand pertinent |
| **Mobile responsive** | Wrapper 640px desktop / 100% mobile via `@media (max-width:480px)` |
| **Anti-spam** | Pas de `<script>`, `<iframe>`, `@import`, pas de URL CID, pas de frameworks |
| **Multi-brand** | Tokens `{{TOKEN}}` paramétrables par BU (couleur, logo, langue, légal) |

## Convention de tokens

Tokens `{{DOUBLE_BRACES}}` substituables au render :

| Token | Description | Valeur exemple |
|---|---|---|
| `{{COLOR_PRIMARY}}` | Couleur primaire BU | `#DC0032` |
| `{{COLOR_SECONDARY}}` | Couleur secondaire BU | `#2e2e2f` |
| `{{LOGO_URL}}` | URL absolue du logo BU (CDN imagino) | `https://cdn.imagino.com/geopost/logo.png` |
| `{{LOGO_ALT}}` | Alt du logo | `Geopost` |
| `{{BU_NAME}}` | Nom complet BU | `Geopost France` |
| `{{LANG}}` | Code langue ISO | `fr-FR` |
| `{{UNSUB_URL}}` | URL absolue désabonnement | `https://geopost.fr/unsub?token=xxx` |
| `{{PREFS_URL}}` | URL préférences | `https://geopost.fr/prefs?token=xxx` |
| `{{LEGAL_ADDRESS}}` | Adresse postale BU | `DPD Etablissement 975…` |
| `{{LEGAL_RGPD}}` | Mention RGPD pays | `En application de la loi…` |

## Catalogue

| # | Bloc | Fichier | Usage |
|---|---|---|---|
| 01 | Wrapper email + reset | `01_wrapper.html` | Base à toujours utiliser |
| 02 | Preheader masqué | `02_preheader.html` | Texte caché avant le rendu |
| 03 | Header logo simple | `03_header_logo.html` | Logo BU centré |
| 04 | Hero texte + visuel décoratif | `04_hero_text_image.html` | H1 texte + image alt="" |
| 05 | Sub-héro (1 phrase + durée) | `05_sub_hero.html` | Sous le H1 |
| 06 | CTA primaire bulletproof | `06_cta_primary.html` | 1 CTA principal, ≥44px |
| 07 | CTA double (App Store + Google Play) | `07_cta_double_apps.html` | Spécifique Promote app |
| 08 | Body 1 colonne (paragraphe) | `08_body_1col.html` | Texte simple |
| 09 | Body 3 cards horizontales | `09_body_3cards.html` | 3 bénéfices |
| 10 | Body 3 étapes verticales numérotées | `10_body_3steps.html` | Onboarding, mode d'emploi |
| 11 | Image + texte droite | `11_image_text_right.html` | Bloc service / nouveauté |
| 12 | Bannière promo (code) | `12_banner_promo.html` | Boost sales variante prix |
| 13 | Bloc data metric (B2B Singular) | `13_metric_data.html` | Chiffres + variation |
| 14 | Signature manuelle AM (B2B) | `14_signature_am.html` | Singular uniquement |
| 15 | Footer légal RGPD | `15_footer_legal.html` | Adresse + RGPD + unsub |
| 16 | Spacer / divider | `16_spacer.html` | Espacement vertical |
| 17 | Tracking pixel transparent | `17_tracking_pixel.html` | 1×1 fin d'email |

## Comment composer un email

```
[01 Wrapper start]
  [02 Preheader masqué]
  [03 Header logo]
  [04 Hero texte + visuel]
  [05 Sub-héro]
  [06 CTA primaire]
  [16 Spacer]
  [08 ou 09 ou 10] body modulaire (1 à 3 blocs max)
  [16 Spacer]
  [11 ou 12 ou 13] bloc spécifique optionnel
  [15 Footer légal]
  [17 Tracking pixel]
[01 Wrapper end]
```

## Rendu et test

- Ouvrir `_index.html` pour voir tous les blocs rendus avec valeurs par défaut
- Chaque bloc est **standalone** — il peut être copié-collé dans imagino directement
- Avant production : tests Litmus ≥30 clients + axe-core WCAG sur l'email assemblé

## Versioning

| Version | Date | Changement |
|---|---|---|
| v1 | 11 mai 2026 | Bootstrap initial — 17 blocs core |
| v1.1 | TBD | Blocs spécialisés Peak (countdown table-based, etc.) |
| v1.2 | TBD | Blocs spécifiques Singular B2B avancés |
