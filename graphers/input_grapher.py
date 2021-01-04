# importing the required module 
import matplotlib.pyplot as plt 

print("Welcome to the grapher!")
  

# creating an empty list 
x = [] 
  
# number of elemetns as input 
n = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, n): 
    el = int(input()) 
  
    x.append(el) # adding the element 

# creating an empty list 
y = [] 
  
# number of elemetns as input 
m = int(input("Enter number of elements : ")) 
  
# iterating till the range 
for i in range(0, m): 
    ele = int(input()) 
  
    y.append(ele) # adding the element 


# x axis values 
# x = [1,2,3] 
# corresponding y axis values 
# y = [2,4,1] 
  
# plotting the points  
plt.plot(x, y) 
  
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
  
# giving a title to my graph 
plt.title('My first graph!') 
  
# function to show the plot 
plt.show() 