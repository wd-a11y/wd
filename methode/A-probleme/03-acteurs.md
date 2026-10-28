# Étape 3 — Identifier les acteurs et leurs droits

**Phase :** A · **Livrable :** section « Acteurs » de `docs/A-probleme.md` · **Durée indicative :** une demi-journée

## Pourquoi

Un logiciel n'est jamais « pour un utilisateur ». Différents profils ont des besoins, des compétences et des droits différents ; d'autres systèmes interagissent avec lui ; et quelqu'un essaiera peut-être d'en abuser.

## Questions à poser

Pour chaque profil humain (débutant, avancé, administrateur, opérateur, technicien, gestionnaire, invité, client, fournisseur…) :

- Qui est-il, pourquoi utilise-t-il le système, à quelle fréquence ?
- Avec quel niveau de compétence et sur quel appareil ?
- Qu'a-t-il le droit de voir et de faire ?

Puis :

- **Quels systèmes externes** interagissent avec le logiciel : service de paiement, envoi de SMS ou de courriels, capteurs, API d'un partenaire, annuaire d'entreprise ? Ce sont des acteurs : ils peuvent être lents, en panne, ou répondre n'importe quoi.
- **Qui aurait intérêt à tricher, voler ou casser** ? Un utilisateur qui veut voir les données d'un autre, un concurrent, un robot qui crée des comptes en masse.

## Livrable

- La liste des profils avec leurs caractéristiques.
- La liste des systèmes externes.
- L'acteur malveillant et ses motivations probables.
- **La matrice des droits** : une ligne par action importante, une colonne par acteur.

## Exemple

| Action | Client | Réceptionniste | Gérant | Service de paiement |
| --- | --- | --- | --- | --- |
| Créer une réservation | Les siennes | Pour tout client | Pour tout client | Non |
| Annuler une réservation | Les siennes, plus de 24 h avant | Toutes | Toutes | Non |
| Voir le chiffre d'affaires | Non | Non | Oui | Non |
| Confirmer un paiement | Non | Non | Non | Oui |

## Pièges

- Oublier les administrateurs et les opérateurs, qui ont souvent le plus de droits.
- Oublier que les systèmes externes tombent en panne.
- Penser « personne n'a intérêt à tricher ».

## Critère de sortie

Chaque acteur, humain ou système, apparaît dans la matrice des droits, et l'acteur malveillant est décrit.
