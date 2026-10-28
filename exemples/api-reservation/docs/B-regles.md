# Règles métier

| Id | Règle | Type | Exemple | Contre-exemple | Besoin |
| --- | --- | --- | --- | --- | --- |
| R-01 | Une place a au plus une réservation active (retenue ou confirmée) par séance. | Invariant | place A12 libre → retenue acceptée | A12 déjà retenue → refus « Place indisponible » | B-01 |
| R-02 | Une retenue expire 10 minutes après sa création si elle n'est pas payée. | Politique (durée réglable) | retenue à 20 h 00, rien à 20 h 10 → expirée | — | B-01 |
| R-03 | Une réservation n'est confirmée que si le prestataire accepte le paiement et si elle est encore retenue. | Invariant (état) | retenue + paiement accepté → confirmée | expirée + paiement accepté → reste expirée, remboursement | B-01 |
| R-04 | Une réservation confirmée s'annule jusqu'à 24 h avant la séance. | Politique | séance demain 20 h, annulation aujourd'hui 18 h → acceptée | annulation aujourd'hui 21 h → refusée | F-02 |
| R-05 | Un spectateur ne lit que ses propres réservations ; un revendeur, celles de ses clients. | Autorisation (parade à M-01) | spectateur lit sa réservation → acceptée | il lit celle d'un autre → réponse « introuvable » | F-03 |
| R-06 | Un client retient au plus 8 places par séance, toutes réservations actives confondues. | Politique (parade à M-02) | 8 places → acceptée | 6 puis 3 → la seconde est refusée | B-01 |
| R-07 | Deux requêtes avec la même clé d'idempotence donnent le même résultat et une seule réservation. | Invariant | réseau coupé, requête renvoyée → même réservation | — | B-01 |
| R-08 | Un revendeur envoie au plus 20 requêtes par seconde ; au-delà, réponse « trop de requêtes ». | Politique (parade à M-03) | 15 par seconde → servies | 50 par seconde → 30 refusées | B-02 |
