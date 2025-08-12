def square(n):
    """take input n, returns the square of n"""  # this is a docstring
    # we have to write docstring just below the function name or just above the function body
    return n**2


x = square(5)
print(x)
print(square.__doc__)


def square(n):
    x = n
    """take input n, returns the square of n"""  # this will not be considered as docstring
    return n**2


x = square(5)
print(x)
print(square.__doc__)  # output will be none
