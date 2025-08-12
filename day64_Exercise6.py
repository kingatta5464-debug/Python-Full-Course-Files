class library:
    def __init__(self):
        self.availible_books = ["Quran Pak", "Don Bradman"]
        self.no_books = len(self.availible_books)

    def addbook(self):
        book = input("Enter Name Of Book You Want To Add : ")
        self.availible_books.append(book)
        print("Added Successfully.")

    def totalnoofbooks(self):
        print("Total Number Of Books:", len(self.availible_books))

    def showavailiblebooks(self):
        for i in self.availible_books:
            print(i)

    def showlibrary(self):
        print("Available Books : ")
        for i in self.availible_books:
            print(i)
        print("Total Number Of Books : ", len(self.availible_books))


l = library()

while True:
    print("What Do You Want?")
    print(
        " 1. Show All Availible Books.\n 2. Add a Book.\n 3. Total Number Of Books.\n 4. Quit The Program."
    )
    c = int(input("Select From Above Options (1-4) : "))

    while c > 4 or c < 1:
        c = int(input("Select Again Only from 1-4 : "))

    if c == 1:
        l.showavailiblebooks()
    elif c == 2:
        l.addbook()
    elif c == 3:
        l.totalnoofbooks()
    else:
        print("Quitting Program!")
        exit()
