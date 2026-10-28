# Étape 16b — Le squelette marchant

**Phase :** C · **Livrable :** un dépôt de code qui tourne, se teste et se déploie · **Durée indicative :** 1 semaine maximum

## Pourquoi

Une analyse, même excellente, reste une hypothèse tant qu'elle n'a pas touché le réel. Le squelette marchant confronte tôt l'architecture à la réalité : la techno choisie fonctionne-t-elle vraiment ? le déploiement est-il possible ? la performance tient-elle ?

## Démarche

On fait traverser **une seule action minuscule** par toutes les couches, jusqu'à un environnement réel :

1. un écran (ou une API, ou une entrée matérielle) ;
2. un cas d'usage ;
3. un objet du domaine avec un seul invariant ;
4. une écriture et une relecture en stockage ;
5. un test automatique qui passe ;
6. un déploiement automatique vers un environnement de test.

Exemple : créer l'objet central avec un seul champ, l'enregistrer, le relire à l'écran. Pour un logiciel embarqué : lire un capteur et allumer une diode, sur la vraie carte.

## L'essai jetable

Si une technologie pose un doute précis (une bibliothèque, un service externe, une performance), on fait d'abord un **essai jetable** limité à 1 ou 2 jours. On note le résultat dans l'hypothèse `H-xx` correspondante, puis **on jette le code** : il a été écrit pour apprendre, pas pour durer.

## Pièges

- Construire un module entier au lieu d'une action minuscule.
- Repousser le déploiement « à la fin » : c'est souvent là que se cachent les mauvaises surprises.
- Garder le code d'un essai jetable en production.

## Critère de sortie

L'action minuscule traverse toutes les couches, un test la vérifie, et elle se déploie automatiquement. Les hypothèses techniques critiques sont tranchées.
