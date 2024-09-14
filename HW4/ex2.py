def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def calculator():
    try:
        num1, operation, num2 = input("Введіть операцію (наприклад, 2 + 2): ").split()
        num1 = int(num1)
        num2 = int(num2)

        if operation == '+':
            print(f"{num1} {operation} {num2} = {add(num1, num2)}")
        elif operation == '-':
            print(f"{num1} {operation} {num2} = {subtract(num1, num2)}")
        elif operation == '*':
            print(f"{num1} {operation} {num2} = {multiply(num1, num2)}")
        elif operation == '/':
            print(f"{num1} {operation} {num2} = {divide(num1, num2)}")
        elif operation == '^':
            print(f"{num1} {operation} {num2} = {power(num1, num2)}")
        else:
            print("Невірний вибір операції!")
    except ValueError:
        print("Помилка! Введіть число.")
    except ZeroDivisionError:
        print("Помилка! Ділення на нуль.")
    except Exception:
        print(f"Невідома помилка")

calculator()
