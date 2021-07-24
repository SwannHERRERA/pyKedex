# pyKedex

pour lancé l'application utilisé la commande :

`python src/main.py`

Et puis laissé vous guider par les informations de commande

## fonctionnalité de base d'un pokedex

 - recherche de pokemon
 - recherche de type
 - recherche d'attaque
 - recherche de lieu
 - recherche d'objet
  
## Conversion image to ascii

Avec le pyKedex quand on lance une recherche de pokemon l'image du pokemon nous est montré dans l'éditeur de texte par défaut de la machine hôte. Pour ce faire nous transformons l'image récupérée sur l'API en ASCII art.
Cela ce fait en 3 temps, d'abord on retaille l'image, ensuite on transforme chaque pixel en une nuance de gris et pour finir on remplace le pixel gris par un caractère plus ou moins remplis en fonction de son obsurité.

## Historisation et journalisation des recherches

Avec le pyKedex il est possible d'avoir des erreurs de faire une mauvaise recherche, de ne pas avoir les droits sur un fichier ...

Pour cela nous avons mis en place un système d'historique. Chacune de vos actions concernant le pokedex est enregistrée, nous enregistrons aussi les erreurs.

Pour finir il est possible d'afficher son historique, soit l'historique récent, soit tout l'historique. On peut également afficher les erreurs.

## Commande

### action de l'historique
- get-actions (No param) liste les 10 dernières actions du journal
- get-all-action (No param) liste toutes les actions
- get-errors (No param) listes toutes les erreurs
### action liée au pokedex
- get-item (name or id)
- get-location (name or id)
- get-move (name or id)
- get-pokemon-by-id (id)
- get-pokemon-by-name (name)
- get-type (name or id)
- list-pokemons (No param)
- list-types (No param)