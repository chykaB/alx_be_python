class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"{self.title} {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()}, File Size: {self.file_size}MB"
        
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()}, Page Count: {self.page_count} pages"

class Library:
    books = []
    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        
    
    def list_books(self):
        for book in self.books:
            print(book)





