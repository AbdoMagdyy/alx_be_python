def robust_division(numerator, denominator):
    """Performs division and handles division by zero."""
    try:
        # Ensure inputs are numbers
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Perform division
        result = numerator / denominator
        
    except ValueError:
        return "Error: Both inputs must be numbers."
    except ZeroDivisionError:
        return "Error: Division by zero is undefined."
    
    return result