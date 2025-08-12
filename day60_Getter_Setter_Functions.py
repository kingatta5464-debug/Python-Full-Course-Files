class Person:
    def __init__(self, name):
        self.name = name  # public attribute


p = Person("Ali")
print(p.name)  # Accessing directly
p.name = "Ahmed"  # Modifying directly

# This works, but there's no control over what gets assigned.


class Person:
    def __init__(self, name):
        self.__name = name  # private attribute (name mangling)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name) > 0:
            self.__name = name
        else:
            print("Name cannot be empty")


p = Person("Ali")
print(p.get_name())  # Getter
p.set_name("Ahmed")  # Setter
print(p.get_name())

# Python provides a cleaner way to use getters and setters using decorators.


class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name  # acts like a getter

    @name.setter
    def name(self, value):
        if len(value) > 0:
            self.__name = value  # acts like a setter
        else:
            print("Name cannot be empty")


p = Person("Ali")
print(p.name)  # calls the getter
p.name = "Ahmed"  # calls the setter
print(p.name)


# In Python, getters and setters are used to control the access and modification of class attributes. They are commonly used to enforce data encapsulation and validate the input before allowing changes to the attribute.

# Here is a simple example to demonstrate the concept of getters and setters in Python:


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Getter method for getting the name attribute
    def get_name(self):
        return self._name

    # Setter method for setting the name attribute
    def set_name(self, name):
        self._name = name

    # Getter method for getting the age attribute
    def get_age(self):
        return self._age

    # Setter method for setting the age attribute
    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print("Age must be a positive number.")


# Creating an instance of the Person class
person = Person("Alice", 30)

# Using the getter method to get the name attribute
print(person.get_name())  # Output: Alice

# Using the setter method to set the name attribute
person.set_name("Bob")
print(person.get_name())  # Output: Bob

# Using the setter method to set the age attribute with an invalid value (negative number)
person.set_age(-5)  # Output: Age must be a positive number.

# Using the setter method to set the age attribute with a valid value
person.set_age(35)
print(person.get_age())  # Output: 35
# In this example, the Person class has getter and setter methods for the name and age attributes. The getter methods allow us to retrieve the values of the attributes, while the setter methods allow us to modify the values with some validation logic.

# By using getters and setters, we can ensure that the class attributes are accessed and modified in a controlled way, which helps in maintaining the integrity of the data within the class.
