# ETUDE 03 — Osmose inverse par vagues : contrainte de pression
**2026-11-01 — analyse de dimension et benchmark scientifique, pas validation de machine.**

## Documents
- Historique : [US4512886A, 1985](https://patents.google.com/patent/US4512886A/en), « Wave-powered desalination of water » ; revendication d'une pompe entraînée par les vagues, pression d'environ 800 psi.
- Actuel : [Das, Frost, Folley & Brewster, Desalination, 2024](https://doi.org/10.1016/j.desal.2024.118064) : essai de RO par vagues avec une récupération d'énergie et ~3,5 kWh/m³ dans les conditions décrites, démonstrateur d'environ 2 m³/j.
- Alternative moderne : [revue 2025](https://doi.org/10.1016/j.dwt.2025.101236), 2–4 kWh/m³ RO selon les conditions et périmètres ; comparer installation complète sur eau potable livrée, et non énergie de membrane seule.

## Hypothèse et mesures
**H0 :** la chaîne de pompe à vagues ne procure aucun avantage en énergie, fiabilité ou coût total, à service rendu égal, par rapport au meilleur SWRO solaire contemporain.
**H1 :** à un site de houle et de coût électrique défini, un pompage mécanique direct à variabilité contrôlée produit un volume d'eau potable annuel à coût et émissions inférieurs à une référence.

Le simple fait que la pompe fonctionne n'est pas suffisant pour rejeter H0.

## Calcul illustratif
`p_Pa = psi × 6894.757293168`.
`E_feed_kWh_m3 = p_Pa / 3_600_000`.
`E_product_kWh_m3 = E_feed_kWh_m3 / (recovery_fraction × efficiency_pump)`.

À 800 psi et pompe parfaite, 1 m³ d'eau d'entrée représente **~1,532 kWh** de travail hydraulique ; ce chiffre dépend d'une pression constante supposée. Avec récupération de 10 %, il faut 10 m³ d'entrée pour 1 m³ de produit et le bilan pompe brut est **15,32 kWh/m³ d'eau produite**, sans récupération de l'énergie de saumure. Avec récupération de 40 %, il tombe à 3,83 kWh/m³, avant toutes les pertes auxiliaires. Ces chiffres **ne sont pas** des consommations d'usines.

Un récupérateur de pression améliore significativement le bilan. La littérature 2024 rapporte 3,5 kWh/m³ avec une pompe Clark ; l'égalité éventuelle entre calcul et mesure serait fortuite. La formule est **incapable** de simuler ce dispositif, la houle ou le rendement membrane sans mesures additionnelles.

## Épreuve contradictoire
- Une pression élevée n'implique pas une facture énergétique élevée si la saumure restitue son énergie de pression.
- Le coût d'achat d'une turbine, la corrosion, la météo marine et les rejets de saumure comptent autant que la dépense énergétique.
- Le dénominateur doit être le **m³ d'eau potable aux normes livré**, pas un volume de liquide pressurisé ni la capacité nominale d'un module.
- Les 3,5 kWh/m³ de l'essai 2024 doivent être lus dans leur définition méthodologique avant toute comparaison quantitative « supérieure/inférieure » au 2–4 kWh/m³ des RO modernes.

## Étapes de réplication
1. Obtenir courbes pression/débit réels, variabilité et rendement de récupération.
2. Relever qualité eau d'entrée, perméat, taux de rejet des sels, température et salinité.
3. Séparer énergie absorbée par module RO, énergie mécanique captée sur les vagues, conversion, auxiliaires, et coût.
4. Tester une même année météorologique contre PV+batterie+RO standard et calculer €/m³ livré.
5. Définir une règle d'arrêt si les gains apparents proviennent uniquement d'une comparaison mal normalisée.

[Script Python sans dépendance](../dessalement_vagues/ro_pressure_budget.py) et [tests unitaires](../../tests/test_ro_pressure_budget.py). **Les calculs sont des vérifications physiques, pas des essais de conversion d'énergie.**
