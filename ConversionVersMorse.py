app = True
traduction = []

def PassageMorse():
        Nombre_espace = 0
        for word in passage:
                if word == "A":
                        traduction.append(".-")
                elif word == "B":
                        traduction.append("-...")
                elif word == "C":
                        traduction.append("-.-.")
                elif word == "D":
                        traduction.append("-..")
                elif word == "E":
                        traduction.append(".")
                elif word == "F":
                        traduction.append("..-.")
                elif word == "G":
                        traduction.append("--.")
                elif word == "H":
                        traduction.append("....")
                elif word == "I":
                        traduction.append("..")
                elif word == "J":
                        traduction.append(".---")
                elif word == "K":
                        traduction.append("-.-")
                elif word == "L":
                        traduction.append(".-..")
                elif word == "M":
                        traduction.append("--")
                elif word == "N":
                        traduction.append("-.")
                elif word == "O":
                        traduction.append("---")
                elif word == "P":
                        traduction.append(".--.")
                elif word == "Q":
                        traduction.append("--.-")
                elif word == "R":
                        traduction.append(".-.")
                elif word == "S":
                        traduction.append("...")
                elif word == "T":
                        traduction.append("-")
                elif word == "U":
                        traduction.append("..-")
                elif word == "V":
                        traduction.append("...-")
                elif word == "W":
                        traduction.append(".--")
                elif word == "X":
                        traduction.append("-..-")
                elif word == "Y":
                        traduction.append("-.--")
                elif word == "Z":
                        traduction.append("--..")
                elif word ==" ":
                        Nombre_espace += 1
                else:
                        print("ERROR")
                        return 
        
        print(Nombre_espace)
        return TraductionMorse()

def TraductionMorse():
        for word in traduction:
                print(word, end = "")
        return reinitialisation()

def reinitialisation():
        compte = len(traduction)
        for i in range(compte):
                for word in traduction:
                        traduction.remove(word)
        return 
        
while app:
    print("\n\n  Attention ecrire en MAJUSCULE et ecrire les chiffres en LETTRE\n\
ecrire quit pour quitter le programme")
    enter = str(input("< Message à traduire en Morse "))
    if enter != "quit":
        passage = list(enter)
        PassageMorse()
    else:
        app = False

print("END")


        
