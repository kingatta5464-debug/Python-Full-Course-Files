# dir(): The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. It is a useful tool for discovering what you can do with an object.
# Example:

x = [1, 2, 3, 4]
print(dir(x))
print(x.__add__)
print(x.reverse)

x = (1, 2, 3, 4)
print(dir(x))
print(x.__add__)


# __dict__: The __dict__ attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection.
# Example:


class person:
    def __init__(self, name, age, version):
        self.name = name
        self.age = age
        self.version = version


p = person("Atta", 24, 1)
print(p.__dict__)

# help(): The help() function is used to get help documentation for an object, including a description of its attributes and methods.
# Example:

print(help(person))
print(help(str))
