Ce repository a été créé dans le cadre d'un module git, dispensé par M. Thibault Clérice pour le master 2 TNAH à l'Ecole nationale des chartes.

## Les contributeurs
- [Arsène Georges](https://github.com/ArsGeo)
- [Axelle Lecroq](https://github.com/axellelecroq)
- [Doriane Hare](https://github.com/D0riane)
- [Hugo Scheithauer](https://github.com/HugoSchtr)
- [Juliette Janes](https://github.com/Juliettejns)
- [Léa Perissier](https://github.com/leaprs)
- [Pauline Breton-Chauvet](https://github.com/PaulineChauvet)

## Le Projet Apollinaire

### Description du projet
Le Projet Apollinaire a vocation à offrir les données structurées et les outils nécessaires à l'édition numérique d'un corpus constitué autour du recueil poétique Alcools.
Les choix spécifiques d'encodage en XML-TEI doivent permettre l'exportation et l'exploitation des données inhérentes à la genèse du processus scriptural, à son évolution jusqu'à la forme définitive, et à la réception du recueil par ses contemporains.

### Le corpus
Le corpus se compose de plusieurs types de source - manuscrite et imprimée - tous disponibles sous forme numérique sur Gallica:
- les [versions préparatoires manuscrites de septs poèmes](https://gallica.bnf.fr/ark:/12148/btv1b52505641f/f37.item.r=Manuscrit%20Apollinaire#) du recueil *Alcools*, édité pour la première fois en 1913:

- un [dossier de presse](https://gallica.bnf.fr/ark:/12148/btv1b525088021/f145.item.r=Apollinaire%20manuscrits) constitué par Guillaume Apollinaire lui-même. Il regroupe articles de périodiques et lettres reçues à l'occasion de la diffusion et de la réception d'Alcools. 


### Feuille de route
1. Transcriptions des folios des versions préparatoires et du dossier de presse : les transcriptions de textes manuscrits ont été effectuées par tous les contributeurs. Les articles de presse ont été quant à eux océrisés.
2. Création d'un échantillon pour l'établissement d'une ODD en vue de l'intégration continue : le groupe a été subdivisé afin de permettre une réflexion approfondie sur les choix d'encodage inhérents à chaque source, envisagée à la fois dans leur singularité et dans l'ensemble où elles s'inscrivent. La réalisation d'un échantillon encodé spécifique à chacune a été le préalable à la génération d'une ODD, indispensable pour l'encodage définitif du corpus dans un cadre d'intégration continue. Chaque étape stratégique et déterminante d'encodage (telle que la sélection des éléments du TeiHeader et la structuration de l'ossature générale de chaque source) a été abordée et validée par l'ensemble des contributeurs.
3. L'encodage définitif : le groupe a été une fois de plus divisé afin de procéder aux encodages complets et définitifs des versions préparatoires et du dossier de presse. Une documentation propre à chacune de ces deux branches du corpus a également été rédigée, structurée en XML-TEI puis transformée en html.
### État actuel
Le projet est à ce jour terminé. Le recueil de versions préparatoires ainsi que le dossier de presse font l'objet de deux répertoires distincts contenant: les fichiers XML-TEI d'encodage et d'ODD, le schéma RNG, la documentation structurée ainsi que son fichier html de transformation.
