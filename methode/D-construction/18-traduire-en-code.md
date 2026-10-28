# Étape 18 — Traduire chaque concept en code

**Phase :** D · **Livrable :** le code de la tranche · **Durée indicative :** selon la tranche

## Pourquoi

Le code n'est pas inventé au moment de l'écrire : il est la traduction d'une analyse déjà faite. Chaque concept du modèle a une place précise dans le code.

## La table de traduction

| Concept métier | En code | Exemple |
| --- | --- | --- |
| Entité | Classe ou structure avec un identifiant stable | `Piece(id, reference, …)` |
| Objet-valeur | Type immuable, comparé par valeur | `Quantite(4)`, `Creneau(debut, fin)` |
| Invariant | Vérifié dans le constructeur et les méthodes : l'objet invalide ne peut pas exister | `Quantite(-3)` lève une erreur |
| Validation d'entrée | À la frontière, avant d'entrer dans le domaine | schéma du formulaire ou de l'API |
| Autorisation | Dans le cas d'usage, avant toute action | refuser si l'utilisateur n'est pas affecté |
| Politique | Paramètre lu dans la configuration | `DELAI_RELANCE_JOURS = 3` |
| Calcul | Fonction pure, sans effet de bord | `total(lignes, remise)` |
| Machine à états | Méthodes de transition explicites ; pas de champ « statut » modifiable librement | `reservation.annuler()` |
| Événement | Objet nommé au passé, publié après l'enregistrement | `StockEpuise(piece_id, date)` |
| Scénario | Cas d'usage (service applicatif) | `SortirPiece.executer(...)` |
| Cas limite | Erreur typée + test dédié | `StockInsuffisant` |
| Relation | Référence par identifiant entre agrégats ; référence directe à l'intérieur | `ligne.produit_id` |
| Logique répétée | Fonction réutilisable | |

## Règles de nommage

- **Les mots du glossaire, et seulement eux**, dans les noms de classes, fonctions, tables, champs, écrans et messages.
- Une méthode porte le nom d'une action métier (`annuler`, `confirmer`), pas d'une opération technique (`setStatus`).
- Le code cite les identifiants qu'il implémente en commentaire quand c'est utile : `# R-04`.

## Exemple (Python)

```python
class StockInsuffisant(Exception):
    pass

class Piece:
    def __init__(self, reference: str, stock: int = 0):
        if stock < 0:
            raise ValueError("R-04 : le stock ne devient jamais négatif")
        self.reference = reference
        self._stock = stock

    def sortir(self, quantite: int) -> None:
        if quantite <= 0:
            raise ValueError("R-02 : une quantité est strictement positive")
        if quantite > self._stock:  # R-04
            raise StockInsuffisant(f"Stock insuffisant : {self._stock} disponibles")
        self._stock -= quantite
```

## Critère de sortie

Chaque concept de la tranche a sa traduction, les noms suivent le glossaire, et aucune règle métier ne vit dans l'interface ou l'infrastructure.
