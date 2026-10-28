# D-01 — La coupure de sécurité ne dépend pas que du logiciel

- **Statut :** acceptée (2026-05-06)
- **Contexte :** R-01 protège la récolte et l'installation. Un logiciel peut se bloquer, et un relais peut rester collé.
- **Options envisagées :**
  1. Coupure assurée uniquement par le micrologiciel.
  2. Micrologiciel + chien de garde matériel qui coupe le relais si le programme cesse de répondre.
  3. Option 2 + thermostat de sécurité câblé, indépendant, qui coupe l'alimentation du chauffage à 32 °C.
- **Décision :** option 3. Trois barrières indépendantes : le logiciel coupe à 30 °C, le chien de garde coupe si le logiciel se bloque, le thermostat câblé coupe à 32 °C même si tout le reste échoue.
- **Conséquences acceptées :** un composant de plus par serre ; un test mensuel du thermostat câblé à prévoir dans la procédure d'exploitation.
