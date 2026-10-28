# Exemple — API de réservation de places de spectacle

Service web, **niveau M**, phases A à C. Ce qu'il illustre surtout :

- une **machine à états** riche (retenue, confirmée, expirée, annulée, utilisée) ;
- le risque principal d'une API publique : **la double réservation sous forte charge** ;
- des **menaces** propres aux API : lecture des données d'autrui, revente massive, saturation.

| Fichier | Contenu |
| --- | --- |
| [docs/A-probleme.md](docs/A-probleme.md) | Problème, mesures, périmètre, acteurs, exigences |
| [docs/B-modele.md](docs/B-modele.md) | Glossaire, objets, cycle de vie d'une réservation |
| [docs/B-regles.md](docs/B-regles.md) | Huit règles |
| [docs/B-scenarios.feature](docs/B-scenarios.feature) | Scénarios, dont les cas de concurrence |
| [docs/B-menaces.md](docs/B-menaces.md) | Trois menaces devenues règles |
| [docs/C-architecture.md](docs/C-architecture.md) | Modules, vues, première tranche |
| [docs/decisions/](docs/decisions/) | D-01 : l'unicité garantie par la base de données |

La phase D n'est pas faite : `wd-check` signale donc que les règles n'ont pas encore de test.
