def calc_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide': 
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Unknown operation"

print("""
  ____    _    _     ____ _   _ _        _  _____ ___  ____  
 / ___|  / \  | |   / ___| | | | |      / \|_   _/ _ \|  _ \ 
| |     / _ \ | |  | |   | | | | |     / _ \ | || | | | |_) |
| |___ / ___ \| |__| |___| |_| | |___ / ___ \| || |_| |  _ < 
 \____/_/   \_\_____\____|\___/|_____/_/   \_\_| \___/|_| \_\
""")



a1 = input("Enter first number: ")
a2 = input("Enter second number: ")
op = input("Enter operation (add, subtract, multiply, divide): ").lower()
result = calc_operation(float(a1), float(a2), op)
print(f"The result is: {result}")


while True:
    cont = input("Do you want to perform calculation on the result? (yes/no): ").lower()
    if cont == 'yes':
        a1 = result
        a2 = input("Enter second number: ")
        op = input("Enter operation (add, subtract, multiply, divide): ").lower()
        result = calc_operation(float(a1), float(a2), op)
    elif cont == 'no':
        if input("Press Enter to exit or type 'new' to start a new calculation: ").lower() != 'new':
            break
        new_op = input("Enter new operation (add, subtract, multiply, divide): ").lower()
        new_a1 = input("Enter new first number: ")
        new_a2 = input("Enter new second number: ")
        result = calc_operation(float(new_a1), float(new_a2), new_op)
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

print(f"The result of {op}ing {a1} and {a2} is: {result}")
