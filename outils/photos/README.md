# Récupérer des photos publiques

La session de Claude qui monte les vidéos n'atteint pas les sites des
organisateurs. Cette action GitHub le fait pour elle.

1. Sur une branche `photos/<quelque-chose>`, poser un fichier
   `photos-a-recuperer.json` dans le dossier de l'édition, par exemple
   `shou-fi-ma-fi/2026-11-09/photos-a-recuperer.json` :

   ```json
   {"edition": "2026-11-09", "photos": [
     {"cle": "rim-murr-theatre-tour-eiffel-2026-11-12",
      "credit": "Visuel : Agenda culturel",
      "urls": ["https://…grande.jpg", "https://…petite.jpg"]}
   ]}
   ```

   `cle` est la clé du rendez-vous dans l'agenda de refley.fr. Plusieurs
   adresses sont permises : la plus grande image obtenue est gardée.
2. Pousser. L'action « Photos à récupérer » télécharge, réduit à 1 600 px de
   large, ré-encode en JPEG (sans métadonnées) et remet sur la même branche
   `photos/<cle>.jpg` et `photos/rapport.json` (source, taille, crédit, échecs).
3. Rien n'arrive sur `main` sans PR.

Seulement des images publiées par les organisateurs ou par REFLEY, avec leur
crédit.
