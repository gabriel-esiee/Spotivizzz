# Spotivizzz

Clément ZELTER et Gabriel ROULEAU

E3FI - Groupe 3

## User Guide

Aprés avoir cloné le projet, comencez par installer les dépendances nécéssaires a son bon fonctionnement avec la command suivante :

```bash
$ python -m pip install -r requirements.txt
```

Vous pourrez ensuite lancer le dashboard avec la commande :

```bash
$ python main.py
```

... et vous y connecter à l'adresse suivante sur votre navigateur :

http://127.0.0.1:8050/

## Rapport d'analyse

Mettre en avant ici les principales conclusions extraites des données.

## Developper Guide

Le projet est structuré en plusieurs sous-dossiers qui ont chacun leurs fonctions propres.

### /

Vous trouverez à la racine du projet tout un tas de fichiers utiles tels que la LICENSE, requirements.txt pour les dépendances ou le script d'entrée main.py.

Pour lancer le dashboard, il vous suffit simplement d'exécuter main.py qui est le point d'entrée du programme.

Le dossier assets, à la racine du projet contient tous les fichiers CSS et les images utiles a notre interface.

Le dossier src, lui contient tout le code python.

### src/

Vous trouverez dans le dossier src le fichier app.py qui construit le layout de l'application.

Le sous-dossier pages contient toutes les pages du projet. Actuellement, il n'y a que la page d'accueil.

Le sous-dossier utils contient des fichiers utiles tels que le fichier api.py qui est en charge des appels à l'API spotify et de la manipulation des données.

Le sous-dossier components contient lui les composants récurrents de l'application tels que les graphiques, les titres ou le footer.

### Dépendences

Les dépendences python suivantes sont utilisées pour ce projet :
- dash (https://pypi.org/project/dash/)
- plotly (https://pypi.org/project/plotly/)
- pandas (https://pypi.org/project/pandas/)
- pycountry-convert (https://pypi.org/project/pycountry-convert/)