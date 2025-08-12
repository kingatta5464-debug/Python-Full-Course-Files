a = input("What is your name : ")
print("My name is ", a)

x = input("Enter First Number : ")
y = input("Enter Second Number : ")
# by default python take input as String
# we have to typecast in order to get desired output
print("Addition : ", x + y)  # output: 1212 if input is 12,12
print("Addition : ", int(x) + int(y))  # output: 24
