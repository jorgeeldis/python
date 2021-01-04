#Question 2: Given a range of first 10 numbers, Iterate from start number to the end number 
#and print the sum of the current number and previous number
#pynative.com

print("Printing current and previous number sum in a given range(10)")
print("Current number:  0 previous number:  0 sum:  0")
for i in range(1, 10):
    print("current number: ", i, "previous number: ", i-1, "sum: ", (i-1)+i)