import random
jeu = True
sentence1 = "Computer choice is {}, Player win one mark"
sentence2 = "Computer choice is {}, Computer win one mark"
lib1 = {"scissors" : 1, "paper" : 2, "rock" : 3}
lib2 = { lib1[k]:k for k in lib1}
mark_player = 0
mark_computer = 0
tour = 3

print("Rock Paper Scissors".center(50, "-"), "\n\n")

def Game(tour = 3, mark_player = 0, mark_computer = 0):
    while tour != 0:
        player = input("\n< scissors, paper or rock ? ")
        computer = int(random.randint(1, 3))
        try:
            if lib1[player] > computer:
                if lib1[player] == 3 and computer == 1:
                    print(sentence1.format(lib2[computer]))
                    mark_player += 1
                else:
                    print(sentence2.format(lib2[computer]))
                    mark_computer += 1
            elif computer > lib1[player]:
                if computer == 3 and lib1[player] == 1:
                    print(sentence2.format(lib2[computer]))
                    mark_computer += 1
                else:
                    print(sentence1.format(lib2[computer]))
                    mark_player += 1
            else:
                print("Same wave")
                tour += 1
            tour -= 1
        except KeyError:
            print("Choose a valid action")
            tour += 1

    print("\nscore : Player => {}\n\
        Computer => {}".format(mark_player, mark_computer))
    if mark_player > mark_computer:
        print("Player WIN\n")
        return 
    else:
        print("Computer WIN\n")
        return 

while jeu:
    enter = input("< Do you want play ? yes/no\n")
    if enter == "yes":
        Game()
    elif enter == "no":
        print("END")
        jeu = False
    else:
        print("Choose a valid action")
