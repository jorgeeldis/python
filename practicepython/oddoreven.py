# Ask the user for a number.
# Depending on whether the number is even or odd,
# print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?

ask = input("Please give me a number: ")

if int(ask) % 2 == 0:
    print("Your number is even.")
else:
    print("Yout number is odd.")
