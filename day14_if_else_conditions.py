a = int(input("Enter your age: "))
print("my age is : ", a)

# Conditional Operators
# <,>,<=,>=,==,!=

print(a > 18)
print(a < 18)
print(a >= 18)
print(a <= 18)
print(a != 18)
if a >= 19:
    print("You Can Drive")
else:
    print("You Can Not Drive")

budget = 100
applePrice = 90

if budget > applePrice:
    print("Buy 1kg Alexa.")
else:
    print("Out Of Budget")


# elif condition

num = int(input("Enter The Number : "))

if num > 0:
    print("Number Is Positive")
    if num <= 10:
        print("Number Is Between 1-10")
    elif num <= 20:
        print("Number Is Between 10-20")
    else:
        print("Number Is Greater Than 20")
elif num < 0:
    print("Number Is Negative")
else:
    print("Number Is Zero")
