# Default Arguments
def average(a=2, b=4):
    print("The Average is : ", (a + b) / 2)


average()
average(8)


def name(f, m="Ul", l="Mustafa"):
    print("My name is ", f, m, l)


name("Atta", "U", "Rehman")
name("Atta")


# Keyword Arguments
def name(f, m="Ul", l="Mustafa"):
    print("My name is ", f, m, l)


name(l="Mustafa", f="Atta", m="Ul")
name(
    l="Rehman", f="Atta", m="Ur"
)  # if we specify arguments when we call function then position does not matter, it will show perfect output
name(
    "Rehman", "Atta", "Ur"
)  # if didnt specify then output will be according to arguments we have passed


# Required Arguments


# The type of arguments that we have had to pass in every case otherwise function will through error, like in the below example a is a required argument, we have to pass it in every function call
def average(a, b=4):
    print("The Average is : ", (a + b) / 2)


average(110)

# Arbitrary Arguments


def ave(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is : ", sum / len(numbers))


ave(4, 6)
ave(4, 6, 8)
ave(4, 6, 44, 26)
ave(4, 6, 11, 35, 66)

# Return Statement


def average(a, b=4):
    return (a + b) / 2


c = average(10, 12)
print(c)
