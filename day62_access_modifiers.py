# Access modifiers control the visibility (accessibility) of class attributes and methods. While Python doesn’t enforce strict access modifiers like C++ or Java, it uses naming conventions to guide developers.
# There is no concept of public, private or protected access modifiers in python.


class student:
    def __init__(self):
        self.name = "Atta"  # Public
        self._roll_no = 11  # Protected
        self.__grade = "A+"  # Private

    def show(self):
        print("Public : ", self.name)
        print("Protected : ", self._roll_no)
        print("Public : ", self.__grade)


s = student()
s.show()

print(s.name)  # ✅ Public: accessible
print(s._roll_no)  # ⚠️ Protected: accessible, but not recommended
# print(s.__grade)  # ❌ Private: AttributeError

# We can not access private attribute directly, but we can access it indirectly by name mangling as shown below

print(s._student__grade)  # Name Mangling # ✅ Works but not recommended
