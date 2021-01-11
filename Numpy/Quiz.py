'''
Data Science - Average of Rows

In a matrix, or 2-d array X, the averages (or means) of the elements of rows is called row means.

Task
Given a 2D array, return the rowmeans.

Input Format
First line: two integers separated by spaces, the first indicates the rows of matrix X (n) and the second indicates the columns of X (p)
Next n lines: values of the row in X

Output Format
An numpy 1d array of values rounded to the second decimal.

2 2
1.5 1
2 2.9

Sample Output
[1.25 2.45]
'''

import numpy as np
n, p = [int(x) for x in input().split()]
i = 0
lst = []
while i <= n-1:
    lst += [y for y in input().split()]
    i += 1
lst_arr = np.array(lst).astype(np.double)
lst_arr_n = lst_arr.reshape((n, p))
lst_out = lst_arr_n.mean(axis=1).round(2)
print(lst_out)
