# D-01 — Base relationnelle avec verrou par pièce

- **Statut :** acceptée (2026-02-21)
- **Contexte :** 50 000 mouvements par an ; deux tablettes peuvent sortir la même pièce au même instant (H-02) ; le stock ne doit jamais devenir négatif (R-04) ; l'historique ne doit jamais être modifié (R-09).
- **Options envisagées :**
  1. Base relationnelle, verrou sur la ligne de la pièce pendant la sortie.
  2. Base documentaire, pièce et mouvements dans un même document, contrôle de version optimiste.
  3. Fichier tableur partagé.
- **Décision :** option 1. Transactions et verrous éprouvés, requêtes d'inventaire simples, déjà maîtrisée par l'équipe.
- **Conséquences acceptées :** les sorties d'une même pièce sont traitées l'une après l'autre (sans effet notable à ce volume) ; le schéma doit être migré à chaque évolution. L'exemple de ce dépôt utilise un dépôt en mémoire avec le même principe de verrou.
