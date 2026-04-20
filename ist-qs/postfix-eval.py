def eval_expression(arr):

    operator = ['+','-','*','/']
    stack = []

    for item in arr:

        if item not in operator: # item is an operand 
            stack.append(item)
        
        else: # item is an operator

            first = int(stack.pop())
            second = int(stack.pop())

            if item == '+':
                stack.append(second+first)

            if item == '-':
                stack.append(second-first)
            
            if item == '*':
                stack.append(second*first)
            
            if item == '/':
                stack.append(second/first)

    return stack[-1]

user_input = input("enter number seperated by spaces: ")
arr = user_input.split()
result = eval_expression(arr)
print(result)
            


    

