# Phase E — Livraison et retour du réel

**Objectif :** que le logiciel tourne, survive aux pannes, et qu'on sache s'il atteint les mesures de réussite de l'étape 1. C'est là que beaucoup de projets échouent, même avec un bon code.
**Livrables :** intégration continue, procédure de déploiement et de retour arrière, tableau des mesures, bilan.

| Étape | Résultat |
| --- | --- |
| [E1. Qualité automatique](E1-qualite-automatique.md) | Chaque modification est vérifiée automatiquement |
| [E2. Déploiement sûr](E2-deploiement.md) | Environnements, migrations, secrets, sauvegardes restaurées, retour arrière |
| [E3. Observer en production](E3-observer.md) | Journaux, erreurs remontées, mesures `B-xx` visibles |
| [E4. Retour du réel](E4-retour-du-reel.md) | Bilan daté, hypothèses mises à jour |
| [21. Répéter le cycle](21-repeter.md) | La boucle suivante, et l'entretien des documents |

## Porte E

- [ ] L'intégration continue bloque tout code dont les tests échouent.
- [ ] Une restauration de sauvegarde a été testée.
- [ ] Le retour arrière est documenté et a été essayé une fois.
- [ ] Les mesures de réussite sont visibles, et la date du bilan est fixée.
