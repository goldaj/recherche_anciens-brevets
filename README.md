# RETRO-LAB | Recherche d'anciens brevets et inventions réévaluables

**Programme de recherche démarré le 1er novembre 2026.** Objectif : identifier des inventions anciennes dont les contraintes techniques, économiques ou réglementaires ont changé, puis **tenter de réfuter** l'hypothèse qu'une réutilisation moderne présente un intérêt. Un brevet ancien n'est pas une démonstration de faisabilité.

## Avancement vérifiable
- **12 documents de brevet identifiés**, avec liens permanents, hypothèses et limites dans [le catalogue](data/candidats.csv). Niveau actuel : *tri documentaire*, pas validation industrielle.
- Première analyse transversale : [CR du 1er novembre 2026](docs/CR_2026-11-01_REVUE_01.md).
- Première expérience paramétrique : [rotor Flettner](etudes/flettner/ETUDE_01.md), [modèle Python](etudes/flettner/rotor_model.py), [résultats CSV](resultats/sensibilite_rotor.csv), [tests](tests/test_rotor_model.py).
- [Méthode de recherche](docs/METHODOLOGIE.md), [références](docs/SOURCES.md), [plan de recherche](docs/PROCHAINES_ETAPES.md).

### Reproduire
```bash
python3 -m unittest discover -s tests -v
python3 etudes/flettner/rotor_model.py --out resultats/sensibilite_rotor.csv
python3 etudes/flettner/rotor_model.py --lift 2.0 --drive-kw 30 --out resultats/sensibilite_prudente.csv
```
Python 3.10+ ; aucune dépendance externe.

## Discipline
1. Lire brevet + revendications + famille + statut légal territorial ; ne jamais déduire la liberté d'exploitation d'un simple champ « expired ».
2. Séparer **principe historique**, **variante modernisée**, **solution déjà dominante aujourd'hui**.
3. Tracer hypothèses, calculs, limites et objections. Une métrique simulée ne prouve ni coût réel, ni sécurité, ni brevetabilité.
4. Les inventions encore très utilisées (caloducs, tubes pulsés, transport pneumatique en niche) servent de **témoins** pour éviter la fausse promesse « oubliée ».
5. Prioriser des domaines civils licites. Pas de prototype dangereux, ni d'expérience avec systèmes sous pression sans revue de sécurité.

**Origine du projet :** [fiche RETRO-LAB archivée à l'identique](archives/RETRO-LAB_FICHE_ORIGINALE_2026-10-31.md), auparavant dans `goldaj/projects-incubator/recherche-et-innovation/retro-lab.md`. La fiche décrivait 10 candidats et une étude reproductible ; la recherche commence ici.

**Statut des conclusions :** exploratoires, au 2026-11-01. Ce dépôt ne délivre pas de conseil juridique, d'autorisation d'exploitation ni de certification d'ingénierie.
