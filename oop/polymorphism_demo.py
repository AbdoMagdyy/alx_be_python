#creating the parent class
class Shape:
    def area(self):
        raise NotImplementedError
#creat the first chiled class
class Rectangle(Shape):
    def __init__(self, length : float , width :float):
        super().__init__()
        self.length = length
        self.width = width
    #Overriding area method
    def area(self):
        return self.length * self.width
#creating the second child class
class Circle(Shape):
    def __init__(self, radius : float):
        super().__init__()
        self.radius = radius
    #overriding area method
    def area(self):
        return 3.141592653589793 * self.radius ** 2
