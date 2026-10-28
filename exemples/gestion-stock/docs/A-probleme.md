# Problème — Stock de l'atelier

Niveau du projet : **M** — une dizaine d'utilisateurs, des erreurs qui coûtent de l'argent, pas de donnée personnelle sensible.

## 1. Problème

> Pour les magasiniers d'un atelier de maintenance, qui notent les entrées et sorties de pièces dans un cahier, le problème est l'écart entre le cahier et les étagères. Aujourd'hui ils recomptent une fois par mois et commandent en urgence, ce qui coûte 2 ruptures imprévues par mois et environ 8 % d'écart à chaque inventaire.

### Preuve

| Personne (rôle) | Date | Ce qu'elle a fait la dernière fois | Ce que ça lui a coûté |
| --- | --- | --- | --- |
| Magasinier A | 2026-02-03 | Cherché des joints notés « 12 en stock », trouvé 0 | Machine arrêtée une demi-journée |
| Magasinier B | 2026-02-04 | Oublié de noter une sortie un jour de rush | Écart découvert 3 semaines plus tard |
| Responsable d'atelier | 2026-02-04 | Passé 2 jours à l'inventaire mensuel | 2 jours par mois |
| Technicien C | 2026-02-05 | Pris des vis sans passer par le magasin | Rupture le lendemain |
| Acheteur | 2026-02-06 | Commandé en express, 3 fois le prix | Surcoût de transport |

### Mesures de réussite

| Id | Mesure | Valeur actuelle | Cible | Comment on la mesure |
| --- | --- | --- | --- | --- |
| B-01 | Écart moyen à l'inventaire | 8 % | moins de 1 % | comparaison stock logiciel / comptage, chaque mois |
| B-02 | Ruptures imprévues | 2 par mois | 0 par mois | événements `StockBas` non suivis d'une commande |

## 2. Périmètre

### Fonctionnalités

| Id | Fonctionnalité | Besoin | Rang |
| --- | --- | --- | --- |
| F-01 | Enregistrer une entrée de pièces | B-01 | Indispensable |
| F-02 | Sortir des pièces du stock | B-01 | Indispensable |
| F-03 | Être alerté d'un stock bas | B-02 | Indispensable |
| F-04 | Créer et archiver une pièce | B-01 | Important |

### Ce que nous ne ferons pas

| Refus | Raison |
| --- | --- |
| Commandes fournisseurs | Gérées dans le logiciel d'achat existant ; on lui envoie seulement l'alerte |
| Valorisation comptable du stock | Hors du problème ; export possible plus tard |
| Lecture de codes-barres | Pas maintenant : on vérifie d'abord H-01 |

### Contraintes

- Délai : première version en 6 semaines.
- Compétences : un développeur Python.
- Matériel : deux tablettes au comptoir du magasin.

## 3. Acteurs

| Acteur | Type | Fréquence | Besoin principal |
| --- | --- | --- | --- |
| Magasinier | humain | toute la journée | enregistrer vite entrées et sorties |
| Responsable d'atelier | humain | chaque jour | voir les alertes, créer et archiver des pièces |
| Logiciel d'achat | système externe | à chaque alerte | recevoir les alertes de stock bas |
| Personne mal intentionnée | malveillant | rare | masquer un vol en modifiant l'historique |

### Matrice des droits

| Action | Magasinier | Responsable | Logiciel d'achat |
| --- | --- | --- | --- |
| Enregistrer une entrée ou une sortie | Oui | Oui | Non |
| Créer ou archiver une pièce | Non | Oui | Non |
| Modifier ou supprimer un mouvement | Non | Non | Non |
| Recevoir une alerte de stock bas | Non | Oui | Oui |

## 4. Processus

Actuel : demande orale → recherche de la pièce → note dans le cahier (parfois oubliée) → inventaire mensuel → découverte des écarts → commande urgente.

Futur : demande → sortie saisie sur la tablette → stock à jour immédiatement → alerte automatique sous le seuil → commande planifiée.

Ce qui reste humain : la décision de commander, et le comptage physique de l'inventaire.

## 4b. Exigences non fonctionnelles

| Famille | Seuil |
| --- | --- |
| Performance | Une sortie s'enregistre en moins de 2 s |
| Volume | 3 000 pièces, 50 000 mouvements par an |
| Disponibilité | Heures d'ouverture de l'atelier ; une heure d'arrêt est tolérable |
| Traçabilité | Aucun mouvement ne peut être modifié ni supprimé |
| Coût | Un petit serveur interne existant |
