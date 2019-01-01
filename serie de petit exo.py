def heureux(n, resultat = 0, intermediaire = 0):
	intermediaire = n
	resultat = 0
	while True:
		for chiffre in list(str(intermediaire)):
			resultat += int(chiffre)**2
		if resultat == 1:
			return "Nombre heureux"
		elif resultat < 10:
			return "Nombre malheureux"
		else:
			intermediaire = resultat
			resultat = 0
			
def distinct(n):
	for chiffre in list(str(n)):
		for indice in range(list(str(n)).index(chiffre)+1, len(list(str(n)))):
			if int(chiffre) == int(list(str(n))[indice]):
				return "Entier non distinct"
	return "Entier distinct"
	
	
def occurrence(n, c = 1, intermediaire = ''):
	for indice in range(len(n)-1):
		if n[indice] == n[indice+1]:
			c += 1
		else:
			intermediaire += str(c) + n[indice]
			c = 1
	intermediaire += str(c) + n[-1]
	return intermediaire
	
def AutoNombre(n):
	for k in range(n):
		a = k
		for h in range(len(str(k))):
			a += int(str(k)[h])
		if a == n:
			return "True : {}".format(k)
	return "False"
	
def prop(n):
	for k in range(1, 6):
		new_n = 0
		for i in range(len(str(n))):
			new_n += int(str(n)[i])**k
		if new_n == n:
			return "Propriété vérifiée pour k = {}".format(k)
	return "Propriété non vérifiée"
	
def nombreP(n):
     for j in range(2, int(sqrt(n))+1):
             if n%j == 0:
                     return 0
     return 1

def circulaire(p, q):
	for k in range(p, q+1):
		if nombreP(k) == True:
			compteur = 0
			ki = k
			for possibilite in range(len(str(k))):
				ron = str(ki)[-1]
				for indice in range(len(str(k))-1):
					ron += str(ki)[indice]
				ki = int(ron)
				if nombreP(ki) == True:
					compteur += 1
				else:
					break
			if compteur == len(str(k)):
				print(k)
	return
 
dic_valeur = {"A" : 1, "E" : 5, "I" : 9, "O" : 15, "U" : 21, "Y" : 25}
def texte(n, valeur = 0):
	for lettre in n.upper():
		if lettre in dic_valeur:
			valeur += dic_valeur[lettre]*(n.upper().index(lettre)+1)
	return valeur
	
def code(n, s = 0):
	intermediaire = n
	while s < 1:
		for chiffre in str(intermediaire):
			s += int(chiffre)
		intermediaire = s
		if s < 9:
			break
		else:
			s = 0
	intermediaire = str(s) + str(n)
	return int(intermediaire)
	
Alphabet ={
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "D" : 4,
    "E" : 5,
    "F" : 6,
    "G" : 7,
    "H" : 8,
    "I" : 9,
    "J" : 10,
    "K" : 11,
    "L" : 12,
    "M" : 13,
    "N" : 14,
    "O" : 15,
    "P" : 16,
    "Q" : 17,
    "R" : 18,
    "S" : 19,
    "T" : 20,
    "U" : 21,
    "V" : 22,
    "W" : 23,
    "X" : 24,
    "Y" : 25,
    "Z" : 0
    }		
	
def cryptage(n, repetition = '', code = ''):
	test = occurrence(n.upper())
	for indice in range(len(test)):
		try:
			if int(test[indice]) in range(1, 10):
				repetition += test[indice]
		except ValueError:
			inter = int(repetition)
			if inter%2 == 0:
				inter /= 2
			else:
				inter *= 2
			code += list(Alphabet.keys())[list(Alphabet.values()).index((inter + Alphabet[test[indice]])%26)]*int(repetition)
			repetition = ''
	return code
	
def cryptographie_ancien(n, code = ''):
	for indice in range(len(n)):
		code += list(Alphabet.keys())[list(Alphabet.values()).index((Alphabet[n.upper()[indice]]+1)%26)]
	return code
	
def ChiffreDeCesar(n, decalage, code = ''):
	for indice in range(len(n)):
		code += list(Alphabet.keys())[list(Alphabet.values()).index((Alphabet[n.upper()[indice]]+decalage)%26)]
	return code
	
Alphabet2 ={
    "A" : "H",
    "B" : "Y",
    "C" : "L",
    "D" : "U",
    "E" : "J",
    "F" : "P",
    "G" : "V",
    "H" : "R",
    "I" : "E",
    "J" : "A",
    "K" : "K",
    "L" : "B",
    "M" : "N",
    "N" : "D",
    "O" : "O",
    "P" : "F",
    "Q" : "S",
    "R" : "Q",
    "S" : "Z",
    "T" : "C",
    "U" : "W",
    "V" : "M",
    "W" : "G",
    "X" : "I",
    "Y" : "T",
    "Z" : "X"
    }
    
def decalage_systematique(n, code = ''):
	for lettre in n:
		code += Alphabet2[lettre.upper()]
	return code
	
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def Vigenere(n, cle, code = '',indice = 0):
	for lettre in n.upper():
		code += alpha[(alpha.find(cle.upper()[indice%len(cle)]) + alpha.find(lettre))%26]
		indice += 1
		if lettre == " ":
			code = code[:-1]
			code += " "
	return code
	
listeM = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
listem = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
listeC = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
def securite(n, pointM = 0, pointm = 0, pointC = 0, cM = 1, cm = 1):
	rappelM, rappelm = [], []
	for indice in range(len(n)):
		if n[indice] in listeM:
			pointM += 1
			try:
				if n[indice+1] in listeM:
					cM += 1
				else:
					rappelM.append(cM)
					cM = 1
			except IndexError:
				pass
		elif n[indice] in listem:
			pointm += 1
			try:
				if n[indice+1] in listem:
					cm += 1
				else:
					rappelm.append(cm)
					cm = 1
			except IndexError:
				pass
		elif n[indice] in listeC:
			pointC += 1
	try:
		score = len(n)*4 + (len(n)-pointM)*2 + (len(n)-pointm)*3 + pointC*5 - (max(rappelm)*2 + max(rappelM)*3)
	except ValueError:
		return "Vous devez avoir dans votre mot de passe au moins une lettre majuscule, une minuscule et un caractères non alphabétiques"
	if score < 20:
		return "Mot de passe : Très faible"
	elif score < 40:
		return "Mot de passe : Faible"
	elif score < 80:
		return "Mot de passe : Fort"
	else:
		return "Mot de passe : Très fort"

def factoriel(n, i = 1):
	for k in range(1, n+1):
		i *= k
	return i		
		
def premier_factoriel(n):
	if nombreP(n) == True:
		for i in range(n+1):
			if factoriel(i) + 1 == n or factoriel(i) - 1 == n:
				return "nombre premier factoriel"
			elif factoriel(i) > n:
				break
		return "nombre premier non factoriel"
	return "Nombre non premier"
	
def TotalnombreP(n):
	liste = []
	for i in range(2, n+1):
		a = 0
		for j in range(2, int(sqrt(i))+1):
			if i%j == 0:
				a = 1
		if a == 0:
			liste.append(i)
	return liste
	
def calcul(n, param, i = 1):
	for j in range(len(TotalnombreP(n)[:param])):
		i *= TotalnombreP(n)[j]
	return i

def premier_primoriel(n):
	if nombreP(n) == True:
		for k in range(n+1):
			if calcul(n, k) + 1 == n or calcul(n, k) - 1 == n:
				return "nombre premier primoriel"
			elif calcul(n, k) > n:
				break
		return "nombre premier non primoriel"
	return "Nombre non premier"
			
def matrix_polybe(n, p = 0):
	for k in range(len(n)):
		if n[k] in n[k+1:] or n[k] in n[:k]:
			return "Mot-Clé sans doublons"
	liste = []
	for k in range(1, len(n)//5 + 2):
		liste.append(list(n.upper()[p:k*5]))
		p = k*5
	for k in range(65, 91):
		compteur = 0
		for j in range(len(liste)):
				if chr(k) not in liste[j]:
					compteur += 1
		if len(liste[-1]) != 5:
			if compteur == len(liste):
				liste[-1].append(chr(k))
		else:
			if compteur == len(liste):
				liste.append([chr(k)])
		if k == 87:
			del liste[-1][-1]
	return liste
	
def Crypter_Polybe(message, motcle, stock = ""):
	a = matrix_polybe(motcle)
	for k in range(len(message)):
		for ligne in range(5):
			for indice in range(5):
				if message.upper()[k] == a[ligne][indice]:
					stock += str(ligne+1) + str(indice+1)
		if message.upper()[k] == "W":
			stock += "oo"
		elif message.upper()[k] == " ":
			stock += "_"
	return stock

def Decrypter_Polybe(message, motcle, stock = "", k = 0):
	a = matrix_polybe(motcle)
	while k < len(message)-1:
		try:
			stock += a[int(message[k])-1][int(message[k+1])-1]
		except ValueError:
			if message[k] == "o":
				stock += "W"
			else:
				stock += " "
				k -= 1
		k += 2
	return stock
	
def robinson(n, u = "0", compteur = 1):
	for k in range(n):
		stock = ""
		for indice in range(len(u)):
			try:
				if u[indice] == u[indice+1]:
					compteur += 1
				else:
					stock += str(compteur) + u[indice]
					compteur = 1
			except IndexError:
				stock += str(compteur) + u[indice]
		u = stock
	return u
	
def autoNombre(n):
	if n < 0:
		return "Nombre positif, s.v.p"
	for k in range(n-1):
		a = 0
		for indice in str(k):
			a += int(indice)
		if n == k + a:
			return "{} n'est pas un auto-nombre : {}".format(n, k)
	return "{} est un auto-nombre".format(n)

def build_matrice(n):
	passage = []
	for ligne in range(5):
		passage.append([row[ligne] for row in n])
	[print(ligne) for ligne in passage]
	return
	
def trier_transposer(n):
	passage = []
	for indice in range(len(n)):
		passage += [sorted(n[indice], reverse=True)]
	n = []
	for ligne in range(5):
		n.append([row[ligne] for row in passage])
	[print(ligne) for ligne in n]
	return
	
import os
import time

def attente(temps):
	for k in range(1, temps+1,1):
		os.system('clear')
		print("[{}] {}%".format("-"*int(k*15/temps), int(k*100/temps)))
		time.sleep(1)

attente(10)
