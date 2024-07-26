# Defining Book class
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    # Showing the results
    def __str__(self):
        return f"Book: {self.title} by {self.author}"

# Defining EBook class
class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

    # Showing the results
    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

# Defining PrintBook class
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    # Showing the results
    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

# Defining composition class (Library)
class Library:
    # Initializing attributes
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            self.books = books

    # Defining add_book method
    def add_book(self, book):
        self.books.append(book)

    # Defining the list_books function
    def list_books(self):
        for book in self.books:
            print(book)
