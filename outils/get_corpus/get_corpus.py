import requests
import click
import time
import os
import sys
from PIL import Image
import io


def ark_query(ark, from_f, to_f):
    """
    A partir d'un identifiant ark et d'un numéro de folio de départ et de fin, enregistre
    dans une liste les url des images des folio situés dans l'intervalle
    via l'API IIIF Gallica.

    :param ark: identifiant ark duquel on veut récupérer des images
    :type ark: str
    :param from_f: folio de départ pour l'intervalle
    :type from_f: int
    :param to_f: folio de fin pour l'intervalle
    :type to_f: int
    :return: liste des url des images pour les folios situés dans l'intervalle
    :rtype: list
    """

    url_img_list = []

    url_query = "https://gallica.bnf.fr/iiif/" + ark + "/manifest.json"
    print("Fetching: {0}".format(url_query))
    r = requests.get(url_query)
    data = r.json()

    if r.status_code == 200:
        for item in data['sequences']:
            for page in item['canvases']:
                for url in page["images"]:
                    url_img = url["resource"]["@id"]
                    url_img_list.append(url_img)

    if from_f > 0:
        from_f = from_f - 1
    url_img_list = url_img_list[from_f:to_f]
    return url_img_list


def download_image(url_img_list, directory_name):
    """
    Permet de télécharger des images à partir d'une liste d'url. Une URL de cette liste donne accès à l'image
    d'un folio spécifique d'un identifiant ark via l'API Gallica IIIF.
    Création d'un nouveau dossier, situé là où se trouve le script
    python, dans lequel seront enregistrées les images.
    Utilise la librairie Pillow (pip install Pillow) pour traiter les fichiers images.

    :param url_img_list: Liste des URL donnant accès à une image via l'API IIIF Gallica
    :type url_img_list: list
    :param directory_name: nom du nouveau dossier dans lequel on souhaite enregistrer les images
    :type directory_name: str
    """

    print(url_img_list)

    try:
        os.mkdir(directory_name)
    except FileExistsError as e:
        print("Ce dossier existe déjà. Choisissez un nom différent svp.")
        sys.exit()

    for request in url_img_list:
        r = requests.get(request)
        if r.status_code == 200:
            print("fetching : {0}".format(request))
            f = io.BytesIO(r.content)
            i = Image.open(f)
            i.save('./{0}/{1}.jpg'.format(directory_name, request[54:58]), 'jpeg')
            i.close()

            # Couche de sécurité pour ne pas surcharger l'API en cas de téléchargement important
            # Ici, une seconde s'écoule entre chaque requête.
            # Possible de rendre le délai moins long, time.sleep(0.5), par exemple.
            # Possible de le désactiver en commantant la ligne suivante/supprimant.
            time.sleep(1)


@click.group()
def group():
    """
    Petit CLI permettant de télécharger les images d'un manifest ark via l'API IIIF de Gallica.
    Il permet de récupérer des images de meilleure qualité par rapport aux téléchargements depuis
    l'interface de Gallica.
    Enregistrement des fichiers image en .jpg dans un nouveau dossier, situé là où se trouve le script python.
    """


@group.command("query")
@click.argument("ark", type=str)
@click.argument("from_f", type=int)
@click.argument("to_f", type=int)
@click.argument("directory_name", type=str)
def run(ark, from_f, to_f, directory_name):
    """
    Lance le téléchargement des images d'un manifest IIIF ark, via l'API IIIF Gallica.
    Télécharge du folio from_f au folio to_f, et enregistre les fichiers .jpg dans un nouveau dossier,
    situé là où se trouve le script python.

    Si je souhaite avoir les images des folio 198 à 206 de l'ark ark:/12148/btv1b525088021 :
    python get_corpus.py query ark from_f to_f directory_name
    python get_corpus.py query ark:/12148/btv1b525088021 198 206 dossier_images_f198_to_f206

    :param ark: Identifiant ark duquel on veut récupérer des images
    :type ark: str
    :param from_f: folio de départ pour un interval de téléchargement
    :type from_f: int
    :param to_f: folio de fin pour un interval de téléchargement
    :type to_f: int
    :param directory_name: nom du dossier dans lequel on souhaite enregistrer les images
    :type directory_name: str
    """

    url_img_list = ark_query(ark, from_f, to_f)
    download_image(url_img_list, directory_name)

    print("Téléchargement terminé")


if __name__ == "__main__":
    group()
