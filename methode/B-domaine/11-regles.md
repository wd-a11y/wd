# Étape 11 — Écrire les règles métier

**Phase :** B · **Livrable :** `docs/B-regles.md` · **Durée indicative :** 1 jour

## Pourquoi

Avant le code, on écrit les vérités du métier en phrases simples. Elles servent de base à toutes les validations et à tous les tests. Une règle qui n'est écrite nulle part finit oubliée ou appliquée différemment selon l'écran.

## Format d'une règle

- **Identifiant** : `R-01`, `R-02`…
- **Énoncé** : « **Quand** [événement], **si** [condition], **alors** [résultat], **sinon** [refus + message]. »
- **Type** (voir ci-dessous).
- **Source** : qui l'a dite, ou quel texte (loi, contrat, procédure).
- **Exemple** chiffré qui respecte la règle.
- **Contre-exemple** chiffré qui la viole.
- **Besoin** servi (`B-xx` ou `F-xx`).

## Les cinq types de règles

Le type dit où la règle vivra dans le code (voir [étape 18](../D-construction/18-traduire-en-code.md)).

| Type | Définition | Exemple | Où dans le code |
| --- | --- | --- | --- |
| **Invariant** | Toujours vrai, sans exception | Le stock ne devient jamais négatif | Dans l'objet : impossible de créer un objet invalide |
| **Validation d'entrée** | Format de ce qui arrive de l'extérieur | La date est au format AAAA-MM-JJ | À la frontière : formulaire, API |
| **Autorisation** | Qui peut faire quoi | Seul l'auteur d'un dossier peut le modifier | Couche application, avant toute action |
| **Politique** | Règle de gestion qui peut changer | Relance après 3 jours sans réponse | Paramètre configurable, jamais en dur |
| **Calcul** | Formule | Total = somme des lignes − remise | Fonction pure, testée à part |

## Exemple complet

> **R-04** — *Invariant.* Quand une sortie de stock est demandée, si la quantité demandée dépasse le stock disponible, alors la sortie est refusée avec le message « Stock insuffisant : N disponibles ».
> *Source :* responsable d'atelier. *Exemple :* stock 10, sortie 4 → acceptée, stock 6. *Contre-exemple :* stock 10, sortie 12 → refusée, stock reste 10. *Besoin :* B-01.

## Pièges

- Une règle sans contre-exemple : on ne sait pas vraiment ce qu'elle interdit.
- Une politique codée en dur : au premier changement, il faut redéployer.
- Une règle écrite seulement dans l'écran : elle est contournée par un appel direct.

## Critère de sortie

Chaque règle a son identifiant, son type, sa source, un exemple et un contre-exemple chiffrés, et le besoin qu'elle sert.
