# Spotivizzz ![Build Passing](https://img.shields.io/badge/build-passing-brightgreen?style=plastic) ![License MIT](https://img.shields.io/badge/license-MIT-brightgreen?style=plastic) ![Version](https://img.shields.io/badge/version-v1.0-orange?style=plastic) ![Dependencies](https://img.shields.io/badge/Python-3.7+-yellow?style=plastic) ![release DAte](https://img.shields.io/badge/release_date-december_2022-red?style=plastic)
<img src="https://github.com/gabriel-esiee/Spotivizzz/blob/master/assets/images/spotivizzz_banner.png"
     alt="Spotivizzz banner">
**A music data analysis tool using** [Spotify API](https://developer.spotify.com/documentation/web-api/)

*by Clément ZELTER & Gabriel ROULEAU (ESIEE - E3FI - Groupe 3)*

## User Guide
### Installation
Aprés avoir cloné le projet, installez les dépendances nécéssaires au bon fonctionnement de Spotivizzz avec la commande suivante:
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
    - Un histogramme présentant la popularité des genres en fonction des pays, de leur indice de popularité dans ces pays et de la population des pays.
- Un comparateur de plus d'une centaines de genres musicaux

De manière générale, il est possible de double-cliquer sur la légende d'une donnée pour l'isoler. Un second double-clique permet de réinitialiser la vue. Il est également possible de masquer une ou plusieurs données en cliquant une seule fois sur leur légende. Un second clique sur la légende rétablit la donnée dans le graph.

## Rapport d'analyse
Le but de ce projet est d'analyser en temps réel les tendances de l'industrie musicale à l'échelle du monde.
Nous avons pour cela utilisé les données fournies par Spotify afin de mettre en évidence des corrélations que nous jugeons intéressantes et révélatrices.

Nous avons divisé nos champs de recherches en deux principales catégories d'analyse:
- les tendances musicales en fonction des genres musicaux
- les tendances musicales en fonction des pays d'écoute

Voici une liste non exhaustive de points qui se dégagent de nos différentes analyses:
- Il y a une corrélation claire entre l'énergie d'un morceau et son volume. Plus le volume est élevé plus l'énergie l'est également, et inversement.
- L'Asie de l'Est est friante de musiques aux durées bien plus élevées que la moyenne mondiale, avoisinnant les 4min, là où la moyenne mondiale est plutôt aux alentours des 3min.
- Le BPM est souvent corrélé avec la durée des titres, mais uniquement en Asie.
- La Pop et l'Urbano Latino semble dominer le monde de l'industrie musicale mais lorsque l'on rapporte ces données à la population des pays concernés on se rend compte que le Modern Bollywood est en réalité le genre dominant malgré sa présence rarement observée en dehors de l'Inde.

### Données utilisées
- Les données relatives aux Top 50 des pays sont récupérées à travers les playlists "Top 50 - [country_name]" générées automatiquement par [Spotify](https://spotify.com/). Example pour la France: [Top 50 - France](https://open.spotify.com/playlist/37i9dQZEVXbIPWwFssbupI?si=5892fcd440b440b3)
- Les données relatives aux genres sont récupérées à travers les playlists "The Sound of [genre_name]" générées algorithmiquement par [The Sound Of Everything](https://everynoise.com/). Example pour la Pop: [The Sound of Pop](https://open.spotify.com/playlist/6gS3HhOiI17QNojjPuPzqc?si=60735af77ea845af)
- Les données relatives à la démographie des pays du monde sont récupérées via le module Python [pypopulation](https://pypi.org/project/pypopulation/)

## Developper Guide
Schéma de l'architecture du code de Spotivizzz:
[![](https://mermaid.ink/img/pako:eNqdVE1vozAQ_SuWe0mkJAo0AcNhpbRopZV2pdXm1iSKHNsUq2Aj22xLo_z3NYYGkl429QHNjOe9-cJzhERSBmOY5vKVZFgZ8PPPVgB7dHV4VrjMgC6l4Wm915yyzbpVwNoqu9bROXc-q98_Rmcfq-zGYDr91l6XdXdV1rtxC2WCtsJ1SKb-MtVFdLILCKZAVUJw8QykIAxgQHF9nUVZu5AUG7xPmSHZaJNYGXxv5I_Azek9egAWOK811x1m1amfYB9-DkmkLqTe08NmtHqvFAOPzgCSh_FuUOdVjSTnTJi2xkcnXzf1zOuiFJiL0ab5zvoGNqcxdRXopliuyxzXILHaQWJFL5rdJWHqnA2HBlKe5_GdlzxEy8VEGyVfWHxHCOnk6SunJov98u0Tge33DeAhfDCAlmE-T9OU_Hf4y0l8iaJv8Q3wIYFrfouNPHSgt2Svs1uQF43v30dHYdM-4xFCl3jvquj-z_sCergOboLDCSyYsg2jdt8cG9sWmowVbAtjK1KsXrZwK07WD1dGrmtBYGxUxSawKu2sWcKxfToFjFOca2stsYDxEb7B-H45C9HS9xCKfN_zgzCYwBrGizCcRQh5QeSj-cK_R8vTBL5LaSnmsygIIz-wZm_hBcHCd3xP7rINyig3Uv1q96Nbk6d_lQK31Q?type=png)](https://mermaid-js.github.io/mermaid-live-editor/edit#pako:eNqdVE1vozAQ_SuWe0mkJAo0AcNhpbRopZV2pdXm1iSKHNsUq2Aj22xLo_z3NYYGkl429QHNjOe9-cJzhERSBmOY5vKVZFgZ8PPPVgB7dHV4VrjMgC6l4Wm915yyzbpVwNoqu9bROXc-q98_Rmcfq-zGYDr91l6XdXdV1rtxC2WCtsJ1SKb-MtVFdLILCKZAVUJw8QykIAxgQHF9nUVZu5AUG7xPmSHZaJNYGXxv5I_Azek9egAWOK811x1m1amfYB9-DkmkLqTe08NmtHqvFAOPzgCSh_FuUOdVjSTnTJi2xkcnXzf1zOuiFJiL0ab5zvoGNqcxdRXopliuyxzXILHaQWJFL5rdJWHqnA2HBlKe5_GdlzxEy8VEGyVfWHxHCOnk6SunJov98u0Tge33DeAhfDCAlmE-T9OU_Hf4y0l8iaJv8Q3wIYFrfouNPHSgt2Svs1uQF43v30dHYdM-4xFCl3jvquj-z_sCergOboLDCSyYsg2jdt8cG9sWmowVbAtjK1KsXrZwK07WD1dGrmtBYGxUxSawKu2sWcKxfToFjFOca2stsYDxEb7B-H45C9HS9xCKfN_zgzCYwBrGizCcRQh5QeSj-cK_R8vTBL5LaSnmsygIIz-wZm_hBcHCd3xP7rINyig3Uv1q96Nbk6d_lQK31Q)
La majeure partie du traitement des données recueillies depuis l'API de Spotify (en passant par le wrapper python Spotipy) est faite sur un serveur, une fois par jour, puis elles sont envoyées, traitées et nettoyées, sur une database NoSQL (Azure Cosmos DB). L'app python Spotivizzz récupère ensuite les données stockées sur la database Azure Cosmos pour les mettre en images via les modules plotly et dash.

Le projet est structuré en plusieurs sous-dossiers qui ont chacun leurs fonctions propres:

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
- [statsmodel](https://pypi.org/project/statsmodels/)
