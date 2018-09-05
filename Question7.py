import functools

lst = [2, 4, 6, 8, 10]
prod = functools.reduce(lambda a, b: a*b, lst)

print('Final Product: ',prod)
