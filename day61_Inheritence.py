class employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showinfo(self):
        print(f"Emplyee Name : {self.name}\nEmployee Id : {self.id}")


class programmer(employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

    def showProInfo(self):
        self.showinfo()
        print(f"Programming Language is : {self.lang}")


e = employee("Atta", 11)
e.showinfo()
p = programmer("Amna", 12, "Python")
p.showProInfo()
