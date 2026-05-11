# Creative Brief — Template `Boost sales`

## 0. Header

| Champ | Valeur |
|---|---|
| **Template** | Boost sales — réactivation comptes inactifs 30j+ |
| **Famille** | Trigger automatisé (lifecycle) |
| **Version brief** | v1 — 11 mai 2026 |
| **Statut** | Draft — à valider Geopost |
| **BU concernées** | BRT, DPD CH, DPD CZ, DPD SK (Geopost corp = B2B corporate, parcours dédié) |
| **Owner agence** | Lead CRM Geopost V1 |
| **Owner Geopost** | [À CONFIRMER GEOPOST] |
| **Deadline first draft** | 24 juillet 2026 |
| **Date d'envoi cible** | Trigger continu — déclenché après 30j sans envoi de colis. Max 3 envois / compte / an. |

---

## 1. Background & opportunity

Un destinataire a envoyé un colis il y a 30 jours puis plus rien. C'est le moment de bascule : soit on **réactive l'usage maintenant**, soit il glissera vers les concurrents (La Poste, Mondial Relay, Chronopost en FR — équivalents par pays). Le coût de réactivation est encore raisonnable à J+30, il devient 5× plus élevé à J+90.

L'opportunité : rappeler la valeur **sans paraître désespéré**. Un email « on vous a oublié, revenez ! » est contre-productif. L'objectif est de **lever un frein spécifique** (prix, complexité, manque de besoin) ou d'**activer un nouvel usage** (point relais, retour).

---

## 2. Single-minded proposition

> **Pour le destinataire inactif depuis 1 mois, Geopost est le service qu'il avait déjà choisi — qu'on rend juste plus facile à utiliser aujourd'hui.**

---

## 3. Audience

| Dimension | Description |
|---|---|
| **Qui** | Compte ayant envoyé ≥1 colis dans les 12 derniers mois mais 0 dans les 30 derniers jours. Mix B2C et SME légers. |
| **Statut Geopost** | Inactif 30-180j. Au-delà de 180j → parcours dédié re-engagement (non couvert par ce brief). |
| **Ce qu'ils savent déjà** | Le service. La marque. Probablement le prix. |
| **Ce qu'ils ressentent** | Indifférents la plupart du temps. **N'attendent rien** de Geopost actuellement. Peut-être insatisfaits silencieusement (sans avoir râlé). |
| **Ce qu'ils veulent** | Ne pas être harcelés. Mais sensibles à un *vrai* bénéfice concret. |
| **Ce qui les freine** | Pas eu besoin · Avait essayé la concurrence · Avait eu un pépin une fois · Trouve compliqué · Trouve cher |

---

## 4. Insight clé

> **« On ne réactive pas un client en lui rappelant qu'il existe. On le réactive en lui rappelant pourquoi il a choisi nous au départ — ou en lui montrant ce qui a changé depuis. »**

Le destinataire ne veut **ni un mail de relance**, ni une promo gratuite — il veut une **raison concrète et nouvelle** de revenir. Soit le prix a baissé, soit on a ajouté une option qui résout sa friction passée, soit on a simplifié quelque chose qu'il trouvait pénible.

---

## 5. Tone of voice

| Ce qu'on est | Ce qu'on n'est PAS |
|---|---|
| **Direct** — on dit pourquoi on revient vers lui | **Mielleux** — pas de « ça fait longtemps qu'on ne s'est pas vus » |
| **Concret** — chiffres, dates, options | **Vague** — pas de « pleins de nouveautés » |
| **Discret** — 1 email, pas une séquence harcelante | **Insistant** — pas de relance dans la relance |

**Mots interdits** + spécifiques : « comme avant », « famille », « offre exceptionnelle », « ne ratez pas », « cher client ».

**Références de ton** : Mailchimp pause campaign email (sobre), Spotify "we miss you" (mais en plus pro, moins lyrique), pas Amazon (trop algorithmique).

---

## 6. Hiérarchie de message — slot par slot

| Zone | Brief | Contrainte | Variantes A/B/C |
|---|---|---|---|
| **Objet** | 3 leviers à tester en parallèle : **prix**, **simplicité**, **nouveauté** | ≤50 car. | **A. Prix.** « -20% sur votre prochain envoi {BU} » · **B. Simplicité.** « Envoyer un colis n'a jamais été aussi rapide » · **C. Nouveauté.** « 3 nouveautés {BU} à découvrir » |
| **Preheader** | Compléter l'objet sans le répéter | ≤110 car. | Selon variante. Ex. (A) : « Code BOOST20 valable jusqu'au {Date+14j}. 1 envoi par compte. » |
| **H1** (texte HTML) | Bénéfice tangible directement | ≤60 car. | **A.** « Économisez 20% sur votre prochain envoi. » · **B.** « 3 minutes pour envoyer. C'est tout. » · **C.** « Voici ce qui a changé depuis. » |
| **Sub-héro** | Rappel ancienneté (factuel, jamais culpabilisant) | ≤20 mots | « Votre dernier envoi remonte au {Dernier_envoi}. Voici ce qu'on a à vous proposer aujourd'hui. » |
| **Body** | Bloc levier choisi (promo / nouveautés / tutoriel) — **adapté à la variante d'objet** | — | Voir §6 bis |
| **CTA primaire** | Verbe orienté action | ≤4 mots, casse normale | **A.** « Profiter de l'offre » · **B.** « Envoyer maintenant » · **C.** « Voir les nouveautés » |
| **CTA secondaire** | Désengagement soft (donner le contrôle) | Lien texte | « Recevoir moins d'emails » (lien préférences) |
| **Signature** | Pas de signature. Service institutionnel. | — | — |

### 6 bis. Structure body par variante

**Variante A (Prix)** : bloc `code_promo` — code BOOST20, date d'expiration, conditions (1 envoi, valable {BU} France, jusqu'à 5kg).

**Variante B (Simplicité)** : bloc `body_3steps` — 3 étapes simplifiées vs. il y a 6 mois (ex. ① Saisir adresse · ② Imprimer étiquette · ③ Déposer en point relais).

**Variante C (Nouveauté)** : bloc `body_3cards` — 3 nouveautés Geopost depuis le dernier envoi (ex. consigne 24/7, livraison soir, retour gratuit).

---

## 7. Direction visuelle

| Élément | Direction |
|---|---|
| **Image héro** | **Décorative**, change selon variante : (A) un colis emballé et étiqueté, soft focus · (B) une étiquette qui s'imprime · (C) icônes ou photo des 3 nouveautés combinées. Pas de visage. Pas d'émotion forcée. |
| **Couleurs** | Tokens BU. Sur variante A (prix), le code promo en bloc visuel fort avec `{COLOR_PRIMARY}`. |
| **Iconographie** | Très peu. Le code promo et la date d'expiration en typo seule, pas dans une bannière kitsch. |
| **Lighting / mood** | Neutre, fonctionnel. |
| **Composition** | CTA visible dès la fold, même mobile. Body court. |
| **Références** | Mailchimp re-engagement (sobre), Linear product update (factuel), pas Booking (trop FOMO). |

---

## 8. Personnalisation

| Token | Source CDP | Usage recommandé | Fallback |
|---|---|---|---|
| `{Prénom}` | imagino base | Optionnel — pas dans objet pour ne pas paraître familier | Aucun |
| `{BU}` | déduit | Partout | — |
| `{Dernier_envoi}` | imagino transactions | Sub-héro factuel | « Il y a plus d'un mois » |
| `{Préférence_destination}` | imagino préférences | Si connue → preheader « Vers {Pays}, le délai est de X jours » | Ne pas afficher |
| `{Code_promo}` + `{Date_expiration}` | génération CDP | Variante A uniquement | — (variante non envoyée si pas de code) |
| `{Nombre_envois_an_dernier}` | imagino agrégat | Si ≥5 → « Vous étiez un client régulier en {Année-1} » | Ne pas afficher |

**Règle d'or** : aucune variante ne s'envoie sans son token critique. Variante A sans code = bascule sur variante B.

---

## 9. Mandatories

| Type | Mandatory |
|---|---|
| **Brand** | Logo BU, palette officielle, ton **discret** (jamais survendeur même sur variante A) |
| **Légal** | Mention RGPD pays, adresse postale BU, lien désabonnement actif + lien préférences fréquence. **Mention conditions code promo** complète en footer si variante A. |
| **Technique** | Wrapper 640px desktop / 100% mobile · responsive · dark mode-ready · WCAG AA · compat Outlook · bulletproof button |
| **Anti-spam** | Score SpamAssassin ≤2 obligatoire (les emails « -X% » sont sur-filtrés). Tester avec et sans le pourcentage dans l'objet. |
| **Règle fréquence** | Max 3 envois / compte / an, ≥90j entre 2 envois Boost. Stop séquence si désabo après 1-2 envois. |

---

## 10. Test plan A/B/C

| Variable testée | Hypothèse | KPI lu | Significativité |
|---|---|---|---|
| **Levier d'objet** (A prix / B simplicité / C nouveauté) | Le levier *prix* (A) gagne en open rate mais perd en désabo. *Nouveauté* (C) plus sain à long terme. | Open rate + réactivation J+14 — **arbitrage** | 95% confiance, ≥5 000 envois / variante |
| **Insertion `{Dernier_envoi}` dans sub-héro** | La factualité de la date augmente la perception de pertinence | CTR | 95% confiance |
| **Position code promo** (variante A) | Code dans le H1 vs code dans bloc dédié sous H1 — bloc dédié gagne en conversion (lisibilité) | Code utilisation rate | 95% confiance |

**Durée** : 30 jours · **Allocation** : 33/33/33 sur les 3 leviers d'objet · **Garde-fou** : stop variante si désabo &gt;0.5%.

---

## 11. KPIs de succès

| KPI | Cible | Mesure | Garde-fou |
|---|---|---|---|
| **Primaire** | Réactivation J+14 (≥1 colis envoyé) | ≥8% | — |
| **Secondaire 1** | Open rate | ≥22% (audience inactive = open plus bas) | — |
| **Secondaire 2** | CTR | ≥6% | — |
| **Secondaire 3** | Désabonnement | &lt;0.3% | stop variante si &gt;0.5% |
| **Code utilisation** (A) | % du clic → utilisation code | ≥40% | — |
| **Régression** | 0 régression Outlook | 0 | — |

---

## 12. Constraints — ce qu'on ne fait PAS

- ❌ Pas de séquence Boost en cascade (1 seul email à la fois, pas de relance Boost à 48h)
- ❌ Pas de « Vous nous manquez », « On vous a oublié », « On pense à vous »
- ❌ Pas de promo &gt;20% (au-delà : signal de marque « low cost » qu'on ne veut pas)
- ❌ Pas d'enregistrement automatique en parcours Peak en parallèle (priorité Peak si fenêtre marketing active)
- ❌ Pas de « offre limitée à 24h » sur Boost (pas notre énergie de marque)

---

## 13. Timeline

| Étape | Owner | Date |
|---|---|---|
| Brief validé Geopost | Lead CRM Geopost | 27 juillet 2026 |
| First draft copy 3 variantes leviers | Agent 02 | 30 juillet 2026 |
| First draft design (3 variantes héro) | Agent 03 | 4 août 2026 |
| HTML intégré + tests anti-spam | Agent 04 | 11 août 2026 |
| Génération codes promo Geopost (variante A) | Geopost CRM | 12 août 2026 |
| Review Geopost + BU pilote | Lead CRM | 17 août 2026 |
| Push imagino sandbox | Chef projet | 19 août 2026 |
| Go live test BRT | Geopost | 24 août 2026 |
| Lecture résultats J+30 | Lead CRM + Geopost | 23 septembre 2026 |

---

## 14. References & inspirations

- **Mailchimp** — "your account has been quiet" · ton sobre, factuel, donne le contrôle. <span class="muted">Ce qu'on garde : le ton.</span>
- **Linear** — product update email · 3 nouveautés expliquées simplement. <span class="muted">Ce qu'on adapte : pour variante C.</span>
- **Spotify** — "Discover what's new" · pas culpabilisant. <span class="muted">Ce qu'on garde : l'absence de culpabilité.</span>
- **Anti-référence** : Booking « Vous nous manquez ! » (trop affectif, contre-productif).

---

## 15. Sign-off

| Rôle | Nom | Date |
|---|---|---|
| Lead CRM Geopost | [À CONFIRMER GEOPOST] | — |
| Owner BU | [À CONFIRMER GEOPOST] | — |
| Legal Geopost (validation conditions promo) | [À CONFIRMER GEOPOST] | — |
| Lead créatif agence | [À COMPLÉTER AGENCE] | — |
