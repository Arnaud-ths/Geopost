# Creative Brief — Template `Commercial peak`

## 0. Header

| Champ | Valeur |
|---|---|
| **Template** | Commercial peak — Noël / Black Friday / Saint-Valentin |
| **Famille** | One-shot (campagne saisonnière) |
| **Version brief** | v1 — 11 mai 2026 |
| **Statut** | Draft — à valider Geopost |
| **BU concernées** | BRT, DPD CH, DPD CZ, DPD SK + Geopost corp B2B (Noël uniquement, sans BF / SV) |
| **Owner agence** | Lead CRM Geopost V1 |
| **Owner Geopost** | [À CONFIRMER GEOPOST] |
| **Deadline first draft** | 1 septembre 2026 (Peak Noël en première fenêtre live) |
| **Date d'envoi cible** | Fenêtres fixes : Noël (mi-nov → 22 déc), Black Friday (semaine du BF, 24-30 nov 2026), Saint-Valentin (1-13 fév) |

---

## 1. Background & opportunity

Les fenêtres saisonnières représentent **40-55% du volume annuel** chez les transporteurs grand public selon les BUs. Noël seul = ~25%. C'est **le moment où Geopost peut gagner ou perdre** la mind share annuelle : un client qui a une bonne expérience à Noël reste; un client qui rate l'envoi de cadeaux part chez le concurrent l'année suivante.

L'opportunité : devenir le **partenaire de tranquillité** sur les moments à enjeu fort, *sans participer au bruit FOMO* de la période (qui sature les inbox). La différenciation se joue sur le ton, pas sur la promo.

---

## 2. Single-minded proposition

> **Pour le destinataire qui a des cadeaux à envoyer à temps, Geopost est le seul service qui s'engage sur des délais garantis — pour qu'il puisse penser à autre chose qu'à la livraison.**

---

## 3. Audience

| Dimension | Description |
|---|---|
| **Qui** | Base active 12 derniers mois. Exclus : inactifs &gt;180j, comptes flagués churn risk. Sur Geopost corp : décideurs B2B / responsables expédition. |
| **Statut Geopost** | Actifs. Sensibles au calendrier (ils savent que Noël arrive, mais sous-estiment toujours les délais). |
| **Ce qu'ils savent déjà** | Qu'il faut s'y prendre tôt. Qu'il y a des délais. Ils ne savent pas *exactement* lesquels. |
| **Ce qu'ils ressentent** | Stress montant à mesure que la fenêtre approche. **Pas encore** à J-21, **clairement** à J-7. |
| **Ce qu'ils veulent** | Que les cadeaux arrivent à temps, point. Pas découvrir un nouveau service. Pas une promo. |
| **Ce qui les freine** | Inertie (« j'ai le temps »), peur des frais imprévus (express), confusion sur les délais réels par destination. |

---

## 4. Insight clé

> **« À Noël, je n'achète pas un service de livraison. J'achète la promesse que je n'aurai pas à m'inquiéter. »**

Le destinataire pendant la fenêtre Peak ne pense pas en termes de prix ou de feature. Il pense en termes de **risque** : et si ça arrive après le 24 ? Et si c'est cassé ? Et si je dois courir le 23 acheter un cadeau de remplacement ? Geopost vend une **assurance émotionnelle**, pas une prestation logistique.

---

## 5. Tone of voice

| Ce qu'on est | Ce qu'on n'est PAS |
|---|---|
| **Rassurant** — on dit « c'est promis » et on tient | **FOMO** — pas de « Plus que 48h ! » |
| **Précis** — on donne les délais réels par destination | **Magique** — pas de « la magie de Noël arrive » |
| **Calme** — l'email respire, contre-courant du bruit de la période | **Excitant** — pas de tons criards, pas de gif paillette |

**Mots interdits** + spécifiques : « magique », « féérique », « ultime », « urgence », « dernière chance ». Et pas d'émoji 🎄🎁 dans l'objet — trop générique, filtres anti-spam.

**Références de ton** : John Lewis Christmas (émotion sobre — pour le ton, pas le copy), Mr Porter holiday gifting (factuel + élégant), Bonne Maman Noël (assumé, calme). **Anti-référence : Wish / Temu** (tout ce qu'on évite).

---

## 6. Hiérarchie de message — slot par slot

### Architecture campagne — 3 emails en séquence

| Email | Timing | Mission | Objet |
|---|---|---|---|
| **#1 Anticipation** | J-21 | « Pensez-y maintenant, pas plus tard. » | « Vos cadeaux à temps. C'est promis. » |
| **#2 Information** | J-14 | « Voici les délais exacts par destination. » | « 14 jours avant Noël : combien de temps pour chaque pays ? » |
| **#3 Last call** | J-7 | « Encore possible. Voici comment. » | « Encore 7 jours. Voici les options garanties. » |

### Email #1 (Anticipation) — détail

| Zone | Brief | Variantes A/B/C |
|---|---|---|
| **Objet** | Promesse engageante, sans FOMO | **A.** « Vos cadeaux à temps. C'est promis. » · **B.** « Encore 21 jours. Largement le temps de bien faire. » · **C.** « Noël arrive le 25. Vos colis : quand vous décidez. » |
| **Preheader** | Argumenter l'anticipation | « Plus on s'y prend tôt, moins on stresse. Les délais garantis {BU} pour chaque destination. » |
| **H1** | Apaiser | « Encore 21 jours. Largement le temps. » |
| **Sub-héro** | Concret | « Pour la France, comptez {Delai_FR} jours ouvrés. Pour {Pays_top}, {Delai_pays}. » |
| **Body** | Bloc `body_2col` — colonne gauche : délais par destination · colonne droite : options express. | — |
| **CTA primaire** | Action utile | « Voir les délais par destination » |
| **CTA secondaire** | Soft | « Modifier mes préférences d'envoi » |

---

## 7. Direction visuelle

| Élément | Direction |
|---|---|
| **Image héro** | **Décorative**. Sujet : un colis emballé soigneusement, posé sur une table en bois. Pas de sapin, pas de paillettes, pas de neige. **Subtilité** plutôt que cliché Noël. Pour BF : même registre, ton plus sombre. Pour SV : même registre, accent rose discret. |
| **Couleurs** | Tokens BU stricts. Pas de rouge/vert Noël hors palette officielle. Si BU autorise palette saisonnière → fournie en token séparé `{COLOR_SEASONAL}`. |
| **Iconographie** | Minimaliste. Numérotation typo pour les délais. Pas d'icône cadeau / coeur kitsch. |
| **Lighting / mood** | Lumière naturelle, fin de journée. Pas de mise en scène théâtrale. |
| **Composition** | Très aérée. L'email respire — message visuel de calme. Beaucoup de blanc. |
| **Références** | Mr Porter holiday email (élégance, sobriété), John Lewis (émotion contenue), Bonne Maman Noël 2024 (assumé sans surenchère). |

---

## 8. Personnalisation

| Token | Source CDP | Usage recommandé | Fallback |
|---|---|---|---|
| `{Prénom}` | imagino base | Optionnel — pas dans objet | Aucun |
| `{BU}` | déduit | Partout | — |
| `{Delai_FR}` | imagino business rules | Body délais — toujours présent | Valeur par défaut BU |
| `{Pays_top}` + `{Delai_pays}` | imagino × historique destinataire | Sub-héro — destination la plus envoyée par ce destinataire | Affiche 3 destinations populaires de la BU |
| `{Dernière_destination_envoi}` | imagino transactions | Body sur email #2 (information) | Ignorer |
| `{Code_express}` | génération CDP | Email #3 last call uniquement | — (variante non envoyée) |

**Règle d'or** : les délais doivent être **dynamiques** et reflèter la vraie disponibilité côté ops (ex. si réseau saturé sur SK → délais affichés = délais ajustés, pas brochure). Sinon perte de confiance lourde.

---

## 9. Mandatories

| Type | Mandatory |
|---|---|
| **Brand** | Logo BU, palette officielle, ton charte. Aucune palette « Noël générique » non-validée par chaque BU. |
| **Légal** | Mention RGPD pays, adresse postale BU, lien désabonnement, **mention conditions garantie délai** complète et lisible (≥10px). |
| **Technique** | Wrapper 640px desktop / 100% mobile · responsive · dark mode-ready · WCAG AA · compat Outlook · bulletproof button |
| **Synchro ops** | Délais affichés = délais validés ops 7j avant l'envoi. Process de gel des délais documenté. Risque réputationnel énorme si non respecté. |
| **Anti-saturation** | Pas plus de 2 emails Peak / fenêtre / compte. Si Boost sales actif en parallèle → priorité Peak, Boost gelé. |

---

## 10. Test plan A/B/C

| Variable testée | Hypothèse | KPI lu | Significativité |
|---|---|---|---|
| **Objet** (A promesse / B durée / C contrôle) | Variante C (« Quand vous décidez ») gagne sur audience CSP+ — variante A (« promis ») plus consensuelle | Open rate + perception marque post-survey | 95% confiance |
| **Visuel héro** (sobre vs. saisonnier modéré) | Le sobre bat le saisonnier sur tout segment 35+ | CTR + désabo | 95% confiance |
| **Séquence 1 vs 3 emails** | La séquence complète (3) bat 1 seul email sur volume d'expéditions, **sans** augmenter le désabo | Volume expéditions fenêtre | 95% confiance |

**Durée** : 1 fenêtre complète (= 21 jours pour Noël). **Allocation** : 33/33/33 sur l'objet, 50/50 sur le visuel. **Garde-fou** : stop si désabo &gt;0.4% sur 1 cohorte.

---

## 11. KPIs de succès

| KPI | Cible | Mesure | Garde-fou |
|---|---|---|---|
| **Primaire** | Volume d'expéditions sur la fenêtre vs N-1 | +15% vs N-1 | — |
| **Secondaire 1** | Open rate | ≥30% (campagne saisonnière) | délivrabilité ≥97% |
| **Secondaire 2** | CTR | ≥8% | — |
| **Secondaire 3** | Désabonnement | &lt;0.2% | stop si &gt;0.4% sur séquence |
| **Brand health** | % « Geopost = livraison fiable » dans post-Peak survey | +5 points vs baseline | — |
| **Régression** | 0 délai non tenu sur les comptes ayant ouvert l'email | 0 | **rétractation publique** si non |

---

## 12. Constraints — ce qu'on ne fait PAS

- ❌ Pas de countdown animé GIF (rendu Outlook cassé + ton FOMO)
- ❌ Pas de « Plus que X heures ! » dans l'objet
- ❌ Pas de visuel cliché (sapin paillettes, Père Noël) sauf validation BU explicite (et même là : on déconseille)
- ❌ Pas de promo dans l'email Peak (la promo c'est Boost — Peak vend la fiabilité, pas le prix)
- ❌ Pas d'emoji 🎄🎁🎅 dans l'objet
- ❌ Pas d'envoi de Peak après J-3 (au-delà, c'est cruel et inutile — express dispo dans l'app suffit)

---

## 13. Timeline

| Étape | Owner | Date |
|---|---|---|
| Brief validé Geopost (campagne Noël) | Lead CRM Geopost | 5 octobre 2026 |
| Validation délais ops par BU | Geopost ops | 12 octobre 2026 |
| First draft copy 3 emails séquence | Agent 02 | 15 octobre 2026 |
| First draft design séquence | Agent 03 | 20 octobre 2026 |
| HTML intégré + tests Litmus | Agent 04 | 27 octobre 2026 |
| Review Geopost + BUs | Lead CRM | 3 novembre 2026 |
| Push imagino sandbox | Chef projet | 6 novembre 2026 |
| Go live email #1 (J-21) | Geopost | mi-novembre 2026 |
| Go live email #2 (J-14) | Geopost | fin novembre 2026 |
| Go live email #3 (J-7) | Geopost | mi-décembre 2026 |
| Bilan campagne | Lead CRM + Geopost | 5 janvier 2027 |

---

## 14. References & inspirations

- **Mr Porter** — holiday gifting · sobriété, élégance, délais clairs. <span class="muted">Ce qu'on garde : le ton.</span>
- **John Lewis** — Christmas campaign · émotion contenue. <span class="muted">Ce qu'on garde : l'apaisement.</span>
- **Patagonia** — Black Friday "don't buy this" · contre-courant assumé. <span class="muted">Ce qu'on s'autorise : assumer le contre-courant.</span>
- **Bonne Maman** — Noël 2024 · saisonnier sans surenchère. <span class="muted">Ce qu'on adapte : la mesure.</span>
- **Anti-référence** : Wish / Temu / Shein Black Friday (countdown, MAJ, paillettes).

---

## 15. Sign-off

| Rôle | Nom | Date |
|---|---|---|
| Lead CRM Geopost | [À CONFIRMER GEOPOST] | — |
| Owner BU | [À CONFIRMER GEOPOST] | — |
| Ops Geopost (validation délais) | [À CONFIRMER GEOPOST] | — |
| Legal Geopost (mention garantie délai) | [À CONFIRMER GEOPOST] | — |
| Lead créatif agence | [À COMPLÉTER AGENCE] | — |
