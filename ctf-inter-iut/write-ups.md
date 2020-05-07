# Write-ups

Les différents Write-Ups du [CTF Inter IUT](https://twitter.com/CTF_Inter_IUT).


## Bibliothèque de Babel

Le [tweet original](https://twitter.com/CTF_Inter_IUT/status/1232953492941287424) nous indique avec un lien vers [PasteBin](https://pastebin.com/raw/MYEYwsfh) :
```
Wall 4, shelf 4, volume 27 !
Page 199.
```

Le lien nous indique `infinite library`. Après une recherche rapide, on tombe sur la [page Wikipedia "La Bibliothèque de Babel"](https://fr.wikipedia.org/wiki/La_Biblioth%C3%A8que_de_Babel) :

```
La bibliothèque de Babel est une nouvelle décrit une bibliothèque de taille gigantesque contenant tous les livres de 410 pages possibles (chaque page formée de 40 lignes d'environ 80 caractères). Les livres sont placés sur des étagères comprenant toutes le même nombre d'étages et recevant toutes le même nombre de livres. Chaque livre a le même nombre de pages et de signes.
```

En se rendant sur le site [libraryofbabel.info](http://libraryofbabel.info/browse.cgi), nous pouvons coller dans Hex Name le contenu du PasteBin et choisir comme indiqué le quatrième mur, la quatrième étagère, le volume 27 et se rendre à la page 199. On tombe enfin sur cela :

```
l equipe offre les kebabs aux elites qui arrivent a resoudre tous les challenges
```

## Brainfuck

Le [tweet](https://twitter.com/CTF_Inter_IUT/status/1239631299595382787) nous donne un lien vers un [PasteBin](https://pastebin.com/raw/jCsvi7YB) avec le contenu suivant :

```
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>+++++.+++++++++++.-------------------.+++++++++++.---.--------.<<++.>>+++++++++++++++++++++.------.--.<<.>>--------.++++++++++++++.+++.<<++++++++++++++.>>---------------.++++++++++++..----.+++.<<++++++++++++.-----------..>>+.-----------.+++++.+++++++++++.----.---.------.<<-.>>---------.++++++++++++.--.<<+.>>++++++++++++.-.<<++++++++.>>------.---.+++.------.--.
```

Avec un peu d'expérience dans les CTF, on devine qu'il s'agit un langage ésotérique nommé le [BrainFuck](https://fr.wikipedia.org/wiki/Brainfuck). Il suffit de se rendre sur un [décodeur](++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>+++++.+++++++++++.-------------------.+++++++++++.---.--------.<<++.>>+++++++++++++++++++++.------.--.<<.>>--------.++++++++++++++.+++.<<++++++++++++++.>>---------------.++++++++++++..----.+++.<<++++++++++++.-----------..>>+.-----------.+++++.+++++++++++.----.---.------.<<-.>>---------.++++++++++++.--.<<+.>>++++++++++++.-.<<++++++++.>>------.---.+++.------.--.), suivre le [lien décodé](https://tinyurl.com/yx7rorlj) et admirer la magnifique image en tant de confinement.

## Capture Wireshark

En ouvrant la [capture](http://challs.hack2g2.fr/02/capture.pcapng) dans Wireshark, on remarque un téléchargement d'image. Pour l'obtenir, dans Wireshark il faut cliquer sur *File > Export Objects > HTTP* et enregistrer l'image. Sur celle le flag est écrit :

Flag : `ENSIBS{w1r3sh4Rk_iS_c00l}`

## Magic code

Le challenge porte sur une [image PNG](https://challs.hack2g2.fr/03/logo_v1.png). Malheureusement, impossible de la visualiser et la commande `file` nous indique que ce fichier n'est pas une image. Nous ouvrons donc l'image dans un éditeur hexadécimal et nous constatons que les huit premiers octets ont été remplacés : `DE AD BE EF CA FE BA BE`. Il nous suffit donc de les remplacer par le magic code des images PNG : `89 50 4E 47 0D 0A 1A 0A` et noter le flag présent sur l'image.

Flag : `ENSIBS{m4g1c_nUmb3rz_t00_ez}`

## AES Ciphertext

```
On peut chiffrer mille fois mille messages, euh non, une fois mille messages mais on ne peut pas chiffrer un message mille fois.
Ou peut-être que si Visage songeur !
La clé est '\xcaV7Zs\xbb\xe3\xec\xcd~\x8ad\xf5ZA\xb7' !
Essayez de déchiffrer ce message : http://challs.hack2g2.fr/04/ciphertext.
```

Le fichier s'appelle ciphertext. Après quelques recherches sur Internet, on peut supposer qu'il s'agit de l'[algorithme de chiffrement AES](https://fr.wikipedia.org/wiki/Advanced_Encryption_Standard). (Cela fut confirmé après lorsque le fichier a été édité avec "AES ciphertext" au début). L'autre indice est qu'il fallait déchiffrer le message mille fois.

Il faut désormais la clé. Pour cela on peut utiliser noter les valeurs ASCII des caractères qui ne sont encore en hexadécimale ou utiliser Python :

```python
import binascii
binascii.hexlify(b'\xcaV7Zs\xbb\xe3\xec\xcd~\x8ad\xf5ZA\xb7')

>>> ca56375a73bbe3eccd7e8a64f55a41b7
```

Avec tout cela, nous pouvons réaliser un script Python.

Note : j'ai perdu beaucoup de temps car j'utilisais le mauvais [mode d'opération](https://fr.wikipedia.org/wiki/Mode_d%27op%C3%A9ration_(cryptographie)) (CBC au lieu d'ECB). J'ai remarqué mon erreur quand j'ai compris le mode CBC nécessité un vecteur d'initialisation donnée.