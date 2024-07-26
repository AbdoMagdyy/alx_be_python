class Book:
    #initializing the attrebutes of the instances
    def __init__ (self , title : str , author : str , year : int):
        self.title = title
        self.author = author
        self.year = year
    #presinting the instance using dunder str
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    #represinting the instance using dunder repr
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    #deleting the instance using dunder del
    def __del__(self):
        return f"Deleting {self.year}"