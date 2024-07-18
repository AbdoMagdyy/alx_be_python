def safe_divide(numerator, denominator):
    """Performs division and handles division by zero."""
    try:
        # Ensure inputs are numbers
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Perform division
        result = numerator / denominator
        
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    return f"The result of the division is{result}"