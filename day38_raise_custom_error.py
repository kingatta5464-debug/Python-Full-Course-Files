x = input("Enter a value between 5 to 9 : ")
if x.upper() == "QUIT":
    print("Quiting Program.")
elif int(x) < 5 or int(x) > 9:
    raise ValueError("Value should be between 5 to 9.")
