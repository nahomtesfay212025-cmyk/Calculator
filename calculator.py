def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    a = float(input("Enter the first number: "))
    op = input("Enter an operator (+, -, *, /): ").strip()
    b = float(input("Enter the second number: "))

    if op not in operations:
        print(f"Unknown operator: {op}")
    else:
        try:
            result = operations[op](a, b)
            print(f"{a} {op} {b} = {result}")
        except ValueError as e:
            print(f"Error: {e}")