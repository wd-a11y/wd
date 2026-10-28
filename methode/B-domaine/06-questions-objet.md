# Étape 6 — Interroger chaque objet

**Phase :** B · **Livrable :** une fiche par objet central et secondaire dans `docs/B-modele.md` · **Durée indicative :** 1 à 2 heures par objet central

## Pourquoi

Le même filtre de questions, appliqué à chaque objet, révèle son rôle réel, ses dépendances et les règles qui le concernent.

## Les douze questions

1. Qui est-il ?
2. Pourquoi existe-t-il ?
3. De quoi a-t-il besoin pour exister ?
4. Que sait-il ? (ses données)
5. Que fait-il ? (ses comportements)
6. Comment évolue-t-il ? (ses états)
7. Avec qui interagit-il ?
8. Quelles règles le concernent ?
9. Quels événements le font changer ?
10. **Qu'est-ce qui le rend unique ?** Deux demandes identiques à la même minute sont-elles un doublon ou deux demandes réelles ?
11. **Qui a le droit** de le créer, le lire, le modifier, le supprimer ?
12. **Comment meurt-il ?** Suppression, archivage, anonymisation ? Combien de temps doit-on le garder, légalement ou pour le métier ?

## Exemple de fiche : Mesure (thermostat de serre)

- *Qui :* une valeur de température lue par un capteur à un instant.
- *Pourquoi :* décider d'allumer ou couper le chauffage, et prouver après coup ce qui s'est passé.
- *Besoin pour exister :* un capteur, une valeur, un horodatage.
- *Unique :* capteur + horodatage ; deux mesures du même capteur à la même milliseconde sont un doublon.
- *Droits :* créée seulement par un capteur enregistré ; jamais modifiée.
- *Mort :* conservée 1 an en détail, puis agrégée par heure.

## Pièges

- Répondre « rien » à « comment meurt-il ? » : tout objet finit par être supprimé, archivé ou oublié, et c'est souvent là que les bugs se cachent.
- Sauter les objets secondaires : ils portent souvent les règles délicates.

## Critère de sortie

Chaque objet central et secondaire a sa fiche, avec une réponse explicite aux questions 10, 11 et 12.
