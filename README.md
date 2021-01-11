
Frédéric LOPEZ et Tanguy VIDAL
# Résolution du problème des n-Dames

Dans ce projet nous avons développé trois fonctions différentes permettant de résoudre le problème des n-dames.
Ce problème des n-dmaes consistait à placer, sur un dmier de n*n dimensions, n dames sans qu'aucune ne soit menacée par une autre ([selon les règles de déplacement des échecs](http://leconsdechecspourdebutants.com/regles/lecon_2_dame.htm))

## Premier Algorithme :  Approche "naïve

Nous avons, pour cet algorithme, utilisé une approche naïve du problème, c'est à dire que nous avons cherché à résoudre le problème sans nous soucier des problématiques de ressources utilisées et de complexité algorithmique. Ce premier algorithme utilise le principe de backtracking. De fait cet algorithme ne permet pas de résoudre le problème dans des temps raisonnables si n>=20 (30s<t<90s environ). Nous nous sommes appuyés sur différents sites pour construire notre logique de backtracking:
* https://interstices.info/le-probleme-des-8-reines/
* https://www.freecodecamp.org/news/lets-backtrack-and-save-some-queens-1f9ef6af5415/

## Deuxième algorithme :  Un algorithme efficace, optimisé

Cet algorithme est plus recherché puisqu'il se veut concu pour trouver une solution au problème quel que soit le n choisi.
Nous avons effectués nos recherche vers la méthode heuristique dite de moindre conflict.
