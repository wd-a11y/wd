# Glossaire

| Terme | Définition | Exemple | Type | Synonymes interdits |
| --- | --- | --- | --- | --- |
| Pièce | Article stocké au magasin, identifié par une référence unique | « VIS-M6 », vis M6 x 20 | Entité, racine d'agrégat | article, produit |
| Référence | Code unique d'une pièce | VIS-M6 | Objet-valeur | code, SKU |
| Quantité | Nombre entier strictement positif d'unités | 4 | Objet-valeur | nombre |
| Mouvement | Entrée ou sortie d'une quantité d'une pièce, à un instant, jamais modifié | Sortie de 4 VIS-M6 le 3 mars à 10 h | Entité, à l'intérieur de l'agrégat Pièce | opération, transaction |
| Stock | Quantité disponible d'une pièce : entrées moins sorties | 6 | Calculé | inventaire |
| Seuil d'alerte | Stock en dessous duquel il faut commander | 5 | Donnée de la pièce | minimum |
| Identifiant de requête | Code unique fourni par la tablette pour chaque saisie, pour ne jamais l'enregistrer deux fois | `a3f9-…` | Objet-valeur | — |
| Archiver | Retirer une pièce de l'usage, en gardant son historique | — | Action | supprimer |
