import random
from Coordonnées import Coordonnées
from Damier import Damier


def solve_n_queen_big(taille, damier):
    """[summary]
    Résoudre le problème des n dames pour n'importe quelle valeure de n
    [description]

    Arguments:
        taille {Integer} -- taille du damier à résoudre
        damier {Damier} -- damier à résoudre

    Returns:
        {Damier} -- Damier contenant une solution
        {Boolean} -- True si le problème a été résolu
    """

    lignes = []  # Stocke le placement de la dame sur chaque ligne du damier
    candidats = []  # Stocke les condidats possibles pour
    # un déplacement de dame

    # placement initial des dames
    initialisation_damier(taille, lignes, candidats)
    damier = dames_to_damier(lignes, damier.get_taille())

    # résoudre le damier
    nbr_mvt = placer_dames(lignes, damier, candidats)
    print(nbr_mvt)
    damier = dames_to_damier(lignes, damier.get_taille())
    # print(damier.toString())
    # print(lignes)
    return damier, True


def initialisation_damier(taille, lignes, candidats):
    """[summary]
    Placement initial des dames
    [description]

    Arguments:
        taille {Integer} -- Taille du damier
        lignes {Array} -- emplacement des dames pour chaque ligne
        candidats {Array} -- condidats possibles pour un déplacement de dame
    """

    # Placement d'une dame par colonne
    for col in range(taille):
        # conflit minimum repéré, 8 par défaut
        min_conflit = 8
        # réinitialisation des candidats
        candidats = []
        # recherche des meilleurs cases pour placer la dame
        lignes.append(0)
        for row in range(len(lignes)):
            nbr_conflits = check_conflits(lignes[row], col, lignes)
            if nbr_conflits == min_conflit:
                candidats.append(row)
            elif nbr_conflits < min_conflit:
                candidats = [row]
                min_conflit = nbr_conflits
        # Sélection d'un candidat aléatoire pour placer la dame
        lignes[col] = random.choice(candidats)


def check_conflits(row, col, lignes):
    """[summary]
    Evalue et retourne le nombre de conflicts sur une case donnée
    [description]

    Arguments:
        row {Integer} -- ligne concernée
        col {Integer} -- colonne concernée
        lignes {Array} -- emplacement des dames pour chaque ligne

    Returns:
        {Integer} -- nombre de conflicts
    """

    conflit_count = 0
    for val in range(len(lignes)):
        # La case courante n'est pas vérifiée
        if val != col:
            ligne_suivante = lignes[val]
            # si il y a une menace alors on incrémente le nombre de menaces
            if ligne_suivante == row or\
                    abs(ligne_suivante - row) == abs(val - col):
                conflit_count += 1

    return conflit_count


def dames_to_damier(lignes, damier_taille):
    """[summary]
    Transfère les emplacement des dames sur chaque lignes vers le damier
    complet
    [description]

    Arguments:
        lignes {Array} -- emplacement des dames pour chaque ligne
        damier_taille {Integer} -- taille du damier

    Returns:
        [Damier] --Damier rempli avec les dames
    """

    # Supressions des anciens placements
    damier_new = Damier(damier_taille)
    # Placement des dames sur le damier vide

    for i in range(len(lignes)):
        case = Coordonnées(i, lignes[i])
        damier_new.set_case_dame(case)

    return damier_new


def placer_dames(lignes, damier, candidats):
    """[summary]
    Cherche à placer toutes les dames de sorte à arriver à
    une solution au problème des n dames.
    [description]

    Arguments:
        lignes {Array} -- emplacement des dames pour chaque ligne
        damier {Damier} -- damier à modifier
        candidats {Array} -- tableau de stockage des candidats
                            possible pour chaque déplacement

    Returns:
        {Integer} -- Nombre de mouvements effectués avant
        de trouver une solution
    """

    nbr_mouvements = 0
    while True:
        nbr_conflits = 0
        candidats = []

        # Vérification du nombre de conflicts sur le damier
        # Si il n'y a pas de conflicts alors la solution est trouvée,
        # Sinon on modifie le placement des dames
        for val in range(len(lignes)):
            nbr_conflits += check_conflits(lignes[val], val, lignes)
        if nbr_conflits == 0:
            return nbr_mouvements

        # On déplace une dame au hasard sur un meilleur
        # emplacement (si possible)
        random_queen = random.randint(0, len(lignes) - 1)
        deplacer_reine(random_queen, lignes, candidats)
        nbr_mouvements += 1

    damier = dames_to_damier(lignes, damier.get_taille())


def deplacer_reine(queen_col, lignes, candidats):
    """[summary]
    Recherche le meilleur placement possible d'une dame sur sa ligne et
    déplace la dame sur ce meilleur emplacement
    (ne déplace pas la dame si aucun meilleurs placement n'est possible)
    [description]

    Arguments:
        queen_col {Integer} -- colonne concernée par le déplacement
        lignes {Array} -- emplacement des dames pour chaque ligne
        candidats {Array} -- stocke les meilleurs emplacement pour la dame
    """

    candidats = []

    # conflit minimu constaté sur la ligne (8 par défaut)
    min_conflit = 8
    # cherche la ligne pour laquelle le conflit est minimum
    for val in range(len(lignes)):
        val_conflit = check_conflits(val, queen_col, lignes)
        if val_conflit == min_conflit:
            candidats.append(val)
        else:
            if val_conflit < min_conflit:
                candidats = []
                min_conflit = val_conflit
                candidats.append(val)
    # Si il existe un (ou plusieurs) meilleur emplacement pour la dame
    # alors on déplace celle ci sur l'un de ces emplacements
    if candidats:
        lignes[queen_col] = random.choice(candidats)


# -----Tests------
damier = Damier(8)
board, solved = solve_n_queen_big(8, damier)
print(board.toString())
