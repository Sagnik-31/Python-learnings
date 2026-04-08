class Stack:

    def __init__(self):
        self.s = []
        self.t = 0

    def length(self):
        return self.t

    def push(self, value):
        self.s.append(value)
        self.t+=1

    def pop(self):
        if self.t==0:
            raise Exception ("The stack is already empty")
        else:
            self.t-=1
            return f"Removed element: {self.s.pop()}"

    def is_empty(self):
        if self.length():
            return True
        else:
            return False

    def top(self):
        if self.is_empty():
            raise Exception("The stack is  empty")
        else:
            return self.t






s1 = Stack()
print(s1.length())
s1.push(5)
s1.push(1)
s1.push(18)
s1.push(90)
print(s1.pop())
print(s1.top())
print(s1.is_empty())