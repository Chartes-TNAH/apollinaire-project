# Règles de nommages au sein du projet Apollinaire

## Nommage des fichiers `.txt`
Les fichiers `.txt` n'ont pas reçu de normalisation
de nommage et ont été nommés de manière arbitraire
par chacun des membres du groupe au cours de la 
transcription du corpus.

## Nommage des fichiers `.xml`
Il a été choisi d'indiqué l'intervalle des folios
suivi du type du document comme suit (voir [issue #21](url:https://github.com/axellelecroq/apollinaire-project/issues/21)) : 
- `172-174_lettre` : tous les folios sont indiqués (même structure pour les poèmes)
- `201_articles` : pour un folio composé d'articles
- `202-203_article` : pour un article sur deux folios différents

## Nommage des `xml:id`
### `xml:id` des documents
Les `xml:id` ne peuvent commencer par un entier,
ainsi le type de document est indiqué en premier
suivi du numéro de folio.Tout comme pour le nommage des fichiers `.xml`,
il a été décidé de garder l'intervalle pour les
`xml:id` (voir [issue #40](url:https://github.com/axellelecroq/apollinaire-project/issues/40)). 
Le nommage se fait donc comme suit : 
- `lettre_172-175`
- `article1_201` : pour le premier article du folio 201
- `article-202-203` : pour un article sur deux folios différents

### `xml:id` des personnes, lieux et références bibliographiques
Après discussion dans l'[issue #47](url:https://github.com/axellelecroq/apollinaire-project/issues/47), il a été choisi d'utiliser exclusivement les miniscules dans les `xml:id` et d'omettre aucun mot. Les espaces sont représentés pas des underscores.
Ainsi, les `xml:id` se présentent comme suit pour les noms de :
- personnes : `fleuret_ferdinand` pour Ferdinand Fleuret.
- lieux : `cap_d_ail` pour Cap d'Ail.
- poèmes : `le_mal_aimé` pour Le mal aimé.