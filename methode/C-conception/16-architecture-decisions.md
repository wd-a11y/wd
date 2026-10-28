# Étape 16 — Traduire le métier en architecture, et écrire les décisions

**Phase :** C · **Livrables :** `docs/C-architecture.md`, `docs/decisions/D-xx-*.md` · **Durée indicative :** 1 à 2 jours

## Pourquoi

Seulement maintenant on pense au logiciel : modules, dossiers, couches, base de données, interfaces. Et chaque choix important est écrit, avec sa raison, pour qu'on sache dans six mois pourquoi il a été fait.

## Les couches, par défaut

| Couche | Contient | Ne contient jamais |
| --- | --- | --- |
| **Domaine** | Objets, invariants, calculs, événements | Base de données, HTTP, écran, framework |
| **Application** | Cas d'usage (un par scénario), autorisations, transactions | Règles métier recopiées |
| **Infrastructure** | Base de données, API externes, envoi de messages, fichiers | Décisions métier |
| **Interface** | Écrans, API publique, ligne de commande, validation des entrées | Calculs métier |

À adapter : un petit outil (niveau S) peut fusionner application et interface ; un logiciel embarqué remplace « base de données » par « mémoire et pilotes matériels ».

## Choisir une technologie

Critères, dans cet ordre :

1. respecte les exigences non fonctionnelles (étape 4b) ;
2. maîtrisée par l'équipe, ou apprenable dans le délai ;
3. coût total (licences, hébergement, maintenance) ;
4. maturité, documentation, communauté.

Préférer **l'ennuyeux et éprouvé** à la nouveauté. Une technologie à la mode choisie par envie est une dette.

## Écrire une décision (format ADR)

Un fichier par décision, une demi-page : `docs/decisions/D-03-base-de-donnees.md`.

```markdown
# D-03 — Base de données relationnelle

- Statut : acceptée (2026-03-12)
- Contexte : 1 million de mouvements par an, relations fortes, cohérence stricte (R-04).
- Options : base relationnelle ; base documentaire ; fichiers.
- Décision : base relationnelle.
- Conséquences acceptées : schéma à migrer à chaque évolution ; requêtes de reporting faciles.
```

Une décision n'est jamais effacée : si on change d'avis, une nouvelle décision **remplace** l'ancienne, qui reste dans l'historique.

## À décider maintenant (difficile à ajouter plus tard)

- format des erreurs renvoyées ;
- journalisation (quoi, où, sans données sensibles) ;
- configuration et secrets (jamais dans le code) ;
- migrations de la base de données ;
- versions des API publiques ;
- fuseau horaire et devise de référence.

## Critère de sortie

Les couches et modules sont fixés, et chaque choix technique important a sa décision `D-xx`.
