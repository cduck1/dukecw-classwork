from random import randint; options = ["Win", "Loss", "Draw", "Win", "Loss"]; print(options[(int(input("Enter 0 for rock, 1 for paper or 2 for scissors")) - randint(0,2)) + 2])
