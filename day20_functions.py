def gmeanCalculator(a, b):
    mean = (a * b) / (a + b)
    print(mean)


def isGreater(a, b):
    if a > b:
        print("First Number Is Greater.")
    else:
        print("Second Number Is Greater or Equal.")


a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
gmeanCalculator(a, b)
isGreater(a, b)


def isLesser(a, b):
    pass  # it means i will write the body of this function later just pass it
