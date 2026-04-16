def infix_to_postfix(infix):
    def p(op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        if op == '^':
            return 3
        return 0
    
    stack = []
    post = ""

    for ch in infix:
        
        if ch.isalnum():
            post += ch
        
        elif ch == '(':
            stack.append(ch)
        
        elif ch == ')':
            while stack and stack[-1] != '(':
                post += stack.pop()
            stack.pop()
        
        else:
            while stack and p(stack[-1]) >= p(ch):
                post += stack.pop()
            stack.append(ch)

    while stack:
        post += stack.pop()

    return post
print(infix_to_postfix("(A+B)*(C*D-E)*F/G"))