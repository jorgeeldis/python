#Day 3 of 100 days of code!
#by Jorge Eldis, Founder of Stoa Community
# Import the modules
import sys
import os
import random

# Ask the question and we get a random answer!
question = input("Ask the magic 8 ball a question: (press enter to quit) ")
answers = random.randint(1,8)

#Conditions where the we compare if you asked a question, and the random module select an answer.
if question == "":
        sys.exit()
elif question.find('?') == -1:
        print("That is not a question! A question needs a ?")
    
elif answers == 1:
        print ("It is certain")

elif answers == 2:
        print ("Outlook good")
    
elif answers == 3:
        print ("You may rely on it")
    
elif answers == 4:
        print ("Ask again later")
    
elif answers == 5:
        print ("Concentrate!!")
    
elif answers == 6:
        print ("Reply hazy")

elif answers == 7:
        print ("My reply is no")

elif answers == 8:
        print ("My sources say no")
input("Press ENTER to continue: ")
os.system('CLS')

#Guessing a number in your mind
print ("let´s play a game, if i guess your number from 1 to 100, i win!")
print ("Ready?")
input ("Press ENTER to continue: ")
os.system('CLS')

#Randomize a number between 1 and 100 
print ("it´s your number... ",random.randint(1,101),"???")

#Conditions if i win or lose
while True:
    condition = input ("YES or NO: ")
    if condition == "YES":
        print("HAHA i win!! now follow @stoacommunity on every social media :)")
    elif condition == "NO":
        print("Oh :( next time i´ll get it :)")
    else:
        condition == "You have to answer YES or NO"
    break
input("Press ENTER to continue: ")
os.system('CLS')

#Last game: Rock, Paper, Scissors!
print ("let´s play a game of rock paper scissors!")
print ("Ready?")
input ("Press ENTER to continue: ")
os.system('CLS')
computer = random.choice(["rock", "paper", "scissors"])

#While loop for the game
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
    break

#Thanks for playing the lucky game!