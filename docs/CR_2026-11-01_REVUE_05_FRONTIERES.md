# CR 05 — Frontières de fonctionnement et préenregistrement des expériences
**Date : 2026-11-01.** Études par équations et analyse contradictoire des assemblages C01/C02/C03/C08. Aucun prototype matériel ou test de coûts réels.

## 1. Découverte négative C02 : débit d'eau requis pour alimenter un ventilateur
Le bilan de conservation `E_Wh = volume_L × 9,81 × h × eta / 3600` donne, pour un **seul** ventilateur fictif de 1 W fonctionnant 24 heures :
- **200 m de chute, η=60 %** : **73,394 L/j** d'eau nécessaires.
- **1000 m, η=60 %** : **14,679 L/j** nécessaires.
En comparaison purement illustrative, la production de **4,25 L/j** décrite dans une [étude AWH+PCM de 2025](https://doi.org/10.1016/j.solmat.2024.113343) est **17,27 fois inférieure** à ce seuil de 200 m. **Ce n'est pas une expérience à 200 m ni une réfutation du brevet en toute circonstance.** Il reste la variabilité climatique, les auxiliaires, l'eau utile et le coût de la conduite. Une turbine n'est pas un système autonome si son débit ne soutient pas sa charge.

## 2. C03 : espace pression-volume réellement exploitable
Le précédent [FR2378958A1](https://patents.google.com/patent/FR2378958A1/en) proposait déjà de pomper l'eau des vagues vers un accumulateur. Le **modèle fictif** utilise précharge 45 bar absolus, pression haute 70 bar absolus, volume initial de gaz 100 L, loi polytropique d'exposant 1,4.

| Pression basse autorisée (absolue) | Volume échangeable calculé | Travail idéal maximum |
|---:|---:|---:|
| 50 bar | 19,81 L | 32,50 Wh |
| 55 bar | 13,71 L | 23,61 Wh |
| 60 bar | 8,49 L | 15,28 Wh |
| 65 bar | 3,96 L | 7,43 Wh |

Si une membrane opérationnelle demande une pression minimale plus haute, la **portion exploitable du tampon chute**. La [revue SWRO 2021](https://www.sciencedirect.com/science/article/pii/S0376738821002416) situe typiquement la pression d'alimentation eau de mer vers **55–70 bar**. L'article [Mi et al. 2023](https://doi.org/10.1016/j.apenergy.2023.121194) offre déjà un vrai prototype à accumulateur ; son banc salinité 3,5 g/L ne doit pas être pris pour la mer à 35 g/L. Le rendement des membranes n'est **pas** entièrement déterminé par une pression minimale fixe : concentrations, osmose, colmatage, température et débit modifient les courbes. Par ailleurs, pressions de cette simulation sont **absolues** alors que la documentation industrielle donne souvent des valeurs **manométriques** ; convertir correctement avant comparaison précise (écart environ une atmosphère).

**Conclusion utile :** explorer précharge, plage de pression et vanne de saumure **ensemble**. Un stockage grossi ne résout pas automatiquement l'absence de houle : le problème est de produire de l'eau de qualité à l'échelle d'une journée, non d'afficher un gros nombre de Wh de gaz.

## 3. C08 : seuil de température pour produire une électricité nette
Pour `Q_in=1000 Wh_thermiques`, générateur fictif à **25 % de Carnot**, `T_rejet=90°C` et **20 Wh d'auxiliaires**, l'électricité nette est positive seulement lorsque :
`T_source_K > T_rejet_K / (1 - 20/(1000*0.25))`.

Le seuil est **121,58°C**. À 100°C de source et 90°C de rejet, l'électricité nette est négative (~-13,30 Wh) ; à 330°C/90°C, elle vaut +79,48 Wh mais réduit la chaleur livrée au sorbant de 700 à ~630,37 Wh pour le modèle à 70 % d'échange. Pour un sorbant demandant 75°C et un pincement d'échangeur de 10°C, la chaleur de rejet à 25°C est inutilisable pour cette régénération.

Ces seuils changent avec les **vrais** rendements des machines, les températures, flux et auxiliaires. Le [couplage chaleur fatale et sorbant MOF publié en septembre 2026](https://doi.org/10.1038/s41467-026-76774-z) montre un antécédent récent et révèle aussi une difficulté importante : **un refroidisseur actif a servi à la condensation dans l'expérience fermée**. Il faut intégrer cette charge avant de conclure à de l'eau « gratuite ».

## 4. C01 : la comparaison PCM n'est pas un essai contrôlé du PCM seul
[Agrawal/Kumar (2025)](https://doi.org/10.1016/j.solmat.2024.113343) : **silice + PCM** = 4,25 L/j ; **tamis moléculaire sans PCM** = 4,40 L/j. La modification de **deux facteurs simultanément** crée une confusion causale. Le protocole préenregistré [C01](PROTOCOLE_C01_AWH_FACTORIEL.md) fixe le même sorbant pour chaque contraste de PCM et ajoute un contrôle pour le caloduc. Aucune preuve ne permet de préférer « avec PCM » ou « sans PCM » à ce stade.

## 5. Contradiction et verdicts
- **C02 :** très faible priorité de fabrication ; le volume d'eau requis est probablement le verrou majeur des applications de petite échelle. *Rejet du scénario fictif d'autonomie*, pas de tous les appareils.
- **C03 :** priorité à une **modélisation dynamique de pression et d'énergie récupérée**, à partir de séries expérimentales d'essai en bassin ou d'un banc instrumenté. *Indéterminé sur gain économique*.
- **C08 :** intéressante pour exploiter une source de **chaleur suffisamment haute**, mais la récupération directe peut être un meilleur témoin. *Ne pas développer à partir de chaleur tiède sans vérification*.
- **C01 :** meilleur potentiel de produire une **réponse expérimentale rigoureuse** avec des moyens limités. *Effet du PCM sur le rendement encore indéterminé*.

**Limites :** rendements, températures, pressions et puissances auxiliaires fictifs ; aucune propagation d'incertitude statistique sans données ; pas de sécurité, coût complet, liberté d'exploitation, homologation ou mesure physique. [Script](../etudes/combinaisons/frontier.py) | [CSV de 19 indicateurs](../resultats/frontieres_assemblages.csv) | [tests](../tests/test_frontier.py).
