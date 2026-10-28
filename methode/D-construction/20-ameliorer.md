# Étape 20 — Corriger, simplifier, améliorer

**Phase :** D · **Livrable :** la tranche « finie » · **Durée indicative :** 10 à 20 % du temps de la tranche

## Pourquoi

Le premier jet n'est jamais parfait. Un bon projet devient plus clair à chaque itération, à condition de prendre le temps de revenir dessus.

## Ce qu'on améliore

- corriger les erreurs ;
- simplifier ;
- renommer clairement, avec les mots du glossaire ;
- mieux découper ;
- réduire les doublons ;
- mieux séparer les responsabilités.

**On ne restructure le code que tests au vert, par petits pas.** Si un test devient rouge, on revient au pas précédent.

## La définition du « fini »

Une tranche est finie quand :

- [ ] tous les tests passent, y compris les cas limites retenus ;
- [ ] chaque règle touchée est citée par un test (`wd-check` sans erreur) ;
- [ ] le code a été relu, par une personne ou un outil de revue ;
- [ ] les noms suivent le glossaire ; il n'y a pas de doublon évident ;
- [ ] glossaire, modèle, règles, décisions et traçabilité sont à jour ;
- [ ] la dette technique acceptée est notée, avec sa raison et une date de révision.

Cette liste est aussi le modèle de pull request du dépôt (`.github/PULL_REQUEST_TEMPLATE.md`).

## Critère de sortie

Toutes les cases de la définition du « fini » sont cochées.
