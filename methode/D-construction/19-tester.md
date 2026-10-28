# Étape 19 — Tester à partir des scénarios

**Phase :** D · **Livrables :** les tests, `docs/tracabilite.md` · **Durée indicative :** en même temps que l'étape 18

## Pourquoi

Les tests confirment que la conception fonctionne réellement. Mais un test écrit après le code a tendance à confirmer le code, bugs compris. **Le test s'écrit avant ou en même temps que le code, à partir du scénario `S-xx` et de la règle `R-xx`.** Il vérifie alors le besoin, pas ce que le code fait déjà.

## Les questions que les tests doivent trancher

- Est-ce que ça fait ce qu'on veut ?
- Est-ce que ça refuse ce qu'on ne veut pas ?
- Est-ce que les données restent cohérentes ?
- Est-ce que le comportement est stable dans le temps ?
- Est-ce qu'un cas limite casse le système ?

## Les niveaux de tests

| Niveau | Ce qu'il prouve | Quantité |
| --- | --- | --- |
| Unitaire | Chaque invariant et chaque calcul : exemple **et** contre-exemple | Beaucoup, rapides |
| Propriétés | Un invariant tient pour des milliers de valeurs tirées au hasard | Pour les règles critiques |
| Intégration | Base de données, services externes simulés, pannes simulées | Moyen |
| Acceptation | Les scénarios Soit / Quand / Alors de bout en bout | Un par scénario clé |

Chaque case « interdit » d'une machine à états (étape 9b) est un test.

## Citer ce qu'on prouve

Un test cite la règle et le scénario qu'il prouve, dans son nom ou son commentaire :

```python
# R-04, S-03
def test_R04_sortie_superieure_au_stock_refusee():
    piece = Piece("Vis M6", stock=10)
    with pytest.raises(StockInsuffisant):
        piece.sortir(12)
    assert piece.stock == 10
```

C'est ce lien que vérifie `wd-check` : il signale toute règle qu'aucun test ne cite.

## La couverture qui compte

**Chaque `R-xx` a au moins un test qui la cite.** Le pourcentage de lignes couvertes est un indicateur secondaire : on peut couvrir 100 % des lignes sans tester une seule règle.

## Critère de sortie

Tous les tests passent, chaque règle de la tranche est citée par au moins un test, et `docs/tracabilite.md` est à jour.
