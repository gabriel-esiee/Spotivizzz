# Spotivizzz

Clément ZELTER et Gabriel ROULEAU

E3FI - Groupe 3

## User Guide

Aprés avoir cloné le projet, comencez par installer les dépendances nécéssaires a son bon fonctionnement
avec la command suivante :

```bash
$ python -m pip install -r requirements.txt
```

Vous pourrez ensuite lancer le dashboard avec la commande :

```bash
$ python main.py
```

## Rapport d'analyse

Mettre en avant ici les principales conclusions extraites des données.

## Developper Guide

Le projet est structuré en plusieurs sous-dossiers qui ont chacuns leurs fonctions propre.

### /

Vous trouverez a la racine du projet tout un tas de fichiers utiles tel que la LICENSE, requirements.txt pour les dépendances ou le script d'entrée main.py.

Pour lancer le dashboard, il vous suffit simplement d'éxécuter main.py qui est le point d'entrée du programme.

Le dossier assets, à la racine du projet contient tout les fichiers CSS et les images utiles a notre interface.

Le dossier src, lui contient tout le code python.

### src/

Vous trouverez dans le dossier src le fichier app.py qui contruit le layout de l'application.

Le sous-dossier pages contient toutes les pages du projet. Actuellement, il n'y que la page d'accueil.

Le sous-dossier utils contient des fichiers utiles tel que le fichier api.py qui est en charge des appels a l'API spotify et de la manipulation des données.

Le sous dossier components contient lui les composants récurrent de l'application tel les graphiques, les titres ou le footer.