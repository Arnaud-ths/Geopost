# Creative Brief — Template `Services`

## 0. Header

| Champ | Valeur |
|---|---|
| **Template** | Services — annonce nouvelle offre (ex. out-of-home / point relais / consigne) |
| **Famille** | One-shot (ou trigger sur life event) |
| **Version brief** | v1 — 11 mai 2026 |
| **Statut** | Draft — à valider Geopost |
| **BU concernées** | Toutes BUs où le service est disponible (variable selon offre) |
| **Owner agence** | Lead CRM Geopost V1 |
| **Owner Geopost** | [À CONFIRMER GEOPOST] |
| **Deadline first draft** | Variable — à la demande Geopost selon lancement offre |
| **Date d'envoi cible** | Au lancement de l'offre OU sur change life event |

---

## 1. Background & opportunity

Geopost a régulièrement de **nouvelles offres ou changements d'usage** à communiquer : point relais ajoutés, consigne 24/7, livraison sur RDV, options de retour, services premium. Sans communication dédiée, ces offres restent **invisibles** : le destinataire ne les découvre pas dans le flow transactionnel, et les emails commerciaux génériques ne suffisent pas.

L'opportunité : **éduquer**, pas argumenter. Quand on annonce une nouvelle option, on n'a pas besoin de la « vendre » — on a besoin que les gens **sachent qu'elle existe** et qu'ils comprennent **comment l'activer la prochaine fois**.

---

## 2. Single-minded proposition

> **Pour le destinataire qui a une habitude de livraison, Geopost ajoute une option qui résout une friction qu'il connaît — sans qu'il ait à changer quoi que ce soit aujourd'hui.**

---

## 3. Audience

| Dimension | Description |
|---|---|
| **Qui** | Base active 12 mois OU segment géographique selon disponibilité du service. Le bon ciblage est plus important ici que sur d'autres templates : annoncer un point relais à Bratislava à un destinataire de Cracovie = bruit. |
| **Statut Geopost** | Actifs avec une habitude établie (≥3 envois ou réceptions / an). |
| **Ce qu'ils savent déjà** | Leur usage actuel (livraison à domicile, par exemple). Ils sont **probablement satisfaits** — sinon ils auraient déjà migré. |
| **Ce qu'ils ressentent** | Neutres. Pas demandeurs. **Curiosité polie** si l'offre semble intéressante. |
| **Ce qu'ils veulent** | Que rien ne change forcément, mais que les options s'élargissent si besoin. |
| **Ce qui les freine** | Inertie habituelle. Peur de la complexité. Doute sur la disponibilité géo réelle. |

---

## 4. Insight clé

> **« Je ne change pas une habitude qui marche. Mais je veux savoir qu'il y a une porte de sortie si elle cesse de marcher. »**

Le destinataire ne va pas adopter l'option **immédiatement**. Il va la mémoriser comme **plan B disponible**. C'est ce plan B qui sera activé la prochaine fois qu'il sera **bloqué** par sa solution actuelle (absent à la livraison, pas chez lui, livreur passé sans sonner). On vend une **disponibilité mentale**, pas une conversion immédiate.

---

## 5. Tone of voice

| Ce qu'on est | Ce qu'on n'est PAS |
|---|---|
| **Pédagogue** — on explique, on n'argumente pas | **Vendeur** — pas de « ne ratez pas cette nouvelle offre » |
| **Factuel** — on dit *quand* c'est utile, pas pourquoi c'est génial | **Lyrique** — pas de « expérience révolutionnaire » |
| **Discret** — on n'insiste pas, on ne relance pas | **Insistant** — pas de séquence éducative à 5 emails |

**Mots interdits** + spécifiques : « innovation », « game changer », « disrupte », « expérience révolutionnaire », « ne ratez plus jamais ».

**Références de ton** : Notion changelog (factuel + utile), Stripe new feature (pédagogie + use cases), Ledger product update (sobre).

---

## 6. Hiérarchie de message — slot par slot

| Zone | Brief | Contrainte | Variantes A/B/C |
|---|---|---|---|
| **Objet** | Bénéfice usage clair, pas tagline | ≤50 car. | **A.** « Recevez vos colis quand vous voulez » · **B.** « 5 000 points relais {BU} près de chez vous » · **C.** « Une option en plus pour vos prochaines livraisons » |
| **Preheader** | Localiser, quantifier | ≤110 car. | « Le plus proche est peut-être à 3 minutes. Disponible dans votre zone de livraison. » |
| **H1** (texte HTML) | Bénéfice ou cas d'usage | ≤60 car. | **A.** « Le point relais qui vous arrange. » · **B.** « Vos colis, à 3 minutes de chez vous. » · **C.** « Une option en plus, sans changer le reste. » |
| **Sub-héro** | Annonce contenu | ≤20 mots | « 5 000 points relais {BU}. Active en 1 clic dans votre prochain envoi. » |
| **Body** | Bloc `body_3steps` : « Comment ça marche » en 3 étapes + bloc `body_2col` 2 cas d'usage concrets | — | ① Choisir l'option à la commande · ② Recevoir le code de retrait · ③ Récupérer aux horaires qui vous arrangent |
| **CTA primaire** | Action utile (pas « profiter ») | ≤4 mots | **A.** « Trouver mon point relais » · **B.** « Voir la carte » · **C.** « Activer pour ma prochaine livraison » |
| **CTA secondaire** | Lien centre d'aide | — | « Voir toutes les options de livraison » |
| **Signature** | Service institutionnel | — | — |

---

## 7. Direction visuelle

| Élément | Direction |
|---|---|
| **Image héro** | **Décorative**. Selon l'offre : devanture de point relais (façade simple, pas zoom marketing), consigne automatique en gros plan, intérieur d'épicerie où sont les points relais. **Authentique**, pas studio. |
| **Couleurs** | Tokens BU stricts. Si l'offre a un sous-branding (ex. logo « Pickup »), respecter la palette officielle de ce sous-brand. |
| **Iconographie** | Pictos line-style monochromes pour les 3 étapes. Pas d'icônes lifestyle. |
| **Lighting / mood** | Quotidien, fonctionnel. Pas de mise en scène. |
| **Composition** | Aérée. Les 3 étapes en hiérarchie claire. CTA bien isolé. |
| **Références** | Notion changelog, Stripe product launch email, Ledger update email. |

---

## 8. Personnalisation

| Token | Source CDP | Usage recommandé | Fallback |
|---|---|---|---|
| `{Prénom}` | imagino base | Optionnel | Aucun |
| `{BU}` | déduit | Partout | — |
| `{Code_postal_principal}` | imagino base | Sub-héro « 3 points relais à {CP} ou autour » | Affichage générique « près de chez vous » |
| `{Nb_points_relais_zone}` | imagino × API points relais | Si ≥3 → afficher; sinon → masquer ce bloc | Bloc remplacé par « disponible dans plus de 5 000 lieux » |
| `{Service_disponible_zone}` | imagino × API services par zone | **Trigger** : si FALSE → email **non envoyé** | — |

**Règle d'or absolue** : **on n'envoie pas un email Services pour un service indisponible dans la zone du destinataire**. C'est la régression marketing #1 sur ce template. Validation obligatoire.

---

## 9. Mandatories

| Type | Mandatory |
|---|---|
| **Brand** | Logo BU + éventuel logo sous-brand officiel (« Pickup », « Locker »…). Palette officielle. Aucun bricolage visuel. |
| **Légal** | Mention RGPD pays, adresse postale BU, lien désabonnement. Si l'offre a des conditions tarifaires différentes → mention claire en footer (pas en small print 8px). |
| **Technique** | Wrapper 640px desktop / 100% mobile · responsive · dark mode · WCAG AA · compat Outlook · bulletproof button |
| **Ciblage** | Validation API services par zone géo destinataire OBLIGATOIRE. Pas d'envoi blind. |
| **Anti-spam** | Pas de superlatifs dans l'objet, score SpamAssassin ≤1.5 |

---

## 10. Test plan A/B/C

| Variable testée | Hypothèse | KPI lu | Significativité |
|---|---|---|---|
| **Angle objet** (A bénéfice usage / B quantification / C minimisation) | C (« option en plus ») bat A et B sur taux d'adoption longue (60j) car ne crée pas de pression | Adoption rate J+60 | 95% confiance, ≥3 000 envois / variante |
| **Insertion `{Code_postal_principal}`** | La localisation explicite double le CTR | CTR | 95% confiance |
| **3 étapes vs 5 étapes** | Le 3-step bat le 5-step même si l'offre est plus complexe — capacité d'attention email | CTR + adoption | 95% confiance |

**Durée** : 60 jours (mesure d'adoption longue) · **Allocation** : 33/33/33 · **Garde-fou** : stop si désabo &gt;0.2%.

---

## 11. KPIs de succès

| KPI | Cible | Mesure | Garde-fou |
|---|---|---|---|
| **Primaire** | Adoption du service à J+60 (≥1 utilisation) | ≥4% | — |
| **Secondaire 1** | Open rate | ≥25% (audience non-demandeuse) | — |
| **Secondaire 2** | CTR | ≥7% | — |
| **Secondaire 3** | Désabonnement | &lt;0.1% | stop si &gt;0.2% |
| **Mémorisation** | % « connaît cette option » dans survey post-3mois | +10 points vs baseline | — |
| **Régression** | 0 régression Outlook | 0 | — |

---

## 12. Constraints — ce qu'on ne fait PAS

- ❌ Pas d'envoi blind sans validation disponibilité zone
- ❌ Pas de séquence Services (1 seul email par offre, pas de relance)
- ❌ Pas de promo de lancement (« -10% sur les 100 premiers ») — le template Services n'est pas un template promo, c'est éducatif
- ❌ Pas de comparatif avec d'autres options Geopost (« mieux que la livraison à domicile ») — on ne dénigre pas le service de base
- ❌ Pas de FOMO (« lancement limité »)
- ❌ Pas de plus de 3 cas d'usage dans le body — au-delà, perte d'attention

---

## 13. Timeline

| Étape | Owner | Date |
|---|---|---|
| Brief validé Geopost (à la demande de lancement) | Lead CRM Geopost | Variable |
| Cartographie zones de disponibilité | Geopost ops | -10j vs envoi |
| First draft copy 3 variantes | Agent 02 | -7j |
| First draft design + visuels | Agent 03 | -5j |
| HTML intégré + tests Litmus | Agent 04 | -3j |
| Push imagino sandbox + ciblage CDP | Chef projet | -2j |
| Go live | Geopost | J0 |
| Lecture résultats J+60 | Lead CRM + Geopost | J+60 |

---

## 14. References & inspirations

- **Notion** — changelog email · pédagogie, 3 use cases. <span class="muted">Ce qu'on garde : la structure.</span>
- **Stripe** — new feature email · factuel, exemples concrets. <span class="muted">Ce qu'on garde : le ton.</span>
- **Ledger** — product update · pas de FOMO, juste l'info. <span class="muted">Ce qu'on garde : la sobriété.</span>
- **Anti-référence** : SFR / Orange « nouvelle offre exclusive » (FOMO, comparatifs).

---

## 15. Sign-off

| Rôle | Nom | Date |
|---|---|---|
| Lead CRM Geopost | [À CONFIRMER GEOPOST] | — |
| Owner BU | [À CONFIRMER GEOPOST] | — |
| Product owner du service annoncé | [À CONFIRMER GEOPOST] | — |
| Ops Geopost (validation zones) | [À CONFIRMER GEOPOST] | — |
| Lead créatif agence | [À COMPLÉTER AGENCE] | — |
