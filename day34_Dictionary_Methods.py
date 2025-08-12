ep1 = {122: 45, 123: 65, 456: 87, 71: 65, 12: 92}
ep2 = {399: 83, 91: 14}

# Update
ep1.update(ep2)
print(ep1)

# Clear
ep1 = {122: 45, 123: 65, 456: 87, 71: 65, 12: 92}
ep1.clear()
print(ep1)

# Pop
ep1 = {122: 45, 123: 65, 456: 87, 71: 65, 12: 92}
ep1.pop(122)
ep1.pop(71)
print(ep1)

# Popitem
ep1 = {122: 45, 123: 65, 456: 87, 71: 65, 12: 92}
ep1.popitem()
print(ep1)

# Delete
# del ep1
# print(ep1)  # Compiler through error because ep1 dictionary got deleted
del ep1[456]
print(ep1)
