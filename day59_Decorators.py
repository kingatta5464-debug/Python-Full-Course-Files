# A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a "decorated" function. The basic syntax for using a decorator is the following:

# @decorator_function
# def my_function():
#     pass


def greet(fx):
    def mfx(*args, **kwargs):
        print("Welcome")
        fx(*args, **kwargs)
        print("Thanks You For Using This Function")

    return mfx


@greet
def hello():
    print("Hello World")


@greet
def summ(a, b):
    print(a + b)


hello()
summ(2, 2)
