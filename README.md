# Spotivizzz ![Build Passing](https://img.shields.io/badge/build-passing-brightgreen?style=plastic) ![License MIT](https://img.shields.io/badge/license-MIT-brightgreen?style=plastic) ![Version](https://img.shields.io/badge/version-v1.0-orange?style=plastic) ![Dependencies](https://img.shields.io/badge/Python-3.7+-yellow?style=plastic) ![release DAte](https://img.shields.io/badge/release_date-december_2022-red?style=plastic)
**A music data analysis tool using** [Spotify API](https://developer.spotify.com/documentation/web-api/) 
*by Clément ZELTER & Gabriel ROULEAU (ESIEE - E3FI - Groupe 3)*

## User Guide
### Installation
Aprés avoir cloné le projet, installez les dépendances nécéssaires au bon fonctionnement de Spotivizz avec la command suivante:
```bash
$ python -m pip install -r requirements.txt
```
### Démarrage
Vous pouvez ensuite vous deplacer à la racine du projet et lancer le dashboard avec la commande suivante:
```bash
$ python main.py
```
... et vous y connecter à l'adresse suivante sur votre navigateur:
```bash
http://127.0.0.1:8050/
```
### Utilisation
Vous trouverez dans le dashboard une multitude de graphs informants sur divers statistiques et données musicales:
- Un planisphère de la musique mondiale
- Des graphiques statiques annexes:
    - Un nuage de points correlant le volume d'un titre avec son caractère énergétique
    - Un nuage de points correlant le BPM moyen des titres des Top 50 nationaux du monde avec leur durée moyenne et la population du pays en question.
    - Un histogramme présentant la durée moyenne d'un titre en fonction de son genre musical parmis une large selection de genre.
- Un comparateur de genres

De manière générale, il est possible de double-cliquer sur la légende d'une donnée pour l'isoler. Un second double-clique permet de réinitialiser la vue. Il est également possible de masquer une ou plusieurs données en cliquant une seule fois sur leur légende. Un second clique sur la légende rétablit la donnée dans le graph.

## Rapport d'analyse
Nous avons utilisé les données fournit par Spotify pour mettre en évidence des corrélations et rechercher des différences entre les musiques de certains pays ou de certains genres.  
  
Nous avons principalement utilisé deux comparaisons pour notre travail : la comparaison de genres et la comparaison entre les pays.  
  
Comparer les genres nous as permis de mettre en évidence une différence quant à la durée des morceaux ainsi qu’une corrélation entre le volume d’un morceaux et son « niveau d’énergie ». Nous avons ainsi démontré qu’un morceau avec un volume supérieur a généralement un niveau d’énergie supérieur.  
  
Comparer les musiques les plus populaires de chaque pays nous a permis de montrer les différences de niveau de BPM (battement par minute, qui représente le tempo de d’un morceau) entre les pays du monde. On remarque alors que les pays d’Amérique du sud on généralement un tempo plus lent que les pays européens. La Roumanie présentant le niveau moyen de BPM le plus haut avec 135 battement par minute en moyenne. On remarque aussi, grâce au graphique de la carte, que les pays d’Asie du Sud-est présentent une durée moyenne bien supérieure que celle de l’europe de l’est. Dans certains de ces pays la durée moyenne d’un morceau du Top 50 est de 240 secondes. Là où la durée moyenne d’un morceau du Top 50 Ukrainien est environ de 170 secondes. C’est une différence considérable. Ces différences montrent un changement de culture (notamment musicale) entre ces régions du monde. Il est aussi intéressant de noter que les durées moyennes des morceaux en europe de l’ouest, en amérique du nord ou en australie sont très proche puisqu’il s’agit tout les trois de civilisations occidentales avec une culture parfois assez proche.

### Données utilisées
- Les données relatives aux Top 50 des pays sont récupérées à travers les playlists "Top 50 - [country_name]" générées automatiquement par [Spotify](https://spotify.com/). Example pour la France: [Top 50 - France](https://open.spotify.com/playlist/37i9dQZEVXbIPWwFssbupI?si=5892fcd440b440b3)
- Les données relatives aux genres sont récupérées à travers les playlists "The Sound of [genre_name]" générées algorithmiquement par [The Sound Of Everything](https://everynoise.com/). Example pour la Pop: [The Sound of Pop](https://open.spotify.com/playlist/6gS3HhOiI17QNojjPuPzqc?si=60735af77ea845af)
- Les données relatives à la démographie des pays du monde sont récupérées via le module Python [pypopulation](https://pypi.org/project/pypopulation/)

## Developper Guide
Le projet est structuré en plusieurs sous-dossiers qui ont chacun leurs fonctions propres.

### /
- A la racine se trouvent les fichiers utiles tels que la `LICENSE`, `requirements.txt` pour les dépendances ou le script d'entrée `main.py`.
- Pour lancer le dashboard, il vous suffit simplement d'exécuter `main.py` qui est le point d'entrée du programme.
- Le dossier `assets`, à la racine du projet contient tous les fichiers CSS et les images utiles à l'interface.
- Le dossier `src` contient l'intégralité du code python.

### src/
- Dans le dossier `src` se trouve le fichier app.py qui construit le layout de l'application.
- Le sous-dossier `pages` contient toutes les pages du projet.
- Le sous-dossier `utils` contient des fichiers utiles tels que le fichier `api.py` qui est en charge des appels à la database et de la manipulation des données.
- Le sous-dossier `components` contient les composants récurrents de l'application tels que les graphiques, les titres ou le footer.

### Dépendances
Liste des dépendances Python utilisées par le projet Spotivizzz :
- [dash](https://pypi.org/project/dash/)
- [plotly](https://pypi.org/project/plotly/)
- [pandas](https://pypi.org/project/pandas/)
- [pycountry-convert](https://pypi.org/project/pycountry-convert/)
- [azure-core](https://pypi.org/project/azure-core/)
- [azure-cosmos](https://pypi.org/project/azure-cosmos/)
- [certifi](https://pypi.org/project/certifi/)
- [idna](https://pypi.org/project/idna/)
- [chardet](https://pypi.org/project/chardet/)
- [requests](https://pypi.org/project/requests/)
- [six](https://pypi.org/project/six/)
- [urllib3](https://pypi.org/project/urllib3/)
- [pypopulation](https://pypi.org/project/pypopulation/)