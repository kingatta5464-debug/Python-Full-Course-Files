l = [3, 2, 4, 54, 779, 45, 80, 12, 67]
print(l)
# Append
l.append(102)
print(l)
# Sort
l.sort()
print(l)
# Reverse Sort
l.sort(reverse=True)
print(l)
# Reverse List
lt = [23, 11, 34, 78, 521, 13, 4, 66, 9]
lt.reverse()
print(lt)
# Find Index
mt = [23, 11, 34, 78, 521, 13, 4, 66, 9, 11]
print(mt.index(78))
print(mt.index(4))
# Count (to fint how many times that number exists in list)
print(mt.count(11))
print(mt.count(4))
# Copy
# m=mt #this is wrong, it will be consider only single list
m = mt.copy()
print(m)

# Concatenation
j = [1, 2, 3, 4]
k = [5, 6, 7, 8]
o = j + k + m
print(o)

# Extend
m.extend(j)
print(m)
