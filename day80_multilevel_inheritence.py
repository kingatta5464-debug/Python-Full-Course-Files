# Multilevel inheritance is a type of inheritance in object-oriented programming where a derived class inherits from another derived class. This type of inheritance allows you to build a hierarchy of classes where one class builds upon another, leading to a more specialized class.


class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show(self):
        print(f"Name : {self.name}")
        print(f"Species : {self.species}")


class dog(animal):
    def __init__(self, name, breed):
        super().__init__(
            name, species="Dog"
        )  # In Python, when you use super(), it automatically passes self, so writing super().__init__(self, ...) will cause typing error
        self.breed = breed

    def show(self):
        animal.show(self)
        print(f"Breed : {self.breed}")


class goldenretriver(dog):
    def __init__(self, name, color):
        super().__init__(name, breed="Golden Retriver")
        self.color = color

    def show(self):
        dog.show(self)
        print(f"Color : {self.color}")


g = goldenretriver("Tommy", "Black")
g.show()
