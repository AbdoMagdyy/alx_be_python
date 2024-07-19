class Book:
    def __init__(self,title,author,_is_checked_out ) :
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out
    #initializing the list to be a store
    list_available_books =[]
    #definition the adding method
    def adding_a_book(self):
        y = input("Enter name of the book")
        x = input("Enter author name")
        self._is_checked_out = 'no'
        # revice the last line the is some thing wrong