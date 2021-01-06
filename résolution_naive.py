import copy
from Damier import *
from Coordonnées import *


# --------------------Fonctions utilitaires-------------------------------

def can_t_attack(taille, damier):
    """[summary]
    Indique si aucune des dame sur le plateau ne peut s'attaquer
    [description]

    Arguments:
        taille {Integer} -- taille du damier
        damier {Damier} -- damier à vérifier

    Returns:
        bool -- True si aucune dame n'est menacée par une autre dame
    """

    can_not_attack = True
    for i in range(0, taille):
        for j in range(0, taille):
            case = Coordonnées(i, j)
            if damier.get_case(case) == 1:
                # La dame est trouvée sur la ligne, on vérifie que la position
                # n'est pas menacée puis on passe à la ligne suivante si celle
                # ci est validée.
                can_not_attack = placement_autorise(damier, case)
                if not can_not_attack:
                    return False

    return can_not_attack


def is_soluce(taille, damier):
    """[summary]
    détermine si le damier envoyé est une solution ou non
    [description]
    
    Arguments:
        taille {Integer} -- taille du Damier(requis pour passer les tests mais non-utilisé)
        damier {Damier} -- Damier à vérifier
    
    Returns:
        [Boolean] -- true si le damier est une solution
    """

    nb_dames = 0
    is_the_soluce = True
    for i in range(0, taille):
        for j in range(0, taille):
            case = Coordonnées(i, j)
            # print(damier.get_case(case))
            if damier.get_case(case) == 1:
                nb_dames += 1
                is_the_soluce = is_the_soluce and placement_autorise(damier, case)
    is_the_soluce = is_the_soluce and nb_dames == taille
    return is_the_soluce, nb_dames


def solve_n_queen_small(board_size, damier):
    """[summary]
    Résoudre le problème des n-dames jusqu'à n=20 
    [description]
    
    Arguments:
        board_size {Integer} -- Taille du damier(requis pour les tests)
        damier {Damier} -- Damier à traiter    
    Returns:
        [Damier] -- Damier solution
        [bool] -- True si une solution a été trouvée
    """
    placer_dames(damier, 0)
    is_solved, tmp = is_soluce(board_size, damier)
    return damier, is_solved


# ------------------//Fonctions utilitaires--------------------------------

def print_board(taille, damier):
    """[summary]
    Affichage du Damier
    [description]

    Arguments:
        taille {Integer} -- taille du damier à afficher (requis pour les tests)
        damier {Array} -- damier à afficher
    """
    print(damier.toString())


def placer_dames(damier, num_colonne):
    """[summary]
    Placer toutes les dames sur un damier donné
    [description]
    
    Arguments:
        damier {Damier} -- Damier sur lequel placer les dames
        num_colonne {Integer} -- Numéro de la colonne où com-
        mencer le placement
    
    Returns:
        bool -- true si une bonne configuration a été trouvée
    """

    # Si la colonnes est supérieur au nombre de colonnes,
    # alors toutes les dames sont placées, problème résolu!
    if num_colonne >= damier.get_taille():
        return True

    for i in range(damier.get_taille()):
        case = Coordonnées(i, num_colonne)
        # print("colonne:")
        # print(case.colonne)
        # print(case.ligne)
        if placement_autorise(damier, case):
            placer_dame(damier, case)

            # placement des autres dames
            if placer_dames(damier, num_colonne + 1):
                return True

            # Le placement de la dame à cet emplacement ne permet
            # pas de placer toutes les autres dames
            # On essaie alors l'emplacement suivant
            damier.supprimer_dame(case)

    # la configuration actuelle ne permet pas de placer cette dame
    # retour en arrière dans le placement (back)
    return False


def placer_dame(damier, case):
    """[summary]
    Place une dame
    [description]

    Arguments:
        damier {Damier} -- Damier concerné
        case {Coordonnée} -- Emplacement souhaité
    """

    damier.set_case_dame(case)


'''----------------------------IsEmpty--------------------------'''


def placement_autorise(damier, case):
    """[summary]
    Vérifie si le positionnement est possible sur la case donnée'''
    [description]

    Arguments:
        damier {Damier} -- Damier concerné
        case {Coordonnées} -- Emplacement souhaité

    Returns:
        bool -- Vrai si la dame peut être placé sur cette case
    """

    if not are_diagonnales_empty(damier, case):
        # print("diagonnale occupée")
        return False
    if not is_ligne_empty(damier, case):
        # print("ligne occupée")
        return False
    if not is_colonne_empty(damier, case):
        # print("colonne occupée")
        return False
    return True


def are_diagonnales_empty(damier, case):
    """[summary]
    Vérifie si les diagonales partants du point sont vides
    [description]

    Arguments:
        damier {Damier} -- Damier concerné
        case {Coordonnées} -- Emplacement souhaité

    Returns:
        bool -- Vrai si les diagonnales sont vide(que des 0)
    """
    diag1 = Coordonnées(case.ligne - 1, case.colonne - 1)

    # partie haute de la diagonale 1
    while diag1.ligne >= 0 and diag1.colonne >= 0:
        if damier.get_case(diag1) == 1:
            return False
        diag1.ligne -= 1
        diag1.colonne -= 1

    # Partie basse de diag1
    diag1 = Coordonnées(case.ligne + 1, case.colonne + 1)
    while diag1.ligne < damier.get_taille() and diag1.colonne < damier.get_taille():
        if damier.get_case(diag1) == 1:
            return False
        diag1.ligne += 1
        diag1.colonne += 1

    diag2 = Coordonnées(case.ligne - 1, case.colonne + 1)

    # partie haute de la diagonale 2
    while diag2.ligne >= 0 and diag2.colonne < damier.get_taille():
        if damier.get_case(diag2) == 1:
            return False
        diag2.ligne -= 1
        diag2.colonne += 1

    # Partie basse de diag2
    diag1 = Coordonnées(case.ligne + 1, case.colonne - 1)
    while diag1.ligne < damier.get_taille() and diag1.colonne >= 0:
        if damier.get_case(diag1) == 1:
            return False
        diag1.ligne += 1
        diag1.colonne -= 1

    return True


def is_ligne_empty(damier, case):
    """[summary]
    Vérification d'une ligne
    [description]

    Arguments:
        damier {Damier} -- Damier concerné
        case {Coordonnées} -- case du damier concernée

    Returns:
        bool -- Vrai si la ligne est vide
    """
    for i in range(0, damier.get_taille()):
        case_tmp = Coordonnées(case.ligne, i)
        if damier.get_case(case_tmp) == 1 and not (case_tmp.colonne == case.colonne):
            return False
    return True


def is_colonne_empty(damier, case):
    """[summary]
    Vérifie si la colonne est vide
    [description]

    Arguments:
        damier {Array} -- Damier concerné
        case {Coordonnées} -- case du damier concernée

    Returns:
        bool -- Vrai si la colonne est vide
    """
    for i in range(0, damier.get_taille()):
        case_tmp = Coordonnées(i, case.colonne)
        if damier.get_case(case_tmp) == 1 and not (case_tmp.ligne == case.ligne):
            return False
    return True


'''----------------------------//IsEmpty--------------------------'''

'''----------------------------Trouver Toutes les solutions----------------'''


def placer_dames_toutes_configs(damier, num_colonne, tab_stockage_solutions):
    """[summary]
    Trouves toutes les solutions possibles au problème des n-dames pour un damier donné
    [description]
    
    Arguments:
        damier {Damier} -- Damier à traiter
        num_colonne {Integer} -- Numéro de la colonne où commencer le traitement
        tab_stockage_solutions {Array} -- Tableau de stockage de toutes les solutions
    """

    # Si la colonnes est supérieur au nombre de colonnes,
    # alors toutes les dames sont placées, problème résolu!
    if num_colonne >= damier.get_taille():
        damier_tmp = copy.deepcopy(damier)  # fait une copie complétement indépendante du damier
        # pour la stocker dans les solutions
        tab_stockage_solutions.append(damier_tmp)
        return

    for i in range(damier.get_taille()):
        case = Coordonnées(i, num_colonne)
        # print("colonne:")
        # print(case.colonne)
        # print(case.ligne)
        if placement_autorise(damier, case):
            placer_dame(damier, case)
            placer_dames_toutes_configs(damier, num_colonne + 1, tab_stockage_solutions)
            # Le placement de la dame à cet emplacement ne permet
            # pas de placer toutes les autres dames
            # On essaie alors l'emplacement suivant
            damier.supprimer_dame(case)


def solve_n_queen_all_soluce(taille, damier):
    """[summary]
    Trouve toutes les solutions et renvoie les solutions dans un tableau
    [description]
    
    Arguments:
        taille {Integer} -- taille du damier, requis pour les tests
        damier {Damier} -- Damier à traiter
    
    Returns:
        Array -- Tableau contenant toutes les solutions
    """

    tab_solutions = []
    placer_dames_toutes_configs(damier, 0, tab_solutions)
    return tab_solutions


'''--------------------------//Trouver toutes les solutions----------------'''


'''-----------------testing functions-----------------------'''
N = 6
damiertestl = Damier(N)
tab = solve_n_queen_all_soluce(N, damiertestl)
print(len(tab))
