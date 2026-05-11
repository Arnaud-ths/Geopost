# Tokens extraits — `geopost.com/fr/entreprise/`

> Source : `design_system/_sources/geopost_corporate_homepage.html` (page corporate Geopost France, sauvegardée le 11/05/2026).
> Méthode : extraction directe par grep sur les attributs `style` et les classes inline du HTML rendu.
> Statut : **point de départ chiffré** pour le brief Claude Design — pas un design system finalisé.

---

## 1. Palette de couleurs (occurrences dans le HTML)

| Hex        | Occurrences | Rôle observé sur le site corporate                              |
|------------|-------------|------------------------------------------------------------------|
| `#dc0032`  | 15          | **Rouge primaire Geopost** — CTA, headings, accents             |
| `#a90034`  | 2           | **Rouge sombre** — hover/active, accent secondaire              |
| `#414042`  | 20          | **Gris foncé** — couleur texte par défaut (body)                |
| `#808285`  | 1           | Gris moyen — texte secondaire / metas                            |
| `#7e8993`  | 1           | Gris bleuté — texte tertiaire                                    |
| `#abb8c3`  | 1           | Gris clair — séparateurs, bordures                               |
| `#ffffff`  | 13          | Blanc — fond, texte sur fond rouge                               |
| `#000000`  | 1           | Noir — exceptions ponctuelles                                    |
| `#32373c`  | 2           | Bleu-gris très foncé — UI éditeur (probable résidu WordPress)   |

Couleurs Gutenberg/WordPress résiduelles (à **exclure** du design system, non-brand) :
`#1787bf`, `#ff6900`, `#ff253a`, `#fcb900`, `#f78da7`, `#cf2e2e`, `#9b51e0`, `#8ed1fc`,
`#7bdcb5`, `#0693e3`, `#00d084`.

---

## 2. Typographie

### 2.1 Polices

| Police              | Rôle observé                | Statut email                                   |
|---------------------|-----------------------------|-----------------------------------------------|
| `PlutoSansMedium`   | Titres, accents             | **Non web-safe** — fallback Arial obligatoire |
| `PlutoSansRegular`  | Body, paragraphes           | **Non web-safe** — fallback Arial obligatoire |

> Pour l'email, proposer un stack `Arial, Helvetica, sans-serif` avec `@font-face` Pluto Sans
> en fallback progressif (uniquement Apple Mail / iOS Mail / certains webmails) — sans dépendance.

### 2.2 Échelle observée

| Taille      | Poids | Line-height | Rôle                |
|-------------|-------|-------------|---------------------|
| `30px`      | 700   | `1.23`      | H1 / H2 (UPPERCASE) |
| `18px`      | 400   | `27px` (~1.5) | Body paragraph    |
| `11px`      | 400   | —           | Legal / fine print  |

Casse observée : titres en `UPPERCASE`, body en casse normale.

---

## 3. Brand voice / piliers (extraits du contenu rédactionnel)

- Positionnement : « leader mondial en livraison de colis et solutions e-commerce ».
- Présence : plus de 50 pays, 5 continents.
- Stratégie 2030 : axée durabilité, transformation responsable.
- Valeurs corporate récurrentes : **Responsabilisation, Entrepreneuriat, Inventivité**.
- Périmètre BUs visibles : Geopost (corporate), DPD, BRT, Chronopost, SEUR, Speedy, Yurtiçi, Jadlog…

> Ces piliers sont à confirmer côté brand guidelines client. Ils servent ici de baseline
> pour calibrer les sous-agents Lead CRM (notamment §13 Tonalité) avant injection des
> guidelines officielles.

---

## 4. Ce que le HTML source ne contient PAS

À demander explicitement à Geopost lors du kick-off :

- Logos officiels (SVG + PNG) par BU (Geopost corporate, BRT, DPD CH, DPD CZ, DPD SK).
- Fichiers de police PlutoSans (.woff2) ou licence d'usage.
- Charte couleurs étendue (semantic : success / warning / error / info — absents du site).
- Guidelines tonalité éditoriale par BU / langue.
- Mentions légales pays par pays (RGPD, CGV, désinscription).
- Brand book email si existant.
- Maquettes Figma des templates POC actuels.
