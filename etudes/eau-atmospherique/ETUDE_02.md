# ETUDE 02 — Eau atmosphérique et récupération gravitaire : quelle autonomie réelle ?
**2026-11-01 — étude physique élémentaire.** Source historique : [US4146372A, 1979](https://patents.google.com/patent/US4146372A/en) ; la description évoque une turbine au moins **200 m** sous le point de captage.

## Hypothèse réfutable
H0 : avec un débit d'eau et un dénivelé fixés, la puissance gravitaire récupérée ne couvre pas l'énergie électrique des ventilateurs.
H1 : des paramètres de production et de dénivelé documentés couvrent le besoin de ventilation réel, y compris pertes mécaniques et durées de fonctionnement.

La turbine n'est qu'une composante du système : le soleil peut fournir l'énergie de régénération ; il faut compter les ventilateurs, pertes de charge, condensation et entretien.

## Bilan de conservation
Pour un volume quotidien V (litres), hauteur H (m), densité eau ~1000 kg/m³, g=9,81 m/s², rendement η entre 0 et 1 :

`E_elec_Wh/j = (V_L / 1000) × 1000 × 9.81 × H × η / 3600`.

Pour un ventilateur de puissance P (W), actif t (h/j), `E_fan = P × t`. **Condition nécessaire**, pas suffisante, d'alimentation autonome par la seule turbine : `E_elec >= E_fan`.

Énergie gravitaire brute : **0,02725 kWh/m³ par 10 m** ; à **200 m : 0,545 kWh/m³**, avant rendement. Ce n'est pas un nombre de la littérature : c'est la conservation de l'énergie.

## Sensibilité transparente
Dans cette table uniquement, η=60 %, ventilation continue et puissance ventilateur=1 W :
| Dénivelé | Production eau supposée | Électricité possible | Énergie ventilateur 1 W/24 h | Verdict hypothétique |
|---:|---:|---:|---:|---|
| 10 m | 10 L/j | 0,164 Wh/j | 24 Wh/j | Insuffisant |
| 200 m | 10 L/j | 3,27 Wh/j | 24 Wh/j | Insuffisant |
| 200 m | 100 L/j | 32,7 Wh/j | 24 Wh/j | **Bilan partiel** positif avant autres auxiliaires |
| 200 m | 1000 L/j | 327 Wh/j | 24 Wh/j | **Bilan partiel** positif avant autres auxiliaires |

À H=200 m, η=60 %, 1 W continu demande au moins `24 / (9.81 × 200 × 0.6 / 3600)` = **73,4 L/j**. Aucune des valeurs de production 10/100/1000 L/j et de puissance ventilateur 1 W n'est observée dans le brevet ou sur un appareil moderne ; les nombres sont illustratifs. La puissance de ventilation requise peut être nettement plus grande.

## Analyse contradictoire
La promesse n'est **pas un mouvement perpétuel** en soi : le cycle utilise l'énergie solaire, les différences de température et le potentiel gravitationnel d'eau captée en altitude. Le problème est de savoir si assez d'eau est captée à la hauteur du site pour fournir assez d'énergie, à coût raisonnable et sans compter deux fois les flux énergétiques.

**Réfutation strictement locale :** la configuration illustrative 10 L/j et ventilateur 1 W continu échoue à couvrir les seuls besoins du ventilateur, donc a fortiori tous les besoins du système. **H1 n'est pas réfutée sur l'ensemble des implantations** : un grand débit, une forte chute, une alimentation solaire distincte ou une ventilation intermittente pourraient changer les résultats.

## Ce qu'il faut mesurer ensuite
- Débit d'eau réellement produit (L/j), par masse de sorbant et par m², aux humidités et températures caractéristiques de sites pertinents.
- COP thermique réel et bilan de régénération ; chaleur de condensation et échange avec stock froid nocturne.
- Pressions/vitesses de circulation d'air, rendement ventilateurs, consommation électrique des pompes, capteurs et automatismes.
- Courbe turbine et pertes dans les conduites, dénivelé **net**, continuité et potabilité de l'eau, pertes lors du transport.
- Coût de construction en site élevé et coût total €/m³ d'eau potable, face au dessalement, stockage et eau livrée.
- Préenregistrer seuils avant collecte ; **ne pas ajuster les hypothèses pour obtenir un résultat favorable**.

Outil et tests : [gravity_budget.py](../eau_atmospherique/gravity_budget.py), [test_gravity_budget.py](../../tests/test_gravity_budget.py). Calcul non dimensionné industriellement, aucune validation de sécurité.
