# language: fr
# Un scénario par cas : normal, atypique, erreur, rare, impossible.
# Chaque scénario porte un identifiant S-xx et cite ses règles entre parenthèses.
# Valeurs concrètes, mots du glossaire, un seul « Quand ».

Fonctionnalité: F-01 [nom de la fonctionnalité]

  Scénario: S-01 [cas normal] (R-01)
    Soit [situation de départ avec des valeurs concrètes]
    Quand [une seule action]
    Alors [résultat attendu]
    Et [effet sur les données]

  Scénario: S-02 [cas d'erreur] (R-01)
    Soit [situation de départ]
    Quand [action qui viole la règle]
    Alors [refus et message exact]
    Et [les données sont inchangées]
