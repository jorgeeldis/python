for number in range(1, 101):
    if number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("buzz") 
    elif number % 3 & number % 5:
        print("fizzbuzz")
    else:
        print(number)

# ! Follow us and give us a like!
