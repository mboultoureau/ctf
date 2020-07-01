# Warmup

## Sommaire

- [Read The Rules](#read-the-rules)
- [CLIsay](#clisay)
- [Metameme](#metameme)
- [Mr. Robot](#mr-robot)
- [UGGC](#uggc)
- [Easy Keesy](#easy-keesy)
- [Peter Rabbit](#peter-rabbit)
- [Pang](#pang)

## Read The Rules

Il suffit de lire les règles.

Flag : `flag{}`

## CLIsay

Il faut exécuter la commande `strings clisay`. Il suffit de prendre la partie du flag au-dessus et en dessous de l'image.

Flag : `flag{Y0u_c4n_r3Ad_M1nd5}`

## Metameme

Il suffit de regarder les métadonnées de l'image. Sous Windows, Propriétés > Détails.
En ligne, on peut utiliser le très bon [ApériSolve](https://aperisolve.fr/).

Flag : `flag{N0t_7h3_4cTuaL_Cr3At0r}`

## Mr. Robot

L'URL original donnée est [http://jh2i.com:50032](http://jh2i.com:50032). Il suffit d'aller sur la page **robots.txt** : [http://jh2i.com:50032/robots.txt](http://jh2i.com:50032/robots.txt).

Flag : `flag{welcome_to_robots.txt}`

## UGGC

Ce [challenge](http://jh2i.com:50018/) demande un login qui doit être admin. Lorsque nous soumettons un login nous pouvons voir que celui-ci est stocké dans un cookie en ROT13 sous la forme : `user=PASSWORD_EN_ROT13`.

Avec Postman sur la page principale, il suffit simplement de faire une requête avec comme cookie : `user=nqzva` (admin en ROT13) et nous obtenons le flag.

Flag : `flag{H4cK_aLL_7H3_C0okI3s}`

## Easy Keesy

La commande `file easy_keesy` nous indique qu'il s'agit d'une base de données de mots de passes Keypass.

Nous allons donc utiliser JohnTheRipper pour trouver le mot de passe. Il nous faut d'abord le hash du mot de passe : `keepass2john easy_keesy > password.hash`. Nous pouvons ensuite lancer l'attaque par dictionnaire avec `john --wordlist=/usr/share/wordlists/rockyou.txt password.hash`. Quelques secondes après nous trouvons le mot de passe **monkeys**. Avec nous pouvons donc ouvrir le fichier dans Keepass et trouvez le flag.

Note : nous utilisons ici la wordlist fourni par Kali Linux. Si ce n'est pas déjà fait, il faudra la décompresser avec `gunzip -d /usr/share/wordlists/rockyou.txt.gz`.

Flag : `Flag{jtr_found_the_keys_to_kingdom}`

## Peter Rabbit

Il suffit de donner l'image à un [interpréteur Piet](https://www.bertnase.de/npiet/npiet-execute.php) et noter le flag.

Flag : `flag{ohhhpietwastherabbit}`

## Pang

Lorsque nous faisons `file pang` nous pouvons constater qu'il s'agit d'une image PNG mais impossible de l'ouvrir elle semble corrompu.

Nous utilisons donc [PCRT](https://github.com/sherlly/PCRT) pour trouver la source du problème :

```sh
git clone https://github.com/sherlly/PCRT.git
cd PCRT
python PCRT.py -v -i pang # -v : verbose ; -i : input image
```

Le programme nous retourne la source de l'erreur :

```
[Detected] Error IHDR CRC found! (offset: 0x1D)
chunk crc: F9F1EA99
correct crc: F9F1DA99
```

Il suffit de régler le problème avec un éditeur hexadécimale et d'ouvrir le fichier.

Flag : `flag{wham_bam_thank_you_for_the_flag_maan}`
