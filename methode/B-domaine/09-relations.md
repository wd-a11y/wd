# Étape 9 — Identifier les relations entre objets

**Phase :** B · **Livrable :** diagramme et tableau des relations dans `docs/B-modele.md` · **Durée indicative :** une demi-journée

## Pourquoi

Les objets ne vivent pas isolés. Les relations construisent la carte structurelle du système, et décident ce qui se passe quand on supprime, modifie ou enregistre plusieurs objets à la fois.

## Questions à poser

- Qui appartient à qui ? Qui contient qui ? Qui dépend de qui ? Qui référence qui ?
- **Cardinalité** : 1–1, 1–N, N–N ? La relation est-elle obligatoire ?
- **Propriété** : si on supprime le parent, que deviennent les enfants ? Suppression en cascade, refus, ou archivage ?
- **Frontière de cohérence** : quels objets doivent changer **ensemble, d'un seul coup**, ou pas du tout ?

## La frontière de cohérence (agrégat)

Un **agrégat** est un groupe d'objets qui doit toujours rester cohérent, et qu'on enregistre en une seule fois. Il a une racine : on passe toujours par elle pour modifier l'intérieur.

- Une commande et ses lignes : **un agrégat**. Le total doit toujours correspondre aux lignes.
- Une commande et le stock du fournisseur : **deux agrégats**. On accepte qu'ils soient cohérents quelques secondes plus tard, via un événement.

Règle pratique : garder les agrégats **petits**. Un gros agrégat se verrouille souvent et ralentit tout le système.

## Exemple

| Relation | Cardinalité | Si le parent disparaît | Même agrégat ? |
| --- | --- | --- | --- |
| Commande → Ligne | 1 – N, au moins 1 | Les lignes disparaissent avec | Oui |
| Ligne → Produit | N – 1 | Suppression du produit refusée ; il est archivé | Non |
| Vol → Siège | 1 – N | Le vol est archivé, jamais supprimé | Oui |
| Capteur → Mesure | 1 – N | Les mesures sont conservées 1 an | Non |

## Pièges

- Supprimer physiquement un objet encore référencé : historique cassé, rapports faux.
- Faire de tout le système un seul agrégat « pour être sûr ».

## Critère de sortie

Chaque relation a sa cardinalité, son comportement à la suppression, et chaque objet appartient à un agrégat identifié.
