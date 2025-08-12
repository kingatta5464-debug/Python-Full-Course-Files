class person:
    name = "Atta"
    ocuupation = "Student"
    cnic = "123"

    def printinfo(self):
        print(
            "My Name Is ",
            self.name,
            "\nI am a ",
            self.ocuupation,
            "\nMy CNIC Is ",
            self.cnic,
        )


a = person()
b = person()
a.printinfo()

b.name = "Ayesha"
b.ocuupation = "Lawyer"
b.cnic = "321"
b.printinfo()
