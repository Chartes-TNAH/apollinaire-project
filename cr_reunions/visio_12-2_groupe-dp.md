
# Structuration encodage dossier de lettre
# à destination du groupe dossier de presse

Présents : Léa, Hugo, Doriane, Axelle.

## Besoins :

- Lettres : 
    - garder la structure sémantique des lettres
    - signaler un recto/verso + renvoyer au folio
    - garder un élément pb pour pouvoir signaler des pages blanches, des structures particulières
- Articles : 
    - signifier leur emplacement sur le folio
    - indiquer lorsqu’ils sont disposés sur différents folios

## Proposition 1 :

```
<div1 type=”lettre/folio”>
    <div2 type=”article/recto/verso” @n @facs>
	</div2>
</div1>
```

### Inconvénients/problèmes:
- différence dans la hiérarchie entre entité physique et conception sémantique dans @type

## Proposition 2 :

`<div type=”article/lettre” @subtype=”recto/verso/?” @n @facs @xml:id @xml:lang>`

### À mettre en place:
- Suppression de la note du libraire avec le numéro de page dans le dossier de presse car sinon apparaîtra plusieurs fois au niveau de chaque `<div>`. Pose la question sur la pertinence au sein du projet de le garder : quelle serait son utilité? pour quoi faire ? 
- Il faut utiliser un xml:id pour signifier les `<div>` qui forment une même lettre et obligation du @n et @facs pour les articles pour signifier le folio
- problème de la proposition 1 se résout dans cette proposition 2. 

## Proposition choisie suite à la discussion du groupe :

`<div type=”article/lettre” @n @xml:id @xml:lang>`
    pour les lettres : `<pb @type @subtype @facs>`
	pour les articles : `<pb @facs>`

- `<pb>` avec @type recto/verso @subtype empty/copy 
- `<pb>` pour articles où plusieurs folios
- Valeur de n=”201, 202” → désigne tous les folios concernés et non une tranche de folios
- Pour les articles : 
    - sur la `<div>` 
        - @n avec les folios concernés 
        - @xml:id 
    - sur la `<pb>`.
        - @facs
- Pour les lettres:
    - sur la `<div>` :
        - @n (montrer la lettre)
        - @xml:id
    - sur la `<pb>`:
        - @facs
        - @type
        - @subtype



# À destination du groupe entier

## Sujets à discussion: 
- Indexation du nom Apollinaire
- Index des titres du poèmes 
- Index de l’oeuvre Alcools 
- De manière générale : importance des xml:id pour les copies afin de pouvoir renvoyer au double si besoin
- sourceDoc : https://www.tei-c.org/release/doc/tei-p5-doc/fr/html/PH.html#PHZLAB qui obligerait à revoir tout l’encodage déjà effectué.
- Glossaire/table des matières

## Suite à la discussion :
- sourceDoc : après réflexion, cela ne nous semble pas approprié au dossier de presse (notamment les renvois vers des fac-similés) car il ne s’agit pas d’une édition génétique du dossier de presse.
- Il a été décidé, pour le dossier de presse, de faire un index des noms de personnes et de rassembler sous un xml:id commun tous les noms des personnes illsibles ou non identifiables. Apollinaire doit aussi être indexé. Exemple ci-dessous pour présenter une entrée dans l'index des personnes:
```
<person xml:id="Carco">
    <persName><forename>Francis</forename><surname>Carco</surname></persName>
    <note>Écrivain/journaliste.</note>
</person>
```

- Il est été décidé pour le dossier de presse de faire un index des villes.
- L'indexation de l'oeuvre _Alcools_ est refusée. Mais un index des titres de poèmes de l'oeuvre _Alcools_ sera effectué afin de permettre une recherche par titres. 
- Pour les xml:id → tout mettre en minuscules + underscore pour espace.


## Faire issue/PR pour réflexion: 
- Liste des xml:id ? 
- Comment indexer titres de poèmes Alcools
- Faire une PR pour acter la suppression de la numérotation du libraire

# Choses qui resteraient à faire:
-- cette partie n'a pas été discuté -- 

- corriger l’encodage en fonction de la proposition choisie
- terminer encodage des articles/lettres non fait
- teiheader
- les index 
- table des matières/glossaire
- produire une ODD commune
- documentation HTML

