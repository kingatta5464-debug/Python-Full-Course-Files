# finally keyword in Python to define a block of code that always runs, no matter what — whether an exception occurs or not.
def indexprinting():
    try:
        x = [1, 2, 3, 4]
        a = int(input("Enter a number : "))
        print(x[a])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("I am always Executed")


x = indexprinting()
print(x)
