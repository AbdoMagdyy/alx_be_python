#defining Book class
class Book:
    def __init__(self,title : str,author : str):
        self.title = title
        self.author = author
    #showing the results
    def __str__(self):
        return f"Book ('{self.title}' , '{self.author}')"
#defining EBook class
class EBook(Book):
    def __init__(self, title: str, author: str , file_size : int):
        self.file_size = file_size
        super().__init__(title, author)
            #showing the results
    def __str__(self):
        return f"EBook ('{self.title}' , '{self.author}' , '{self.file_size}')"
#defining PrintBook class
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count : int):
        self.page_count = page_count
        super().__init__(title, author)
            #showing the results
    def __str__(self):
        return f"PrintBook ('{self.title}' , '{self.author}' , '{self.page_count}')"