# a for loop can have an optional else block. This else block is executed only if the loop completes without encountering a break.

for i in range(5):
    print(i)
    if i == 4:
        break
else:
    print(
        "Else Condition Executed"
    )  # in this example else condition will not be executed


numbers = [1, 3, 5, 7]

for num in numbers:
    if num % 2 == 0:
        print("Even number found:", num)
        break
else:
    print("No even number found.")

# Useful for search-like operations, where you're looping to find something, and want to run code if it wasn’t found.
