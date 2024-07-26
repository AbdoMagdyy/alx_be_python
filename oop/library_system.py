#starting the (books) list
books = []

#defining Book class
class Book:
    def __init__(self,title : str,author : str):
        self.title = title
        self.author = author
    #defining add_book method **
    def add_book (self,book):
        book = input()
        books.appen(book)
    #defining list_books
    def list_books (self):
        print(books)
#defining EBook class
class EBook (Book):
    def __init__(self, title: str, author: str , file_size : int):
        self.file_size = file_size
        super().__init__(title, author)
#defining PrintBook class
class PrintBook (Book):
    def __init__(self, title: str, author: str, page_count : int):
        self.page_count = page_count
        super().__init__(title, author)