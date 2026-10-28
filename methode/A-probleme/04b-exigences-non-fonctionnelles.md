# Étape 4b — Exigences non fonctionnelles

**Phase :** A · **Livrable :** section « Exigences non fonctionnelles » de `docs/A-probleme.md` · **Durée indicative :** une demi-journée

## Pourquoi

Les fonctionnalités disent ce que le logiciel **fait**. Les exigences non fonctionnelles disent ce qu'il doit **être** : rapide, sûr, disponible, abordable. Un excellent modèle métier peut donner un logiciel inutilisable (trop lent), illégal (données personnelles mal protégées) ou trop cher à héberger. Ces exigences guident les choix techniques de la phase C : il faut les connaître avant.

## Questions à poser, avec un seuil mesurable pour chacune

| Famille | Question | Exemple de seuil |
| --- | --- | --- |
| Performance | Combien de temps l'utilisateur peut-il attendre ? | Écran principal affiché en moins de 1 s |
| Volume | Combien d'utilisateurs et de données dans 1 an ? dans 3 ans ? | 1 million d'enregistrements la première année |
| Disponibilité | Que se passe-t-il s'il est arrêté une heure ? | Saisie possible hors connexion, synchronisation ensuite |
| Temps réel | Quel délai maximal entre un événement et la réaction ? | Chauffage coupé moins de 2 s après un dépassement |
| Sécurité | Quelles données sont sensibles ? Qui ne doit jamais les voir ? | Données sensibles chiffrées, connexion à deux facteurs pour les administrateurs |
| Données personnelles | Quelle loi s'applique ? Combien de temps garde-t-on ? | Suppression du compte = effacement sous 30 jours |
| Traçabilité | Faut-il prouver qui a fait quoi ? | Chaque accès à un dossier est journalisé 5 ans |
| Accessibilité et langues | Qui doit pouvoir l'utiliser, sur quel appareil, en quelle langue ? | Utilisable sur un téléphone d'entrée de gamme, en 2 langues |
| Coût | Combien peut coûter l'exploitation par mois ? | Plafond d'hébergement fixé avant de choisir la techno |
| Maintenabilité | Qui le fera évoluer, avec quelles compétences ? | Un développeur seul comprend un module en 1 heure |
| Ressources matérielles | Mémoire, processeur, énergie disponibles ? | Moins de 64 Ko de mémoire vive sur le microcontrôleur |

## Pièges

- Des adjectifs au lieu de seuils : « rapide », « sécurisé », « scalable ».
- Viser trop haut par réflexe (« disponible 99,999 % ») alors que le métier tolère une heure d'arrêt : cela coûte très cher pour rien.
- Découvrir la contrainte légale après la mise en production.

## Critère de sortie

Chaque famille pertinente pour le projet a un seuil chiffré, ou une mention explicite « sans objet ».
