from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from math import sqrt

e = 1.6e-19
c = 3e8
m = 9.1e-31

def g(x, a, b):
	return a*x+b
	
popt, autre = curve_fit(g, [1/300e-9, 1/400e-9], [1.85, 0.82])

print('a = {} V.m et b = {} V\n'.format(popt[0], popt[1]))

''' Question 1 '''
h = popt[0]*e/c
print('question 1 : Nous avons constante de planck h = %s J.s\n' %h)

''' Question 2 '''
W = -popt[1]*e
print("question 2 : Le travail d'extraction du sodium est W = %s J\n" %W)

''' Question 3 '''
Y = h*c/W*10**9
print("question 3 : la longueur d'onde seuil pour le sodium est %s nm\n" %Y)

''' Question 4 '''
print('question 4 : Pour 200nm nous avons %s V\n' %g(1/200e-9, popt[0], popt[1]))

''' Question 5 '''
P = 0.01
r = 10**-16
Im = r*P*e*300e-9/(h*c)
print("question 5 : Le courant produit pour un faisceau lumineux de longueur d'onde\n de 300 nm avec une puissance de 10 mW est Im = %s A\n" %Im)

''' Question 6 '''
Ec = h*c/300e-9-W
v = sqrt(2*Ec/m)
print("question 6 : Ec = {} J et v = {} m/s\n".format(Ec, v))

plt.plot([1/200e-9, 1/300e-9, 1/400e-9], [g(1/200e-9, popt[0], popt[1]), 1.85, 0.82], "r.")
plt.show()