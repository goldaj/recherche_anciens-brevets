# CR 04 — Recherche approfondie par combinaisons de brevets
**Date : 2026-11-01.** Objet : priorisation contradictoire de dix assemblages ; lecture de revendications, rapprochement de publications, bilans conservatifs. **Pas de tests matériels ni de validation économique.**

## Faits consolidés
1. **Antériorité déjouant une fausse nouveauté :** [US4285702A (1981)](https://patents.google.com/patent/US4285702A/en) revendiquait déjà le stockage de froid à matériau à changement de phase, les capteurs, échangeurs et le solaire dans l'appareil d'adsorption d'eau atmosphérique. Le concept C01 peut encore être **optimisé**, mais pas qualifié de combinaison inédite.
2. **Expérience de 2025 confondue :** [Agrawal/Kumar](https://doi.org/10.1016/j.solmat.2024.113343) compare 4,25 L/j avec silice et PCM contre 4,40 L/j avec tamis moléculaire sans PCM. On **ne peut pas isoler l'effet du PCM**, deux paramètres ont changé. Étude factorielle contrôlée recommandée : même sorbant, PCM oui/non, nombre de cycles égal, conditions T/RH identiques et ordres randomisés.
3. **Houle + stockage pression :** [FR2378958A1](https://patents.google.com/patent/FR2378958A1/en) décrit déjà le flotteur pompant vers accumulateur. [Mi et al. 2023](https://doi.org/10.1016/j.apenergy.2023.121194) ont expérimenté une association proche en bassin à l'échelle 1:10. Leur salinité d'essai (3,5 g/L) n'est **pas la salinité marine 35 g/L**, et leurs extrapolations ne sont pas des essais grandeur nature. [Das et al. 2024](https://doi.org/10.1016/j.desal.2024.118064) ont testé un récupérateur Clark, avec SEC ~3,5 kWh/m³ dans leur montage.
4. **Stirling + PCM :** déjà expérimenté en [2026](https://doi.org/10.3389/fenrg.2026.1720534). L'intérêt original possible de C08 est une **optimisation de l'exergie** de chaleur rejetée pour désorption d'eau, pas la cogénération en général.
5. **Chaleur fatale + sorbant :** déjà démontré par [Chen et al. 2026](https://doi.org/10.1038/s41467-026-76774-z), avec batterie et MOF. La production d'eau utilise un **refroidisseur actif pour condenser** dans le montage de laboratoire : ne jamais présenter l'eau comme intégralement gratuite.
6. **Désorption vibratoire :** la [revue 2026](https://www.nature.com/articles/s44359-026-00154-5) décrit de faibles coûts d'énergie au niveau d'une *étape* de régénération. Ce n'est pas une mesure de la consommation énergétique d'une chaîne complète produisant de l'eau potable.

## Études paramétriques
[Calculs C02/C03/C08](../etudes/combinaisons/ETUDE_04_BILANS.md) et [code reproductible](../etudes/combinaisons/hybrid_budgets.py), [CSV](../resultats/assemblages_scenarios.csv) : **15 points** d'ordres de grandeur. Les valeurs numériques sont tirées des équations, sauf les hypothèses identifiées, qui sont **fictives**. L'exécution locale / CI est à consulter avant de les déclarer validées.

## Hiérarchie des prochaines preuves
- C01 : essai causal apparié sur AWH avec **même** sorbant, mêmes cycles ; gain eau/jour, auxiliaires et dégradation.
- C03 : commande adaptative de pression incluant récupérateur de saumure, via un modèle où les vagues sont une série temporelle et où la pression osmotique dépend de la salinité.
- C08 : carte d'exergie détaillée, températures de source et puits mesurées, comparaison directe sans Stirling et avec PV électrique.
- C09 : étude sur énergie de la chaîne complète (captage → extraction → condensation → eau potable) et non sur seul mécanisme ultrasonique.
- Développement plus large : prolonger le corpus hors eau/énergie. **Aucun verdict de brevetabilité ni de liberté d'exploitation**.

## Conclusion scientifique
La recherche par assemblage **élimine plusieurs propositions superficielles** plutôt qu'elle ne produit une invention spectaculaire. Les pistes solides sont des **problèmes d'intégration et de protocole expérimental**. Les manières de réfuter chacune sont détaillées dans la matrice et l'étude.
