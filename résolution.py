'''Remplir le tableau'''


class Coordonnées:
	def __init__(self,ligne,colonne):
		self.ligne=ligne
		self.colonne=colonne

'''prend un type Coordonnées et renvoie la case correspondante'''
def get_case(coordonnées, damier):
	return damier[coordonnées.ligne][coordonnées.colonne] 

def set_case_dame(coordonnées, damier):
	damier[coordonnées.ligne][coordonnées.colonne]=1

'''le damier est un tableau de lignes'''
def new_damier(taille):
	tab=[]
	for i in range(0,taille):
		ligne=[]
		for j in range(0,taille):
			ligne.append(0)
		tab.append(ligne)
	return tab


def print_board(taille, damier):
	for i in range(0,taille):
		ligne=""
		for j in range(0,taille):
			ligne += " " + str(damier[i][j])
		print(ligne)

def remplir_damier(damier):
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
	if(placement_autorise(damier, case)):
		set_case_dame(case, damier)
		return True
	return False


'''----------------------------IsEmpty--------------------------'''

'''Vérifie si le positionnement est possible sur la case donnée'''
def placement_autorise(damier, case):
	if(get_case(case, damier)==1):
		print("case occupée")
		return False
	if(not is_diagonnale_empty(damier, case)):
		print("diagonnale occupée")
		return False
	if(not is_ligne_empty(damier, case.ligne)):
		print("ligne occupée")
		return False
	if(not is_colonne_empty(damier, case.colonne)):
		print("colonne occupée")
		return False
	return True


'''return true si la ligne est vide (que des 0)'''
def is_diagonnale_empty(damier, case):
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


'''return true si la ligne est vide (que des 0)'''
def is_ligne_empty(damier, numLigne):
	for i in range(0,len(damier[numLigne])):
		if damier[numLigne][i]==1:
			return False
	return True


'''return true si la colonne est vide (que des 0)'''
def is_colonne_empty(damier, numColonne):
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
print(is_diagonnale_empty(board,case))
print(is_colonne_empty(board,1))
print(is_ligne_empty(board,1))
print(placement_autorise(board,case))
