def perform_operation(num1:float,num2:float,operation ):
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    if operation == 'add':
        print(num1 + num2)
    elif operation == 'subtract':
        print(num1 - num2)
    elif operation == 'multiply':
        print(num1 * num2)
    elif operation == 'divide':
        print(num1 / num2)
