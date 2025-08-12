s1 = {1, 2, 3, 4}
s2 = {7, 10, 6, 8, 9, 4, 3}

# Union(neglect the common values)
print(s1.union(s2))
print(s1)
print(s2)


# Update
s1.update(s2)
print(s1)

# Intersection (Consider only common values)

print(s1.intersection(s2))

# Intersection_Update

s1.intersection_update(s2)
print(s1)

# Symmetric Difference and Symmteric Difference Update
# Consider Values Which are not common
x1 = {1, 2, 3, 4, 5}
x2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(x1.symmetric_difference(x2))

x1.symmetric_difference_update(x2)
print(x1)

# Difference (a-b)

m1 = {1, 2, 3, 4, 5, 12}
m2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(m1.difference(m2))
m1.difference_update(m2)
print(m1)

# isDisjoint (sets having no common values)

m1 = {1, 2, 3, 4, 5, 12}
m2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}

n1 = {12}
n2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(m1.isdisjoint(m2))
print(n1.isdisjoint(n2))

# isSuperSet
# if a set n1 has all the elements that are present in set n2, then set n1 will be a superset of set n2 and set n2 will be subset of n1 as shown below

n1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
n2 = {1, 2, 3, 4, 5}
print(n1.issuperset(n2))

# Add (used to item to set)

n2 = {1, 2, 3, 4, 5}

n2.add(99)
print(n2)

# Remove

n2.remove(2)
print(n2)

# pop
n2.pop()
print(n2)


# delete

x = {1, 2, 3, 4, 5}
del x
# print(x) #Delete whole set

# Clear

x = {1, 2, 3, 4, 5}
x.clear()  # just delete set items not whole set
print(x)
