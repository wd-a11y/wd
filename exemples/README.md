# Exemples

Trois projets volontairement très différents, pour montrer que la méthode ne dépend ni du domaine ni de la technologie.

| Exemple | Type de logiciel | Niveau | Phases couvertes | Ce qu'il illustre surtout |
| --- | --- | --- | --- | --- |
| [gestion-stock](gestion-stock/) | Logiciel de gestion | M | A à D, code et tests | Invariants, concurrence, idempotence, traçabilité vérifiée par `wd-check` |
| [api-reservation](api-reservation/) | Service web (API) | M | A à C | Machine à états, double réservation sous charge, menaces sur une API publique |
| [thermostat-embarque](thermostat-embarque/) | Logiciel embarqué critique | L | A à C | Exigences temps réel, sécurité physique, pannes matérielles |

Les deux derniers s'arrêtent à la porte C : `wd-check` y signale donc des règles sans test. C'est attendu, et c'est exactement ce que la phase D doit combler.

Les données de ces exemples sont fictives.
