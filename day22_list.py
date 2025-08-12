marks = [
    33,
    43,
    64,
    "Atta",
    True,
    9.3,
    12,
    4,
    567,
    87,
]  # we can add value of different data types in list
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])

# if we have given negative indexing , then we have to convert them in positive indexing and then we have to print it, as shown below

# print(marks(-3))# this will through error because of negative indexing
print(marks[len(marks) - 3])
print(marks[6 - 3])
print(marks[3])

# Check Whether an item is present in list or not

if 9.3 in marks:
    print("Yes")
else:
    print("No")
#  same thing applies for strings as well!
if "ta" in "Atta":
    print("Yes")
else:
    print("No")

# To Print all members of list

print(marks)
print(marks[:])
print(marks[1:])
print(marks[1:-1])
print(marks[1 : len(marks) - 1])

# jump Index
# i added jump index 2, it will print every second index value after last indexing as shown below
print(marks[1:-1:2])
print(marks[1:-1:3])

# List Comrehension

lst = [i for i in range(10)]
print(lst)

lst = [i * i for i in range(10)]
print(lst)

lst = [i * i for i in range(10) if i % 2 == 0]
print(lst)
