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


def calc(num1,num2,operation):

    match operation:
        case '+':
            return num1+num2
        
        case '-':
            return num1-num2
        
        case '*':
            return num1*num2
        
        case '/':
            if num2 == 0:
                return "cant divide by zero"
            return num1/num2
        
        case '**' | '^':
            return num1**num2
        
        case _:
            return "invalid operator"

print(calc(5,6,'+'))
