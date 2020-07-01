# Warmup

## Sommaire

- [Read The Rules](#read-the-rules)
- [CLIsay](#clisay)
- [Metameme](#metameme)
- [Mr. Robot](#mr-robot)
- [UGGC](#uggc)

## Read The Rules

Il suffit de lire les règles.

Flag : `flag{}`

## CLIsay

Il faut exécuter la commande `strings clisay`. Il suffit de prendre la partie du flag au-dessus et en dessous de l'image.

Flag : `flag{Y0u_c4n_r3Ad_M1nd5}`

## Metameme

Il suffit de regarder les métadonnées de l'image. Sous Windows, Propriétés > Détails. Sous Linux |...|.

ICI

En ligne, on peut utiliser le très bon [ApériSolve](https://aperisolve.fr/).

Flag : `flag{N0t_7h3_4cTuaL_Cr3At0r}`

## Mr. Robot

L'URL original donnée est [http://jh2i.com:50032](http://jh2i.com:50032). Il suffit d'aller sur la page **robots.txt** : [http://jh2i.com:50032/robots.txt](http://jh2i.com:50032/robots.txt).

Flag : `flag{welcome_to_robots.txt}`

## UGGC

Ce [challenge](http://jh2i.com:50018/) demande un login qui doit être admin. Lorsque nous soumettons un login nous pouvons voir que celui-ci est stocké dans un cookie en ROT13 sous la forme : `user=PASSWORD_EN_ROT13`.

Avec Postman sur la page principale, il suffit simplement de faire une requête avec comme cookie : `user=nqzva` (admin en ROT13) et nous obtenons le flag.

Flag : `flag{H4cK_aLL_7H3_C0okI3s}`
