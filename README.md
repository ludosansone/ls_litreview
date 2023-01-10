# ls_litreview
9ème projet du parcours DA - Python d'OpenClassrooms.




## Clonage du dépôt

Pour commancer, il vous faut cloner le dépôt du projet. Nous partons du principe que le programme git est installé sur votre ordinateur :

1. Ouvrez un invite de commande si vous êtes sous Windows, ou un terminal si vous êtes sous Linux ou MacOSX

2. Rendez-vous dans le dossier dans lequel vous souhaitez cloner le dépôt

3. Saisissez la commande `git clone https://github.com/ludosansone/ls_litreview.git`

4. Le dépôt est pret, vous pouvez y accéder en tapant `cd ls_litreview`




## Installation de l'environnement virtuel

Afin de garentir le bon fonctionnement de cette application web, vous devez l'exécuter dans le même environnement virtuel que le développeur. Pour se faire, suivez les instructions d'installation ci-dessous.
Attention, nous partons du principe que les paquets pip et venv sont bien installés sur votre ordinateur. Si tel n'est pas le cas, veuillez vous référer à leur documentation respective pour procéder à leur installation.


### Installation sous Windows

1. Ouvrez l'invite de commandes

2. Déplacez-vous à la racine du dossier ls_litreview, à l'aide de la commande cd

3. Pour créer l'environnement virtuel, saisissez la commande : `python -m venv env`

4. Pour démarrer ce dernier, saisissez la commande : `env\Scripts\activate`

5. Pour y installer les paquets nécessaires à la bonne exécution du projet, saisissez la commande : `pip install -r requirements.txt`


### Installation sous Linux ou MacOSX

1. Ouvrez un terminal

2. Déplacez-vous à la racine du dossier ls_litreview, à l'aide de la commande cd

3. Pour créer l'environnement virtuel, saisissez la commande : `python -m venv env`

4. Pour démarrer ce dernier, saisissez la commande : `source env/bin/activate`

5. Pour y installer les paquets nécessaires à la bonne exécution du projet, saisissez la commande : `pip install -r requirements.txt`



## Utilisation de Flake8

Afin de vérifier que le code du programme répond bien à la norme PEP-8, vous pouvez utiliser la commande Flake8.

Pour que Flake8 affiche son rapport directement dans la console : 

1. Déplacez-vous à la racine du projet, dans le dossier ls_litreview/litreview, à l'aide de la commande cd

2. puis saisissez la commande `flake8`




## Lancement de l'application

Attention, avant de lancer l'application, assurez-vous que l'environnement virtuel est activé.

1. Ouvrez l'invite de commandes

2. Déplacez-vous à la racine du projet, dans le dossier ls_litreview/litreview, à l'aide de la commande cd

3. Saisissez la commande `python manage.py runserver`

4. Le serveur de développement se lance, et nous invite à nous rendre à l'adresse http://127.0.0.1:8000/

5. Ouvrez votre navigateur, et rendez-vous à l'adresse indiquée

6. L'application est prête




## utilisation de l'application

L'application web LitReview, permet à ses utilisateurs de consulter, solliciter et proposer des critiques littéraires. Pour connaître les détails de son utilisation, reportez-vous aux sections ci-dessous.


### Inscription et connexion

L'application vous accueille en vous proposant de vous inscrire, ou si vous possédez déjà un compte, de vous connecter.

Ppour vous connecter, saisissez simplement vos identifiants dans le formulaire, sur la partie droite de la page.

Pour vous inscrire, cliquez sur le lien "S'inscrire", puis saisissez vos informations personnelles. Votre compte sera instantanément créé, et vous serez automatiquement connecté.


### Navigation

La page d'accueil, comme l'ensemble des pages de l'application, contient le menu de navigation. Il vous permet d'accéder à :

- vos abonnements
- vos contributions
- ou à la déconnexion


### Accueil

La page d'accueil affiche votre flux. Il est constitué de :

- vos contributions : Les critiques que vous avez publiées, et celles que vous avez sollicitées via des tickets
- les contributions des utilisateurs que vous suivez
- les critiques répondant à vos tickets, même si son auteur ne fait pas partie des utilisateurs que vous suivez

Cliquez simplement sur l'intitulé d'une contribution, pour accéder à ses détails, et réaliser les opérations adaptées au type de contribution sélectionnée.

Pour revenir à la page d'accueil de l'application, il vous suffit de cliquer sur l'entête LitReview, se trouvant en haut de chaque page.


### Mes abonnements

C'est sur cette page que vous pourez retrouver la liste des utilisateurs que vous suivez, et de ceux qui vous suivent.

Pour suivre un nouvel utilisateur, il vous suffit de saisir son nom dans la zone d'édition située au dessus du tableau, puis de cliquer sur "Valider le suivi".

En cliquant sur le nom d'un utilisateur dans le tableau, vous accèderez à la page de ses contributions.

Pour cesser de suivre un utilisateur, cliquez sur "Ne plus suivre", dans la colonne d'actions.


## Mes contributions

Cette page contient les tickets et critiques dont vous êtes l'auteur.

En cliquant sur l'intitulé de la contribution, vous accédez aux détails de cette dernière.

Vous pouvez également supprimer ou modifier la contribution, en cliquant dans la colonne d'actions du tableau, sur la ligne appropriée.

Si vous décidez de supprimer une contribution, vous serez redirigé vers une page, vous demandant de confirmer cette suppression.


### Déconnexion

En cliquant sur "Déconnexion", vous serez redirigé vers la page de connexion de l'application.
