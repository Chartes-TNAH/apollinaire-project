# Description

Petit CLI permettant de télécharger les images d'un manifest ark, 
s'il est dans le domaine public, via l'API IIIF de Gallica.
Il permet de récupérer des images de meilleure qualité par
rapport aux téléchargements depuis l'interface web de Gallica.
A vous donc le travail hors-connexion, les tests d'OCR, les annotations, les agrandissements
et autres ! 

Télécharge des fichiers images à partir d'un intervalle de folios,
présents dans un id ark. __Ce script présuppose donc une connaissance 
du contenu de l'ark duquel on souhaite avoir les images.__ 

Enregistrement des fichiers image en __.jpg__ dans un nouveau dossier, situé
là où se trouve le script python. Le nommage des fichiers respecte le numéro de folio. 

Ainsi, si je télécharge l'image du folio 198, mon fichier sera nommé "f198.jpg" et sera
enregistré dans mon répertoire lenomdurépertoirequejaichoisi 

Selon le volume, le téléchargement peut prendre un certain temps. J'ai en effet
ajouté une couche de sécurité correspondant à un délai de 1 seconde entre chaque
téléchargement, afin d'éviter de surcharger l'API de Gallica. 

# Comment ça marche

Une seule commande est disponible : query

Pour exécuter le script :

```
python get_corpus.py query ark from_f to_f directory_name
```

* ark : ID ARK
* from_f : numéro de folio indiquant le départ de l'intervalle de téléchargement
* to_f : numéro de folio indiquant la fin de l'intervalle de téléchargement
* directory_name : nom du nouveau dossier créé, dans lequel seront enregistrées les images. 


Par exemple, pour récupérer les folios 198 à 206 du dossier de presse ([https://gallica.bnf.fr/iiif/ark:/12148/btv1b525088021/manifest.json](https://gallica.bnf.fr/iiif/ark:/12148/btv1b525088021/manifest.json))
sur lequel on travaille : 

```
python get_corpus.py query ark:/12148/btv1b525088021 198 206 dossier_images_f198_to_f206
```

# Requirements

Pour faire fonctionner ce script :

Téléchargez-le et déplacez-le dans un nouveau dossier.
Dans ce dossier, créez un nouvel environnement virtuel qui sera utilisé
pour installer les librairies nécessaires au fonctionnement du script et dans lequel vous l'exécuterez. 
Il est également possible d'utiliser un autre environnement virtuel que vous avez créé précédemment. 

Les librairies à télécharger dans l'environnement virtuel que vous utilisez sont les suivantes : 

* requests
* click
* Pillow

Vous pouvez les retrouver dans requirements.txt

Pillow est une librairie permettant d'ouvrir, manipuler et sauvegarder des formats d'images. 
Le script utilise ici le module Image de Pillow.
Voir le site officiel de Pillow : https://pillow.readthedocs.io/en/stable/index.html
Documentation spécifique à l'installation : https://pillow.readthedocs.io/en/stable/installation.html

Pour l'installer, une fois que vous êtes dans un environnement virtuel : 

```
pip install Pillow
```

# Pour terminer

N'hésitez pas à modifier le script à votre guise ! :+1: Une sortie csv serait peut-être
chouette à implémenter, histoire de garder les métadonnées de chaque folio. 

