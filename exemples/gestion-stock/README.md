# Exemple — Gestion de stock d'un atelier

Logiciel de gestion, **niveau M**, parcouru de la phase A à la phase D : documents, code Python et tests.

| Dossier | Contenu |
| --- | --- |
| [docs/](docs/) | Les livrables des phases A à C, et la matrice de traçabilité générée |
| [src/stock/](src/stock/) | Le code : domaine, application, stockage en mémoire |
| [tests/](tests/) | Les tests, chacun citant les règles `R-xx` et scénarios `S-xx` qu'il prouve |

## Lancer

Depuis la racine du dépôt :

```bash
python -m pytest exemples/gestion-stock
python outils/wd-check/wd_check.py exemples/gestion-stock --strict
```

## Ce qu'il faut regarder

- [docs/B-regles.md](docs/B-regles.md) : dix règles, chacune typée, avec exemple et contre-exemple.
- [src/stock/domaine.py](src/stock/domaine.py) : les invariants vivent dans l'objet ; une pièce invalide ne peut pas exister.
- [tests/test_application.py](tests/test_application.py) : S-07, deux sorties simultanées, dont une seule réussit.
- [docs/tracabilite.md](docs/tracabilite.md) : chaque règle, où elle est définie, citée, testée et codée.
