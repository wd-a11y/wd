# Règles métier

| Id | Règle | Type | Source | Exemple | Contre-exemple | Besoin |
| --- | --- | --- | --- | --- | --- | --- |
| R-01 | Quand une pièce est créée, si sa référence existe déjà, alors la création est refusée. | Invariant | Responsable d'atelier | VIS-M6 puis VIS-M8 → acceptées | VIS-M6 deux fois → refus | F-04 |
| R-02 | Une quantité de mouvement est un entier strictement positif. | Validation d'entrée et invariant | Responsable d'atelier | 4 → accepté | 0, −3, 2,5 → refusés | F-01, F-02 |
| R-03 | Seuls un magasinier ou un responsable peuvent enregistrer un mouvement. | Autorisation | Responsable d'atelier ; menace M-02 | magasinier sort 4 → accepté | visiteur sort 4 → refusé | B-01 |
| R-04 | Quand une sortie est demandée, si la quantité dépasse le stock, alors elle est refusée avec « Stock insuffisant : N disponibles » ; le stock ne devient jamais négatif. | Invariant | Responsable d'atelier | stock 10, sortie 10 → stock 0 | stock 10, sortie 12 → refus, stock 10 | F-02 |
| R-05 | Quand une sortie fait passer le stock sous le seuil d'alerte, alors l'événement `StockBas` est publié, une seule fois par passage. | Politique (seuil réglable par pièce) | Acheteur | seuil 5, stock 6, sortie 2 → alerte | stock déjà 3, sortie 1 → pas de nouvelle alerte | F-03, B-02 |
| R-06 | Une pièce archivée n'accepte plus aucun mouvement. | Invariant (état) | Responsable d'atelier | pièce active, entrée 5 → accepté | pièce archivée, entrée 5 → refus | F-04 |
| R-07 | Le stock est la somme des entrées moins la somme des sorties ; les mouvements font foi. | Calcul | Responsable d'atelier | entrées 10 + 5, sortie 4 → 11 | — | B-01 |
| R-08 | Un mouvement reçu deux fois avec le même identifiant de requête n'est enregistré qu'une fois. | Invariant (idempotence) | Analyse des cas limites | même sortie envoyée 2 fois → 1 mouvement | — | B-01 |
| R-09 | Un mouvement n'est jamais modifié ni supprimé ; une erreur se corrige par un mouvement inverse. | Invariant | Menace M-01 | erreur de 4 → entrée corrective de 4 | modifier la quantité d'un mouvement → impossible | B-01 |
| R-10 | Seul un responsable peut créer ou archiver une pièce. | Autorisation | Responsable d'atelier | responsable crée VIS-M6 → accepté | magasinier crée VIS-M6 → refusé | F-04 |
