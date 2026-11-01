# Étude 01 — Rotor Flettner, bilan de puissance d'ordre de grandeur
**2026-11-01 — stade : modèle préliminaire illustratif, NON calibré sur un navire réel.**

## Origine et pertinence
Brevet historique [US1674169A](https://patents.google.com/patent/US1674169A/en), Anton Flettner (publié en 1928, priorité 1923). Le cylindre tournant extrait une poussée du vent apparent par effet Magnus. L'étude physique de l'époque [NACA 1925](https://ntrs.nasa.gov/citations/19930080992) atteste un travail historique sur la propulsion, non une rentabilité actuelle.

Le sujet n'est **pas une technologie disparue** : littérature [2025 sur la viabilité](https://doi.org/10.3390/su17135909) et [2026 sur la commande énergétique](https://doi.org/10.1016/j.oceaneng.2026.127317). Notre vraie question : **dans quelles conditions météo et énergétiques la commande d'un rotor modernisé n'apporte-t-elle aucun gain, et quels seuils permettraient de sélectionner les routes intéressantes ?**

## Hypothèse falsifiable
H0 : sous un jeu de conditions route/vent donné, l'énergie motrice économisée ne compense pas l'énergie consommée par le rotor, même avant CAPEX et entretien.
H1 : gain net strictement positif **à conditions identiques**, puis compétitif face à un autre système de propulsion assistée après prise en compte des coûts et contraintes.

**Critère minimal d'arrêt du scénario :** puissance carburant nette <= 0, ou qualité des données insuffisante. Ne pas confondre H1 énergétique avec rentabilité.

## Équations
Direction `theta` du **vecteur d'écoulement du vent apparent** relative à l'avant du bateau : 0° pousse vers l'avant, 90° travers, 180° s'écoule vers l'arrière (vent venant de l'avant). Rotation supposée orientée pour favoriser la portance axiale.

- `A = H × D`, surface projetée du rotor (m²).
- `q = 0.5 × rho × Vvent²` (N/m²).
- `C_ax = CL × |sin(theta)| + CD × cos(theta)` (sans dimension). **Approximation** de projection des forces, pas une polaire mesurée.
- `F_ax = q × A × C_ax` (N).
- `P_arbre_economisee = F_ax × Vnavire / eta_prop` (W), approximation linéaire marginale.
- `P_carburant_nette = P_arbre_economisee / eta_moteur - P_electrique_rotor / eta_aux` (même unité de puissance chimique).
- `gain_% = 100 × P_carburant_nette / (P_arbre_reference / eta_moteur)`.

Aucune création d'énergie : le vent apporte la puissance mécanique, la rotation du rotor consomme de l'électricité. L'énergie équivalente carburant ne doit **pas** être confondue avec une mesure en litres de carburant.

## Paramètres d'illustration (NON sourcés d'un essai)
| Paramètre | Valeur | Rôle / limite |
|---|---:|---|
| Densité air | 1,225 kg/m³ | Approximation niveau de la mer |
| Hauteur × diamètre | 18 × 3 m | Rotor fictif unique |
| Vitesse navire | 6 m/s | Régime fixe, ~11,7 nœuds |
| CL / CD | 3,0 / 1,0 | **Choix illustratifs** ; changent avec vent, vitesse de rotation, Reynolds, interférences |
| Puissance électrique rotor | 20 kW | Hypothèse fixe, irréaliste à certains régimes |
| Rendement propulsif | 0,65 | Hypothèse fixe, ne représente pas courbe d'hélice |
| Rendement moteur principal | 0,45 | Hypothèse |
| Rendement production électrique | 0,35 | Hypothèse auxiliaire |
| Puissance arbre de référence | 2 500 kW | Navire fictif, régime constant |

Tous les champs ci-dessus sont modifiables dans [le script](rotor_model.py), au moins CL et puissance via arguments CLI. Sans polaire et carnet de voyages, une valeur de gain n'est pas transférable à un navire.

## Exécution et résultats
Test local réalisé le 2026-11-01 : `python -m unittest discover -s tests -v` : **6/6 réussis** ; `python etudes/flettner/rotor_model.py` : **35 scénarios CSV**, 7 vitesses de vent × 5 angles.

| Vent apparent et direction de l'écoulement | Gain énergétique en % de l'énergie carburant de référence, rotor allumé |
|---|---:|
| 0 m/s | -1,03 % |
| 5 m/s, travers 90° | **-0,11 %** |
| 10 m/s, travers 90° | **+2,64 %** |
| 15 m/s, travers 90° | **+7,21 %** |
| 10 m/s, 180° (écoulement vers l'arrière) | **-2,25 %** |

**Seuil de bilan nul à 90° : ~5,30 m/s** avec coefficients et 20 kW constants. **Ce seuil est une propriété de nos hypothèses**, non de la technologie en général.

Le meilleur choix quand `P_net <= 0` semble être d'arrêter le rotor, mais le modèle ne représente pas l'aérodynamique du cylindre arrêté. Il ne faut **pas** remplacer automatiquement un gain négatif par zéro en prétendant prédire un véritable bateau.

## Comparateur et réalité
- **Référence contemporaine sans rotor :** 0 % de gain relatif par construction (même navire fictif, même route).
- **Rotor modernisé :** équations ci-dessus, outil de sensibilité.
- **Solution à comparer ultérieurement :** aile rigide ou voile aspirée, avec surfaces, occupation de pont, aléas météo et CAPEX équivalents. Aucune donnée homogène disponible dans cette première passe : verdict suspendu.
- **Rotor historique :** aucune simulation « 1925 vs 2026 » n'est légitime avant accès à des mesures de puissance, météo et géométrie compatibles.

**Contradiction documentée :** [Yu & Roh (2026)](https://doi.org/10.1016/j.oceaneng.2026.127317) rapportent sur leur cas simulé avec données de voyage 2,6 % de gains conventionnels et 3,6 % avec une commande qui gère mieux l'activation des générateurs : les gains **système** ne se déduisent pas de la seule poussée. [Scientific Reports (2025)](https://www.nature.com/articles/s41598-025-21263-4) trouve des conditions où la puissance nette devient négative. Nos +2,64 % ne valident pas leur résultat, la proximité éventuelle est fortuite.

## Incertitude et analyse critique
1. Modèle stationnaire, pas de série météo, houle, cap, obstacles ni rotor multiple.
2. CL/CD supposés fixes ; manque de polaires en fonction de vitesse du vent et du ratio de rotation. Danger de surestimation important.
3. Traînée du cylindre à l'arrêt et effet de gîte/lacets absents.
4. Production auxiliaire modélisée avec un seul rendement, pas de surcharge ni de sauts de nombre de groupes.
5. CO2 / consommation / maintenance / coût installation exclus.
6. Aucun intervalle de confiance honnête sans données : ne pas en inventer.

## Expériences suivantes
- Extraire les polaires d'essais en soufflerie et les profils vitesse-angle d'articles avec autorisation de réutilisation.
- Produire **deux scénarios contradictoires** (favorable et défavorable) avec valeurs attribuées et bornes justifiées.
- Construire une commande de mise en marche `P_net > 0` incluant coûts de démarrage et traînée à l'arrêt.
- Confronter énergie nette vs configuration sans rotor, puis aile rigide, avec météo au moins saisonnière et coût total actualisé.
- Ne relâcher une décision « prometteur » que si le gain robuste dépasse incertitudes, coûts et dangers.

**Conclusion :** modèle de conservation d'énergie utile pour falsifier les promesses simplistes, **aucune preuve industrielle** à ce stade.
