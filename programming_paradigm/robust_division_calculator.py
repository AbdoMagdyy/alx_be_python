def safe_divide(numerator, denominator):
    try:
        Result = float (numerator) / float (denominator)
        return Result
    except ZeroDivisionError:
        print('Error: Cannot divide by zero.')
    except ValueError:
        print('Error: Please enter numeric values only.')