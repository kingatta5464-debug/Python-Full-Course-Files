# Operator Overloading is a feature in Python that allows developers to redefine the behavior of mathematical and comparison operators for custom data types. This means that you can use the standard mathematical operators (+, -, *, /, etc.) and comparison operators (>, <, ==, etc.) in your own classes, just as you would for built-in data types like int, float, and str.

# Why do we need operator overloading?
# Operator overloading allows you to create more readable and intuitive code. For instance, consider a custom class that represents a point in 2D space. You could define a method called 'add' to add two points together, but using the + operator makes the code more concise and readable:


class vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(cls, v):
        return vector(cls.i + v.i, cls.j + v.j, cls.k + v.k)


v1 = vector(2, 5, 8)
v2 = vector(4, 6, 2)
print(v1)
print(v2)
print(type(v1 + v2))
