# Adapter la méthode à la taille du projet

On choisit un niveau au début du projet (étape 2), on l'écrit dans `docs/A-probleme.md`, et on peut le réviser si le projet grandit.

| Niveau | Quand | Étapes obligatoires | Volume de documents |
| --- | --- | --- | --- |
| **S** | Outil personnel, script, prototype jetable, exercice | 1, 2, 5, 11, 12, 13, 18, 19 | 1 page |
| **M** | Application ou service avec de vrais utilisateurs | Toutes, en version légère ; 13b et décisions `D-xx` pour les choix majeurs seulement | 5 à 15 pages |
| **L** | Argent, santé, sécurité physique, données sensibles, plusieurs équipes | Toutes, complètes, avec revue de sécurité externe | Autant que nécessaire, tenu à jour |

## Questions pour choisir

- Une erreur du logiciel peut-elle blesser quelqu'un, coûter de l'argent ou exposer des données personnelles ? → au moins **L** pour les parties concernées.
- D'autres personnes que moi vont-elles l'utiliser ou le maintenir ? → au moins **M**.
- Le code sera-t-il jeté dans moins d'un mois ? → **S** suffit.

Un même projet peut mélanger les niveaux : niveau L pour le module de paiement, niveau M pour le reste.

## Durées indicatives (niveau M)

| Phase | Durée maximale de la première boucle |
| --- | --- |
| A. Problème | 3 à 5 jours |
| B. Domaine | 1 semaine |
| C. Conception, squelette marchant compris | 1 semaine |
| D. Construction de la première tranche | 1 à 2 semaines |
| E. Première livraison | 2 à 3 jours |

Si une étape dépasse sa durée, on note les questions ouvertes en hypothèses `H-xx` et on avance. On y reviendra quand on en saura plus.
