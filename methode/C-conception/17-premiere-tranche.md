# Étape 17 — Choisir la première tranche

**Phase :** C · **Livrable :** section « Ordre de construction » de `docs/C-architecture.md` · **Durée indicative :** 1 heure

## Pourquoi

On ne commence jamais par hasard. Et on ne commence pas par un objet isolé : un objet seul, sans écran ni stockage, ne prouve rien à l'utilisateur. On commence par une **tranche verticale** : le premier scénario complet qui apporte de la valeur.

## Critères, dans l'ordre

1. **Le plus risqué** : celui qui peut faire échouer le projet (règle complexe, intégration externe incertaine, performance critique).
2. **Le plus central** : celui sans lequel le logiciel n'a pas de sens.
3. **Le plus simple à isoler** : celui qui dépend du moins d'autres choses.

## Exemple

| Projet | Première tranche | Pourquoi |
| --- | --- | --- |
| Gestion de stock | F-02 Sortir une pièce (S-01, S-03, S-07) | Central, et porte la règle la plus risquée : stock jamais négatif, même en concurrence |
| API de réservation | F-01 Réserver un siège (S-01, S-04) | Risque principal : double réservation sous forte charge |
| Thermostat | F-01 Couper le chauffage au-dessus du seuil (S-01, S-02) | Risque principal : sécurité physique |

## Puis l'ordre de construction

Lister les tranches suivantes dans l'ordre, avec pour chacune les fonctionnalités, scénarios et règles qu'elle couvre. Cet ordre se révise à chaque boucle.

## Critère de sortie

La première tranche est choisie, ses scénarios et règles sont listés, et la raison du choix est écrite.
