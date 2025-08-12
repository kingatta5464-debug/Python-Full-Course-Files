# The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to a variable within an expression. This can be useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation.

# The Walrus Operator is represented by the := syntax and can be used in a variety of contexts including while loops and if statements.

# Here's an example of how you can use the Walrus Operator in a while loop:


n = True
print(n)

x = True
# print(x=False)#this will through error
# with warlus operator we can do this easily no error will come
# for example

print(x := False)

l = [1, 2, 3, 4, 5, 6]

while n := len(l) > 0:
    print(l.pop())

# WITHOUT WARLUS OPERATOR

# foods = []
# while True:
#     food = input("what is your favort food?")
#     if food == "quit":
#         break
#     foods.append(food)

# WITH WARLUS OPERATOR

foods = []
while food := input("Your favort food?\n") != "quit":
    foods.append(food)
