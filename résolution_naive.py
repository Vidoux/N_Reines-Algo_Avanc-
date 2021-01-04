'''Remplir le tableau'''
from Coordonnées import *
from Damier import *


# --------------------Fonctions utilitaires-------------------------------

def can_t_attack(taille, damier):
    """[summary]
    
    [description]
    
    Arguments:
        taille {[type]} -- [description]
        damier {[type]} -- [description]
    """
    can_not_attack = True
    for i in range(0, taille):
        for j in range(0, taille):
            case = Coordonnées(i, j)
            if damier.get_case(case) == 1:
                # La dame est trouvée sur la ligne, on vérifie que la position
                # n'est pas menacée puis on passe à la ligne suivante si celle 
                # ci est validée.
                j = taille + 1
                can_not_attack = placement_autorise(damier, case)
                if not can_not_attack:
                    return False

    return can_not_attack


def is_soluce(taille, damier):
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
    placer_dames(damier, 0)
    is_solved, tmp = is_soluce(board_size, damier)
    return damier, is_solved

# ------------------//Fonctions utilitaires--------------------------------


def new_damier(taille):
    """[summary]
    le damier est un tableau de lignes

    [description]
        
    Arguments:
        taille {Integer} -- taille du damier à générer
    
    Returns:
        [Array] -- Damier(2 dimentions)
    """
    tab = []
    for i in range(0, taille):
        ligne = []
        for j in range(0, taille):
            ligne.append(0)
        tab.append(ligne)
    return tab


def print_board(taille, damier):
    """[summary]
    Affichage du Damier
    [description]
    
    Arguments:
        taille {Integer} -- taille du damier à afficher
        damier {Array} -- damier à afficher
    """
    print(damier.toString())


def placer_dames(damier, num_colonne):
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
            if placer_dames(damier, num_colonne + 1) == True:
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
        damier {Array} -- Damier concerné
        case {Coordonnée} -- Emplacement souhaité
    """

    damier.set_case_dame(case)


'''----------------------------IsEmpty--------------------------'''


def placement_autorise(damier, case):
    """[summary]
    Vérifie si le positionnement est possible sur la case donnée'''
    [description]
    
    Arguments:
        damier {Array} -- Damier concerné
        case {Coordonnées} -- Emplacement souhaité
    
    Returns:
        bool -- Vrai si la dame peut être placé sur cette case
    """
    # if(damier.get_case(case)==1):
    #     #print("case occupée")
    #     return False
    if (not are_diagonnales_empty(damier, case)):
        # print("diagonnale occupée")
        return False
    if (not is_ligne_empty(damier, case)):
        # print("ligne occupée")
        return False
    if (not is_colonne_empty(damier, case)):
        # print("colonne occupée")
        return False
    return True


def are_diagonnales_empty(damier, case):
    """[summary]
    Vérifie si les diagonales partants du point sont vides
    [description]
    
    Arguments:
        damier {Array} -- Damier concerné
        case {Coordonnées} -- Emplacement souhaité
    
    Returns:
        bool -- Vrai si les diagonnales sont vide(que des 0)
    """
    diag1 = Coordonnées(case.ligne - 1, case.colonne - 1)

    '''partie haute de la diagonale 1'''
    while (diag1.ligne >= 0 and diag1.colonne >= 0):
        if (damier.get_case(diag1) == 1):
            return False
        diag1.ligne -= 1
        diag1.colonne -= 1

    '''Partie basse de diag1'''
    diag1 = Coordonnées(case.ligne + 1, case.colonne + 1)
    while (diag1.ligne < damier.get_taille() and diag1.colonne < damier.get_taille()):
        if (damier.get_case(diag1) == 1):
            return False
        diag1.ligne += 1
        diag1.colonne += 1

    diag2 = Coordonnées(case.ligne - 1, case.colonne + 1)

    '''partie haute de la diagonale 2'''
    while (diag2.ligne >= 0 and diag2.colonne < damier.get_taille()):
        if (damier.get_case(diag2) == 1):
            return False
        diag2.ligne -= 1
        diag2.colonne += 1

    '''Partie basse de diag2'''
    diag1 = Coordonnées(case.ligne + 1, case.colonne - 1)
    while (diag1.ligne < damier.get_taille() and diag1.colonne >= 0):
        if (damier.get_case(diag1) == 1):
            return False
        diag1.ligne += 1
        diag1.colonne -= 1

    return True


def is_ligne_empty(damier, case):
    """[summary]
    Vérification d'une ligne
    [description]
    
    Arguments:
        damier {Array} -- Damier concerné
        numLigne {Integer} -- numéro de la ligne à vérifier
    
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
        numColonne {Integer} -- numéro de la colonne à vérifier
    
    Returns:
        bool -- Vrai si la colonne est vide
    """
    for i in range(0, damier.get_taille()):
        case_tmp = Coordonnées(i, case.colonne)
        if damier.get_case(case_tmp) == 1 and not (case_tmp.ligne == case.ligne):
            return False
    return True


'''----------------------------//IsEmpty--------------------------'''

'''-----------------function for test_nqueen.py -----------------------'''

# a=Damier(4);
# print(is_ligne_empty(a,2))
# print(a.toString())


# board = [[0, 0, 0, 0],
#         [0, 1, 1, 0],
#         [0, 0, 0, 0],
#         [0, 0, 0, 0]]

# case = Coordonnées(1,1)
# print(are_diagonnales_empty(a,case))
# print(is_colonne_empty(a,1))
# print(is_ligne_empty(a,1))
# print(placement_autorise(a,case))

damiertest = Damier(8)
print(placer_dames(damiertest, 0))
print(damiertest.toString())

print(can_t_attack(8, damiertest))
