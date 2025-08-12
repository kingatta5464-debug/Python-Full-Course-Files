# Multiple inheritance is a powerful feature in object-oriented programming that allows a class to inherit attributes and methods from multiple parent classes. This can be useful in situations where a class needs to inherit functionality from multiple sources.


class employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Employee name is {self.name}.")


class dance:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"The Dance is {self.dance}.")


class danceremployee(employee, dance):
    def __init__(self, name, dance):
        super().__init__(name)
        self.dance = dance

    def show(self):
        employee.show(self)
        dance.show(self)


d = danceremployee("Amna", "Belly Dance")
d.show()
print(danceremployee.mro())
d.show()
