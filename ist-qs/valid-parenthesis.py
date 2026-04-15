# if u find closing bracket but stack is empty -> False
# if brackets doesnt match -> False
# at the end stack is not empty -> False

s = input("enter expression: ")
stack = []

for bracket in s:

    if bracket == "(" or bracket == "{" or bracket == "[":
        stack.append(bracket)

    else:
        if len(stack)==0:
            print("False")
            break

        ch = stack.pop()

        if(
            (bracket == ")" and ch == "(")
            or(bracket == "}" and ch=="{")
            or(bracket == "]" and ch=="[")
        ):
            continue
        else:
            print("False")
            break

if len(stack) == 0:
    print("True")
else:
    print("False")



