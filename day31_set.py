# Set is a well defined set of object
# Sets do not contains duplicate items
# Sets can not be changed once created
# it dont take repeated values in set as shown below
s = {2, 3, 4, 2, 6}  # output will be{2,3,4,6}
print(s)

info = {"Atta", 19, 0.5, 7, True, 19}
print(type(info), info)

Atta = {}
print(type(Atta))
Atta = set()
print(type(Atta))

# Set do not maintain order

for i in info:
    print(i)
