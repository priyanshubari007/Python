def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not possible.")
    return a / b

def calculator():
    print("Select operation: +,-,*,/")
    operation = input("Enter choice (+,-,*,/): ")\

    if operation not in ['+','-','*','/']:
        print("Invalid operation choice.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        print(f"Result: {result}")

    except ValueError:
        print("Error : Please enter valid numbers only.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")


if __name__ =="__main__":
    calculator()