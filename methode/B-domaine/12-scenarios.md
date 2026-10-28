# Étape 12 — Dérouler des scénarios complets

**Phase :** B · **Livrable :** `docs/B-scenarios.feature` · **Durée indicative :** 1 jour

## Pourquoi

On raconte des histoires réelles du début à la fin. Elles révèlent l'ordre naturel des opérations, les oublis du modèle, et deviennent les tests d'acceptation.

## Format : Soit / Quand / Alors (Gherkin)

```gherkin
# language: fr
Fonctionnalité: F-02 Sortir une pièce du stock

  Scénario: S-03 Sortie refusée si le stock est insuffisant (R-04)
    Soit une pièce "Vis M6" avec un stock de 10
    Quand le magasinier sort 12 "Vis M6"
    Alors la sortie est refusée avec le message "Stock insuffisant : 10 disponibles"
    Et le stock de "Vis M6" reste 10
```

Ce format se lit par une personne du métier **et** s'exécute comme test (Cucumber, Behave, pytest-bdd, SpecFlow…).

## Règles d'écriture

- Un identifiant `S-xx` et les règles touchées entre parenthèses.
- Des **valeurs concrètes** (10, 12, « Vis M6 »), jamais « une certaine quantité ».
- Un seul « Quand » par scénario : une seule action testée.
- Les mots du glossaire, et seulement eux.

## Les familles de scénarios à couvrir

| Famille | Exemple |
| --- | --- |
| Normal | Sortie de 4 sur un stock de 10 |
| Atypique | Sortie qui amène le stock exactement à 0 |
| Erreur | Sortie de 12 sur un stock de 10 |
| Rare | Inventaire pendant qu'une sortie est en cours |
| Impossible | Sortie d'une pièce archivée |

Pour les cas **impossibles**, la bonne question est : comment les rendre impossibles **par construction** (l'écran ne propose pas la pièce archivée, l'objet refuse la transition) plutôt que par une vérification ajoutée ?

## Critère de sortie

Chaque fonctionnalité indispensable a au moins un scénario normal et un scénario d'erreur ; chaque règle est citée par au moins un scénario.
