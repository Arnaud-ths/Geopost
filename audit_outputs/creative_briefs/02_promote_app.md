# Creative Brief — Template `Promote mobile app download`

## 0. Header

| Champ | Valeur |
|---|---|
| **Template** | Promote mobile app download |
| **Famille** | Trigger automatisé |
| **Version brief** | v1 — 11 mai 2026 |
| **Statut** | Draft — à valider Geopost |
| **BU concernées** | BRT, DPD CH, DPD CZ, DPD SK (Geopost corp = pas d'app utilisateur final → exclu) |
| **Owner agence** | Lead CRM Geopost V1 |
| **Owner Geopost** | [À CONFIRMER GEOPOST] |
| **Deadline first draft** | 13 juin 2026 |
| **Date d'envoi cible** | J+7 après création de compte si app non installée. 1 relance à J+21 si toujours pas d'install. |

---

## 1. Background & opportunity

Le destinataire a créé un compte web il y a 7 jours mais n'a pas téléchargé l'app mobile. Pour Geopost, l'**app est le canal le plus rentable** : opt-in notifications push (vs. SMS payant), engagement quotidien (consultation tracking), upsell d'options livraison. Un destinataire avec app = ~3× plus de valeur par an qu'un destinataire web-only.

L'opportunité : convertir le doute mobile en install **sans paraître promotionnel**. L'app n'est pas un produit en plus — c'est *le même service*, plus pratique.

---

## 2. Single-minded proposition

> **Pour le destinataire qui suit ses colis sur web, Geopost mobile est le même service qu'il connaît déjà — mais dans sa poche, avec les notifications qu'il manque aujourd'hui.**

---

## 3. Audience

| Dimension | Description |
|---|---|
| **Qui** | Tous comptes B2C 28-55 ans sans install app détectée. Exclus : SME B2B (parcours Singular). |
| **Statut Geopost** | J+7 post-création. A donc *au moins* commencé à utiliser le web (sinon il serait dans le funnel d'activation, pas le push app). |
| **Ce qu'ils savent déjà** | Le tracking colis sur le web. La marque. Probablement vu une mention de l'app pendant l'inscription. |
| **Ce qu'ils ressentent** | Indifférent à l'app. *« Je m'en sors très bien sans. »* Ou méfiance : *« Encore une app de plus sur mon téléphone. »* |
| **Ce qu'ils veulent** | Ne pas être encombré. Recevoir leurs colis sans surveiller. |
| **Ce qui les freine** | Stockage, RAM, énième notification, doute sur la valeur ajoutée réelle vs. SMS / email actuels. |

---

## 4. Insight clé

> **« Je ne télécharge pas une app pour avoir une app. Je la télécharge quand je manque concrètement quelque chose sans elle. »**

Le destinataire ne veut pas « l'app Geopost ». Il veut **savoir où est son colis sans avoir à ouvrir son ordinateur, sans avoir à scroller dans ses emails à 18h depuis le métro**. L'app est la réponse à ce moment précis, pas une feature.

---

## 5. Tone of voice

| Ce qu'on est | Ce qu'on n'est PAS |
|---|---|
| **Utilitaire** — on parle de moments de vie, pas de features | **Tech-bro** — pas de « expérience native » ou « stack mobile » |
| **Honnête** — on assume qu'une app de plus, ça pèse | **Vendeur** — pas de « la meilleure app de livraison » |
| **Spécifique** — on cite *quels* moments | **Générique** — pas de « pour tout suivre, tout le temps » |

**Mots interdits** + spécifiques : « révolution mobile », « expérience inégalée », « tout-en-un ».

**Références de ton** : Vinted promote app (utilitaire, cite des moments), Yuka (bénéfice tangible), pas Klarna (trop vendeur).

---

## 6. Hiérarchie de message — slot par slot

| Zone | Brief | Contrainte | Variantes A/B/C |
|---|---|---|---|
| **Objet** | Promesse de **moment** plus que de produit | ≤50 car. | **A.** « Suivez vos colis en temps réel. L'app {BU}. » · **B.** « {Prénom}, ne ratez plus jamais une livraison » · **C.** « 3 secondes pour savoir où est votre colis » |
| **Preheader** | Compléter avec les 3 bénéfices clés | ≤110 car. | « Notifications, tracking, modifications de dernière minute — tout depuis votre mobile. » |
| **H1** (texte HTML) | Bénéfice tangible court | ≤60 car. | **A.** « Vos colis, dans votre poche. » · **B.** « Plus besoin de chercher. » · **C.** « 3 secondes au lieu de 30. » |
| **Sub-héro** | Mode d'emploi en 1 phrase | ≤20 mots | « L'app {BU} sur App Store et Google Play. Installation en moins d'1 minute. » |
| **Body** | 3 bénéfices concrets — bloc `body_3cards` ou `body_3steps` | 1 phrase chacun | ① 📍 Tracking temps réel · ② 🔔 Notifications push (jamais de SMS) · ③ ⚙️ Modifier la livraison en 1 tap |
| **CTA primaire** | 2 boutons juxtaposés (bloc `cta_double`) — App Store + Google Play | 2 boutons ≥44px chacun | Boutons : « App Store » + « Google Play » avec deep links |
| **CTA secondaire** | Lien texte vers QR code (desktop) | — | « Voir le QR code (depuis ordinateur) » |
| **Signature** | Pas de signature personnelle | — | — |

---

## 7. Direction visuelle

| Élément | Direction |
|---|---|
| **Image héro** | **Décorative** — main tenant un smartphone (cropped) avec interface app blurrée. Suggère, ne montre pas. Pas de screenshot lisible (devient obsolète). Ratio 16:9. |
| **Couleurs** | Tokens BU. App Store / Play badges en versions officielles obligatoires (noir sur fond clair, blanc sur fond sombre). |
| **Iconographie** | Emoji autorisés *uniquement* dans les 3 cards (📍 🔔 ⚙️) — sinon icônes monochromes line-style. Pas d'icônes dans header / footer. |
| **Lighting / mood** | Quotidien, intérieur. Pas de hero shot studio. |
| **Composition** | CTA app+play centrés, isolés visuellement. QR code dans bloc séparé sous CTA. |
| **Références** | Vinted app push email, Deliveroo "get the app" (bénéfice-driven), pas Klarna (trop produit). |

---

## 8. Personnalisation

| Token | Source CDP | Usage recommandé | Fallback |
|---|---|---|---|
| `{Prénom}` | imagino base | Objet variante B | « Vous » impersonnel |
| `{BU}` | déduit | Objet, H1, signature | — |
| `{Dernier_envoi_date}` | imagino transactions | Si récent (≤30j) → preheader « Votre dernier colis : {DATE}. La prochaine fois, depuis votre mobile. » | Preheader générique |
| `{OS_détecté}` | UA détecté côté web précédent | Réordonne App Store / Play en fonction (iOS-first ou Android-first) | App Store en premier (défaut FR/IT) |

**Règle d'or** : si OS inconnu → ordre App Store / Google Play par défaut. Pas de « Choisissez votre OS ».

---

## 9. Mandatories

| Type | Mandatory |
|---|---|
| **Brand** | Logo BU + badges officiels Apple (« Download on the App Store ») et Google (« Get it on Google Play ») — utiliser les versions localisées dans la langue de la BU |
| **Légal** | Mention permissions app (« avec votre accord, l'app vous enverra des notifications push »), RGPD du pays de la BU, lien désabonnement, adresse postale BU |
| **Technique** | Deep links Universal Link (iOS) + App Link (Android), UTM standardisés `utm_source=email&utm_medium=trigger&utm_campaign=promoteapp&utm_content={BU}` |
| **Tracking** | Attribution Firebase / AppsFlyer côté CDP — feedback install sous 24h pour pause campagne |

---

## 10. Test plan A/B/C

| Variable testée | Hypothèse | KPI lu | Significativité |
|---|---|---|---|
| **Objet** (A/B/C) | La quantification du temps (C: « 3 secondes ») bat la promesse fonctionnelle (A) sur open. La personnalisation prénom (B) maximise si data ≥80%. | Open rate | 95% confiance, ≥3 000 envois / variante |
| **H1** (A/B/C) | Le bénéfice émotionnel « plus besoin de chercher » (B) bat les bénéfices fonctionnels (A, C) sur CTR | CTR | 95% confiance |
| **Ordre Apple/Play** | Auto-détection OS bat affichage statique sur install attribution | Install rate | 95% confiance |

**Durée** : 21 jours · **Allocation** : 33/33/33 · **Garde-fou** : stop si désabo &gt;0.4% (push email avec relance = sensible)

---

## 11. KPIs de succès

| KPI | Cible | Mesure | Garde-fou |
|---|---|---|---|
| **Primaire** | Install rate (clic → install) | ≥15% | — |
| **Primaire bis** | First open dans les 48h post-install | ≥70% | — |
| **Secondaire 1** | Open rate | ≥28% | délivrabilité ≥97% |
| **Secondaire 2** | CTR | ≥10% | — |
| **Secondaire 3** | Désabonnement | &lt;0.2% | stop si &gt;0.4% |

---

## 12. Constraints — ce qu'on ne fait PAS

- ❌ Pas de screenshot d'app lisible (deviendrait obsolète à chaque update UI)
- ❌ Pas de promo « première commande -10% avec l'app » (l'app ne se vend pas, elle se justifie par l'usage)
- ❌ Pas de « notre app a été notée 4.8/5 » (vendeur, contre l'insight)
- ❌ Pas plus de 3 bénéfices dans le body — au-delà, on perd l'attention
- ❌ Pas de FOMO (« Téléchargez avant qu'il ne soit trop tard »)

---

## 13. Timeline

| Étape | Owner | Date |
|---|---|---|
| Brief validé Geopost | Lead CRM Geopost | 22 juin 2026 |
| First draft copy (3 variantes A/B/C) | Agent 02 | 24 juin 2026 |
| First draft design + badges localisés | Agent 03 | 26 juin 2026 |
| HTML intégré + tests deep links | Agent 04 | 1 juillet 2026 |
| Review Geopost + BU pilote (BRT) | Lead CRM | 3 juillet 2026 |
| Push imagino sandbox BRT | Chef projet | 6 juillet 2026 |
| Go live BRT + tracking attribution | Geopost | 8 juillet 2026 |
| Réplication 3 autres BUs (DPD CH/CZ/SK) | Agent 06 | 15 juillet 2026 |

---

## 14. References & inspirations

- **Vinted** — "L'app, c'est tout de suite plus pratique" · ton utilitaire, cite des moments. <span class="muted">Ce qu'on garde : la spécificité des moments.</span>
- **Deliveroo** — push app post-1er order · bénéfice tangible, pas de FOMO. <span class="muted">Ce qu'on garde : la sobriété du CTA.</span>
- **Yuka** — bénéfice émotionnel ("ne plus se demander si c'est bon"). <span class="muted">Ce qu'on adapte : "ne plus se demander où est mon colis".</span>
- **Anti-référence** : Klarna app push (vendeur, « débloquez votre expérience shopping »).

---

## 15. Sign-off

| Rôle | Nom | Date |
|---|---|---|
| Lead CRM Geopost | [À CONFIRMER GEOPOST] | — |
| Owner BU pilote (BRT) | [À CONFIRMER GEOPOST] | — |
| Owner App produit Geopost | [À CONFIRMER GEOPOST] | — |
| Lead créatif agence | [À COMPLÉTER AGENCE] | — |
