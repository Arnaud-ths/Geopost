# Creative Brief — Template `[NOM_TEMPLATE]`

> **Format & usage** : 1 brief par template. Validé par le Lead CRM Geopost avant lancement design et copy. Re-validé à chaque évolution majeure.
> Toute mention `[À CONFIRMER GEOPOST]` doit être levée avant production.

---

## 0. Header

| Champ | Valeur |
|---|---|
| **Template** | [NOM_TEMPLATE] |
| **Famille** | [Trigger automatisé / One-shot] |
| **Version brief** | v1 — JJ/MM/AAAA |
| **Statut** | [Draft / Validé Geopost / En production] |
| **BU concernées** | [Geopost corp / BRT / DPD CH / DPD CZ / DPD SK] |
| **Owner agence** | [Nom + rôle] |
| **Owner Geopost** | [Nom + rôle] |
| **Deadline first draft** | JJ/MM/AAAA |
| **Date d'envoi cible** | [continue / fenêtre] |

---

## 1. Background & opportunity

**Pourquoi cet email existe.** En 3-5 lignes : le moment de vie destinataire, le contexte business Geopost, l'opportunité éditoriale.

---

## 2. Single-minded proposition

**Une phrase. Une seule.** Ce qu'on veut que le destinataire pense, ressente ou fasse après avoir lu l'email.

> Format : « Pour [audience], [Geopost] est [bénéfice unique] qui [reason to believe]. »

---

## 3. Audience

| Dimension | Description |
|---|---|
| **Qui** | Profil socio-démo, persona-type |
| **Statut Geopost** | Lifecycle, ancienneté, fréquence d'usage |
| **Ce qu'ils savent déjà** | Niveau de familiarité avec Geopost et le service |
| **Ce qu'ils ressentent** | État émotionnel au moment de réception |
| **Ce qu'ils veulent** | Le bénéfice qu'ils recherchent ici, pas ailleurs |
| **Ce qui les freine** | Le doute, la friction, la concurrence dans leur tête |

---

## 4. Insight clé

**La vérité humaine** sur laquelle on s'appuie. 1 phrase forte. Pas un constat business — un constat d'observation.

> Exemple format : « Recevoir un colis à la maison est un acte de confiance — pas une transaction. »

---

## 5. Tone of voice

| Ce qu'on est | Ce qu'on n'est PAS |
|---|---|
| [Adjectif 1] | [Anti-adjectif 1] |
| [Adjectif 2] | [Anti-adjectif 2] |
| [Adjectif 3] | [Anti-adjectif 3] |

**Mots interdits** : révolutionnaire, ultime, exceptionnel, magique, incroyable, expérience inégalée, partenaire de confiance, simplicité déconcertante, sans précédent.

**Références de ton** : [3 marques / exemples concrets qui incarnent le ton voulu]

---

## 6. Hiérarchie de message — slot par slot

| Zone | Brief | Contrainte | Variantes A/B |
|---|---|---|---|
| **Objet** | [intention en 1 ligne] | ≤50 car., pas d'emoji superflu, pas de MAJ caps lock | 3 obligatoires |
| **Preheader** | [intention — teaser unique, jamais doublon du H1] | ≤110 car. | 1 |
| **H1** (texte HTML) | [accroche, bénéfice ou question] | ≤60 car., 1 seul H1 par email | 3 |
| **Sub-héro** | [bénéfice concret + durée si applicable] | 1 phrase ≤20 mots | 1 |
| **Body** | [structure — quels blocs assembler, dans quel ordre] | Phrases ≤20 mots, 1 idée par bloc | — |
| **CTA primaire** | [verbe d'action] | ≤4 mots, casse normale, ≥44px tactile | 3 |
| **CTA secondaire** | [optionnel — soft engagement] | Lien texte, label explicite | 1 |
| **Signature** | [si pertinent — name + rôle] | — | — |

---

## 7. Direction visuelle

| Élément | Direction |
|---|---|
| **Image héro** | Décorative uniquement (jamais porteuse du H1) — sujet / mood / ratio |
| **Couleurs** | Tokens BU primary/secondary, jamais hors palette officielle |
| **Iconographie** | Style (lifestyle / data / abstract / aucun) |
| **Lighting / mood** | Ton clair, naturel / studio / etc. |
| **Composition** | Centrée / décalée / cinematic |
| **Références** | [3-5 références concrètes — Pinterest / dribbble / mood board agence] |

---

## 8. Personnalisation

Variables CDP utilisables — listées par priorité d'impact :

| Token | Source CDP | Usage recommandé | Fallback |
|---|---|---|---|
| `{Prénom}` | imagino base | Objet, salutation | « Bonjour, » |
| `{Dernier_envoi}` | imagino transactions | Sub-héro, body | Ne pas afficher |
| `{Préférence_destination}` | imagino préférences | Body | Ne pas afficher |
| `{...}` | ... | ... | ... |

**Règle d'or** : aucune variable affichée sans fallback. Si la donnée n'existe pas, le bloc disparaît élégamment (pas de « Bonjour {Prénom} »).

---

## 9. Mandatories

| Type | Mandatory |
|---|---|
| **Brand** | Logo BU, palette officielle, ton de voix charte |
| **Légal** | Mention RGPD pays-spécifique, adresse postale BU, lien désabonnement actif, sender domain authentifié SPF/DKIM/DMARC |
| **Technique** | Wrapper 640px desktop / 100% mobile, mobile responsive obligatoire, dark mode-ready, WCAG AA strict, compat Outlook 2007→M365 |
| **Conformité** | Tests Litmus ≥30 clients, validation WCAG axe-core, vérification anti-spam (SpamAssassin) |

---

## 10. Test plan A/B

| Variable testée | Hypothèse | KPI lu | Seuil de significativité |
|---|---|---|---|
| Objet (3 variantes) | « [insight testé] » | Open rate | 95% confiance, ≥2 000 envois / variante |
| H1 (3 variantes) | « [insight testé] » | CTR | 95% confiance, ≥2 000 envois / variante |
| CTA (3 variantes) | « [verbe vs. bénéfice vs. urgence] » | Conversion | 95% confiance, ≥2 000 envois / variante |

**Durée test** : minimum 7 jours · **Trafic alloué** : 33/33/33 ou 50/50

---

## 11. KPIs de succès

| KPI | Cible | Mesure | Garde-fou |
|---|---|---|---|
| **Primaire** | [Activation J+7 / Install / Réactivation] | [valeur cible] | — |
| **Secondaire 1** | Open rate | [valeur] | ≥97% délivrabilité |
| **Secondaire 2** | CTR | [valeur] | ≤0.2% désabonnement |
| **Secondaire 3** | [autre] | — | 0 régression Outlook |

---

## 12. Constraints — ce qu'on ne fait PAS

- ❌ Pas de H1 dans une image — jamais
- ❌ Pas de CTA en MAJUSCULES caps lock
- ❌ Pas de mots interdits (cf. §5)
- ❌ Pas de personnalisation sans fallback
- ❌ Pas plus de 1 CTA primaire
- ❌ [Contraintes spécifiques au template]

---

## 13. Timeline

| Étape | Owner | Date |
|---|---|---|
| Brief validé Geopost | Lead CRM Geopost | JJ/MM/AAAA |
| First draft copy (variantes A/B/C) | Agent 02 CRO & UX Writing | +2j |
| First draft design (wireframe + spec) | Agent 03 Template Design | +3j |
| HTML intégré + tests Litmus | Agent 04 HTML Integration | +5j |
| Review Geopost | Lead CRM Geopost + BU locale | +6j |
| Final corrections | Agents 02/03/04 selon scope | +7j |
| Push imagino sandbox | Chef de projet humain | +8j |
| QA finale + go live | Geopost | +10j |

---

## 14. References & inspirations

- [Lien 1 — best in class du même type d'email] · pourquoi c'est bien
- [Lien 2 — référence d'un autre secteur] · ce qu'on en garde
- [Lien 3 — exemple d'erreur à ne pas reproduire] · pourquoi on évite

---

## 15. Sign-off

| Rôle | Nom | Signature | Date |
|---|---|---|---|
| Lead CRM Geopost | [Nom] | — | — |
| Owner BU locale | [Nom + BU] | — | — |
| Lead créatif agence | [Nom] | — | — |
| Chef de projet agence | [Nom] | — | — |

---

*Brief produit dans le dispositif Geopost Lead CRM V1. Re-validation obligatoire à chaque évolution majeure du template ou changement de moment de vie destinataire.*
