# Global Variable
# A global variable is declared outside any function, and it is accessible throughout the program — including inside functions (unless shadowed by a local variable of the same name).

# Local Variable
# A local variable is declared inside a function and is only accessible within that function.

# Modifying Global Variables Inside a Function
# If you want to modify a global variable from inside a function, you must use the global keyword. as shwon below


x = 10


def atta():
    global x
    x = 5
    print("Hello Ji")
    print(x)


atta()
print(x)
