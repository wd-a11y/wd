# Étape 21 — Répéter le cycle

**Phase :** E, puis retour en A · **Livrable :** la boucle suivante · **Durée indicative :** —

## Pourquoi

La méthode ne s'arrête pas au premier module. C'est sa répétition qui permet de gérer des projets gros et complexes.

## Démarche

Chaque nouvelle fonctionnalité reparcourt A → E en version courte :

| Phase | Version courte |
| --- | --- |
| A | Quel besoin `B-xx` sert-elle ? Quelles nouvelles hypothèses ? |
| B | Nouveaux termes, règles, états, scénarios, cas limites, menaces |
| C | Nouveaux modules ou décisions ? Sinon, rien |
| D | Code et tests de la tranche |
| E | Livraison, mesure, bilan |

## Entretenir les documents

- **Une règle qui change** = nouvelle version de la `R-xx` (on note la date et la raison), test modifié **avant** le code.
- **Une décision remplacée** = nouvelle décision `D-xx` qui remplace l'ancienne, conservée dans l'historique.
- **Un document qui ne correspond plus au code est un bug**, à corriger comme tel.

## Ce qu'il faut garder en tête

Le but n'est pas de commencer vite. Le but est de commencer juste. Quand la conception est bonne, les objets, les fonctions, les fichiers et les règles deviennent évidents, et le code devient beaucoup plus facile à écrire. La méthode WD ajoute : **et on peut prouver, à tout moment, que c'est toujours juste.**
