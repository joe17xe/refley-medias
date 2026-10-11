# Logos partenaires

**Le dépôt de référence pour les agents.** Le maître des logos est le Kit de
communication de la plateforme Solid'Pilot (bucket `communication`), mais ce
bucket est **privé** et son domaine est refusé par la politique réseau des
environnements d'exécution : aucun agent ne peut l'atteindre. Ce dossier est
la copie de travail, lisible par n'importe quel outil à une URL directe.

Nommage : le nom court du partenaire, en minuscules, sans accent. Tous les
fichiers sont détourés au plus près du dessin, sans marge, en PNG.

| Fichier | Partenaire | Fond | Provenance |
| --- | --- | --- | --- |
| `meae.png` | ministère de l'Europe et des Affaires étrangères | transparent | Fourni par le président, 10/2026. |
| `departement-yvelines.png` | Département des Yvelines | blanc | Fourni par le président, 10/2026. |
| `ycid.png` | YCID | transparent | Fourni par le président, 10/2026. Remplace une version détourée d'une capture d'écran. |
| `villepreux.png` | commune de Villepreux | blanc | Fourni par le président, 10/2026. |
| `azour.png` | Municipalité d'Azour | blanc | Fourni par le président, 10/2026. |
| `jouy-en-josas.png` | Ville de Jouy-en-Josas | blanc | Fourni par le président, 10/2026. Second volet du programme CEM (Jouy-en-Josas — Jeïta). |
| `jumelage.png` | Comité de Jumelage de Jouy-en-Josas | blanc | Fourni par le président, 10/2026. |
| `refley.png` | REFLEY | blanc | Détouré de `public/images/logo-refley.jpg` du dépôt REFLEYFR. |

Plusieurs fichiers ont un **fond blanc opaque**, pas de la transparence : les
poser sur un cartouche crème fait apparaître leur rectangle. Sur fond clair,
utiliser du **blanc pur**.

## Règles d'usage

1. **Sur fond sombre, pastille ou cartouche clair.** Deux raisons, et
   `pourquoi-une-pastille.png` les montre côte à côte. D'abord, **six de ces
   huit fichiers n'ont aucune transparence** : ils portent un rectangle blanc
   cuit dans l'image. Retirer la pastille ne donne pas un logo détouré, ça
   donne une boîte blanche à angles vifs, en plus laide. Ensuite, le seul
   vraiment transparent — YCID — a son texte en noir : posé sur le vert
   sombre, son anneau devient illisible.
   **La vraie solution, le jour où on l'aura** : demander aux partenaires
   leur version monochrome blanche, que la plupart des chartes fournissent,
   à commencer par celle de l'État. Alors seulement le fond peut disparaître.
2. **On ne recolore pas, on n'inverse pas, on ne déforme pas** le logo d'un
   partenaire. S'il ne tient pas, on lui donne un fond.
3. **Ordre d'affichage** : celui de l'en-tête de la fiche projet dans
   `docs/communication/projets/` du dépôt REFLEYFR, les partenaires hors
   fiche venant ensuite.
4. **Normaliser à l'œil, pas à la règle.** Caler huit logos sur une même
   hauteur écrase les logos larges et noie les logos hauts. Chaque logo a sa
   hauteur propre : `departement-yvelines` est trois fois plus large que haut,
   `jumelage` et `jouy-en-josas` sont à l'inverse des portraits.
5. **Le logo du ministère est un bloc-marque d'État** : taille minimale, zone
   de protection, pas de déformation. Dans un bandeau à huit logos sur une
   vidéo verticale, il arrive à la limite de lisibilité de sa devise — si un
   support doit le porter en grand, lui donner une ligne à lui.
6. **Un bandeau partenaires incomplet ne se publie pas** quand il manque un
   financeur. Mieux vaut citer les partenaires en toutes lettres.
