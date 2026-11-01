# Programme de recherche ouvert — backlog scientifique

## Immédiat, ordre de valeur de preuve
- [x] Conserver intégralement la fiche d'origine de l'incubateur.
- [x] Établir méthode, registre de sources et premier catalogue de 12 brevets.
- [x] Étendre à 20 documents en ouvrant trois nouveaux groupes (eau atmosphérique, échange thermique, dessalement par vagues).
- [x] Examiner le lien entre brevets de l'eau atmosphérique et tester le plafond énergétique d'une turbine à 200 m de dénivelé.
- [x] Écrire un modèle simple d'équilibre énergétique de rotor et six tests.
- [x] Calculer 35 scénarios de sensibilité **illustratifs** avec export CSV.
- [ ] P01 : extraire de NACA 1925 et d'études 2025–2026 des valeurs **mesurées** CL/CD/consommation rotor en fonction du ratio de vitesse de rotation ; comparer à l'étude actuelle et vérifier échelles, incertitudes et événements de sous-performance.
- [ ] P01 : météo/route ouverte, modèle d'arrêt du rotor, coefficient de traînée rotor arrêté ; comparer à aile rigide et voile aspirée sous même contrainte d'encombrement.
- [ ] P07 : archives d'essais historiques des colonnes d'eau oscillantes ; confirmer les facteurs de coûts et les hypothèses d'optimisation ; reconstituer LCOE crédible en monnaie constante.
- [ ] P06 : volant 15 min / 2 h / 8 h vs batteries LFP et supercondensateurs, dégradation et risque de confinement inclus.
- [ ] P11 : PCM vs ballon d'eau et stockage solide sur un cycle de température fixé, coût et vitesse de charge, inflammabilité/corrosion.
- [ ] P03 : audit énergétique complet air comprimé → tube Ranque → froid utile, COP global vs pompe à chaleur.
- [ ] P02 : comparaison hydrolienne Darrieus vs turbine horizontale sur vitesses variables ; fatigue et amarrage.
- [ ] P10, P12 : revue bibliographique indépendante, uniquement si niche et données chiffrées identifiées.
- [ ] Analyser familles de brevets (EPO/INPADOC), titulaires, continuations et améliorations pour les 4 finalistes, et registres nationaux si une exploitation concrète se dessine.

## Deuxième vague (élargissement contrôlé)
- [ ] Porter le corpus à 30 brevets, incluant bâtiments, hydraulique, transmission mécanique, instrumentation et mobilité, pas uniquement énergie.
- [ ] Documenter **pourquoi** chaque invention a décliné ou non : études techniques, échecs commerciaux, dates, coûts et concurrents ; statut « inconnu » si non prouvé.
- [ ] Extraire systématiquement les citations postérieures, familles, revendications indépendantes et contraintes physiques dominantes.
- [ ] Organiser revue rouge (hypothèse défavorable) à chaque étude avant prononcer « prometteur ».
- [ ] Définir une procédure permettant d'interrompre une voie non compétitive et d'archiver ses résultats négatifs.

## Barrière de publication
Aucun « prêt pour production », aucune sécurité garantie, aucun statut libre d'exploitation, et aucun pourcentage économisé **réel** à partir du script exploratoire. Les propositions expérimentales sur dispositifs sous pression, rotatifs, cryogéniques ou forte puissance exigent une revue de risque avant tout prototype.

## Suite spécifique de la revue 02
- [ ] P16 : obtenir le rapport d'essai originel d'exploitation, si existant ; comparer eau produite (L/m²/jour), humidité, solaire reçu, masse sorbant et entretien aux ouvrages de 1938, 1981 et 2023–2025.
- [ ] P16 : auditer sans complaisance la mention du brevet de **turbine 200 m plus bas** : débit, durée des ventilateurs, pertes d'eau, stockage, ensoleillement, prise d'eau et risque de compter deux fois le dénivelé.
- [ ] P13–P18 : modéliser le cycle de sorption comme **grappe de 5 brevets**, non 5 innovations indépendantes, avec deux contrôles modernes (sorbant solaire moderne et dessiccation/compression électrique).
- [ ] P20 : relever pompe annoncée autour de 800 psi dans la revendication, lire essais hydrauliques et coûts ; convertir en kWh et m³ d'eau, vérifier état de mer et sécurité système.
- [ ] Identifier 10 brevets hors secteurs thermo-hydraulique pour atteindre 30 documents couvrant réellement plusieurs marchés.

## Troisième revue : connaissance contemporaine et définition d'un benchmark
- [x] P20 : identifier **un essai publié** de dessalement entraîné par les vagues, pas seulement une notice de brevet (Das et al., 2024).
- [x] P20 : comparer les équations de pression/débit d'un procédé RO à 800 psi avec et sans récupération d'énergie (analyse de bornes, **pas** simulation hydrodynamique).
- [ ] P20 : lire le texte intégral Das et al. 2024 et relever la définition exacte du SEC, mode de mesure des pertes, variabilité des vagues et fréquence des inversions de flux ; obtenir les barres d'erreur.
- [ ] P20 : établir LCOE de la source mécanique et **LCOW (€/m³ d'eau)** en zone côtière, comparer à panneaux solaires + SWRO + batterie, incluant entretien, corrosion et arrêts.
- [ ] P20 : caractériser les coûts et risques propres aux conduites hydrauliques haute pression ; aucune construction avant revue de sécurité.
- [ ] P16 : utiliser la revue 2026 AWH comme trame pour benchmark (eau/jour/m², eau/kg sorbant, kWh thermiques & électriques/m³, coût total, potabilité et humidité).
- [ ] P16 : ne pas comparer un rendement eau/kg de sorbant à un rendement eau/m²/jour sans rapporter masse chargée par surface et durée des cycles.

## Garantie de continuité
- [x] Introduire un garde-fou machine : tests de modèles + vérification hors ligne du catalogue et des chemins documentaires.
- [ ] Ajouter vérification des identifiants de publication via API bibliographique (avec cache, limites de débit et provenance), sans dépendre d'une requête réseau non reproductible lors des tests unitaires.

## Phase 04 : architectures hybrides (2026-11-01)
- [x] Identifier dix assemblages et rechercher la nouveauté déjà revendiquée, notamment US4285702A rev.15.
- [x] Inclure FR2378958A1 (1978) : pompage des vagues vers accumulateur hydraulique.
- [x] Trois bilans conservatifs et CSV sous hypothèses fictives, avec tests Python.
- [ ] C01 : protocole factoriel : sorbant fixe ; PCM oui/non ; caloduc oui/non, météo et cycles appariés, protocole gelé.
- [ ] C03 : récupérer séries pression/débit de Mi et al. (2023) ; comparer commande fixe/variable avec saline marine, récupération Clark, coûts et contrôle de surpression.
- [ ] C08 : vérifier chaleur de rejet utile selon sorbant, débits et températures mesurés ; comparaison cogénération vs chaleur directe.
- [ ] C09 : modéliser **chaîne complète** de désorption vibratoire jusqu'à eau potable collectée ; rejeter si comparateur thermique moderne meilleur.
- [ ] Identifier des brevets hors énergie et eau pour éviter biais du corpus.
