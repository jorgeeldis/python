#Day 2 of 100 days of code!
#by Jorge Eldis, Founder of Stoa Community
#We begin importing a plot library for our graph
import matplotlib.pyplot as plt 
import matplotlib.patheffects as path_effects

#A brief introduction about what this program does
print("Welcome to answers generator!")
print("It consist that you input 2 numbers and we give you different operations and answers between these 2")

#Asking for the 2 variables
var1 = float(input("Please enter your first number: "))
var2 = float(input("Please enter your second number: "))

#Operations 
op1 = var1+var2
op2 = var1-var2
op3 = var1*var2
op4 = var1/var2
op5 = var1%var2
op6 = pow(var1, var2)

#Showing the results
print("We are showing you now the sum, substraction, multiplication, division, remainder of the division & the power between var1 and var2!")
print("Sum (var1 + var2) :", op1)
print("Substraction (var1 - var2) :", op2)
print("Multiplication (var1 * var2) :", op3)
print("Division (var1 / var2) :", op4)
print("Remainder of the division (var1 % var2) :", op5)
print("The power of var1 to the var2 is: ", op6)
input("Press Enter to continue...")

#A condition for checking who is bigger
print("Now let's check who is bigger: ")
if var1 > var2:
    print("var1 is bigger: ", var1)
elif var1 == var2:
    print("var1 is the same number as var2: ", var1)
else:
    print("var2 is bigger: ", var2)
input("Press Enter to continue...")

#Making a graph with our results
print("We're gonna show you know a graph taking all the values of our operations as y-axis and x-axis would be progressive from 0. ")  
print("The power operation won´t be in the graph!")

#x axis values 
x = [1,2,3,4,5] 

#y axis values 
y = [op1,op2,op3,op4,op5] 

#Showing a little message
fig = plt.figure(figsize=(5, 1.5))
text = fig.text(0.5, 0.5, 'Dont forget to follow us!\n@stoacommunity\nOn every social media!', ha='center', va='center', size=20)
text.set_path_effects([path_effects.Normal()])
plt.show()
  
#plotting the points  
plt.plot(x, y, color="black") 
  
#naming the x axis 
plt.xlabel('x - axis') 
#naming the y axis 
plt.ylabel('y - axis') 
  
#giving a title to my graph 
plt.title('Graph with results!!') 
  
#function to show the plot 
plt.show()