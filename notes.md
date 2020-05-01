# CTF Notes

Ce sont des notes aléatoires de mes différents CTF et challenges effectués.

## Cryptographie

### Brainfuck

Vous avez un message de ce type :

```brainfuck
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++.>+.+++++++..+++.<<++.>+++++++++++++++.>.+++.------.--------.
```

Brainfuck est un langage de programmation exotique. Les seuls caractères autorisés sont `>`, `<`, `+`, `-`, `.`, `,`, `[` et `]`.

[Décodeur](https://www.dcode.fr/langage-brainfuck)
[Visualiseur](https://fatiherikli.github.io/brainfuck-visualizer)
[Wikipedia](https://fr.wikipedia.org/wiki/Brainfuck)

### Bibliothèque de Babel

La bibliothèque de Babel est une nouvelle décrit une bibliothèque de taille gigantesque contenant tous les livres de 410 pages possibles (chaque page formée de 40 lignes d'environ 80 caractères) et dont toutes les salles hexagonales sont disposées d'une façon identique. Les livres sont placés sur des étagères comprenant toutes le même nombre d'étages et recevant toutes le même nombre de livres. Chaque livre a le même nombre de pages et de signes. L'alphabet utilisé comprend vingt-cinq caractères (vingt-deux lettres minuscules, l'espace, la virgule et le point).

[Visualiseur](http://libraryofbabel.info/browse.cgi)
[Wikipedia](https://fr.wikipedia.org/wiki/La_Biblioth%C3%A8que_de_Babel)

## Réseau

### Analyseur réseau : WireShark

Les fichiers `.pcap` ou encore `.pcapng` sont des fichiers de WireShark. Pour enregistrer des fichiers capturés (images, fichier HTML, etc) : File > Export Objects > HTTP.

[WireShark](https://www.wireshark.org/)

## Reverse Engineering

## Utilisation de GDB (GNU Debugger)

Ouvrez votre fichier binaire avec `gdb nomDuFichier`.

Commandes :

-   `set disassembly-flavor intel` : change la syntaxe de l'assembleur
-   `disassemble [where]` : désassemble le code (ex : `disassemble main`)
-   `break <code>` : ajoute un breakpoint (ex : `break *main` ; `break *main+200` ; `break \*0x373`)
-   `info registers` : affiche le contenu des registres
-   `si` : exécute l'instruction suivante
-   `ni` : comme `si` exécute l'instruction suivante, mais en cas d'appel de fonction, exécute la fonction jusqu'à son appel de retour
-   `set $<registre>=<valeur>`: définit une valeur a un registre (ex : set \$eax=0)
-   `x/s <adresse>` : affiche le contenu d'une adresse (ex : x/s \*0x293)

Appuie sur ENTRÉE exécute automatiquement la dernière commande entrée.

## Commandes utiles

-   `file nomFichier` : affiche des informations sur le type du fichier
-   `hexdump -C nomFichier` : affiche le contenu du fichier en hexadécimal
-   `strings` : affiche tous les suites de caractères ascii de plus d'une certaine longueur (par défaut 4)
-   `objdump -d nomFichier` : affiche le code assembleur du programme
-   `strace nomFichier` : affiche tous les appels systèmes (syscalls)
-   `ltrace nomFichier` : affiche les appels des différentes librairies
