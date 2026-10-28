# Étape 14 — Définir les responsabilités

**Phase :** C · **Livrable :** section « Modules » de `docs/C-architecture.md` · **Durée indicative :** une demi-journée

## Pourquoi

Chaque partie du système doit avoir un rôle clair. Un module qui fait le travail de tous les autres devient impossible à comprendre, à tester et à modifier.

## Questions à poser

- Qui crée quoi ? Qui valide quoi ? Qui calcule quoi ?
- Qui stocke quoi ? Qui affiche quoi ? Qui notifie quoi ?
- Qui décide quoi ?

## Deux règles vérifiables

1. **Une phrase par module :** « Ce module est responsable de … et de rien d'autre. » Si la phrase contient « et » deux fois, le module est trop gros : on le découpe.
2. **Les dépendances vont dans un seul sens.** Le cœur métier (le domaine) ne connaît ni la base de données, ni l'écran, ni les services externes. Ce sont eux qui dépendent du domaine. On peut ainsi changer de base ou d'interface sans toucher aux règles, et tester les règles sans base de données.

```text
Interface  ─►  Application  ─►  Domaine  ◄─  Infrastructure
(écrans, API)   (cas d'usage)    (règles)     (base, services externes)
```

## Exemple

| Module | Responsabilité |
| --- | --- |
| `domaine.stock` | Garantir que chaque mouvement respecte les règles du stock. |
| `application.sorties` | Orchestrer une sortie : vérifier les droits, appeler le domaine, enregistrer, publier l'événement. |
| `infrastructure.depot_sql` | Lire et écrire les pièces et mouvements dans la base de données. |
| `interface.api` | Recevoir les requêtes HTTP, valider leur format, renvoyer les réponses. |

## Critère de sortie

Chaque module a sa phrase de responsabilité, et aucune flèche de dépendance ne part du domaine vers l'extérieur.
