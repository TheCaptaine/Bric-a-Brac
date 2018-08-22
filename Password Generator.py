import random

def password():
	liste = []
	n = input("< password weak or strong ? ")
	if n == "weak":
		a = int(random.randint(8, 12))
		for k in range(a):
			if k == 0:
				liste.append(chr(int(random.randint(65, 90))))
			elif k == a-1:
				liste.append(chr(int(random.randint(48, 57))))
			else:
				liste.append(chr(int(random.randint(97, 122))))
		
			random.shuffle(liste)
		return "".join(liste)
	elif n == "strong":
		for k in range(20):
			if k < 5:
				liste.append(chr(int(random.randint(65, 90))))
			elif k < 10:
				liste.append(chr(int(random.randint(48, 57))))
			elif k < 15:
				liste.append(chr(int(random.randint(97, 122))))
			else:
				alea = int(random.randint(0, 4))
				if alea is 0:
					liste.append(chr(int(random.randint(33, 47))))
				elif alea is 1:
					liste.append(chr(int(random.randint(58, 64))))
				elif alea is 2:
					liste.append(chr(int(random.randint(91, 96))))
				else:
					liste.append(chr(int(random.randint(123, 126))))
		random.shuffle(liste)
		return "".join(liste)
	else:
		return "parameter not found"
