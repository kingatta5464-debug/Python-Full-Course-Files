# Single Inheritance in Python
# Single inheritance is a type of inheritance where a class inherits properties and behaviors from a single parent class. This is the simplest and most common form of inheritance.


class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("sound made by the animal")


class dog(animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def make_sound(self):
        print("Bark")


class cat(animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def make_sound(self):
        print("Meow")


a = animal("Dog", "Dogger")
a.make_sound()

d = dog("Butcher", "Dogger", "German Shepherd")
d.make_sound()

c = cat("Lexy", "Catter", "Domitus")
c.make_sound()
