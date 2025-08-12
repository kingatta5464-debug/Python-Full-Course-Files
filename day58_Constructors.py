class person:
    def __init__(self, name, occ):
        print("Hey I Am  A Constructor!")
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is {self.occ}")


a = person("Atta", "HR")
b = person("Amna", "Manager")
a.info()
b.info()
