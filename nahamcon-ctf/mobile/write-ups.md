# Mobile

## Sommaire

- [Candroid](#candroid)
- [Simple App](#simple-app)

## Candroid

Nous pouvons utiliser **apktool** pour décompiler l'application :

```sh
apktool d candroid.apk
```

Il suffit ensuite de rechercher dans le code le flag qui commence par _flag{_. On constate qu'il se trouve dans `res/values/strings.xml`.

Flag : `flag{4ndr0id_1s_3asy}`

## Simple App

Nous faisons exactement pareil que le challenge [Candroid](#candroid) :

```sh
apktool d candroid.apk
```

Il suffit ensuite de rechercher dans le code le flag qui commence par _flag{_. On constate qu'il se trouve dans `smali/com/example/simple_app/MainActivity.smali`.

Flag : `flag{3asY_4ndr0id_r3vers1ng}`
