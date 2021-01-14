#input 2
#      1.2 0 0.5 -1
#output [[1.2 0.]
#        [0.5 -1.]]


import numpy as np

r = int(input())

lst = [float(x) for x in input().split()]

arr = np.array(lst)

newarr = arr.reshape(r, -1)

print(newarr)
