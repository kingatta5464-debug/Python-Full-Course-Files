# is-  comapre exact location of object in memory
# ==   compare value

a = 4
b = "4"

print(a is b)  # false
print(a == b)  # false

a = 4  # for constant and same values python store only one time and then point to its addres if other same value added, like in the below example that's why 'is' shows "true" when compare it with other same value
b = 4

print(a is b)  # true
print(a == b)  # true

a = "Atta"
b = "Atta"

print(a is b)  # true
print(a == b)  # true

a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)  # false, because list is mutable(can be changed)
print(a == b)  # true

a = (1, 2, 3)
b = (1, 2, 3)

print(a is b)  # true, because list is immutable(can't be changed)
print(a == b)  # true

a = None
b = None

print(a is b)  # true
print(a == b)  # true

a = None
b = None

print(a is None)  # true
print(a == None)  # true
