import os

terrain, Game = [], True
for k in range(7):
	passage =[]
	for i in range(7):
		if k is 0 or i is 6:
			if k is not 6:
				passage.append('O')
			else:
				passage.append('X')
		elif i is 0 or k is 6:
			passage.append('X')
		else:
			passage.append(" ")
	terrain += [passage]

def deplacement(ligne, colonne, symbole):
	terrain[ligne][colonne] = symbole
	return 

def suppr(ligne, colonne):
	terrain[ligne][colonne] = " "
	return

def verification1(ligne, colonne):
	if ligne < 0 or colonne < 0:
		os.system('clear')
		print("Please enter positive number")
		return False
	try:
		if terrain[ligne][colonne] is " ":
			os.system('clear')
			print("Error, ({}, {}) is empty".format(ligne, colonne))
			return False
		symbole = terrain[ligne][colonne]
		return symbole
	except IndexError:
		os.system('clear')
		print("Out of range")
		return False

def verification2(lgne, clnne, ligne, colonne, symbole):
	try:
		if terrain[ligne][colonne] is " ":
			if (ligne, colonne) in [(lgne, clnne-1), (lgne, clnne+1), (lgne-1, clnne), (lgne+1, clnne)]:
				deplacement(ligne, colonne, symbole)
				suppr(lgne, clnne)
				return
			else:
				print("Impossible movement")
				return
	except IndexError:
		print("Out of range")
		return
	print("Error, ({}, {}) is not empty".format(ligne, colonne))
	return

while Game:
	for k in range(7):
		print("  %s  "%k, end = "")
	print('')
	for k in range(7):
		print(terrain[k], " %s"%k)
	try:
		enter11 = int(input("\n< Choose the table ligne of symbol do you want move "))
		enter12 = int(input("< Choose the table column of symbol do you want move "))
		objet = verification1(enter11, enter12)
		if objet is not False:
			print("\nWhere do you want move this object ?")
			enter21 = int(input("< Choose the table ligne "))
			enter22 = int(input("< Choose the table column "))
			os.system('clear')
			if enter21 >= 0 and enter22 >= 0:
				verification2(enter11, enter12, enter21, enter22, objet)
			else:
				print("Please enter positive number")
	except ValueError:
		os.system('clear')
		print("Please enter integer")