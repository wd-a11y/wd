# language: fr

Fonctionnalité: F-01 Retenir puis confirmer des places

  Scénario: S-01 Retenue puis confirmation (R-01, R-03)
    Soit la place "A12" libre pour la séance du 14 mars à 20 h
    Quand le spectateur retient "A12" puis le prestataire accepte le paiement
    Alors la réservation est confirmée
    Et "A12" n'est plus proposée

  Scénario: S-02 Place déjà retenue (R-01)
    Soit la place "A12" retenue par un autre client
    Quand le spectateur retient "A12"
    Alors la demande est refusée avec le message "Place indisponible"

  Scénario: S-03 Retenue expirée (R-02)
    Soit une retenue de "A12" créée à 20 h 00
    Quand il est 20 h 10 et aucun paiement n'est arrivé
    Alors la réservation est expirée
    Et "A12" est de nouveau libre

  Scénario: S-04 Cinquante clients veulent la même place au même instant (R-01)
    Soit la place "A12" libre
    Quand 50 requêtes de retenue sur "A12" arrivent dans la même milliseconde
    Alors une seule retenue est créée
    Et les 49 autres reçoivent "Place indisponible"

  Scénario: S-05 Paiement arrivé après expiration (R-03)
    Soit une réservation de "A12" expirée
    Quand le prestataire accepte le paiement
    Alors la réservation reste expirée
    Et le paiement est remboursé automatiquement

  Scénario: S-06 Requête répétée après coupure réseau (R-07)
    Soit un revendeur qui retient "B4" avec la clé d'idempotence "k-981"
    Quand il renvoie la même requête avec la clé "k-981"
    Alors il reçoit la même réservation
    Et une seule réservation existe

  Scénario: S-07 Plus de 8 places (R-06)
    Soit un client qui a déjà 6 places actives pour la séance
    Quand il retient 3 places de plus
    Alors la demande est refusée avec le message "8 places au plus par séance"

Fonctionnalité: F-02 Annuler une réservation

  Scénario: S-08 Annulation trop tardive (R-04)
    Soit une réservation confirmée pour demain 20 h
    Quand le client annule aujourd'hui à 21 h
    Alors l'annulation est refusée

Fonctionnalité: F-03 Accès des revendeurs partenaires par API

  Scénario: S-09 Lecture de la réservation d'un autre (R-05)
    Soit la réservation "R-ID-1043" d'un autre client
    Quand le spectateur demande "R-ID-1043"
    Alors il reçoit "introuvable", sans indication que la réservation existe

  Scénario: S-10 Revendeur trop rapide (R-08)
    Quand un revendeur envoie 50 requêtes en une seconde
    Alors 20 sont servies et 30 reçoivent "trop de requêtes"
