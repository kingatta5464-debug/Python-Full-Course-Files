# A class method is a type of method that is bound to the class and not the instance of the class. In other words, it operates on the class as a whole, rather than on a specific instance of the class. Class methods are defined using the "@classmethod" decorator, followed by a function definition. The first argument of the function is always "cls," which represents the class itself.


class employee:
    company_name = "Apple"

    def show(self):
        print(
            f"The Name of employee is {self.name} and the company name is {self.company_name}."
        )

    @classmethod
    def changecompany(
        self, newname
    ):  # by default a function first arguument is self, but in class method function first argument is class
        self.company_name = newname


e1 = employee()
e1.name = "Atta"
e1.show()
e1.company_name = (
    "Google"  # it will change company name only for this instance of employee
)
e1.show()

e1.changecompany("Nestle")
e1.show()  # (because e1 still has its own instance variable)
e2 = employee()
e2.name = "Rubina"
e2.show()
# to change company name for all instance of a class we have to build a class method
