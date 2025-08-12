# A lambda function is a shortcut or a one-line function in Python.

# Instead of writing a full function using def, you can write a small, simple function in just one line using lambda.


def double(x):
    return x * 2


print(double(5))

# OR


def appl(fx, value):
    return fx(value)


double = lambda x: x * 2
cube = lambda x: x * x * x
average = lambda x, y, z: (x + y + z) / 3
print(double(5))
print(cube(5))
print(average(5, 10, 15))
print(appl(cube, 3))


# When the function is very short/simple

# When you only need it once or for a short task

# Used with functions like map(), filter(), and sorted()
