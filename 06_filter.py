def greater_than(x):
    if x > 5:
        return True
    else:
        return False


def g(num): return num > 10


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 548, 25, 4, 8, 4]
print(list(filter(greater_than, l)))
print(list(filter(g, l)))
