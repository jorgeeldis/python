import random

computer = random.choice(["rock", "paper", "scissors"])

while True:
    player = input("rock, paper, scissors? ")
    print ("computer: " + computer)
    if player == "rock":
        if computer == "paper":
            print("you lose")
        elif computer == "rock":
            print("you tied")
        else:
            print("you won")
    elif player == "paper":
        if computer == "paper":
            print("you tied")
        elif computer == "rock":
            print("you won")
        else:
            print("you lose")
    elif player == "scissors":
        if computer == "paper":
            print("you won")
        elif computer == "rock":
            print("you lose")
        else:
            print("you tied")
    else:
        print("No one wins. Please check your spelling again. Something is wrong!")
    computer = random.choice(["rock", "paper", "scissors"])
