# library_management.py

class Book:
    """A class representing a book in a library."""

    def __init__(self, title: str, author: str):
        """Initialize a new book with a title and an author."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
        else:
            print(f"The book '{self.title}' is already checked out.")

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
        else:
            print(f"The book '{self.title}' is not currently checked out.")

    def is_checked_out(self) -> bool:
        """Return the check-out status of the book."""
        return self._is_checked_out


class Library:
    """A class representing a library containing books."""

    def __init__(self):
        """Initialize an empty library."""
        self._books = []

    def add_book(self, book: Book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title: str):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title:
                if not book.is_checked_out():
                    book.check_out()
                    print(f"'{title}' has been checked out.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title: str):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.is_checked_out():
                    book.return_book()
                    print(f"'{title}' has been returned.")
                else:
                    print(f"'{title}' is not checked out.")
                return
        print(f"Book '{title}' not found in the library.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if not book.is_checked_out()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books available.")
