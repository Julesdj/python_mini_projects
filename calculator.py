def calculator():
    print("Simple Calculator")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    if op == "+":
        print(f"Result: {a + b}")
    elif op == "-":
        print(f"Result: {a - b}")
    elif op == "*":
        print(f"Result: {a * b}")
    elif op == "/":
        print(f"Result: {a / b}")
    else:
        print("Invalid operation")


calculator()
