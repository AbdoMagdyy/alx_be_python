FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

x = int(input("Enter the temperature to convert:"))
y = input("input", "Is this temperature in Celsius or Fahrenheit? (C/F):")

def convert_to_celsius(x):
    if not isinstance(x, int):
        print('Invalid temperature. Please enter a numeric value')
    celsius = x * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return celsius
def convert_to_fahrenheit(x):
    if not isinstance(x, int):
        print('Invalid temperature. Please enter a numeric value')
    fahrenheit = (x - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return fahrenheit

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    if unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    elif unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
    else:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        
if __name__ == "__main__":
     main()