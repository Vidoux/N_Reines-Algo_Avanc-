
Frédéric LOPEZ et Tanguy VIDAL
# Résolution du problème des n-Dames

Dans ce projet nous avons développé trois fonctions différentes permettant de résoudre le problème des n-dames.
Ce problème des n-dames consistait à placer, sur un damier de n*n dimensions, n dames sans qu'aucune ne soit menacée par une autre ([selon les règles de déplacement des échecs](http://leconsdechecspourdebutants.com/regles/lecon_2_dame.htm))

## Premier Algorithme :  Approche "naïve

Nous avons, pour cet algorithme, utilisé une approche naïve du problème, c'est-à-dire que nous avons cherché à résoudre le problème sans nous soucier des problématiques de ressources utilisées et de complexité algorithmique. Ce premier algorithme utilise le principe de backtracking. De fait cet algorithme ne permet pas de résoudre le problème dans des temps raisonnables si n>=20 (30s<t<90s environ). Nous nous sommes appuyés sur différents sites pour construire notre logique de backtracking:
* https://interstices.info/le-probleme-des-8-reines/
* https://www.freecodecamp.org/news/lets-backtrack-and-save-some-queens-1f9ef6af5415/

## Deuxième algorithme :  Un algorithme efficace, optimisé

Cet algorithme est plus recherché puisqu'il se veut conçu pour trouver une solution au problème quel que soit le n choisit.
Nous avons effectué nos recherches vers la méthode heuristique dite de moindre conflit.
Cette méthode se base sur une évaluation des conflits sur chaque case pour placer la dame de chaque ligne (ou colonne selon l'approche) sur la case soumise au moins de conflits. La complexité algorithmique moyenne de cet algorithme est bien plus faible que le premier.
Pour développer cet algorithme nous avons utilisé différents sites internet afin de comprendre complètement l'approche de cette méthode et l'appliquer dans notre cas.Nous n'avons cependant pas réussi/eu le temps d'aboutir à un résultat complètement satisfaisant puisque notre algorithme reste bloqué dans une boucle infinie si la configuration ne permet aucune solution (n=3 par exemple). Les principaux sites sur lesquels nous nous sommes appuyés ici sont les suivants:
* https://en.wikipedia.org/wiki/Min-conflicts_algorithm
* https://wikimili.com/en/Min-conflicts_algorithm
* https://medium.com/@carlosgonzalez_39141/using-ai-to-solve-the-n-queens-problem-2a5a9cc5c84c
* https://github.com/naderAsadi/N-Queen/blob/master/min_conflict.py

## Dernier algorithme :  Lister toutes les solutions possibles

Pour cet algorithme nous sommes repartis du premier en l'adaptant de sorte à ne pas s'arrêter à la première solution mais en cherchant jusqu'à la dernière solution. L'adaptation majeure ici consistait au stockage de la solution une fois trouvée puis reprendre l'algorithme en continuant le backtracking, jusqu'à ce que le backtracking soit complètement fini. Ici l'algorithme est donc encore plus gourmand en performances que le premier.

### Notes: Ci dessous un diagramme résumant notre réflexion pour la conceptions des algorithmes 1 et 3.
![schéma](/schema.png)


