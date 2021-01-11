# integersums.py
""" Sum of Integers Up To n
    Write a function, add_it_up(), that takes a single integer as input
    and returns the sum of the integers from zero to the input parameter.

    The function should return 0 if a non-integer is passed in.
"""

def add_it_up(n):

    sum = 0

    try:
        val = int(n)
    except ValueError:
        print("0")

    for i in range(0, int (n)+1):
        sum = sum + i
    print(sum)

n = input("Please enter a number: ")
if isinstance(n, (int)):
    add_it_up(n)
else:
    print("not int")
