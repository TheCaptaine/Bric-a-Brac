import collections
tour = 1
vainqueur = 0
game = True

dic = {"a" : 0, "b" : 1, "c" : 2}
liste = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
         
def winner(tableau):
    global vainqueur
    for indice in range(len(tableau)):
        for key in range(1, 3):
            if collections.Counter(tableau[indice])[key] == 3:
                vainqueur = key
                return vainqueur
    return vainqueur

def colonne(tableau):
    panelC = []
    colonne, colonne2, colonne3 = [], [], []
    for x in range(3):
        colonne.append(tableau[x][0])
        colonne2.append(tableau[x][1])
        colonne3.append(tableau[x][2])
    panelC.append(colonne)
    panelC.append(colonne2)
    panelC.append(colonne3)
    return panelC
	
def diagonale(tableau):
    panelD = []
    diagonale, diagonale2 = [], []
    for i in range(3):
        if i == 1:
            diagonale.append(tableau[i][i])
            diagonale2.append(tableau[i][i])
        elif i == 2:
            diagonale.append(tableau[2][i])
            diagonale2.append(tableau[0][i])
        else:
            diagonale.append(tableau[0][i])
            diagonale2.append(tableau[2][i])
    panelD.append(diagonale)
    panelD.append(diagonale2)
    return panelD
	
while game:
    enter = list(input("\n< Where do you want play ? "))
    try:
        if tour%2 == 0 and liste[dic[enter[1]]][dic[enter[0]]] == 0:
            liste[dic[enter[1]]][dic[enter[0]]] = 2
        elif tour%2 == 1 and liste[dic[enter[1]]][dic[enter[0]]] == 0:
            liste[dic[enter[1]]][dic[enter[0]]] = 1
        else:
            print("/!\ You can't play here /!\ ")
            tour -= 1
    except KeyError:
        print("Choose a valid action\n")
        tour -= 1
    except IndexError:
        print("Choose a valid action\n")
        tour -= 1
    if winner(liste) != 0 or winner(colonne(liste)) != 0 or winner(diagonale(liste)) != 0 or tour == 9:
        if tour == 9 and vainqueur == 0:
            print("Draw...")
        else:
            print("End the winner is the Player {}".format(vainqueur))
        game = False
    else:
        tour += 1
    for k in range(3):
        print(liste[k])
        
