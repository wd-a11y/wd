# Contribuer à la méthode WD

Merci de vouloir améliorer la méthode. Les contributions les plus utiles :

1. **Un retour d'usage** : vous avez appliqué la méthode sur un projet réel. Qu'est-ce qui a aidé, qu'est-ce qui a gêné, quelle étape manquait ? Ouvrez une issue « Retour d'usage ».
2. **Un nouvel exemple** dans un domaine absent (jeu, application mobile hors ligne, pipeline de données, bibliothèque logicielle…). Suivez la structure de `exemples/gestion-stock/`.
3. **Une correction ou une précision** sur une étape.
4. **Une amélioration de `wd-check`**, avec ses tests.

## Règles

- **Langue** : français clair, phrases courtes, pas de jargon sans définition.
- **Une étape = une page** : questions, livrable, exemples, pièges, critère de sortie. Gardez ce format.
- **Exemples variés** : la méthode est généraliste. Évitez de faire tourner une page autour d'un seul domaine.
- **Le code passe ses tests** : `python -m pytest` à la racine doit rester vert, et `wd-check` doit passer sur `exemples/gestion-stock`.

## Proposer un changement

1. Créez une branche : `git checkout -b ma-modification`.
2. Faites vos changements et vérifiez les tests.
3. Ouvrez une pull request ; remplissez la liste de contrôle du modèle.
