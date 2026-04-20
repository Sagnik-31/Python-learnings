# def calculator(num1, num2, operation):

#     match operation:
#         case '+':
#             return num1 + num2

#         case '-':
#             return num1 - num2

#         case '*':
#             return num1 * num2

#         case '/':
#             if num2 == 0:
#                 return "Error: Cannot divide by zero"
#             return num1 / num2

#         case '%':
#             if num2 == 0:
#                 return "Error: Cannot divide by zero"
#             return num1 % num2

#         case '^' or '**':
#             return num1 ** num2

#         case _:
#             return "Error: Invalid operation"


# print("=== Simple Arithmetic Calculator ===")
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operation = input("Enter operation (+, -, *, /, %, ^): ")

# result = calculator(num1, num2, operation)
# print(f"{num1} {operation} {num2} = {result}")

while True:
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("enter choice: "))

    if choice == 5:
        print("program terminated")
        break
   
    A = float(int(input("enter a number: ")))
    B = float(int(input("enter second number: ")))

    match choice:
        case 1:
            print("Result",A+B)
        case 2:
            print("Result", A-B)
        case 3:
            print("Result",A*B)
        case 4:
            if B==0:
                print("cant divide by zero")
            print("Result",A/B)
        case _:
            print("invalid choice")


