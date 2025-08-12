x = "Atta"
for i in x:
    print(i)
    if i == "t":
        print("Special Charatcer ", i)


l = ["Red", "Green", "Yellow", "Blue", "Black"]

for g in l:
    print(g)
    for j in g:
        print(j)


# range()

for i in range(5):
    print(i)

for i in range(0, 10):
    print(i + 1)

for i in range(1, 10, 2):
    print(i + 1)
