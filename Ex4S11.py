import random
import decimal

# def CreationMatrice():
# 	liste, passage = [], []
# 	for k in range(3):
# 		for i in range(3):
# 			passage.append(float(decimal.Decimal((random.randint(0,100)))/100))
# 		liste += [passage]
# 		passage = []
# 	return liste

# ok = CreationMatrice()

ok = [[0.5,0.4,0.1],[0.2,0.4,0.4],[0.3,0.2,0.5]]
U = [[0.375, 0.625]]
V = [[0.95, 0.05], [0.03, 0.97]]

def eststochastique(p):
    for ligne in range(len(p)):
        somme = 0
        for element in range(len(p[ligne])):
            somme += p[ligne][element]
        if somme != 1:
            print("%s n'est pas une matrice stochastique" % p)
            return False
    print("%s est une matrice stochastique" % p)
    return True

def estbistochastique(p, f):
    for colonne in range(len(p[0])):
        somme = 0
        for element in range(len(p)):
            somme += p[element][colonne]
        if somme != 1:
            print("%s n'est pas une matrice bistochastique" % p)
            return False
    if f == True:
        print("%s est une matrice bistochastique" % p)
        return True
    else:
        print("%s n'est pas une matrice bistochastique" % p)
        return False

def vecteurstable(A, B):
    y = [[float("%.3f"%sum([x*y[j] for (x,y) in zip(a,B)])) for j in range(len(B[0]))] for a in A]
    if y == A:
        print("{} est un vecteur propre stable de {}".format(U, V))
        return True
    else:
        print("{} n'est pas un vecteur propre stable de {}".format(U, V))
        return False

r = estbistochastique(ok, eststochastique(ok))
vecteurstable(U, V)

