class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    @staticmethod
    def add(a,b):
        return a + b
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b