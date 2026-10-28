# Les principes de la méthode WD

La méthode WD guide un projet logiciel du problème réel jusqu'au logiciel en production. Elle tient en une phrase : **commencer juste plutôt que commencer vite, et pouvoir prouver à tout moment que c'est toujours juste.**

## Les cinq phases

| Phase | Question | Étapes | Porte de sortie |
| --- | --- | --- | --- |
| [A. Problème](A-probleme/README.md) | Pourquoi ce logiciel, pour qui, et comment saura-t-on qu'il réussit ? | 1 à 4b | Problème confirmé et mesuré |
| [B. Domaine](B-domaine/README.md) | Que manipule le métier, quelles règles, quels cas difficiles ? | 5 à 13b | Règles et scénarios relus par le métier |
| [C. Conception](C-conception/README.md) | Comment découper le logiciel, et la techno tient-elle ? | 14 à 17 | Le squelette marchant tourne |
| [D. Construction](D-construction/README.md) | Comment traduire le modèle en code prouvé par des tests ? | 18 à 20 | Chaque règle touchée a son test |
| [E. Livraison](E-livraison/README.md) | Comment livrer, survivre aux pannes, apprendre du réel ? | E1 à E4, 21 | Restauration testée, mesures visibles |

## Les sept principes

### 1. Une étape = un livrable

Une réflexion qui n'est pas écrite n'existe pas : elle s'oublie, se déforme, ne se transmet pas. Chaque étape produit un fichier court, rangé dans `docs/` (voir le [gabarit](../gabarit/docs/)).

### 2. Une phase = une porte

À la fin de chaque phase, une liste de contrôle. On avance seulement si tout est coché. Sinon on revient en arrière : c'est le rôle de la porte, pas un échec.

### 3. Tout est identifié et relié

| Préfixe | Désigne |
| --- | --- |
| `B-` | Besoin ou mesure de réussite |
| `F-` | Fonctionnalité |
| `H-` | Hypothèse |
| `R-` | Règle métier |
| `S-` | Scénario |
| `T-` | Test |
| `D-` | Décision d'architecture |
| `M-` | Menace |

Un identifiant est défini une seule fois, puis cité partout : une règle cite son besoin, un scénario cite ses règles, un test cite ce qu'il prouve, un commit cite ce qu'il change. On peut ainsi répondre à tout moment à deux questions : « pourquoi ce code existe-t-il ? » et « qu'est-ce qui prouve que cette règle est respectée ? ».

### 4. Les hypothèses sont visibles

Tout ce qu'on suppose sans l'avoir vérifié devient une hypothèse `H-xx`, avec la façon de la vérifier et une date limite. Une hypothèse finit toujours confirmée ou abandonnée, jamais oubliée.

### 5. Le risque décide de l'ordre

On traite d'abord ce qui peut faire échouer tout le projet : un problème que personne n'a, une techno incertaine, une contrainte légale, une performance difficile. Ce qui est agréable ou facile vient ensuite.

### 6. Itérer en petites boucles

Les phases A à E se parcourent d'abord pour une tranche fine du produit, puis à nouveau pour chaque fonctionnalité. Les documents sont vivants : un glossaire ou un modèle qui ne correspond plus au code est un bug.

### 7. Proportionner l'effort

La méthode complète sur un script de 200 lignes la tuerait. Chaque projet choisit un [niveau S, M ou L](niveaux-S-M-L.md), et chaque étape a une durée maximale. Une question qui déborde devient une hypothèse, et on avance.

## Comment lire chaque étape

Chaque page d'étape suit le même plan :

- **Pourquoi** : le problème que l'étape évite ;
- **Questions à poser** ;
- **Livrable** : ce qu'on écrit, et où ;
- **Exemples** : tirés de projets variés ;
- **Pièges** ;
- **Critère de sortie** : comment savoir que l'étape est finie.
