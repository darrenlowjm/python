"""
SOLID design principles

Single Responsibility classes principles
A class should have only 1 respoinsibility and no more
"""

class Books_cls:
"""
This is responsible for storing the books title only
"""
    def __init__(self):
        self.books: dict = dict()
        self.number: int = 0
    def add_book(self, book):
        self.number += 1
        self.books[self.number] = book
    def __repr__(self):
        return str(self.books)
        

class display_books:
"""
This is responsible for display and print to file only
"""

    @staticmethod
    def print_books_to_file( file, books:Books_cls):
        print(books.books)
        
a = Books_cls()
a.add_book('harry porter')
display_books.print_books_to_file(None,a)
