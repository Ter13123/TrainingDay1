def calculator():

    num1 = float(input("Enter the first number: "))

    operation = input("Choose an operator: ")

    num2 = float(input("Enter the second number: "))

    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '*':
        print(num1 * num2)
    elif operation == '/':
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print(num1 / num2)
    else:
        print("Invalid operation")

calculator()