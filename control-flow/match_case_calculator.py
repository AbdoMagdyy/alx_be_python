num1 = int(input('Enter the first number:'))
num2 = int(input('Enter the second number:'))
operation = input('Choose the operation (+, -, *, /):')
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2 
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 // num2
print(f'The result is {result}')
