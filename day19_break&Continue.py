for i in range(1, 15):
    print(" 5 x", i, "=", 5 * i)
    if i == 10:
        print("Loop Ko Chor Raha")
        break


for i in range(1, 15):
    if i == 10:
        print("Iteration Ko Chor Raha")
        continue
    print(" 5 x", i, "=", 5 * i)
