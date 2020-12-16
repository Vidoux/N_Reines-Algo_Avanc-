'''Remplir le tableau'''
from Coordonnées import *
from Damier import *



def get_case(coordonnées, damier):
	"""[description]
	
	Arguments:
		coordonnées {Coordonnées} -- emplacement de la case à retourner
		damier {Array} -- damier dans lequel prendre la valeur
	
	Returns:
		[Integer] -- 1=dame ou 0=vide
	"""
	return damier[coordonnées.ligne][coordonnées.colonne] 

def set_case_dame(coordonnées, damier):
	"""[summary]
	Met une dame dans la case du damier
	[description]
	
	Arguments:
		coordonnées {[Coordonnées]} -- emplacement de la case à retourner
		damier {Array} -- damier dans lequel prendre la valeur
	"""
	damier[coordonnées.ligne][coordonnées.colonne]=1
	
def new_damier(taille):
	"""[summary]
	le damier est un tableau de lignes

	[description]
		
	Arguments:
		taille {Integer} -- taille du damier à générer
	
	Returns:
		[Array] -- Damier(2 dimentions)
	"""
	tab=[]
	for i in range(0,taille):
		ligne=[]
		for j in range(0,taille):
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
	for i in range(0,taille):
		ligne=""
		for j in range(0,taille):
			ligne += " " + str(damier[i][j])
		print(ligne)

def remplir_damier(damier):
	"""[summary]
	Plcer toutes les dames dans le damier
	Les dames ne doivent pas se menacer(règles des échecs)
	[description]
	
	Arguments:
		damier {[Array]} -- damier à compléter
	"""
	nb_dames_placées = 0
	while(nb_dames_placées < len(damier)):
		damierTmp=new_damier(len(damier))
		for i in range(0,len(damier)):
			dame_place=False
			# j correspond à la colonne
			j=0
			# On essaye de placer la dame sur toutes les cases de la ligne
			while(not dame_place and j<len(damier)):
				case = Coordonnées(i,j)
				dame_place=placer_dame(damierTmp,case)
				j+=1

def placer_dame(damier, case):
	"""[summary]
	Place une dame si l'emplacement spécifier est possible
	[description]
	
	Arguments:
		damier {Array} -- Damier concerné
		case {Coordonnée} -- Emplacement souhaité
	
	Returns:
		bool -- vrai si la dame a été placée, faux sinon
	"""
	if(placement_autorise(damier, case)):
		set_case_dame(case, damier)
		return True
	return False

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
	if(get_case(case, damier)==1):
		print("case occupée")
		return False
	if(not are_diagonnales_empty(damier, case)):
		print("diagonnale occupée")
		return False
	if(not is_ligne_empty(damier, case.ligne)):
		print("ligne occupée")
		return False
	if(not is_colonne_empty(damier, case.colonne)):
		print("colonne occupée")
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
	diag1= Coordonnées(case.ligne-1, case.colonne-1)

	'''partie haute de la diagonale 1'''
	while(diag1.ligne >= 0 and diag1.colonne >= 0):
		if(get_case(diag1, damier)==1):
			return False
		diag1.ligne-=1
		diag1.colonne-=1

	'''Partie basse de diag1'''
	diag1=Coordonnées(case.ligne+1, case.colonne+1)
	while(diag1.ligne <len(damier) and diag1.colonne<len(damier)):
		if(get_case(diag1, damier)==1):
			return False
		diag1.ligne+=1
		diag1.colonne+=1

	diag2= Coordonnées(case.ligne-1, case.colonne+1)

	'''partie haute de la diagonale 2'''
	while(diag2.ligne>=0 and diag2.colonne<len(damier)):
		if(get_case(diag2, damier)==1):
			return False
		diag2.ligne-=1
		diag2.colonne+=1

	'''Partie basse de diag2'''
	diag1=Coordonnées(case.ligne+1, case.colonne-1)
	while(diag1.ligne<len(damier) and diag1.colonne>=0):
		if(get_case(diag1, damier)==1):
			return False
		diag1.ligne+=1
		diag1.colonne-=1

	return True

def is_ligne_empty(damier, numLigne):
	"""[summary]
	Vérification d'une ligne
	[description]
	
	Arguments:
		damier {Array} -- Damier concerné
		numLigne {Integer} -- numéro de la ligne à vérifier
	
	Returns:
		bool -- Vrai si la ligne est vide
	"""
	for i in range(0,len(damier[numLigne])):
		if damier[numLigne][i]==1:
			return False
	return True

def is_colonne_empty(damier, numColonne):
	"""[summary]
	Vérifie si la colonne est vide
	[description]
	
	Arguments:
		damier {Array} -- Damier concerné
		numColonne {Integer} -- numéro de la colonne à vérifier
	
	Returns:
		bool -- Vrai si la colonne est vide
	"""
	for i in range(0,len(damier)):
		if damier[i][numColonne]==1:
			return False
	return True	
'''----------------------------//IsEmpty--------------------------'''

			
a=new_damier(4);
print(is_ligne_empty(a,2))
print_board(4, new_damier(4))

board = [[0, 0, 0, 0],
        [0, 1, 1, 0],
	    [0, 0, 0, 0],
	    [0, 0, 0, 0]]

case = Coordonnées(1,1)
print(are_diagonnales_empty(board,case))
print(is_colonne_empty(board,1))
print(is_ligne_empty(board,1))
print(placement_autorise(board,case))
