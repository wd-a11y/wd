# Étape 13 — Chercher les cas limites

**Phase :** B · **Livrable :** nouveaux scénarios dans `docs/B-scenarios.feature` · **Durée indicative :** une demi-journée

## Pourquoi

C'est l'étape qui évite le plus de bugs. La plupart des pannes en production viennent de cas que personne n'a imaginés : une valeur vide, une coupure réseau, deux actions en même temps.

## La grille

On passe chaque scénario dans cette grille. Chaque case pertinente devient un nouveau scénario ou une nouvelle règle.

| Famille | À vérifier |
| --- | --- |
| **Entrées** | vide, nul, zéro, négatif, énorme, trop long, caractères spéciaux, mauvais format, doublon |
| **Temps** | fuseau horaire, minuit, fin de mois, 29 février, changement d'heure, horloge de l'appareil fausse, expiration, délai dépassé |
| **Concurrence** | double clic, deux appareils en même temps, deux utilisateurs sur le même objet, course entre lecture et écriture |
| **Réseau** | coupure pendant l'envoi, délai dépassé, réponse perdue, requête reçue deux fois |
| **Systèmes externes** | panne, lenteur, réponse invalide, réponse arrivée après abandon, changement de format |
| **Matériel** | capteur défaillant, valeur hors plage, batterie faible, redémarrage brutal |
| **Données** | relation cassée, objet supprimé entre-temps, données anciennes après une migration |
| **Volume** | 0 élément, 1 élément, la limite exacte, 100 000 éléments |
| **Humain** | erreur de saisie, annulation, retour arrière, abandon au milieu, copier-coller |

## Le cas qu'on oublie toujours : la requête reçue deux fois

Le réseau peut perdre la réponse ; l'application renvoie alors la requête. Si le serveur la traite deux fois, on obtient deux commandes, deux paiements. La parade s'appelle l'**idempotence** : refaire la même action, avec le même identifiant de requête, donne le même résultat qu'une seule fois.

## Exemple

> **S-07** — Deux magasiniers sortent chacun 6 « Vis M6 » au même moment, sur un stock de 10. *Attendu :* une sortie acceptée (stock 4), l'autre refusée. *Règle :* R-04. *Conséquence de conception :* la sortie doit verrouiller le stock de la pièce (étape 9, agrégat).

## Critère de sortie

La grille est passée sur chaque scénario, et chaque cas retenu est devenu un scénario, une règle ou une hypothèse.
