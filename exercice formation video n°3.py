import random


CreationPNJ = "Choix des noms"
DebutCombat = "Début du combats"
finCombat = "Fin du combat"
commentaire_combat = "{} attaque\nIl inflige {} point de degat\n"
fail = "{} Rate sa cible\n"
win = "{} gagne\n"

class pnj:
    def __init__(self, nom, pv = 250):
        self.nom = nom
        self.pv = pv
    

""" Première partie """
    
print(CreationPNJ.center(50, "-"), "\n\n")

Nom = input("< choisissez le nom du joueur 1\n")
Joueur1 = pnj(Nom)

Nom = input("< choisissez le nom du joueur 2\n")
Joueur2 = pnj(Nom)


""" Deuxième partie """

print(DebutCombat.center(50, "-"), "\n\n")

for k in range(1, 5):
    tentative = bool(random.randint(0, 1))
    if tentative == True and k%2 == 1:
        degat = random.randint(0, 100)
        print(commentaire_combat.format(Joueur1.nom, degat))
        Joueur2.pv = Joueur2.pv - degat
    
    elif tentative == True and k%2 == 0:
        degat = random.randint(0, 100)
        print(commentaire_combat.format(Joueur2.nom, degat))
        Joueur1.pv = Joueur1.pv - degat
        
    else:
        if k%2 == 1:
            print(fail.format(Joueur1.nom))
        else:
            print(fail.format(Joueur2.nom))

print("Point de vie restant:\n{} à {}\n{} à {}\n".format(Joueur1.nom, Joueur1.pv, Joueur2.nom, Joueur2.pv))


""" Troisième partie """

print(finCombat.center(50, "-"), "\n\nQui est le vainqueur??\n")

if Joueur1.pv == Joueur2.pv:
    print("Egalité")
elif Joueur1.pv > Joueur2.pv:
    print(win.format(Joueur1.nom))
else:
    print(win.format(Joueur2.nom))
    
    
print("FIN".center(50, "-"), "\n\n")
