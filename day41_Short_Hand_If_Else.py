# We use shorthand if...else (ternary operator) in Python when we want to make our code shorter, cleaner, and more readable — especially for simple conditions and value assignments.


a = 9
b = 10
print("a") if (a > b) else print("b") if (b > a) else print("Both Are Equal")

c = 9 if (a > b) else 0
print(c)

# Dont use short hand if else When the logic is complex (e.g., multiple conditions or multiple statements)
# or When it hurts readability
