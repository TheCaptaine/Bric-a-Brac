import os

""" Règle du jeu """

print("Vous disposez d'une grille de 100 cases (10*10) que vous devez remplir avec un nombre par case de 1 à 100\n", "mais vous avez deux contraintes de déplacement :\n",
	"Si vous vous déplacez en vertical ou en horizontal vous devez toujours sauter 2 cases\n", 
	"Et si vous vous déplacez en diagonale, vous devez toujours sauter 1 case.\n")

print("Exemple de déplacement possible :\n") 
print("-----".join(" "*(5)), "\n", end = '')
print("     ".join("|"*(5)))
print("  1--", "-----".join(" "*(3)), "->2  ")
print("     ".join("|"*(5)))
print("-----".join(" "*(5)), "\n")

input("< Appuier sur entrer pour commencer le jeu. ")

""" Jeux """

chiffre, arene, passage, Game = 0, [], [], True
for i in range(10):
	for k in range(10):
		passage.append(' ')
	arene += [passage]
	passage = []

def draw():
	for k in range(10):
		print("   {}  ".format(k), end = '')
	print('')
	for k in range(10):
		print("-----".join(" "*(11)), "\n|", end = '')
		j = ''
		for e in arene[k]:
			if len(e) < 2:
				j += '  {}  |'.format(e)
			else:
				j += ' {}  |'.format(e)
		print(j + "  {}".format(k))
	print("-----".join(" "*(11)))
	return

def deplacement(ligne, colonne):
	global chiffre
	arene[ligne][colonne] = str(chiffre)
	chiffre += 1
	return

def verification1(ligne, colonne):
	global chiffre
	for l in range(len(arene)):
		for c in range(len(arene)):
			if arene[l][c] == str(chiffre - 1):
				lgne = l
				clnne = c
	if (ligne, colonne) in [(lgne,clnne-3), (lgne,clnne+3), (lgne-2,clnne-2), 
	(lgne-2,clnne+2), (lgne+2,clnne-2), (lgne+2,clnne+2),(lgne-3,clnne), (lgne+3,clnne)]:
		try:
			if arene[ligne][colonne] != " ":
				print("\nDeplacement impossible\n")
				return False
			else:
				return deplacement(ligne, colonne)
		except IndexError:
			print("\nDeplacement impossible car vous sortez du tableau\n")
			return False

	print("\nDeplacement impossible\n")
	return False

def verification2(ligne, colonne, chance=0):
	global chiffre
	for k in [(ligne-2, colonne-2), (ligne-2, colonne+2), (ligne+2, colonne-2), (ligne+2, colonne+2),
(ligne, colonne-3), (ligne, colonne+3), (ligne-3, colonne), (ligne+3, colonne)]:
		try:
			if arene[k[0]][k[1]] == " " and k[0] >= 0 and k[1] >= 0:
				print('{}, {}'.format(k[0], k[1]))
				chance += 1
		except IndexError:
			print("IndexError : {}, {}".format(k[0], k[1]))
	if chance > 0:
		return
	else:
		print('Vous avez réussie à placer {} nombres'.format(chiffre))
		return False
		
deplacement(0, 0)

while Game:
	draw()
	try:
		enter1 = int(input("\n< Quelle ligne voulez vous jouer ? "))
		enter2 = int(input("< Quelle colonne voulez vous jouer ? "))
		os.system('clear')
		if enter1 >= 0 and enter2 >= 0:
			if verification1(enter1, enter2) is not False:
				if verification2(enter1, enter2) is False:
					draw()
					Game = False
		else:
			print("\n/!{} Nombre positif requis\n".format(chr(92)))
	except ValueError:
		os.system('clear')
		print("\nVeuillez choisir des nombres entiers compris entre [0, 9]")
