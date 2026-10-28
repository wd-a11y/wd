# Étape 5 — Lister les objets et fixer le vocabulaire

**Phase :** B · **Livrables :** `docs/B-glossaire.md`, début de `docs/B-modele.md` · **Durée indicative :** 1 jour

## Pourquoi

Les objets du métier sont la matière première du logiciel. Et si deux personnes utilisent le même mot pour deux choses différentes, le code héritera de la confusion.

## Démarche

1. **Inventaire brut.** Tout ce qui existe dans le domaine, sans trier trop vite : utilisateur, compte, produit, commande, ligne de commande, patient, rendez-vous, vol, siège, réservation, capteur, mesure, consigne, message, paiement… Les processus de l'étape 4 en fournissent la plupart.
2. **Classement :**
   - objets **centraux** : la raison d'être du logiciel ;
   - objets **secondaires** : ils servent les centraux ;
   - objets **de référence** : listes stables (pays, catégories, unités) ;
   - objets **événementiels** : ce qui arrive à un moment (paiement, mesure, connexion) ;
   - objets **techniques** éventuels (session, fichier importé).
3. **Entité ou objet-valeur ?**
   - Une **entité** a une identité qui dure même quand ses données changent : un client reste le même client s'il déménage.
   - Un **objet-valeur** n'est défini que par ses valeurs, ne change jamais, et se remplace : un montant, une adresse, une période, une température. Deux montants de 5 € sont interchangeables ; deux clients nommés Martin ne le sont pas.
4. **Glossaire.** Un terme = une définition d'une phrase + un exemple. **Les synonymes sont interdits** : on choisit « client » ou « usager », pas les deux. Ces mots servent ensuite partout : documents, code, écrans, tests, conversations.

## Exemple d'entrée de glossaire

| Terme | Définition | Exemple | Type |
| --- | --- | --- | --- |
| Réservation | Engagement d'un client sur un créneau d'une ressource | Martin, salle 2, mardi 18 h–19 h | Entité |
| Créneau | Intervalle de temps avec un début et une fin | mardi 18 h–19 h | Objet-valeur |
| Mouvement de stock | Entrée ou sortie d'une quantité d'une pièce, à un instant | Sortie de 4 vis M6 le 3 mars à 10 h | Entité événementielle |

## Pièges

- Classer trop vite et oublier des objets : l'inventaire brut d'abord.
- Garder des mots flous : « dossier », « élément », « données », « info ».
- Inventer des mots techniques là où le métier a déjà les siens.

## Critère de sortie

Chaque objet est classé et typé (entité ou objet-valeur), et chaque terme du glossaire a une seule définition, sans synonyme.
