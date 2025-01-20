"""
    Your Task: library_management.py
Implement a Book class with public attributes title and author, 
and a private attribute _is_checked_out to track its availability.
Implement a Library class with a private list _books to store instances of Book. Include methods to add_book, check_out_book(title), return_book(title), and list_available_books

"""
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    def is_available(self):
        return not self._is_checked_out
    
class Library:
    def __init__(self):
        self._books = []
    def add_book(self, book):
        self._books.append(book)
    def check_out_book(self,title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Book {title}, checked out succesfully")
                return True
        print(f"Book {title} is not available")
    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Book {title}, is returned successfully")
                return True
        print(f"Book {title}, not checked out")
        return False
    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"Title: {book.title}, Author: {book.author} ")
            else:
                print("No books")

