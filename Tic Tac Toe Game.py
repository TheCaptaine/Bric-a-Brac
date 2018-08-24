import collections
tour, vainqueur, game = 1, 0, True

dic2 = {"0" : "   ", "1" : " X ", "2": " O "}
dic = {"a" : 0, "b" : 1, "c" : 2}                                 # a    b    c       
liste = [[0, 0, 0],        #  =====>                           # a  aa   ba   ca
         [0, 0, 0],        #  =====>                           # b  ab   bb   cb
         [0, 0, 0]]        #  =====>                           # c  ac   bc   cc
         
def draw(tableau):
    for k in range(3):
        print("---".join(" "*(4)), "\n|", end = '')
        print('|'.join(dic2[str(e)] for e in liste[k]), '|')
    print("---".join(" "*(4)))
    return

def winner(tableau):
    global vainqueur
    for indice in range(len(tableau)):
        for key in range(1, 3):
            if collections.Counter(tableau[indice])[key] == 3:
                vainqueur = key
                return vainqueur
    return vainqueur

def colonne(tableau):
    colonne, colonne2, colonne3, panelC = [], [], [], []
    for x in range(3):
        colonne.append(tableau[x][0])
        colonne2.append(tableau[x][1])
        colonne3.append(tableau[x][2])
    panelC.append(colonne)
    panelC.append(colonne2)
    panelC.append(colonne3)
    return panelC
	
def diagonale(tableau):
    diagonale, diagonale2, panelD = [], [], []
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
    draw(liste)                                               #                                ^^^
    enter = list(input("\n< Where do you want play ? "))      # enter the coordinates ( see up ||| )
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
    
