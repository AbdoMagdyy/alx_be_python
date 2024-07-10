FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

x = int(input("Enter the temperature to convert:"))
y = input("input", "Is this temperature in Celsius or Fahrenheit? (C/F):")

def convert_to_celsius(x):
    if not isinstance(x, int):
        print('Invalid temperature. Please enter a numeric value')
    result = x * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return result 

def convert_to_fahrenheit(x):
    if not isinstance(x, int):
        print('Invalid temperature. Please enter a numeric value')
    result = (x - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return result

if y == "C":
    CELSIUS_TO_FAHRENHEIT_FACTOR
elif y == "F":
    FAHRENHEIT_TO_CELSIUS_FACTOR
else:
    print ("Invalid temperature. Please enter a numeric value.")