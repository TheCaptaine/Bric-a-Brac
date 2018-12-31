#coding:utf-8
import random

liste = []

def PileOuFace():
	n = random.randint(1, 10)
	if n%2 == 0:
		return "1024"
	else:
		return "0"

def lister(passage = ""):
	for k in range(len(n)):
		try:
			if n[k] == "0":
				if n[k+1] == "2":
					passage += n[k]
				else:
					liste.append(n[k])
			else:
				passage += n[k]

			if passage == "1024":
				liste.append(passage)
				passage = ""
		except IndexError:
			liste.append(n[k])
	return

with open("texte", "w") as files:
	files.write("")

with open("texte", "a") as files:
	for k in range(random.randint(1, 100)):
		donnee = PileOuFace()
		files.write(donnee)

with open("texte", "r") as files:
	n = files.readlines()[0]

lister()
print(liste)
