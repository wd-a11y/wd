# Les pièges à éviter

| Piège | Symptôme | Antidote | Étape |
| --- | --- | --- | --- |
| Paralysie d'analyse | Trois semaines de documents, zéro ligne qui tourne | Durée maximale par étape, squelette marchant | 16b |
| Solution avant problème | « On va faire une appli » avant de savoir pour qui et pourquoi | Énoncé du problème et preuve | 1 |
| Périmètre qui gonfle | Chaque réunion ajoute une fonctionnalité | Liste « ce que nous ne ferons pas » | 2 |
| Mots flous | « Compte » veut dire deux choses selon la personne | Glossaire sans synonymes | 5 |
| Modèle anémique | Les objets n'ont que des données ; toutes les règles sont dans des « services » | Invariants dans l'objet lui-même | 18 |
| Objet-dieu | Une classe de 2 000 lignes qui fait tout | Une phrase de responsabilité par module | 14 |
| Statuts incohérents | Un objet passe de « annulé » à « livré » | Machine à états, transitions explicites | 9b |
| Règles cachées dans l'écran | Un appel direct à l'API contourne la règle | Règles dans le domaine ; l'écran ne fait que prévenir | 11, 18 |
| Donnée calculée sans source de vérité | Un total affiché ne correspond pas aux lignes | Décider qui fait foi | 8 |
| Nombres à virgule pour l'argent | 0,1 + 0,2 ≠ 0,3 | Entiers en plus petite unité ou décimaux exacts | 7 |
| Dates sans fuseau horaire | Un rendez-vous décalé d'une heure au changement d'heure | Stocker en temps universel, afficher en local | 7, 13 |
| Suppression physique de données référencées | Historique cassé, rapports faux | Archivage ou suppression logique | 9 |
| Double envoi | Un double clic crée deux commandes | Idempotence | 13 |
| Tests écrits après coup | Ils confirment le code, bugs compris | Tests tirés des scénarios | 19 |
| Techno choisie par envie | Personne ne sait la maintenir | Décision `D-xx` avec critères | 16 |
| Sauvegarde jamais restaurée | Découverte le jour de la panne qu'elle est vide | Restauration testée | E2 |
| Documents morts | Le glossaire dit l'inverse du code | Mise à jour dans la définition du « fini » | 20 |
