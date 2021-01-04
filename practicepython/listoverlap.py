a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

in_a = set(a)
in_b = set(b)

c = list(in_b - in_a)

result = a + list(c)

print(result)