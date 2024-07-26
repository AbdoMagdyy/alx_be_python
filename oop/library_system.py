#defining Book class
class Book:
    def __init__(self,title : str,author : str):
        self.title = title
        self.author = author
    #showing the results
    def __str__(self):
        return f"{self.title} by {self.author}"
#defining EBook class
class EBook(Book):
    def __init__(self, title: str, author: str , file_size : int):
        self.file_size = file_size
        super().__init__(title, author)
            #showing the results
    def __str__(self):
        return f"{self.title} by {self.author}, File Sie: {self.file_size}"
#defining PrintBook class
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count : int):
        self.page_count = page_count
        super().__init__(title, author)
            #showing the results
    def __str__(self):
        return f"{self.title} by {self.author}, Page Count: {self.page_count}"
#defining composition class (Library)
class Library:
    # initializing attributs
    def __init__(self, books):
        self.books = []
    #defining add_book method
    def add_book(self,book):
        self.books.append(book)
    #defining the list_books function
    def list_books(self):
        for book in self.books:
            print(book)