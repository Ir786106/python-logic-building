num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
operation=input("Enter operation (+, -, *, /, %): ")

match operation:
    case "+":
        result=num1+num2
        print(f"Result: {result}")
    case "-":
        result=num1-num2
        print(f"Result: {result}")
    case "*":
        result=num1*num2
        print(f"Result: {result}")
    case "/":
        if num2 != 0:
            result=num1/num2
            print(f"Result: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    case "%":
        if num2 != 0:
            result=num1%num2
            print(f"Result: {result}")
        else:
            print("Error: Modulo by zero is not allowed.")
    case _:
        print("Invalid operation entered. Please use +, -, *, /, or %.")