import random

word = "EVAPORATE"
tour, barre, inconnue = 1, 0, list("_"*len(word))
    
print("_ "*len(word))
while True:
    enter = input("< Choose a letter ").upper()
    if len(enter) == 1:
        if enter in word:
            for letter in range(len(word)):
                if enter == word[letter]:
                    inconnue[letter] = enter
        else:
            barre += 1
            print("/!\ Not in word : {} /!\ ".format(barre*"| "))
        print("\n", " ".join(inconnue))
        if inconnue == list(word):
                print("You won :)\
                    Try : {}".format(tour))
                break
        elif barre == 6:
            print("You lose :(\
            The word was {}".format(word))
            break
        else:
            tour += 1
    else:
        print("Choose one letter..")
    



