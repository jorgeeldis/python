import time
import sys
import winsound
import os
import turtle 


print("Hi! I guess today is your birthday? Am i right? :)")
answer = input("Y/N: ")
os.system('CLS')

if answer == "Y":
	print("Happy Birthday, i hope you have an amazing day, im gonna give you some gifts!!!")
else:
	print("Oh i'm sorry")

name = input("So what is your name?: ")

winsound.Beep(264, 250)
sys.stdout.write('Ha')	
time.sleep(500/2000.0)
sys.stdout.write('ppy ')
winsound.Beep(264, 250)
time.sleep(250/2000.0)
sys.stdout.write('birth')
winsound.Beep(297, 1000)
time.sleep(250/2000.0)
sys.stdout.write('day ')
winsound.Beep(264, 1000)
time.sleep(250/2000.0)
sys.stdout.write('to ')
winsound.Beep(352, 1000)
time.sleep(250/2000.0)
print('you')
winsound.Beep(330, 2000)
time.sleep(500/2000.0)

sys.stdout.write('Ha')
winsound.Beep(264, 250)
time.sleep(500/2000.0)
sys.stdout.write('ppy ')
winsound.Beep(264, 250)
time.sleep(250/2000.0)
sys.stdout.write('birth')
winsound.Beep(297, 1000)
time.sleep(250/2000.0)
sys.stdout.write('day ')
winsound.Beep(264, 1000)
time.sleep(250/2000.0)
sys.stdout.write('to ')
winsound.Beep(396, 1000)
time.sleep(250/2000.0)
print('you')
winsound.Beep(352, 2000)
time.sleep(500/2000.0)

sys.stdout.write('Ha')
winsound.Beep(264, 250)
time.sleep(250/2000.0)
sys.stdout.write('ppy ')
winsound.Beep(264, 500)
time.sleep(250/1000.0)
sys.stdout.write('birth')
winsound.Beep(440, 1000)
time.sleep(250/2000.0)
sys.stdout.write('day ')
winsound.Beep(352, 1000)
time.sleep(250/2000.0)
sys.stdout.write('dear ')
winsound.Beep(330, 1000)
print(name)
time.sleep(250/2000.0)
winsound.Beep(297, 1000)

winsound.Beep(440, 1000)
time.sleep(250/2000.0)

time.sleep(500/2000.0)
sys.stdout.write('Ha')
winsound.Beep(466, 250)
time.sleep(500/2000.0)
sys.stdout.write('ppy ')
winsound.Beep(466, 250)
time.sleep(250/2000.0)
sys.stdout.write('birth')
winsound.Beep(440, 1000)
time.sleep(250/2000.0)
sys.stdout.write('day ')
winsound.Beep(352, 1000)
time.sleep(250/2000.0)
sys.stdout.write('to ')
winsound.Beep(396, 1000)
time.sleep(250/2000.0)
print('you')
winsound.Beep(352, 2000)
time.sleep(250/2000.0)

print ('HAPPY BIRTHDAY ' + name + ' <3 !!!')

print ("  --------------------------------------------------------------------------------------------------------")

print ("  | |  | |    /\    |  __ \ |  __ \ \ \   / / |  _ \|_   _||  __ \|__   __|| |  | ||  __ \    /\ \ \   / /")

print ("  | |__| |   /  \   | |__) || |__) | \ \_/ /  | |_) | | |  | |__) |  | |   | |__| || |  | |  /  \ \ \_/ /  ")

print ("  |  __  |  / /\ \  |  ___/ |  ___/   \   /   |  _ <  | |  |  _  /   | |   |  __  || |  | | / /\ \ \   /  ")

print ("  | |  | | / ____ \ | |     | |        | |    | |_) |_| |_ | | \ \   | |   | |  | || |__| |/ ____ \ | |   ")

print ("  |_|  |_|/_/    \_\|_|     |_|        |_|    |____/|_____||_|  \_\  |_|   |_|  |_||_____//_/    \_\|_|   ")

#Speed of drawing
turtle.speed(9)

# Creating a turtle object(pen) 
pen = turtle.Turtle() 

# Defining a method to draw curve 
def curve(): 
	for i in range(200): 

		# Defining step by step curve motion 
		pen.right(1) 
		pen.forward(1) 

# Defining method to draw a full heart 
def heart(): 

	# Set the fill color to red 
	pen.fillcolor('red') 

	# Start filling the color 
	pen.begin_fill() 

	# Draw the left line 
	pen.left(140) 
	pen.forward(113) 

	# Draw the left curve 
	curve() 
	pen.left(120) 

	# Draw the right curve 
	curve() 

	# Draw the right line 
	pen.forward(112) 

	# Ending the filling of the color 
	pen.end_fill() 

# Defining method to write text 
def txt(): 

	# Move turtle to air 
	pen.up() 

	# Move turtle to a given position 
	pen.setpos(-68, 95) 

	# Move the turtle to the ground 
	pen.down() 

	# Set the text color to lightgreen 
	pen.color('white') 

	# Write the specified text in 
	# specified font style and size 
	pen.write("Happy Birthday!", font=( 
	"Verdana", 12, "bold")) 

# Draw a heart 
heart() 

# Write text 
txt() 

# To hide turtle 
pen.ht() 

# Having the window to stay
turtle.exitonclick()