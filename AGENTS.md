# AGENTS — protocole de collaboration / continuité

## Avant une modification
1. Lire `README.md`, `docs/METHODOLOGIE.md`, `docs/CHATGPT_PROJECT_HISTORY.md`, le dernier CR et `docs/PROCHAINES_ETAPES.md`.
2. Inspecter les autres branches et les contributions concurrentes avant toute fusion.
3. Préserver les documents sources, hypothèses négatives et versions antérieures. Pas de suppression silencieuse des résultats contradictoires.

## Preuves et attribution
- Un identifiant de brevet + lien vérifié prouve l'existence du **document**, non la performance, l'abandon, la priorité d'invention ni l'absence de droits actuels.
- Vérifier date de priorité/dépôt/publication, le périmètre exact des revendications, les familles INPADOC, les registres nationaux et les publications postérieures. Les champs de Google Patents sont indicatifs.
- Au minimum : problème, hypothèse falsifiable, application, méthode, unités, paramètres sourcés ou explicitement fictifs, baseline, critères d'arrêt, sensibilité, degré de confiance, prochaine preuve.
- Documenter aussi les **non-résultats**. Ne jamais transformer des paramètres illustratifs en observations.
- Ne pas proclamer de « brevet libre » sans analyse pays par pays et sans avis professionnel adapté.

## Modèle et tests
- Faire tourner `python3 -m unittest discover -s tests -v` puis le script principal après modification.
- Mettre les résultats dérivés dans `resultats/`. CSV reproductible, pas seulement captures d'écran.
- Si aucune exécution réelle n'a eu lieu, l'écrire explicitement. Tests unitaires ≠ validation avec données de terrain.
- Ne pas introduire de dépendances ou outils lourds avant justification.

## Journal de continuité
Après chaque recherche, créer un CR daté distinguant **faits vérifiés / hypothèses / calculs / conclusions provisoires / objections / suite** ; mettre à jour `docs/CHATGPT_PROJECT_HISTORY.md` (texte exact uniquement quand réellement disponible ; sinon résumé non verbatim) et `docs/PROCHAINES_ETAPES.md`. Maintenir les liens relatifs et le catalogue.

## Sécurité
Dépôt public : pas d'identifiants, secrets, informations privées ou documents sous licence non redistribuable. Les brevets donnent des descriptions techniques, pas une validation de sûreté. Pour tout appareil sous pression, cryogénique, électromagnétique ou à haute vitesse de rotation, commencer par une étude papier et une revue des dangers, non par une fabrication improvisée.
