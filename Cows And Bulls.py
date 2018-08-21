import random

def game(Try = 1):
	Nombre_a_deviner = list(str(int(random.randint(0, 9999))))
	print("Cows And Bulls".center(50, "-"), "\n\n")
	while True:
		cow, bull = 0, 0
		enter = list(input("< enter a {}-digit number ".format(len(Nombre_a_deviner))))
		if enter == Nombre_a_deviner:
			return "Gradulation !! You tried {} time".format(Try)
		else:
			try:
				for indice in range(len(Nombre_a_deviner)):
					if enter[indice] is Nombre_a_deviner[indice]:
						cow += 1
				for key in collections.Counter(enter):
					if key in collections.Counter(Nombre_a_deviner):
						if collections.Counter(Nombre_a_deviner)[key] < collections.Counter(enter)[key]:
							bull += collections.Counter(Nombre_a_deviner)[key]
						else:
							bull += collections.Counter(enter)[key]
			except IndexError:
				print("Respect instructions")
				Try -= 1
			bull -= cow
			Try += 1
		print("{} cow(s), {} bull(s)\n".format(cow, bull))
