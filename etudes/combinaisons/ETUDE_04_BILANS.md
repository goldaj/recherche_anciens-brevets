# Étude 04 : trois bilans contradictoires sur des assemblages de brevets

Date : 2026-11-01. [Modèle](hybrid_budgets.py) · [tests](../../tests/test_hybrid_budgets.py) · [sortie CSV](../../resultats/assemblages_scenarios.csv). **Données de simulation : illustrations, pas mesures**, sauf résultats explicitement attribués aux publications.

## A. Eau atmosphérique et turbine en altitude (P16+P17)
L'étude [Agrawal/Kumar, 2025](https://doi.org/10.1016/j.solmat.2024.113343) indique 4,25 L/j pour un appareil avec PCM et gel de silice (contre 4,40 L/j pour un montage à autre sorbant sans PCM). **La production de 4,25 L/j n'a pas été mesurée à 200 ou 1000 m**. Nous l'utilisons comme hypothèse pour contredire la revendication d'une autonomie électrique par turbine seule.

`E_electrique = masse_eau × 9,81 × hauteur_nette × rendement_turbine / 3600`, Wh/j.
- 4,25 L/j, 200 m, η=0,6 → **1,390 Wh/j**, environ **5,79 %** d'une charge fictive de 1 W fonctionnant pendant 24 h.
- Même débit, 1000 m → **6,949 Wh/j**, soit **28,95 %** de cette charge.
La petite installation hypothétique **ne couvre pas ce seul ventilateur**. Le brevet P16 ne fournit pas de débit transposable et n'est pas globalement réfuté ; conduites, captage, autres auxiliaires non comptés.

## B. Vagues, accumulateur et osmose inverse (P21+P20)
Modèle d'un **gaz idéal** `p×V^n=const`, avec pressions **absolues**. Hypothèse (non issue des essais) : précharge à 45 bar, fonctionnement entre 50 et 70 bar, volume de gaz à précharge de 100 litres, exposant polytropique n=1,4.
- Volume hydraulique utilisable calculé : **19,815 L**.
- Travail maximum idéal du gaz entre ces points : **32,497 Wh**.
- À 10 % de récupération membranaire hypothétique, 19,815 L de charge ne représentent qu'environ **1,98 L de perméat par passage**, et à 40 % environ **7,93 L**, *si* la pression réelle permet l'osmose sur tout l'intervalle.

Ce n'est pas un dimensionnement industriel. **Piège :** la plage 50–70 bar comporte un bas de plage pouvant être insuffisant pour une eau de mer donnée. Il faut estimer la pression osmotique et les pertes. L'accumulateur lisse des fluctuations : il **ne crée aucune énergie**, et une récupération sur saumure n'ajoute pas une seconde fois la même énergie. [Mi et al. 2023](https://doi.org/10.1016/j.apenergy.2023.121194) fournissent une baseline expérimentale.

## C. Moteur Stirling et régénération du sorbant (P12+P17+P11)
Une cascade proposée chaleur → Stirling → chaleur de rejet → sorbant AWH nécessite `T_rejet ≥ T_régénération + deltaT_échangeur`. Ne pas supposer que la chaleur à 25°C peut régénérer un sorbant qui demande 75°C.

Hypothèses illustratives : **1 kWh thermique** de chaleur d'entrée, Stirling produisant **25 % du rendement Carnot**, auxiliaires de **20 Wh**, échangeur de régénération transférant **70 %**, sorbant exigeant 75°C + pincement de 10°C. Valeurs hypothétiques **non calibrées**.

| Source / rejet | Électricité nette fictive | Chaleur compatible livrée à régénération | Comparateur sans Stirling |
|---|---:|---:|---:|
| 330 / 90°C | **79,48 Wh** | **630,37 Wh** | 700 Wh |
| 100 / 90°C | **-13,30 Wh** | **695,31 Wh** | 700 Wh |
| 330 / 25°C | **106,33 Wh** | **0 Wh** : température insuffisante | 700 Wh possibles théoriquement par chemin direct |

**Ne pas additionner** les Wh de chaleur à 90°C aux Wh électriques : ces services ne sont pas interchangeables. En 330/90, on abandonne environ **69,63 Wh de chaleur livrée** pour disposer de **79,48 Wh électriques nets**. L'intérêt dépend du besoin simultané d'électricité et d'eau, du coût d'un générateur, du transfert réel de chaleur et de l'usage alternatif de cette chaleur.

La publication [Chen et al. 2026](https://doi.org/10.1038/s41467-026-76774-z) montre un autre couple chaleur fatale / sorbant ; aucune originalité fondamentale ne peut être revendiquée ici.

## Pistes de réfutation et critères d'arrêt
- **A :** arrêter l'idée de récupération électrique dédiée si, sur profils climatiques pertinents, l'électricité disponible ne couvre pas les auxiliaires marginaux et coûts d'infrastructure.
- **B :** arrêter la commande hybride si la variabilité ou la pression minimale dégrade la quantité d'eau **potable livrée** et la durée de vie des membranes, contre un RO actuel optimisé.
- **C :** arrêter la cascade si la température de rejet est inférieure à la consigne de désorption + pincement ou si un chauffage direct/une récupération de chaleur simple remplit mieux les deux services.

Aucune preuve de coût, de potabilité, de résistance mécanique, de sûreté ou de liberté d'exploitation.
