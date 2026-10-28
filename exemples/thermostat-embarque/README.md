# Exemple — Régulateur de chauffage pour serres

Logiciel embarqué sur microcontrôleur, **niveau L** (sécurité physique des cultures et de l'installation), phases A à C. Ce qu'il illustre surtout :

- des **exigences temps réel et matérielles** (délai de réaction, mémoire limitée, fonctionnement sans réseau) ;
- les **pannes matérielles** comme cas limites de premier plan : capteur muet, valeur absurde, redémarrage brutal ;
- un **état sûr par défaut** et une décision d'architecture qui ne confie pas la sécurité au seul logiciel.

| Fichier | Contenu |
| --- | --- |
| [docs/A-probleme.md](docs/A-probleme.md) | Problème, mesures, périmètre, acteurs, exigences |
| [docs/B-modele.md](docs/B-modele.md) | Glossaire, objets, modes de fonctionnement |
| [docs/B-regles.md](docs/B-regles.md) | Huit règles, dont trois de sécurité |
| [docs/B-scenarios.feature](docs/B-scenarios.feature) | Scénarios, dont les pannes de capteur |
| [docs/B-menaces.md](docs/B-menaces.md) | Commande à distance et mise à jour du micrologiciel |
| [docs/C-architecture.md](docs/C-architecture.md) | Modules, vues, première tranche |
| [docs/decisions/](docs/decisions/) | D-01 : la coupure de sécurité ne dépend pas que du logiciel |

La phase D n'est pas faite : `wd-check` signale donc que les règles n'ont pas encore de test.
