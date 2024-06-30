num1 = int(input('Enter the first number:'))
num2 = int(input('Enter the second number:'))
oppereation = input('Choose the operation (+, -, *, /):')
if oppereation == '+':
    result = num1 + num2
elif oppereation == '-':
    result = num1 - num2 
elif oppereation == '*':
    result = num1 * num2
elif oppereation == '/':
    result = num1 // num2
print(f'The result is {result}')
