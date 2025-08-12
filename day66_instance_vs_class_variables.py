class employee:
    company_name = "Apple"
    no_of_employees = 0

    def __init__(self, name):
        self.name = name
        employee.no_of_employees += 1

    def showdetails(self):
        print(
            f"The name of the employee is {self.name} working in {self.no_of_employees} sized company"
        )


emp1 = employee("Atta")
emp1.showdetails()
emp2 = employee("Ayesha")
emp2.showdetails()
# in both above examples name is instance variable which is different for every instance of employee class

print(emp1.company_name)
print(emp2.company_name)

# both of the above print statements are calling class variable which is same for all the instances of employee class

emp1.company_name = "Nestle"
print(emp1.company_name)
print(emp2.company_name)


# Instance vs class variables
# In Python, variables can be defined at the class level or at the instance level. Understanding the difference between these types of variables is crucial for writing efficient and maintainable code.

# Class Variables
# Class variables are defined at the class level and are shared among all instances of the class. They are defined outside of any method and are usually used to store information that is common to all instances of the class. For example, a class variable can be used to store the number of instances of a class that have been created.


class MyClass:
    class_variable = 0

    def __init__(self):
        MyClass.class_variable += 1

    def print_class_variable(self):
        print(MyClass.class_variable)


obj1 = MyClass()
obj2 = MyClass()
obj1.print_class_variable()  # Output: 2
obj2.print_class_variable()  # Output: 2
# In the example above, the class_variable is shared among all instances of the class MyClass. When we create new instances of MyClass, the value of class_variable is incremented. When we call the print_class_variable method on obj1 and obj2, we get the same value of class_variable.

# Instance Variables
# Instance variables are defined at the instance level and are unique to each instance of the class. They are defined inside the init method and are usually used to store information that is specific to each instance of the class. For example, an instance variable can be used to store the name of an employee in a class that represents an employee.


class MyClass:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)


obj1 = MyClass("John")
obj2 = MyClass("Jane")
obj1.print_name()  # Output: John
obj2.print_name()  # Output: Jane
# In the example above, each instance of the class MyClass has its own value for the name variable. When we call the print_name method on obj1 and obj2, we get different values for name.
