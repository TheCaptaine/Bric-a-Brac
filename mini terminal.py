import time

print("Terminal Beta OS".center(50, "-"), "\n\n")

nom = "Défaut"
terminal = True

while terminal:
    entree = input("[{}] ".format(nom))
    if entree == "run":
        for i in range(5):
            print(".", end="")
            time.sleep(1)
    elif entree == "name":
       new_entree = input("Sudo [{}] : New name ".format(nom))
       nom = new_entree
    elif entree == "help":
        print("- run  : Post five point\n\
        - name : Change the name of terminal\n\
        - help : Show all command and their description\n\
        - quit : Quit the terminal")
    elif entree == "quit":
        terminal = False
    else:
        print("ERROR : Command was not found")
        
print("End".center(50, "-"), "\n\n")
