from random import randint

playerchoice = input("Enter r (rock), p (paper) or s (scissors)")
computerchoice = randint(0,2)
#0 is rock, 1 is paper, 2 is scissors
if computerchoice == 0 and playerchoice == "r":
    print("Rock. Draw.")
#endif
if computerchoice == 0 and playerchoice == "p":
    print("Rock. I win.")
#endif
if computerchoice == 0 and playerchoice == "s":
    print("Rock. You win.-")
#endif
#if computer gets paper
if computerchoice == 1 and playerchoice == "r":
    print("Paper. I win.")
#endif
if computerchoice == 1 and playerchoice == "p":
    print("Paper. Draw.")
#endif
if computerchoice == 1 and playerchoice == "s":
    print("Paper. You win.")
#endif
#if computer gets scissors
if computerchoice == 2 and playerchoice == "r":
    print("Scissors. You win.")
#endif
if computerchoice == 2 and playerchoice == "p":
    print("Scissors. I win.")
#endif
if computerchoice == 2 and playerchoice == "s":
    print("Scissors. Draw.")
#endif
