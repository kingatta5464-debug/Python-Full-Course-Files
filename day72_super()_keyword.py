# The super() keyword in Python is used to refer to the parent class. It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes.

# When a class inherits from a parent class, it can override or extend the methods defined in the parent class. However, sometimes you might want to use the parent class method in the child class. This is where the super() keyword comes in handy.


class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def parent_method(self):
        print("this is parent method")


class programmer(employee):
    def parent_method(self):
        print("parent from child")

    def __init__(self, name, age, lang):
        super().__init__(name, age)
        self.lang = lang

    def child_method(self):
        print("this is child method")
        super().parent_method()


e = employee("Atta", 24)
print(e.name, e.age)
p = programmer("Mustafa", 23, "Python")
print(p.name, p.age, p.lang)

p.child_method()
p.parent_method()
