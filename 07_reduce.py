

from functools import reduce
def sum(a, b): return a*b


l = [5, 1, 2, 4, 5, 4]

val = reduce(sum, l)
print(val)
