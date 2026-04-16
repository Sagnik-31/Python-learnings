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

print(eval_expression(["2","1","+","3","*"])) # 9

            


    

