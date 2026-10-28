# language: fr

Fonctionnalité: F-01 Couper le chauffage en cas de danger

  Scénario: S-01 Surchauffe (R-01)
    Soit le régulateur en régulation, chauffage allumé
    Quand le capteur mesure 30,4 °C
    Alors le chauffage est coupé en moins de 2 s
    Et l'alarme se déclenche

  Scénario: S-02 Capteur débranché (R-02)
    Soit le régulateur en régulation
    Quand aucune mesure n'arrive pendant 10 s
    Alors le chauffage est coupé et l'alarme se déclenche

  Scénario: S-03 Valeur absurde du capteur (R-03, R-02)
    Soit le régulateur en régulation
    Quand le capteur envoie 127,0 °C pendant 12 s
    Alors les mesures sont ignorées
    Et le chauffage est coupé au bout de 10 s sans mesure valide

  Scénario: S-04 Redémarrage brutal (R-07)
    Soit une coupure de courant de 1 s pendant que le chauffage est allumé
    Quand le régulateur redémarre et reçoit une seule mesure valide
    Alors le chauffage reste coupé

Fonctionnalité: F-02 Réguler autour d'une consigne

  Scénario: S-05 Hystérésis (R-04)
    Soit une consigne de 18 °C et le chauffage allumé
    Quand le capteur mesure 18,2 °C
    Alors le chauffage reste allumé
    Quand le capteur mesure 18,6 °C
    Alors le chauffage s'arrête

Fonctionnalité: F-03 Changer la consigne depuis le téléphone

  Scénario: S-06 Consigne hors plage (R-05)
    Quand l'exploitant demande une consigne de 35 °C
    Alors la demande est refusée avec le message "Consigne entre 5 et 28 °C"

  Scénario: S-07 Commande non signée (R-06)
    Quand une commande de consigne non signée arrive par radio
    Alors elle est ignorée
    Et la tentative est journalisée

Fonctionnalité: F-04 Mettre à jour le micrologiciel

  Scénario: S-08 Mise à jour qui ne démarre pas (R-08)
    Soit une mise à jour signée installée
    Quand elle ne démarre pas trois fois de suite
    Alors l'ancienne version est restaurée
