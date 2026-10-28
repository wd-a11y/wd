# Étape 8 — Obligatoire, facultatif, calculé

**Phase :** B · **Livrable :** compléter les fiches de `docs/B-modele.md` · **Durée indicative :** 2 heures

## Pourquoi

Cette distinction évite de stocker n'importe quoi, d'exiger des informations inutiles, et surtout d'avoir deux versions contradictoires de la même vérité.

## Pour chaque donnée

| Catégorie | Définition | Exemple |
| --- | --- | --- |
| **Obligatoire** | Sans elle, l'objet n'existe pas | la quantité d'un mouvement de stock |
| **Facultative** | L'objet existe sans elle, mais elle apporte de la valeur | un commentaire, une catégorie |
| **Calculée** | Elle s'obtient à partir d'autres données | le stock actuel = somme des mouvements |

## Questions supplémentaires

- **Donnée calculée : la stocke-t-on ou la recalcule-t-on ?** Si on la stocke (un total, un stock, un solde) pour aller plus vite, on écrit **quelle donnée fait foi** en cas de désaccord, et quand on recalcule.
- **Valeur par défaut** : laquelle, et est-elle vraiment sûre ?
- **Historique** : faut-il garder les anciennes valeurs ? (Un prix qui change ne doit pas modifier les anciennes factures.)

## Exemple

> Le stock d'une pièce est **calculé** comme la somme de ses mouvements. Il est **stocké** pour l'affichage rapide. **Les mouvements font foi** : un recalcul nocturne corrige le stock stocké et signale tout écart.

## Pièges

- Rendre obligatoire une donnée que l'utilisateur ne connaît pas au moment de la saisie : il inventera une valeur.
- Stocker un calcul sans dire qui fait foi : tôt ou tard, les deux divergent.

## Critère de sortie

Chaque donnée est classée ; chaque donnée calculée stockée a sa source de vérité écrite.
