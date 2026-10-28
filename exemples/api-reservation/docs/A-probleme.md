# Problème — Réservation de places de spectacle

Niveau du projet : **M** — argent en jeu et forte charge ponctuelle, mais paiement délégué à un prestataire spécialisé.

## 1. Problème

> Pour un réseau de 12 salles de spectacle, qui vendent leurs places via leur site et 5 revendeurs partenaires synchronisés par fichiers toutes les heures, le problème est la vente de la même place deux fois. Aujourd'hui ils remboursent et s'excusent, ce qui coûte environ 40 doubles ventes par mois et des clients furieux à l'entrée.

### Mesures de réussite

| Id | Mesure | Valeur actuelle | Cible | Comment on la mesure |
| --- | --- | --- | --- | --- |
| B-01 | Places vendues deux fois | 40 par mois | 0 | rapprochement des billets scannés |
| B-02 | Temps de réponse à l'ouverture d'une billetterie | non mesuré, site saturé | 95 % des réponses en moins de 300 ms à 2 000 requêtes par seconde | mesure côté serveur |

## 2. Périmètre

| Id | Fonctionnalité | Besoin | Rang |
| --- | --- | --- | --- |
| F-01 | Retenir puis confirmer des places | B-01 | Indispensable |
| F-02 | Annuler une réservation | B-01 | Important |
| F-03 | Accès des revendeurs partenaires par API | B-01, B-02 | Indispensable |
| F-04 | Contrôle des billets à l'entrée | B-01 | Important |

Ce que nous ne ferons pas : le paiement lui-même (délégué à un prestataire), le placement libre (seulement des places numérotées), la revente entre particuliers.

## 3. Acteurs

| Acteur | Type | Besoin principal |
| --- | --- | --- |
| Spectateur | humain, via le site | réserver vite, ses places à lui |
| Revendeur partenaire | système externe | réserver pour ses clients, par API |
| Prestataire de paiement | système externe | confirmer ou refuser un paiement ; peut être lent ou en panne |
| Contrôleur à l'entrée | humain | valider un billet en moins d'une seconde |
| Revendeur abusif | malveillant | accaparer des places pour les revendre plus cher |

### Matrice des droits

| Action | Spectateur | Revendeur | Contrôleur | Prestataire de paiement |
| --- | --- | --- | --- | --- |
| Retenir des places | Oui, 8 au plus par séance | Oui, dans son quota | Non | Non |
| Lire une réservation | Les siennes | Celles de ses clients | Par billet scanné | Non |
| Confirmer un paiement | Non | Non | Non | Oui |
| Marquer un billet utilisé | Non | Non | Oui | Non |

## 4b. Exigences non fonctionnelles

| Famille | Seuil |
| --- | --- |
| Performance | 95 % des réponses en moins de 300 ms à 2 000 requêtes par seconde |
| Disponibilité | 99,5 % par mois ; 99,9 % pendant les ouvertures de billetterie annoncées |
| Sécurité | Authentification par clé pour les partenaires, jetons pour les spectateurs |
| Données personnelles | Nom et courriel seulement ; effacés 1 an après la séance |
