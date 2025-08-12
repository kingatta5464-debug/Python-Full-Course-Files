# Tuples are Immutable like Strings , but Lists are Mutable
tup = (1, 2, 3, 4)
print(type(tup), tup)
tup = (1, 2, 3, 4, "Atta", 5.54)
print(tup)
# Tuple is uncahngeable,e.g;

# tup[0]=12      #this wil through an error, because we can not change values in tuple
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(tup[4])
print(tup[5])

# Negative indexing (same like list)

print(tup[-1])
print(tup[-2])

# Searching in Tuple
if 4 in tup:
    print("Yes")
else:
    print("No")
if 342 in tup:
    print("Yes")
else:
    print("No")

# Slicing

print(tup[1:4])

tup2 = tup[1:4]
print(tup2)
