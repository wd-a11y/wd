# Étape 2 — Définir le périmètre

**Phase :** A · **Livrable :** section « Périmètre » de `docs/A-probleme.md` et `docs/hypotheses.md` · **Durée indicative :** une demi-journée

## Pourquoi

Sans limites écrites, chaque réunion ajoute une fonctionnalité et le projet ne finit jamais. Le périmètre protège contre la dérive et oblige à choisir.

## Questions à poser

- Quelle est la plus petite version qui résout déjà le problème de l'étape 1 ?
- Quelles fonctionnalités sont indispensables, importantes, bonus ?
- Que refuse-t-on volontairement de faire, et pourquoi ?
- Quelles contraintes s'imposent : délai, budget, compétences disponibles, lois, matériel cible ?
- Que suppose-t-on sans l'avoir vérifié ?
- Quel est le niveau du projet : S, M ou L ?

## Livrable

- **Les fonctionnalités `F-xx`**, chacune reliée à un besoin `B-xx`, triées en : *Indispensable / Important / Bonus / Pas maintenant*.
- **La liste « Ce que nous ne ferons pas »**, avec une raison par ligne.
- **Les contraintes**.
- **Les hypothèses `H-xx`** dans `docs/hypotheses.md` : énoncé, comment la vérifier, avant quand, statut (ouverte, confirmée, abandonnée).
- **Le niveau** S, M ou L ([voir les niveaux](../niveaux-S-M-L.md)).

## Exemples

- *Pas maintenant :* paiement en ligne (les clients paient sur place aujourd'hui ; on le reconsidère après 3 mois d'usage).
- *Ce que nous ne ferons pas :* gestion de la comptabilité (un logiciel existe déjà ; on exporte seulement les données).
- *H-02 :* les techniciens ont du réseau mobile sur site. Vérification : test sur 5 sites. Date : avant la fin de la phase B.

## Pièges

- Tout classer « indispensable ».
- Oublier de relier une fonctionnalité à un besoin : si elle ne sert aucun `B-xx`, pourquoi la faire ?
- Garder les hypothèses dans sa tête.

## Critère de sortie

Chaque fonctionnalité a un rang et un besoin, la liste des refus existe, les hypothèses ont une date de vérification, le niveau est choisi.
