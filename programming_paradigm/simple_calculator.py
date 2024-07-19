class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""

    def add(self, a: float, b: float) -> float:
        """Return the addition of a and b."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Return the subtraction of b from a."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Return the multiplication of a and b."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """
        Return the division of a by b.
        
        Raises:
            ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError("Error: Cannot divide by zero.")
        return a / b
