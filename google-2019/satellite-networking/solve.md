# Satellite Networking

Lors de l'ouverture de `init_sat`, le programme demande le nom du satellite. Celui-ci est visible sur l'image du PDF `osmium`. Ensuite, nous avons le choix entre (a) afficher les données de configuration, (b) effacer toutes les données, (c) se déconnecter.

En appuyant sur (a), le terminal affiche :
```
Username: brewtoot password: ********************	166.00 IS-19 2019/05/09 00:00:00	Swath 640km	Revisit capacity twice daily, anywhere Resolution panchromatic: 30cm multispectral: 1.2m	Daily acquisition capacity: 220,000km²	Remaining config data written to: https://docs.google.com/document/d/14eYPluD_pi3824GAFanS29tWdTcKxP_XUxx7e303-3E
```

En suivant le [lien](https://docs.google.com/document/d/14eYPluD_pi3824GAFanS29tWdTcKxP_XUxx7e303-3E), on obtient `VXNlcm5hbWU6IHdpcmVzaGFyay1yb2NrcwpQYXNzd29yZDogc3RhcnQtc25pZmZpbmchCg==`, ce qui décodé en base64 donne :

```
Username: wireshark-rocks
Password: start-sniffing!
```

Il faut probablement donc utilisé WireShark. Et en effet, en analysant on trouve le flag.

CTF{4efcc72090af28fd33a2118985541f92e793477f}