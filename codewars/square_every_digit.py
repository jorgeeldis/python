number = input("Please enter your number: ")
sum = ''

for digits in str(number):

    result = int(digits)**2
    sum = str(sum) + str(result)

print(int(sum))
