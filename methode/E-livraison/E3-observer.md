# Étape E3 — Observer en production

**Phase :** E · **Livrable :** journaux, alertes, tableau des mesures · **Durée indicative :** 1 jour

## Pourquoi

Sans observation, on découvre les pannes par les plaintes des utilisateurs, et on ne sait jamais si le logiciel atteint son but.

## Ce qu'on met en place

- **Journaux structurés** : qui, quoi, quand, résultat, identifiant de requête. **Jamais de données sensibles** dedans (mots de passe, données de santé, numéros de carte).
- **Remontée automatique des erreurs** vers l'équipe, avec leur contexte.
- **Alertes** sur ce qui compte : taux d'erreur, lenteur, file d'attente qui grossit, espace disque.
- **Les mesures de réussite `B-xx` de l'étape 1**, calculées automatiquement et visibles par l'équipe.

## Exemple

| Mesure | Source | Cible | Fréquence |
| --- | --- | --- | --- |
| B-01 Doubles réservations par mois | requête sur les réservations | 0 | quotidienne |
| B-02 Temps de prise de réservation | durée entre ouverture et confirmation | moins de 1 min | hebdomadaire |

## Critère de sortie

Une erreur en production arrive à l'équipe sans qu'un utilisateur la signale, et les mesures `B-xx` sont visibles.
