# Étape E2 — Déploiement sûr

**Phase :** E · **Livrable :** section « Exploitation » de `docs/C-architecture.md` · **Durée indicative :** 1 à 2 jours (une fois par projet)

## Pourquoi

Un déploiement manuel et non répété est la source la plus fréquente de pannes. Et une panne sans retour arrière ni sauvegarde fiable peut détruire des mois de données.

## Liste de contrôle

- **Au moins deux environnements** : un de test, un de production. Le même procédé de déploiement pour les deux.
- **Déploiement automatisé**, déclenché par une action simple et tracée.
- **Migrations de la base de données** versionnées, appliquées automatiquement, et si possible réversibles.
- **Secrets** (mots de passe, clés, jetons) hors du code, dans la configuration de l'environnement ou un coffre à secrets.
- **Sauvegardes automatiques, et une restauration testée.** Une sauvegarde jamais restaurée n'est pas une sauvegarde.
- **Plan de retour arrière** : comment revenir à la version précédente, en combien de temps (cible : moins de 15 minutes).

Pour un logiciel embarqué : mise à jour à distance signée, avec retour automatique à la version précédente si la nouvelle ne démarre pas.

## Critère de sortie

Le déploiement est automatique, une restauration a réussi, et le retour arrière a été essayé une fois.
