# Protocole préenregistré C01 — Quantifier l'effet causal du PCM dans une récupération d'eau atmosphérique

**Version 0.1, 2026-11-01 ; plan seulement, aucun essai effectué.**

## Problème
Un [article de 2025](https://doi.org/10.1016/j.solmat.2024.113343) compare un montage **PCM + gel de silice** à un montage **sans PCM + tamis moléculaire**. Cette comparaison ne permet pas d'estimer l'effet isolé du matériau PCM. Les revendications de [US4285702A (1981)](https://patents.google.com/patent/US4285702A/en) incluaient déjà un réservoir capable de changer de phase.

## Essai factoriel : 2 × 2 (avant l'ajout éventuel d'un caloduc)
| Condition | Sorbant | Stockage froid PCM |
|---|---|---|
| A | gel de silice | NON |
| B | gel de silice | OUI |
| C | tamis moléculaire | NON |
| D | tamis moléculaire | OUI |

La variable d'intérêt n'est **pas** B–C. Les contrastes pour mesurer l'effet du PCM sont B–A et D–C ; un effet d'interaction est (B–A)–(D–C). Prévoir un volet séparé « caloduc OUI/NON » **uniquement si** cette première analyse montre une limite thermique identifiée et reproductible.

## Paramètres à contrôler
- Même surface de capteur, orientation, exposition et flux d'air ; humidité, température, pression et irradiation **enregistrées en continu**.
- Même masse sèche du sorbant ou deux normalisations explicitement distinguées (g eau/kg sorbant et L eau/m² capteur/jour).
- Même durée des phases adsorption/désorption, même température de fin de régénération et même **état de charge initial du PCM**.
- Même architecture de condensateur ; suivre puissance auxiliaire, chaleur fournie, eau collectée, teneur en sels et contamination.
- Randomiser l'ordre des configurations entre journées/blocs. Attention aux effets de météo, de mémoire de sorbant et de rémanence PCM.
- Répéter sur **journées ou blocs réellement indépendants** ; ne pas compter les multiples minutes d'une même journée comme réplicats indépendants.

## Critères fixés avant relevé
- Principal : **litres d'eau potable collectés par jour et par m²** sous contraintes climatiques appariées (ou L/kg sorbant sous hypothèse secondaire).
- Énergie : kWh électriques/m³ et kWh thermiques/m³, séparés ; qualité et taux de récupération des condensats.
- Secondaires : nombre de cycles, durabilité, dégradation des sorbants, coût du système et entretien.
- **Résultat négatif parfaitement recevable** si le PCM n'apporte pas d'amélioration robuste, dégrade le coût ou augmente la puissance des auxiliaires.
- Fixer la taille d'échantillon **après un pilote non utilisé pour conclure**, avec variance observée et différence minimale d'intérêt préalablement justifiée. Ne pas inventer de « significativité » avant données.

## Publication attendue
Données CSV brutes par bloc, code de calcul, intervalles de confiance adaptés, contrôle des comparaisons, CR documentant les exclusions et figures. Aucune manipulation d'adsorbants, machines sous pression ou dispositifs électriques humides sans analyse de risque et encadrement adapté.
