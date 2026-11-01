# Matrice d'assemblages techniques : dix hypothèses

**Date :** 2026-11-01. [Catalogue exploitable](../data/combinaisons.csv) | [Sources vérifiées](SOURCES_ASSEMBLAGES.md). Le niveau d'antériorité est séparé de l'intérêt de l'expérience.

| ID | Composants | Architecture étudiée | Diagnostic critique | Priorité |
|---|---|---|---|---|
| C01 | P17 + P11 + P04 | Eau atmosphérique + PCM + caloduc | PCM **déjà dans la rev.15** de P17 ; expérience 2025 confond l'effet du PCM avec celui du sorbant | Haute pour **expérience causale**, pas pour nouveauté |
| C02 | P16 + P17 | Eau atmosphérique + micro-hydroélectricité en altitude | Idée hydro déjà dans P16. Débit probablement limitant dans petits dispositifs | Basse / témoin négatif |
| C03 | P21 + P20 | Houle + accumulateur + osmose inverse + récupération de saumure | Architecture proche testée en 2023 ; récupération d'énergie étudiée en 2024 | Haute pour **commande adaptative** |
| C04 | P12 + P11 + P04 | Stirling + PCM + transfert thermique passif | Stirling + PCM testé en 2026 | Moyenne, rechercher niches |
| C05 | P19 + P11 | Échange air-sol + PCM | Déjà étudié numériquement en 2025 ; contraintes d'hygiène et de ventilateurs | Basse |
| C06 | P03 + P17 | Tube vortex pour refroidir le condenseur d'eau atmosphérique | Compresseur souvent plus coûteux énergétiquement que le bénéfice attendu | Très basse sauf air comprimé résiduel |
| C07 | P06 + P20 | Volant inertiel comme tampon d'osmose inverse à vagues | Conversions supplémentaires et confinement vs accumulateur hydraulique direct | Basse |
| C08 | P12 + P17 + P11 | Stirling → électricité + chaleur de rejet → désorption d'eau | Nécessite **température de rejet assez élevée** ; comparer chaleur directe | Haute pour borne thermodynamique |
| C09 | P17 + P04 | Désorption vibratoire + récupération de chaleur + condenseur | Revue 2026 ; système complet à comparer, et non énergie de désorption isolée | Exploration |
| C10 | P17 + P11 + chaleur fatale batterie | Sorbant MOF comme gestion thermique batterie et producteur d'eau | Démonstration publiée **septembre 2026** ; énergie de condensation et risque eau/électrique | Déjà démontré en laboratoire |

## Règles d'assemblage
1. Identifier les **flux** : eau (L/j), énergie (Wh), puissance (W), température (°C), pression (bar), temps.
2. Tester la **compatibilité physique** : pincement thermique, pression osmotique, débit stable, stabilité du matériau, maintenance.
3. Identifier le **double comptage** : une même quantité d'énergie ne peut pas être valorisée deux fois et ne devient pas gratuite en traversant une interface.
4. Imposer un **témoin moderne de service identique** : sans moteur de Stirling, réfrigération électrique classique, RO électrique + PV, etc.
5. Chercher d'abord une expérience qui **invalide** l'idée, puis seulement une configuration favorable.

## Classement sans illusion de propriété intellectuelle
- C01 : meilleur **protocole de recherche causale** (même sorbant avec et sans PCM, cycles et météo appariés).
- C03 : meilleur **problème d'ingénierie mesurable** (commande hydraulique d'une RO à vagues, avec essai existant).
- C08 : meilleur **raisonnement de systèmes** (cascade thermodynamique) mais faible probabilité d'innovation de principe.
- C09 : risque élevé de confondre une étape efficace avec un dispositif efficace.
- C02/C06/C07 : consacrer peu d'effort tant que les déficits physiques ne sont pas levés.

**Aucune combinaison n'est déclarée brevetable ou rentable.** « Ancien » n'implique ni liberté d'exploitation, ni absence d'art antérieur récent.
