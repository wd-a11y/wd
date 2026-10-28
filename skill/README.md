# Skill pour agent IA

Le dossier `methode-wd/` contient une skill au format `SKILL.md` (utilisé notamment par Claude Code). Elle fait conduire la méthode par l'agent : questions, livrables, vérification des portes, refus de coder avant la porte C.

## Installation (Claude Code)

Copiez le dossier dans vos skills personnelles ou dans celles du projet :

```bash
# pour tous vos projets
cp -r skill/methode-wd ~/.claude/skills/methode-wd

# ou pour un seul projet
cp -r skill/methode-wd mon-projet/.claude/skills/methode-wd
```

Puis demandez simplement : « Je démarre un nouveau projet, applique la méthode WD. »

## Autres agents

Le contenu de `SKILL.md` est un texte d'instructions ordinaire. Il peut servir de consigne système ou de fichier d'instructions pour d'autres assistants de code.
