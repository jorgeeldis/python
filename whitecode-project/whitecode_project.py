import winsound
import random
import webbrowser
import os
import time
import urllib.request
import urllib.parse
import re

print("Ok let´s begin: ")

name = input("Please enter your name: ")
print("Hi " + name + " my name is WhiteCode")

while True:
    
    try:
        age = int(input("How old are you? "))

        if age <= 18:
            print("Oh so you are still a kid!")
            break
        elif age >= 18:
            print("You are very old haha im just kidding")
            break

    except Exception as e:
        print(e)
        frequency = 3000  # Set Frequency To 2500 Hertz
        duration = 1000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)

        frequency = 1000  # Set Frequency To 2500 Hertz
        duration = 1000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)

        frequency = 5000  # Set Frequency To 2500 Hertz
        duration = 1000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
        print("This is not a whole number.")
        break

while True:
    frequency = int(input("Give me frequency higher than 5000hz: "))
    duration = int(input("Give me duration higher than 1000: "))
    winsound.Beep(frequency, duration)
    print("========================================")
    break


print("Now let´s play a game")

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
        frequency = 1000  # Set Frequency To 2500 Hertz
        duration = 1000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
        print("No one wins. Please check your spelling again. Something is wrong!")
    computer = random.choice(["rock", "paper", "scissors"])
    break

print("Here is my website!")

while True:
    website = input("Do you want to see it? Please write yes or no: ")
    if website == "yes":
        print("Look at it")
        webbrowser.open("https://stoacommunity.tech")
        time.sleep(5)
        opinion = input("How does it look? Make sure to subscribe for better content! Press any key! ")
        webbrowser.open("https://stoacommunity.tech/subscribe.html/")
        break
    elif website == "no":
        print("Oh ok, maybe next time")
        break
    else:
        frequency = 1000  # Set Frequency To 2500 Hertz
        duration = 1000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
        print("Im sorry, but you didn´t specify yes or no.")
        break

sci = input("Now who is your favorite scientist? ")
print("Wow " + sci + " was one of the greatest minds in history! Mine was Nikola Tesla! ")

music = input("What kind of music do you like? ")
print(music + " is an amazing genre.")

song = print("Lets see whats you favorite song? ")
query_string = urllib.parse.urlencode({"search_query" : input()})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())

url_to_open = "http://www.youtube.com/watch?v=" + search_results[0]

webbrowser.open(url_to_open)

print("I have found the song for you!\nHere it is: " "http://www.youtube.com/watch?v=" + search_results[0])


print("Goodbye!")

time.sleep(5)

input("Please press enter to finish the dialogue")