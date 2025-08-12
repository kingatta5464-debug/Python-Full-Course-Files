# strings are immutable

name = "***Atta ******* Atta**"
print(name)
print(len(name))
print(name.upper())
print(name.lower())
print(name.rstrip("*"))
print(name.rsplit(" "))

str = "how are you?"
print(str.capitalize())
str2 = "how aRe You?"
print(str2.capitalize())
heading = "Janam Ji"
print(len(heading))
print(heading.center(20))
print(len(heading.center(20)))

print(name.count("Atta"))


s = "My name is Atta, who is he?"
print(s.find("is"))  # return index of first 'is'
print(s.find("ishh"))  # this will return -1 because there is no occurence of 'ishh'

# print(s.index("ishh"))#this will through error

an = "Atta"
print(an.isalnum())
print(an.isalpha())
print(an.swapcase())


print(s.title())
