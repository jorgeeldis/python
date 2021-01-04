# 100 Days Of Code - Day 1!
# Created by Jorge Eldis - Founder of Stoa Community
# Create a program that asks the user to enter their name and their age. 
# Print out a message to them that tells them the year that they will turn 100 years old.

name = input("Hi, please enter your name: ")
age = int(input("Hi, please enter your age: "))

birth = 2020 - age
 
year = birth + 100

print("Hi", name, "my calculations tells me that you're gonna be 100 in", year)


