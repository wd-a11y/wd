# wd-check

Vérificateur de traçabilité pour les projets qui suivent la méthode WD. Il répond à deux questions : **chaque règle est-elle prouvée par un test ?** et **chaque identifiant cité existe-t-il ?**

Aucune dépendance : un seul fichier Python (3.9 ou plus récent).

## Utilisation

```bash
python outils/wd-check/wd_check.py mon-projet
python outils/wd-check/wd_check.py mon-projet --strict
python outils/wd-check/wd_check.py mon-projet --matrice mon-projet/docs/tracabilite.md
```

Exemple de sortie :

```text
wd-check — mon-projet
Définis : 2 besoins, 4 fonctionnalités, 9 règles, 12 scénarios
ERREUR      R-09 n'est cité par aucun test (défini en docs/B-regles.md:14)
ERREUR      R-15 est cité mais défini nulle part (docs/B-scenarios.feature:30)
ATTENTION   S-06 n'est cité par aucun test (défini en docs/B-scenarios.feature:41)
Résultat : 2 erreur(s), 1 avertissement(s).
```

Code de sortie : `0` sans erreur, `1` avec erreurs (utile en intégration continue), `2` si le dossier `docs/` est introuvable.

## Ce qui est vérifié

| Vérification | Niveau |
| --- | --- |
| Un identifiant est défini deux fois | Erreur |
| Un identifiant est cité mais défini nulle part | Erreur |
| Une règle `R-xx` n'est citée par aucun test | Erreur |
| Un scénario `S-xx` n'est cité par aucun test | Avertissement (erreur avec `--strict`) |
| Un besoin, une fonctionnalité ou une menace n'est cité nulle part | Avertissement (erreur avec `--strict`) |

## Conventions

- **Définition** (dans `docs/`, fichiers `.md` et `.feature`) : première colonne d'un tableau `| R-04 |`, début de titre `### R-04`, gras en début de ligne `**R-04**`, ou `Scénario: S-05`.
- **Citation** : toute autre apparition, dans les docs, les tests ou le code.
- **Tests** : fichiers dans un dossier `tests/`, `test/`, `spec/`, ou nommés `test_*`, `*_test.*`, `*.test.*`, `*.spec.*`. Dans un test, `test_R04_…` vaut citation de `R-04`.
- `docs/tracabilite.md` et `docs/bilans/` citent sans définir.
- Les identifiants `T-xx` sont libres et ne sont pas vérifiés.

## Tests

```bash
python -m pytest outils/wd-check
```
