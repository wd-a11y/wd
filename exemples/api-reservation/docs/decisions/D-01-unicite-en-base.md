# D-01 — L'unicité des places actives est garantie par la base de données

- **Statut :** acceptée (2026-04-02)
- **Contexte :** R-01 doit tenir même quand 50 requêtes visent la même place dans la même milliseconde (S-04), sur plusieurs serveurs d'API en parallèle.
- **Options envisagées :**
  1. Vérifier dans le code (« la place est-elle libre ? ») puis écrire.
  2. Verrou applicatif partagé entre serveurs.
  3. Index unique partiel en base sur (séance, place) pour les réservations actives ; l'écriture concurrente perdante échoue.
- **Décision :** option 3. L'option 1 laisse passer deux requêtes entre la lecture et l'écriture ; l'option 2 ajoute un composant à faire tourner et à surveiller. La base garantit l'unicité quel que soit le nombre de serveurs.
- **Conséquences acceptées :** l'échec d'unicité de la base est traduit en « Place indisponible » par le dépôt ; la tâche d'expiration doit changer le statut avant de libérer, pour que l'index reflète la réalité.
