class base:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Name : {self.name}")


class derived_1(base):
    def __init__(self, name, model):
        super().__init__(name)
        self.model = model

    def show(self):
        super().show()
        print(f"Model : {self.model}")


class derived_2(base):
    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed

    def show(self):
        super().show()
        print(f"Speed : {self.speed}")


class derived_2_i(derived_2):
    def __init__(self, name, speed, color):
        super().__init__(name, speed)
        self.color = color

    def show(self):
        super().show()
        print(f"Color : {self.color}")


d1 = derived_1("Honda 70", 2015)
d1.show()

d2 = derived_2("Suzuki 110", "110 km/h")
d2.show()

d3_i = derived_2_i("Suzuki 110", "110 km/h", "Black")
d3_i.show()
