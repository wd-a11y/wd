# Étape E4 — Retour du réel

**Phase :** E · **Livrable :** `docs/bilans/AAAA-MM-JJ.md` · **Durée indicative :** une demi-journée par bilan

## Pourquoi

Un logiciel livré n'est pas un logiciel réussi. Le bilan ferme la boucle ouverte à l'étape 1 : le problème est-il vraiment résolu ?

## Démarche

À date fixe (par exemple 2 semaines après chaque livraison importante) :

1. **Comparer les mesures `B-xx` à leurs cibles.**
2. **Écouter les utilisateurs** : 3 à 5 conversations courtes, mêmes règles qu'à l'étape 1 (faits, pas opinions).
3. **Mettre à jour les hypothèses `H-xx`** : confirmées, abandonnées, nouvelles.
4. **Décider** : continuer, corriger, ou abandonner une fonctionnalité.

## Modèle de bilan

```markdown
# Bilan du 2026-05-14

| Mesure | Avant | Cible | Mesuré | Verdict |
| --- | --- | --- | --- | --- |
| B-01 | 3 / mois | 0 | 0 | atteint |
| B-02 | 4 min | 1 min | 2 min | partiel |

Ce que disent les utilisateurs : …
Hypothèses mises à jour : H-03 abandonnée (…), H-05 nouvelle (…).
Décisions pour la boucle suivante : …
```

## Critère de sortie

Le bilan est écrit, daté, et ses décisions alimentent la boucle suivante.
