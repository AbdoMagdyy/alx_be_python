FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(x):
    if not isinstance(x, int):
        print('Invalid data type')
    result = x * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return result 

def convert_to_fahrenheit(x):
    if not isinstance(x, int):
        print('Invalid data type')
    result = (x - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return result