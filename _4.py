class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

class Book(Author):
    def __init__(self, name, nationality, title, genre, availability=True):
        super().__init__(name, nationality)
        self.title = title
        self.genre = genre
        self.availability = availability

    def borrow_book(self):
        if self.availability:
            self.availability = False
            print(f"The book '{self.title}' has been borrowed.")
        else:
            print(f"The book '{self.title}' is available.")

    def display_book_info(self):
        status = 'Available' if self.availability else 'Borrowed'
        print(f"Title: {self.title}\nAuthor: {self.name}\nStatus: {status}")

book1 = Book('Charles Dickens', 'American', 'Oliver Twist', 'Realistic Fiction')
book2 = Book('George Orwells', 'American', 'Animal Farm', 'Fiction')

book1.borrow_book()

print('-'*60)
book1.display_book_info()
print('-'*60)
book2.display_book_info()