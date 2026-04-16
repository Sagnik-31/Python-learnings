# push , pop , top , size , is_empty -> LIFO principle
# TC -> O(1)

class Stack:

    def __init__(self):
        self.items = []
        self.l = 0

    def push(self,val):
        self.items.append(val)
        self.l += 1
    
    def pop(self):
        if self.l == 0:
            return "stack is empty cannot remove element"
        self.l -= 1
        x = self.items.pop()
        return x
    
    def top(self):
        if self.l == 0:
            return "stack is empty cannot return top element"
        return self.l[-1]
    
    def size(self):
        return self.l
    
    def is_empty(self):
        if self.l==0:
            return "stack is empty"
        return "stack is not empty"
    
    def display(self):
        if self.l == 0:
            print("Stack is empty")
        else:
            print("Stack elements (top to bottom):", self.items[::-1])
            #   print("Stack elements (bottom to top):", self.items)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.display()
print(stack.pop())
print(stack.is_empty())
stack.display()
        
