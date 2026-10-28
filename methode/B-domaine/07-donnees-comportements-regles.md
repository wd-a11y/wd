# Étape 7 — Séparer données, comportements et règles

**Phase :** B · **Livrable :** compléter les fiches de `docs/B-modele.md` · **Durée indicative :** une demi-journée

## Pourquoi

Mélanger ce qu'un objet contient, ce qu'il fait et ce qu'il a le droit de faire donne un modèle confus. Les séparer garde le modèle propre et prépare directement le code.

## Les trois angles

| Angle | Question | Exemples |
| --- | --- | --- |
| **Données** | Que contient-il ? | nom, date, quantité, montant, statut, identifiant, description |
| **Comportements** | Que peut-il faire ? | créer, modifier, valider, annuler, calculer, archiver, transférer |
| **Règles** | Qu'a-t-il le droit de faire ? | une quantité n'est jamais négative ; une réservation ne se chevauche pas ; une commande validée ne se modifie plus |

## Préciser chaque donnée

Pour chaque donnée : **type, unité, format, plage permise, longueur maximale**.

Trois pièges classiques à régler dès maintenant :

- **L'argent** ne se stocke jamais en nombre à virgule flottante (0,1 + 0,2 ≠ 0,3). On utilise un entier dans la plus petite unité (centimes) ou un décimal exact, avec la devise.
- **Une date sans fuseau horaire est ambiguë.** On stocke en temps universel (UTC) et on affiche en heure locale ; une date sans heure (anniversaire) reste une date sans heure.
- **Un texte a une longueur maximale** et un jeu de caractères ; un nom peut contenir des accents, des apostrophes, des tirets.

## Exemple

| Donnée | Type | Unité / format | Plage | Remarque |
| --- | --- | --- | --- | --- |
| quantite | entier | pièces | 0 à 1 000 000 | jamais négative |
| prix_unitaire | entier | centimes, avec devise | ≥ 0 | |
| debut | date et heure | UTC, ISO 8601 | futur à la création | affiché en heure locale |
| temperature | décimal | °C, 1 décimale | −40 à 85 | plage du capteur |

## Critère de sortie

Chaque donnée de chaque objet a un type, une unité ou un format, et une plage. Comportements et règles sont listés séparément.
