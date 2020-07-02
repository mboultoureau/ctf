# Web

## Sommaire

- [Agent 95](#agent-95)
- [Localghost](#localghost)

## Agent 95

Dans Postman il suffit de mettre le champ "User-Agent" à "Windows 95".

Flag : `flag{user_agents_undercover}`

## Localghost

On voit en observant le code source de la page que le code du fichier **jquery.jscroll2.js** semble offusqué. On peut en partie le rendre plus lisible grâce à [Beautifier.io](https://beautifier.io/). En observant le code obtenu on trouve une ligne intéressante :

```javascript
window['localStorage']['setItem']('flag', atob('SkNURntzcG9vb29va3lfZ2hvc3RzX2luX3N0b3JhZ2V9'));
```

En ouvrant la console et entrant la fonction atob avec son paramètre on trouve le flag.

Note : la fonction atob décode en base64 la chaine.

Flag : `JCTF{spoooooky_ghosts_in_storage}`
