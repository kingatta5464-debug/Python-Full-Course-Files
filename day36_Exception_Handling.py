# try...except is used to handle errors (exceptions) gracefully — instead of crashing, the program can respond to errors in a controlled way.
a = input("Enter a Number : ")
print(f"Multiplication table of {a} is as under: ")

try:
    for i in range(1, 11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except:
    print("Invalid Input!")


print("Important lines of code")
print("End of Program")

try:
    num = int(input("Enter an Integer : "))
    a = [2, 3]
    print(a[num])
except ValueError:
    print("Value Error Occured")
except IndexError:
    print("Index Error Occured")
