# Étape 13b — Menaces et abus

**Phase :** B · **Livrable :** `docs/B-menaces.md` · **Durée indicative :** une demi-journée (niveau M), plus une revue externe (niveau L)

## Pourquoi

Les cas limites supposent un utilisateur de bonne foi. Les menaces supposent l'inverse : quelqu'un qui cherche à tricher, voler ou casser. Une faille de sécurité découverte après la mise en production coûte bien plus cher qu'une règle écrite maintenant.

## La grille STRIDE, simplifiée

Pour chaque donnée sensible et chaque action importante, six questions :

| Lettre | Menace | Question | Parade typique |
| --- | --- | --- | --- |
| S | Usurpation | Peut-on se faire passer pour quelqu'un d'autre ? | Authentification forte |
| T | Altération | Peut-on modifier une donnée sans en avoir le droit ? | Autorisation à chaque action, signature |
| R | Répudiation | Peut-on nier avoir fait une action ? | Journal d'audit non modifiable |
| I | Divulgation | Peut-on lire ce qu'on ne devrait pas ? | Contrôle d'accès, chiffrement |
| D | Déni de service | Peut-on bloquer le service ? | Limites de débit, quotas |
| E | Élévation de privilège | Peut-on obtenir plus de droits ? | Moindre privilège, vérification côté serveur |

## Livrable

Pour chaque menace retenue :

- un identifiant `M-xx`, la donnée ou l'action visée, l'acteur malveillant (étape 3) ;
- la probabilité et la gravité (faible, moyenne, forte) ;
- **la parade, qui devient une règle `R-xx` et donc un test.**

## Exemple

> **M-02** — *Divulgation.* Un utilisateur connecté change l'identifiant dans l'adresse `/dossiers/1042` en `/dossiers/1043` et lit le dossier d'un autre. *Gravité :* forte. *Parade :* **R-12** — chaque lecture de dossier vérifie que l'utilisateur y est affecté ; sinon réponse « introuvable », sans révéler que le dossier existe.

## Pièges

- Vérifier les droits seulement dans l'interface : un attaquant appelle l'API directement.
- Des messages d'erreur trop bavards (« mot de passe incorrect pour cet utilisateur » révèle que l'utilisateur existe).
- Des secrets (mots de passe, clés) écrits dans le code.

## Critère de sortie

Chaque donnée sensible et chaque action importante est passée dans la grille, et chaque menace retenue a une règle `R-xx`.
