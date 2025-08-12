# MAP
# syntax
# map(function,iterator)
def cube(x):
    return x * x * x


print(cube(3))

l = [2, 3, 4, 5, 6, 7]

# newl = []
# for i in l:
#     newl.append(cube(i))

newl = list(map(cube, l))

print(newl)

# FILTER

# when a function take a function as an input then that function is called high order function

# syntax
# filter(function,iterator)


def filter_object(a):
    return a > 4


newl = list(filter(filter_object, l))
print(newl)


# REDUCE
from functools import reduce

# syntax
# reduce(function,iterator)
# in order to use reduce function we have to import it as above
numbers = [3, 4, 6, 2, 42, 2]


def sum(x, y):
    return x + y


x = reduce(sum, numbers)
print(x)
