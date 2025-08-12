class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls, str):
        return cls(str.split("-")[0], str.split("-")[1])


e1 = employee("Atta", 400000)
print(e1.name, e1.salary)
s = "Amna-200000"  # if we get data in this format we have to split and then add this as shown undwe
e2 = employee(s.split("-")[0], s.split("-")[1])
print(e2.name, e2.salary)
# to reomve above compexion, we simply made class method function which will be used as an alternative constructor
e3 = employee.fromstr("Zainab-100000")
print(e3.name, e3.salary)
