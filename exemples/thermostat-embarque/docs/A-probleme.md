# Problème — Régulation du chauffage des serres

Niveau du projet : **L** — une erreur peut détruire une récolte entière ou provoquer une surchauffe de l'installation.

## 1. Problème

> Pour les exploitants de serres maraîchères, qui règlent le chauffage à la main avec un thermostat mécanique, le problème est la surchauffe ou le gel la nuit, quand personne n'est là. Aujourd'hui ils passent vérifier vers minuit, ce qui coûte du sommeil et, 2 à 3 fois par saison, une partie de la récolte.

### Mesures de réussite

| Id | Mesure | Valeur actuelle | Cible | Comment on la mesure |
| --- | --- | --- | --- | --- |
| B-01 | Dépassements de 30 °C non traités | 2 à 3 par saison | 0 | journal du régulateur |
| B-02 | Temps passé dans ±0,5 °C autour de la consigne | environ 60 % | 90 % | journal du régulateur |

## 2. Périmètre

| Id | Fonctionnalité | Besoin | Rang |
| --- | --- | --- | --- |
| F-01 | Couper le chauffage en cas de surchauffe ou de panne de capteur | B-01 | Indispensable |
| F-02 | Réguler autour d'une consigne | B-02 | Indispensable |
| F-03 | Changer la consigne depuis le téléphone | B-02 | Important |
| F-04 | Mettre à jour le micrologiciel à distance | B-01 | Important |

Ce que nous ne ferons pas : l'arrosage, l'aération automatique, les prévisions météo.

## 3. Acteurs

| Acteur | Type | Besoin principal |
| --- | --- | --- |
| Exploitant | humain, sur place ou via l'application | fixer la consigne, être alerté |
| Capteur de température | système externe matériel | fournir une mesure toutes les secondes ; peut tomber en panne |
| Relais du chauffage | système externe matériel | allumer ou couper le chauffage |
| Application de l'exploitant | système externe | envoyer des commandes signées |
| Personne malveillante à proximité | malveillant | envoyer de fausses commandes par radio |

## 4b. Exigences non fonctionnelles

| Famille | Seuil |
| --- | --- |
| Temps réel | Chauffage coupé moins de 2 s après une mesure au-dessus de 30 °C |
| Disponibilité | La régulation et la sécurité fonctionnent sans réseau |
| Ressources | 64 Ko de mémoire vive, 512 Ko de mémoire de programme |
| Énergie | Fonctionne sur batterie de secours 12 h en cas de coupure secteur |
| Sécurité | Commandes à distance signées ; micrologiciel signé |
| Traçabilité | 30 jours de journal en mémoire locale |
