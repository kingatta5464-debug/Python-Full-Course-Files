# The enumerate() function adds a counter to an iterable (like a list, tuple, or string) and returns it as an enumerate object (which you can loop over).

marks = [54, 98, 23, 78, 67, 54, 92, 12, 56]
index = 0
for mark in marks:
    print(mark)
    if index == 3:
        print("Atta, Awesome")
    index += 1

# instead of above statement we can write function as

for index, mark in enumerate(marks):
    print(mark)
    if index == 3:
        print("Atta, Awesome")

for index, mark in enumerate(marks, start=1):
    print(mark)
    if index == 3:
        print("Atta, Awesome")

fruits = ["Apple", "Banana", "Mango", "Orange"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
