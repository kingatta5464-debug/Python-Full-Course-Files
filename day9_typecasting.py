# Explicit Typecasting

a = "1"
b = "2"
print(a + b)  # output: 12
print(int(a) + int(b))  # output: 3 [TYPECASTING]


# Implicit Typecasting

a = 9.9
b = 7
print(a + b, type(a + b), type(a), type(b))
