# Étape 10 — Définir les événements métier

**Phase :** B · **Livrable :** liste des événements dans `docs/B-modele.md` · **Durée indicative :** une demi-journée

## Pourquoi

Un logiciel évolue à partir d'événements. Chaque événement devient plus tard un flux logique : quelque chose arrive, le système réagit.

## Commande ou événement ?

| | Commande | Événement |
| --- | --- | --- |
| Nature | Une intention | Un fait accompli |
| Temps | Impératif | Passé |
| Peut être refusée ? | Oui | Non, c'est déjà arrivé |
| Exemple | « Valider la commande » | `CommandeValidée` |

## Pour chaque événement

- **Nom au passé** : `CommandeValidée`, `PaiementÉchoué`, `SeuilDépassé`, `StockÉpuisé`.
- **Déclencheur** : quelle commande ou quel fait extérieur.
- **Données transportées** : ce dont les réactions ont besoin.
- **Réactions** : ce qui doit se passer ensuite (notifier, recalculer, déclencher autre chose).
- **Si une réaction échoue** : réessayer ? combien de fois ? prévenir qui ?

## Technique : l'atelier Event Storming

Avec des personnes du métier, on colle des notes sur un mur ou un tableau blanc numérique :

1. les événements, au passé, de gauche à droite dans l'ordre du temps ;
2. puis les commandes qui les déclenchent ;
3. puis les acteurs, les règles, les systèmes externes ;
4. on entoure les zones où les questions s'accumulent : ce sont les zones de risque.

## Exemple

| Événement | Déclencheur | Données | Réactions | Si échec |
| --- | --- | --- | --- | --- |
| `SeuilDépassé` | Mesure > 30 °C | capteur, valeur, heure | couper le chauffage, alarme | alarme locale sonore, nouvel essai toutes les 2 s |
| `StockÉpuisé` | Sortie qui amène le stock à 0 | pièce, date | proposer une commande fournisseur | file d'attente, nouvel essai |

## Critère de sortie

Chaque changement d'état de l'étape 9b correspond à un événement nommé, avec ses réactions et son comportement en cas d'échec.
