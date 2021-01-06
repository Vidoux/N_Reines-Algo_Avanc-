class Damier:

    def __init__(self, taille):
        self.taille = taille
        self.grille = self.__new_grille()

    def supprimer_dame(self, coordonnées):
        self.grille[coordonnées.ligne][coordonnées.colonne] = 0

    def set_case_dame(self, coordonnées):
        self.grille[coordonnées.ligne][coordonnées.colonne] = 1

    def get_case(self, coordonnées):
        return self.grille[coordonnées.ligne][coordonnées.colonne]

    def toString(self):
        string = ""
        for i in range(0, self.taille):
            ligne = ""
            for j in range(0, self.taille):
                ligne += " " + str(self.grille[i][j])
            string += ligne
            if i < self.taille - 1:
                string += "\n"
        return string

    def get_taille(self):
        return self.taille

    def set_grille_spécifique(self, grille):
        self.grille = grille

    # PRIVATE functions
    def __new_grille(self):
        tab = []
        for i in range(0, self.taille):
            ligne = []
            for j in range(0, self.taille):
                ligne.append(0)
            tab.append(ligne)
        return tab
