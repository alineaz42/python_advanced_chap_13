from functools import reduce
l = [1, 2, 3, 4, 5, 6, 45, 68, 50, 79, 100]

a = reduce(max, l)
print(a)
