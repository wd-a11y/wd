# Règles métier

Les règles R-01, R-02 et R-07 sont des **règles de sécurité** : elles l'emportent sur toutes les autres.

| Id | Règle | Type | Exemple | Contre-exemple | Besoin |
| --- | --- | --- | --- | --- | --- |
| R-01 | Quand une mesure valide dépasse 30 °C, le chauffage est coupé en moins de 2 s, quoi qu'il arrive. | Invariant de sécurité | 30,4 °C → coupé en 0,3 s | chauffage encore allumé 3 s après 31 °C → défaut | B-01 |
| R-02 | Si aucune mesure valide n'est reçue depuis 10 s, le chauffage est coupé et l'alarme déclenchée. | Invariant de sécurité | capteur débranché → coupé à 10 s | — | B-01 |
| R-03 | Une mesure hors de −40 à 85 °C est invalide et ignorée. | Validation d'entrée | 21,5 °C → valide | 127,0 °C → invalide | B-01 |
| R-04 | En régulation, le chauffage s'allume sous consigne − 0,5 °C et s'arrête au-dessus de consigne + 0,5 °C. | Calcul | consigne 18, mesure 17,4 → allumé | mesure 18,2 et chauffage allumé → reste allumé | B-02 |
| R-05 | La consigne est comprise entre 5 et 28 °C. | Validation d'entrée | 18 → acceptée | 35 → refusée | F-03 |
| R-06 | Seule une commande signée par l'application de l'exploitant change la consigne. | Autorisation (parade à M-01) | commande signée → appliquée | commande non signée → ignorée et journalisée | F-03 |
| R-07 | Après un démarrage, le chauffage reste coupé jusqu'à 2 mesures valides consécutives. | Invariant de sécurité | redémarrage, 2 mesures à 17 °C → régulation | redémarrage, 1 mesure → reste coupé | B-01 |
| R-08 | Un micrologiciel n'est installé que s'il est signé ; s'il ne démarre pas, l'ancienne version est restaurée. | Invariant (parade à M-02) | mise à jour signée qui démarre → gardée | mise à jour non signée → refusée | F-04 |
