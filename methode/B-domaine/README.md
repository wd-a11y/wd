# Phase B — Le domaine

**Objectif :** un modèle du métier assez précis pour qu'un développeur qui ne connaît pas le métier puisse coder sans deviner.
**Livrables :** `docs/B-glossaire.md`, `docs/B-modele.md`, `docs/B-regles.md`, `docs/B-scenarios.feature`, `docs/B-menaces.md`.

| Étape | Résultat |
| --- | --- |
| [5. Lister les objets et fixer le vocabulaire](05-objets-glossaire.md) | Inventaire, classement, glossaire, entités et objets-valeurs |
| [6. Interroger chaque objet](06-questions-objet.md) | Le rôle réel de chaque objet |
| [7. Séparer données, comportements et règles](07-donnees-comportements-regles.md) | Chaque donnée typée : unité, format, plage |
| [8. Obligatoire, facultatif, calculé](08-obligatoire-facultatif-calcule.md) | Source de vérité, valeurs par défaut, historique |
| [9. Relations](09-relations.md) | Cardinalités, propriété, frontières de cohérence |
| [9b. Cycle de vie](09b-machine-a-etats.md) | Une machine à états par objet à statut |
| [10. Événements métier](10-evenements.md) | Commandes, événements, réactions |
| [11. Règles métier](11-regles.md) | Règles `R-xx` identifiées, typées, avec exemple et contre-exemple |
| [12. Scénarios](12-scenarios.md) | Scénarios `S-xx` au format Soit / Quand / Alors |
| [13. Cas limites](13-cas-limites.md) | Grille systématique passée sur chaque scénario |
| [13b. Menaces et abus](13b-menaces.md) | Menaces `M-xx` devenues règles et tests |

## Porte B

- [ ] Le glossaire n'a ni synonyme ni terme flou ; le code utilisera ces mots.
- [ ] Chaque objet est classé : entité ou objet-valeur.
- [ ] Chaque objet à statut a sa machine à états.
- [ ] Chaque règle a un identifiant, un type, un exemple et un contre-exemple chiffrés.
- [ ] Chaque fonctionnalité indispensable a au moins un scénario normal et un scénario d'erreur.
- [ ] La grille des cas limites est passée sur chaque scénario.
- [ ] Les menaces retenues sont devenues des règles.
- [ ] Une personne du métier a relu règles et scénarios.
