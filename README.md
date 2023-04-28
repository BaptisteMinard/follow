# Follow

Découpé en 3 partie

## app

Partie applicative, renvoie la page HTML avec les données à afficher sur la map pour suivre le trajet. 

## folium

Instance du folium

## telegrambot

Traitement des commandes envoyées au bot pour actualiser les données. 

Les commandes dispo sont : 
- **/refreshmap** pour forcer le refresh de map.html
- **/editcomment** pour obtenir la liste des 10 dernières localisation et editer le commentaire de celui sélectionné

- Créer un bot telegram et récupérer sa clé API qui est à configurer dans le fichier [telegrambot/.env](telegrambot/.env)