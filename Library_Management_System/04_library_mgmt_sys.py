class Library:
    def __init__(self):
        self.noOfBooks = 0
        self.books = []

    def addbook(self, book):
        self.books.append(book)
        self.noOfBooks = len(self.books)

    def show(self):
        print(f'There are {self.noOfBooks} books, They are:\n')
        for book in self.books:
            print(book)

a = Library()
a.addbook("Chief's hardcore moves")
a.addbook('Chief goes to abroad')
a.show()
