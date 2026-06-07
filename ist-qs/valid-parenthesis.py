# if u find closing bracket but stack is empty -> False
# if brackets doesnt match -> False
# at the end stack is not empty -> False
def is_matched(expr):
    lefty = '({['
    righty = ')}]'
    stack = []

    for c in expr:
        if c in lefty:
            stack.append(c)

        elif c in righty:
            if len(stack) == 0:
                return False
            if righty.index(c) != lefty.index(stack.pop()):
                return False
    
    return len(stack) == 0

expr = input("Enter expression: ")

if is_matched(expr):
    print("Parentheses are Balanced")
else:
    print("Parentheses are Not Balanced")

    
# s = input("enter expression: ")
# stack = []

# for bracket in s:

#     if bracket == "(" or bracket == "{" or bracket == "[":
#         stack.append(bracket)

#     else:
#         if len(stack)==0:
#             print("False")
#             break

#         ch = stack.pop()

#         if(
#             (bracket == ")" and ch == "(")
#             or(bracket == "}" and ch=="{")
#             or(bracket == "]" and ch=="[")
#         ):
#             continue
#         else:
#             print("False")
#             break

# if len(stack) == 0:
#     print("True")
# else:
#     print("False")



