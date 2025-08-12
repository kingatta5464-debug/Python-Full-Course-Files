import math

# x = math.factorial(4)
# print(x)
# y = math.sqrt(4)
# print(y)

from math import factorial, pi, sqrt

x = factorial(4)
print(x)
y = sqrt(4)
print(y)

from math import factorial as fac, pi as p, sqrt as s

a = fac(7)
print(a * p)
b = s(9)
print(b)

import math as m

x = m.factorial(4)
print(x)
y = m.sqrt(4)
print(y)

# to check what type of functions and method any module offer we can check by writing dir function like as under

print(dir(math))

# we can import the files that we created and use that file functions variables in our working file. for example

from atta import welcome, atta

print(atta)
welcome()
