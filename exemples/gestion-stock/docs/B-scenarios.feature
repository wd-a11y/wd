# language: fr

Fonctionnalité: F-01 Enregistrer une entrée de pièces

  Scénario: S-01 Entrée de pièces (R-02, R-07)
    Soit une pièce "VIS-M6" avec un stock de 0
    Quand le magasinier enregistre une entrée de 10 "VIS-M6"
    Alors le stock de "VIS-M6" est 10

  Scénario: S-04 Quantité nulle ou négative refusée (R-02)
    Soit une pièce "VIS-M6" avec un stock de 10
    Quand le magasinier enregistre une sortie de 0 "VIS-M6"
    Alors le mouvement est refusé avec le message "Une quantité doit être un entier strictement positif"
    Et le stock de "VIS-M6" reste 10

Fonctionnalité: F-02 Sortir des pièces du stock

  Scénario: S-02 Sortie normale (R-04, R-07)
    Soit une pièce "VIS-M6" avec un stock de 10
    Quand le magasinier sort 4 "VIS-M6"
    Alors le stock de "VIS-M6" est 6

  Scénario: S-03 Sortie supérieure au stock refusée (R-04)
    Soit une pièce "VIS-M6" avec un stock de 10
    Quand le magasinier sort 12 "VIS-M6"
    Alors la sortie est refusée avec le message "Stock insuffisant : 10 disponibles"
    Et le stock de "VIS-M6" reste 10

  Scénario: S-05 Sortie qui amène le stock exactement à zéro (R-04)
    Soit une pièce "VIS-M6" avec un stock de 10
    Quand le magasinier sort 10 "VIS-M6"
    Alors le stock de "VIS-M6" est 0

  Scénario: S-07 Deux sorties simultanées sur la même pièce (R-04)
    Soit une pièce "VIS-M6" avec un stock de 10
    Quand deux magasiniers sortent chacun 6 "VIS-M6" au même instant
    Alors une seule sortie est acceptée
    Et le stock de "VIS-M6" est 4

  Scénario: S-09 Sortie reçue deux fois (R-08)
    Soit une pièce "VIS-M6" avec un stock de 10
    Quand la même sortie de 4 "VIS-M6" arrive deux fois avec le même identifiant de requête
    Alors le stock de "VIS-M6" est 6
    Et la pièce a un seul mouvement de sortie

  Scénario: S-10 Personne non autorisée (R-03)
    Soit une pièce "VIS-M6" avec un stock de 10
    Quand un visiteur sort 4 "VIS-M6"
    Alors la sortie est refusée pour accès non autorisé
    Et le stock de "VIS-M6" reste 10

  Scénario: S-12 Correction d'une erreur de saisie (R-09, R-07)
    Soit une pièce "VIS-M6" avec un stock de 10
    Et une sortie de 4 "VIS-M6" saisie par erreur
    Quand le magasinier enregistre une entrée corrective de 4 "VIS-M6"
    Alors le stock de "VIS-M6" est 10
    Et les deux mouvements restent visibles dans l'historique

Fonctionnalité: F-03 Être alerté d'un stock bas

  Scénario: S-06 Alerte au passage sous le seuil (R-05)
    Soit une pièce "VIS-M6" avec un stock de 6 et un seuil d'alerte de 5
    Quand le magasinier sort 2 "VIS-M6"
    Alors l'événement StockBas est publié pour "VIS-M6" avec un stock de 4
    Quand le magasinier sort encore 1 "VIS-M6"
    Alors aucune nouvelle alerte n'est publiée

Fonctionnalité: F-04 Créer et archiver une pièce

  Scénario: S-08 Mouvement refusé sur une pièce archivée (R-06)
    Soit une pièce "VIS-M6" archivée
    Quand le magasinier enregistre une entrée de 5 "VIS-M6"
    Alors le mouvement est refusé avec le message "La pièce VIS-M6 est archivée"

  Scénario: S-11 Référence en double refusée (R-01)
    Soit une pièce "VIS-M6"
    Quand le responsable crée une pièce "VIS-M6"
    Alors la création est refusée

  Scénario: S-13 Un magasinier ne crée pas de pièce (R-10)
    Quand un magasinier crée une pièce "VIS-M8"
    Alors la création est refusée pour accès non autorisé
