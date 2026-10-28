# Gabarit de projet

Copiez le dossier `docs/` à la racine de votre projet, puis remplissez les fichiers dans l'ordre des phases.

```bash
cp -r gabarit/docs mon-projet/docs
```

| Fichier | Phase | Étapes |
| --- | --- | --- |
| `docs/A-probleme.md` | A | 1, 2, 3, 4, 4b |
| `docs/hypotheses.md` | A, puis toutes | 2, 16b, E4 |
| `docs/B-glossaire.md` | B | 5 |
| `docs/B-modele.md` | B | 5 à 10 |
| `docs/B-regles.md` | B | 11 |
| `docs/B-scenarios.feature` | B | 12, 13 |
| `docs/B-menaces.md` | B | 13b |
| `docs/C-architecture.md` | C | 14 à 17, E2 |
| `docs/decisions/` | C, puis toutes | 16 |
| `docs/tracabilite.md` | D | 19 (générée par `wd-check`) |
| `docs/bilans/` | E | E4 |

## Conventions lues par `wd-check`

Un identifiant (`B-01`, `F-02`, `H-03`, `R-04`, `S-05`, `D-06`, `M-07`) est **défini** dans `docs/` quand il apparaît :

- dans la première colonne d'un tableau : `| R-04 | … |`
- au début d'un titre : `### R-04 — …`
- en gras au début d'une ligne ou d'un élément de liste : `**R-04**` ou `- **R-04** …`
- après `Scénario:` dans un fichier `.feature` : `Scénario: S-05 …`

Partout ailleurs, il est **cité**. Dans les tests, on peut aussi l'écrire sans tiret dans un nom de fonction : `test_R04_sortie_refusee`.

Les identifiants d'exemple de ce gabarit (`B-01`, `R-01`…) sont à remplacer par les vôtres.
