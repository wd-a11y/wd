# Traçabilité

Fichier généré par `wd-check`. Ne pas le modifier à la main.

| Id | Nature | Défini dans | Cité dans les docs | Cité dans les tests | Cité dans le code |
| --- | --- | --- | --- | --- | --- |
| B-01 | besoin | `docs/A-probleme.md` | `docs/A-probleme.md`, `docs/B-regles.md` | — | — |
| B-02 | besoin | `docs/A-probleme.md` | `docs/A-probleme.md`, `docs/B-regles.md`, `docs/C-architecture.md` | — | — |
| F-01 | fonctionnalité | `docs/A-probleme.md` | `docs/B-regles.md`, `docs/B-scenarios.feature`, `docs/C-architecture.md` | — | — |
| F-02 | fonctionnalité | `docs/A-probleme.md` | `docs/B-regles.md`, `docs/B-scenarios.feature`, `docs/C-architecture.md` | — | — |
| F-03 | fonctionnalité | `docs/A-probleme.md` | `docs/B-regles.md`, `docs/B-scenarios.feature`, `docs/C-architecture.md` | — | — |
| F-04 | fonctionnalité | `docs/A-probleme.md` | `docs/B-regles.md`, `docs/B-scenarios.feature`, `docs/C-architecture.md` | — | — |
| H-01 | hypothèse | `docs/hypotheses.md` | `docs/A-probleme.md`, `docs/C-architecture.md` | — | — |
| H-02 | hypothèse | `docs/hypotheses.md` | `docs/C-architecture.md`, `docs/decisions/D-01-stockage-relationnel.md` | — | — |
| R-01 | règle | `docs/B-regles.md` | `docs/B-modele.md`, `docs/B-scenarios.feature`, `docs/C-architecture.md` | `tests/test_application.py` | `src/stock/application.py` |
| R-02 | règle | `docs/B-regles.md` | `docs/B-modele.md`, `docs/B-scenarios.feature`, `docs/C-architecture.md` | `tests/test_domaine.py` | `src/stock/application.py`, `src/stock/domaine.py` |
| R-03 | règle | `docs/B-regles.md` | `docs/B-menaces.md`, `docs/B-modele.md`, `docs/B-scenarios.feature` | `tests/test_application.py` | `src/stock/application.py` |
| R-04 | règle | `docs/B-regles.md` | `docs/B-scenarios.feature`, `docs/C-architecture.md`, `docs/decisions/D-01-stockage-relationnel.md` | `tests/test_application.py`, `tests/test_domaine.py` | `src/stock/domaine.py` |
| R-05 | règle | `docs/B-regles.md` | `docs/B-modele.md`, `docs/B-scenarios.feature`, `docs/C-architecture.md` | `tests/test_application.py`, `tests/test_domaine.py` | `src/stock/domaine.py` |
| R-06 | règle | `docs/B-regles.md` | `docs/B-modele.md`, `docs/B-scenarios.feature`, `docs/C-architecture.md` | `tests/test_application.py`, `tests/test_domaine.py` | `src/stock/domaine.py` |
| R-07 | règle | `docs/B-regles.md` | `docs/B-modele.md`, `docs/B-scenarios.feature`, `docs/C-architecture.md` | `tests/test_domaine.py` | `src/stock/domaine.py` |
| R-08 | règle | `docs/B-regles.md` | `docs/B-modele.md`, `docs/B-scenarios.feature`, `docs/C-architecture.md` | `tests/test_domaine.py` | `src/stock/domaine.py` |
| R-09 | règle | `docs/B-regles.md` | `docs/B-menaces.md`, `docs/B-modele.md`, `docs/B-scenarios.feature`, `docs/decisions/D-01-stockage-relationnel.md` | `tests/test_domaine.py` | `src/stock/domaine.py` |
| R-10 | règle | `docs/B-regles.md` | `docs/B-modele.md`, `docs/B-scenarios.feature`, `docs/C-architecture.md` | `tests/test_application.py` | `src/stock/application.py` |
| S-01 | scénario | `docs/B-scenarios.feature` | `docs/C-architecture.md` | `tests/test_domaine.py` | — |
| S-02 | scénario | `docs/B-scenarios.feature` | — | `tests/test_domaine.py` | — |
| S-03 | scénario | `docs/B-scenarios.feature` | — | `tests/test_domaine.py` | — |
| S-04 | scénario | `docs/B-scenarios.feature` | — | `tests/test_domaine.py` | — |
| S-05 | scénario | `docs/B-scenarios.feature` | `docs/C-architecture.md` | `tests/test_domaine.py` | — |
| S-06 | scénario | `docs/B-scenarios.feature` | `docs/C-architecture.md` | `tests/test_domaine.py` | — |
| S-07 | scénario | `docs/B-scenarios.feature` | `docs/C-architecture.md` | `tests/test_application.py` | `README.md` |
| S-08 | scénario | `docs/B-scenarios.feature` | `docs/C-architecture.md` | `tests/test_domaine.py` | — |
| S-09 | scénario | `docs/B-scenarios.feature` | `docs/C-architecture.md` | `tests/test_domaine.py` | — |
| S-10 | scénario | `docs/B-scenarios.feature` | — | `tests/test_application.py` | — |
| S-11 | scénario | `docs/B-scenarios.feature` | `docs/C-architecture.md` | `tests/test_application.py` | — |
| S-12 | scénario | `docs/B-scenarios.feature` | — | `tests/test_domaine.py` | — |
| S-13 | scénario | `docs/B-scenarios.feature` | `docs/C-architecture.md` | `tests/test_application.py` | — |
| M-01 | menace | `docs/B-menaces.md` | `docs/B-regles.md` | — | — |
| M-02 | menace | `docs/B-menaces.md` | `docs/B-regles.md` | — | — |
| D-01 | décision | `docs/decisions/D-01-stockage-relationnel.md` | `docs/C-architecture.md` | — | `src/stock/depot_memoire.py` |
