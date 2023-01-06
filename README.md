# ls_litreview
9ème projet du parcours DA - Python d'OpenClassrooms.




## Clonage du dépôt

Pour commancer, il vous faut cloner le dépôt du projet. Nous partons du principe que le programme git est installé sur votre ordinateur :

1- Ouvrez un invite de commande si vous êtes sous Windows, ou un terminal si vous êtes sous Linux ou MacOSX

2- Rendez-vous dans le dossier dans lequel vous souhaitez cloner le dépôt

3- Saisissez la commande `git clone https://github.com/ludosansone/ls_litreview.git`

4- Le dépôt est pret, vous pouvez y accéder en tapant `cd ls_litreview`




## Installation de l'environnement virtuel

Afin de garentir le bon fonctionnement de cette application web, vous devez l'exécuter dans le même environnement virtuel que le développeur. Pour se faire, suivez les instructions d'installation ci-dessous.
Attention, nous partons du principe que les paquets pip et venv sont bien installés sur votre ordinateur. Si tel n'est pas le cas, veuillez vous référer à leur documentation respective pour procéder à leur installation.


### Installation sous Windows

1- Ouvrez l'invite de commandes

2- Déplacez-vous à la racine du dossier ls_litreview, à l'aide de la commande cd

3- Pour créer l'environnement virtuel, saisissez la commande : `python -m venv env`

4- Pour démarrer ce dernier, saisissez la commande : `env\Scripts\activate`

5- Pour y installer les paquets nécessaires à la bonne exécution du projet, saisissez la commande : `pip install -r requirements.txt`


### Installation sous Linux ou MacOSX

1- Ouvrez un terminal

2- Déplacez-vous à la racine du dossier ls_litreview, à l'aide de la commande cd

3- Pour créer l'environnement virtuel, saisissez la commande : `python -m venv env`

4- Pour démarrer ce dernier, saisissez la commande : `source env/bin/activate`

5- Pour y installer les paquets nécessaires à la bonne exécution du projet, saisissez la commande : `pip install -r requirements.txt`



## Utilisation de Flake8

Afin de vérifier que le code du programme répond bien à la norme PEP-8, vous pouvez utiliser la commande Flake8.

Pour que Flake8 affiche son rapport directement dans la console : 

1- Déplacez-vous à la racine du projet, dans le dossier ls_litreview/litreview, à l'aide de la commande cd

2- puis saisissez la commande `flake8`




## Lancement de l'application

Attention, avant de lancer l'application, assurez-vous que l'environnement virtuel est activé.

1- Ouvrez l'invite de commandes

2- Déplacez-vous à la racine du projet, dans le dossier ls_litreview/litreview, à l'aide de la commande cd

3- Saisissez la commande `python manage.py runserver`

4- Le serveur de développement se lance, et nous invite à nous rendre à l'adresse http://127.0.0.1:8000/

5- Ouvrez votre navigateur, et rendez-vous à l'adresse indiquée

6- L'application est prête
