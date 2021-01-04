#Question 1: Given a two integer numbers return their product and  
#if the product is greater than 1000, then return their sum
#pynative.com

var1 = input ("Please enter a number: ")
var2 = input ("Please enter another number: ")

product = int(var1)  * int(var2)
sum1 = int(var1)  + int(var2)

if product > 1000:
    print("The sum of this 2 numbers is: ", sum1) 
else:
    print("The product of this 2 numbers is: ", product)

