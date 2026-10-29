# Journal des versions

Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/). Numérotation [SemVer](https://semver.org/lang/fr/).

## [2.0.0] — 2026-10-29

Première version publique.

### Ajouté

- **La méthode** (`methode/`) : 5 phases (Problème, Domaine, Conception, Construction, Livraison), 29 étapes d'une page chacune, une porte de contrôle par phase, les niveaux S / M / L et 17 pièges courants.
- **Huit étapes nouvelles** par rapport à la v1 : exigences non fonctionnelles (4b), machine à états (9b), menaces et abus (13b), squelette marchant (16b), qualité automatique (E1), déploiement sûr (E2), observation en production (E3), retour du réel (E4) ; et une porte de contrôle explicite à la fin de chaque phase.
- **Les identifiants traçables** : `B-` besoin, `F-` fonctionnalité, `H-` hypothèse, `R-` règle, `S-` scénario, `T-` test, `D-` décision, `M-` menace.
- **Le gabarit** (`gabarit/docs/`) : onze livrables vides à copier dans tout projet.
- **Trois exemples** de domaines différents : gestion de stock (jusqu'au code Python testé), API de réservation, régulateur de chauffage embarqué.
- **`wd-check`** (`outils/wd-check/`) : vérificateur de traçabilité sans dépendance (règles sans test, références cassées, doublons, matrice de traçabilité).
- **La skill pour agent IA** (`skill/methode-wd/`).
- **Les modèles GitHub** : issues, pull request, vérification automatique.

## [1.0.0]

Version initiale en PDF : 23 sections, du problème réel aux tests, sans livrables ni vérification automatique.
