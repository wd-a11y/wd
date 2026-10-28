# Étape E1 — Qualité automatique

**Phase :** E · **Livrable :** configuration d'intégration continue · **Durée indicative :** une demi-journée (une fois par projet)

## Pourquoi

Une vérification qui dépend de la mémoire humaine finit par être oubliée. L'intégration continue la rend automatique et systématique.

## Ce qu'on met en place

- **Tout le code est versionné** (git), documents compris.
- **À chaque modification proposée**, un service d'intégration continue (GitHub Actions, GitLab CI…) lance :
  1. la vérification du style et du formatage ;
  2. la vérification des types, si le langage le permet ;
  3. tous les tests ;
  4. `wd-check` sur le projet.
- **Rien n'est fusionné si un de ces contrôles échoue.**
- Les messages de commit citent les identifiants concernés : `R-04 : refuser les sorties supérieures au stock`.

Exemple de configuration : [.github/workflows/verification.yml](../../.github/workflows/verification.yml) dans ce dépôt.

## Critère de sortie

Une modification qui casse un test ne peut pas être fusionnée.
