# Creative Brief — Template `Welcome`

## 0. Header

| Champ | Valeur |
|---|---|
| **Template** | Welcome — onboarding post-création de compte |
| **Famille** | Trigger automatisé |
| **Version brief** | v1 — 11 mai 2026 |
| **Statut** | Draft — à valider Geopost |
| **BU concernées** | Geopost corp, BRT, DPD CH, DPD CZ, DPD SK |
| **Owner agence** | Lead CRM Geopost V1 + Agent 02 (copy) + Agent 03 (design) |
| **Owner Geopost** | [À CONFIRMER GEOPOST] |
| **Deadline first draft** | 6 juin 2026 (post-kickoff) |
| **Date d'envoi cible** | Trigger continu — déclenché à chaque création de compte CDP imagino |

---

## 1. Background & opportunity

Un nouveau destinataire vient de créer un compte sur le site / app Geopost. Il a un **objectif court terme** (envoyer un colis, suivre une livraison à venir) et il a investi 2-3 minutes de son temps. **L'email de welcome est sa première interaction avec la marque hors interface produit** — c'est le moment où Geopost passe de « service utilitaire » à « marque que je connais ».

L'opportunité : transformer une inscription utilitaire en **adoption d'usage régulier**. La fenêtre critique est de 7 jours — au-delà, le compte tombe à 30% de probabilité d'activation.

---

## 2. Single-minded proposition

> **Pour le destinataire qui vient de s'inscrire, Geopost est le service de livraison qui lève les 3 premières frictions d'envoi en moins de 2 minutes.**

---

## 3. Audience

| Dimension | Description |
|---|---|
| **Qui** | 28-55 ans, mix B2C (≈80%) et SME B2B (≈20%). Urbains et péri-urbains. Achat e-commerce régulier ou activité commerciale. |
| **Statut Geopost** | J0 — compte fraîchement créé, aucun envoi encore effectué. |
| **Ce qu'ils savent déjà** | Que Geopost livre des colis. Connaissent vaguement le réseau (point relais, livraison à domicile). |
| **Ce qu'ils ressentent** | Léger soulagement (l'inscription est passée). Curiosité prudente. *« Bon, maintenant comment ça marche concrètement ? »* |
| **Ce qu'ils veulent** | Faire leur 1er envoi (ou suivre leur 1ère livraison) **sans avoir à chercher**. |
| **Ce qui les freine** | Peur de mal faire (mauvaise étiquette, mauvais tarif), peur de la complexité, peur de l'app inutile. |

---

## 4. Insight clé

> **« Quand je crée un compte quelque part, ce que je veux, ce n'est pas un mot de bienvenue. C'est savoir quoi faire dans les 5 prochaines minutes. »**

Les gens n'ouvrent pas un welcome email pour se sentir accueillis. Ils l'ouvrent pour **finir ce qu'ils ont commencé** — l'inscription, c'était l'étape 1 d'un parcours plus long. Le welcome doit être le mode d'emploi, pas la carte de vœux.

---

## 5. Tone of voice

| Ce qu'on est | Ce qu'on n'est PAS |
|---|---|
| **Pratique** — on guide, on n'enchante pas | **Lyrique** — pas de « ravis de vous accueillir » |
| **Concret** — on donne des étapes, des durées | **Vague** — pas de « facilement et rapidement » |
| **Confiant** — on tutoie l'expertise du destinataire | **Condescendant** — pas de « pas de panique » |

**Mots interdits** (cf. règle commune) + spécifiques à éviter ici : « famille », « ravis », « précieux », « parcours utilisateur ».

**Références de ton** : Doctolib welcome (mode d'emploi en 3 étapes), Stripe « getting started » (factuel, pro), Citymapper première ouverture (utile dès la 1ère seconde).

---

## 6. Hiérarchie de message — slot par slot

| Zone | Brief | Contrainte | Variantes A/B/C |
|---|---|---|---|
| **Objet** | Annoncer la promesse + nombre d'étapes | ≤50 car. | **A.** « Bienvenue chez {BU}, voici vos 3 prochaines étapes » · **B.** « Votre compte {BU} est prêt — 2 minutes pour démarrer » · **C.** « {Prénom}, bienvenue. On commence par où ? » |
| **Preheader** | Compléter — quantifier le temps + lever la friction « long » | ≤110 car. | « Activez votre compte en 3 étapes simples. Comptez 2 minutes maximum. » |
| **H1** (texte HTML) | Confirmer + cadrer | ≤60 car. | **A.** « Bienvenue chez {BU}. » · **B.** « Votre compte est prêt. » · **C.** « On démarre ensemble. » |
| **Sub-héro** | Annoncer le contenu en 1 phrase + durée | ≤20 mots | « 3 actions pour bien démarrer. **2 minutes** chrono. » |
| **Body** | 3 cards verticales numérotées — 1 phrase + 1 lien chacune. Structure modulaire bloc `body_3steps`. | — | ① Confirmer votre adresse · ② Télécharger l'app · ③ Envoyer ou suivre un colis |
| **CTA primaire** | Verbe d'action sur l'étape n°1 | ≤4 mots | **A.** « Activer mon compte » · **B.** « Commencer maintenant » · **C.** « Faire les 3 étapes » |
| **CTA secondaire** | Lien texte vers FAQ / centre d'aide | — | « Voir toutes les options » |
| **Signature** | Pas de signature personnelle. Le service parle. | — | — |

---

## 7. Direction visuelle

| Élément | Direction |
|---|---|
| **Image héro** | **Décorative**, jamais porteuse du H1. Sujet : un colis posé sur un meuble dans un intérieur lumineux, vue plongeante. Évite la livraison en cours (camions, livreurs) — on est *avant* l'action, pas *pendant*. Ratio 16:9, max 220px hauteur mobile. |
| **Couleurs** | Token BU `{COLOR_PRIMARY}` sur CTA et accents. Body en `#1a1a1a` sur fond `#fff`. Aucune couleur hors palette. |
| **Iconographie** | Numérotation simple `01 / 02 / 03` typo, pas d'icônes lifestyle. Si icônes : monochromes, line-style 1.5px. |
| **Lighting / mood** | Naturel, matinal. Pas de night-mode dans le visuel. |
| **Composition** | Aérée. Beaucoup de blanc autour du H1. CTA isolé visuellement (pas collé au body). |
| **Références** | Apple welcome email (composition aérée), Doctolib (numérotation), N26 onboarding (durée annoncée). |

---

## 8. Personnalisation

| Token | Source CDP | Usage recommandé | Fallback |
|---|---|---|---|
| `{Prénom}` | imagino base profil | Objet variante C, salutation body | « Bonjour, » |
| `{BU}` | déduit du domaine d'inscription | Objet, H1, signature | — (toujours présent) |
| `{Adresse_postale}` | imagino base profil | Étape ① (« confirmer votre adresse à `{Adresse_postale}` ») | Lien générique « confirmer mon adresse » |
| `{App_installée}` | imagino × Firebase | Si TRUE → masquer étape ② | Afficher étape ② |
| `{Préférence_langue}` | imagino préférences | Sélection de la version BU/langue à envoyer | Langue compte par défaut |

**Règle d'or** : si `{Prénom}` absent, la variante C (« {Prénom}, bienvenue ») ne part **pas**. Pas de fallback « , bienvenue ».

---

## 9. Mandatories

| Type | Mandatory |
|---|---|
| **Brand** | Logo BU 140px, palette officielle BU, sender name `{BU} — Bienvenue` |
| **Légal** | Mention RGPD du pays de la BU, adresse postale BU complète, lien désabonnement actif. CNIL (FR), GDPR (CZ/SK), FADP (CH), Privacy IT (BRT). |
| **Technique** | Wrapper 640px desktop / 100% mobile · responsive obligatoire · dark mode-ready · WCAG AA strict · compat Outlook 2007→M365 · bulletproof button CTA |
| **Conformité** | Tests Litmus ≥30 clients · validation axe-core · score SpamAssassin ≤2 · domaine sender SPF/DKIM/DMARC authentifié |

---

## 10. Test plan A/B/C

| Variable testée | Hypothèse | KPI lu | Significativité |
|---|---|---|---|
| **Objet** (A/B/C) | La quantification du temps (B) bat l'accueil générique (A). La personnalisation prénom (C) bat les deux si data ≥80% | Open rate | 95% confiance, ≥2 000 envois / variante |
| **H1** (A/B/C) | Variante action (« On démarre ensemble ») bat le formel (« Bienvenue ») sur CTR | CTR | 95% confiance |
| **CTA primaire** (A/B/C) | « Activer mon compte » (A) bat « Commencer » (B) car plus spécifique | Click-to-open | 95% confiance |

**Durée** : 14 jours minimum (trafic welcome ~constant) · **Allocation** : 33/33/33 · **Garde-fou** : stop si désabo &gt;0.3%

---

## 11. KPIs de succès

| KPI | Cible | Mesure | Garde-fou |
|---|---|---|---|
| **Primaire** | Activation J+7 (≥1 envoi de colis OU app installée) | ≥40% | — |
| **Secondaire 1** | Open rate | ≥35% (benchmark welcome) | délivrabilité ≥97% |
| **Secondaire 2** | CTR | ≥12% | — |
| **Secondaire 3** | Désabonnement | &lt;0.1% | stop si &gt;0.3% sur 1 cohorte |
| **Régression** | 0 régression Outlook sur 30 clients testés | 0 | — |

---

## 12. Constraints — ce qu'on ne fait PAS sur Welcome

- ❌ Pas de promo / réduction dans le welcome (on n'achète pas un destinataire qui vient d'arriver)
- ❌ Pas de push commercial agressif (« Profitez de notre offre… ») — c'est le rôle de Boost sales, pas du Welcome
- ❌ Pas de « N'hésitez pas à nous contacter » — c'est un cliché, on remplace par lien centre d'aide concret
- ❌ Pas de signature manuelle (le service institutionnel parle, pas Jean-Michel du SAV)
- ❌ Pas d'emoji dans l'objet (TTS variable + Outlook ne les rend pas tous)

---

## 13. Timeline

| Étape | Owner | Date |
|---|---|---|
| Brief validé Geopost | Lead CRM Geopost | 15 juin 2026 |
| First draft copy (3 variantes A/B/C) | Agent 02 CRO & UX Writing | 17 juin 2026 |
| First draft design (wireframe Figma + tokens) | Agent 03 Template Design | 18 juin 2026 |
| HTML intégré + tests Litmus 30 clients | Agent 04 HTML Integration | 22 juin 2026 |
| Review Geopost + BU locale (BRT pilote) | Lead CRM Geopost | 24 juin 2026 |
| Final corrections | Agents 02/03/04 selon scope | 25 juin 2026 |
| Push imagino sandbox BRT | Chef de projet agence | 26 juin 2026 |
| QA finale Geopost + go live BRT | Geopost CRM team | 29 juin 2026 |
| Réplication 4 autres BUs (tokens uniquement) | Agent 06 Multi-Brand | 6 juillet 2026 |

---

## 14. References & inspirations

- **Apple — welcome new Apple ID** · accueil aéré, 1 seul CTA, pas de promo. <span class="muted">Ce qu'on garde : la composition aérée.</span>
- **Doctolib — bienvenue post-inscription** · 3 étapes numérotées, durée annoncée. <span class="muted">Ce qu'on garde : la structure 3 étapes.</span>
- **N26 — first email** · ton confiant, pas condescendant, micro-copy précis. <span class="muted">Ce qu'on garde : le ton.</span>
- **Anti-référence** : welcome Booking / Airbnb post-COVID (lyrique, « bienvenue dans la grande famille des voyageurs »). <span class="muted">Ce qu'on évite.</span>

---

## 15. Sign-off

| Rôle | Nom | Date |
|---|---|---|
| Lead CRM Geopost | [À CONFIRMER GEOPOST] | — |
| Owner BU pilote BRT | [À CONFIRMER GEOPOST] | — |
| Lead créatif agence | [À COMPLÉTER AGENCE] | — |
| Chef de projet agence | [À COMPLÉTER AGENCE] | — |
