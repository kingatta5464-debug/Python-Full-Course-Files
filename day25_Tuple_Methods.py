# we can directly change delete or add any item to a tuple, first we have to convert it into list then we can do changes, after changes we can reconvert it into tuple as shown below

countries = ("Pakistan", "Russia", "China", "America")
temp = list(countries)
temp.append("Itly")  # add item
print(type(temp), temp)
temp.pop(3)  # remove item
print(type(temp), temp)
temp[1] = "Germany"  # change item
print(temp)
countries = tuple(temp)  # Reconvert into tuple
print(type(countries), countries)

countries2 = ("Afghanistan", "Switzer-Land", "Iran")
countries3 = countries + countries2

print(countries3)

# Count Occerence of an item
tup = (1, 2, 1, 1, 1, 11, 2, 22, 3, 2, 22, 3, 3223, 23, 23, 2, 3)
print(tup.count(1))
print(tup.count(2))
# Get Index Of Particular item
print(tup.index(23))
print(
    tup.index(3, 5, 15)
)  # Slicing of tuple then seaching index of the iteration of that number

# Length of tuple

print(len(tup))
