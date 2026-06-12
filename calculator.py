def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")


def get_operator():
    while True:
        op = input("Enter an operator (+, -, *, /): ").strip()
        if op in OPERATIONS:
            return op
        print(f"Error: '{op}' is not a valid operator. Choose from +, -, *, /")


def calculate(a, op, b):
    return OPERATIONS[op](a, b)


if __name__ == "__main__":
    print("Simple Calculator (type 'q' to quit)\n")
    while True:
        try:
            raw = input("Enter first number (or 'q' to quit): ").strip()
            if raw.lower() == "q":
                print("Goodbye!")
                break
            a = float(raw)
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        op = get_operator()

        b = get_number("Enter second number: ")

        try:
            result = calculate(a, op, b)
            print(f"  {a} {op} {b} = {result}\n")
        except ZeroDivisionError as e:
            print(f"Error: {e}\n")
