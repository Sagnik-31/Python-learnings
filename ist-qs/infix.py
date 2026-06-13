def infix_postfix(expression):
    def p(op):
        if op == '+' or op == '-':
            return 1
        elif op == '*' or op == '/':
            return 2
        elif op == '^' or op == '**':
            return 3
        return 0

    post = ""
    stack = []

    for ch in expression:
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

print(infix_postfix("(A+B)*(C*D-E)*F/G"))