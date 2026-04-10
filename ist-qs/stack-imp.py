class Stack:

    def __init__(self):
        self.items = []
        self.t = 0

    def length(self):
        return self.t

    def push(self, value):
        self.items.append(value)
        self.t+=1

    def pop(self):
        if self.t==0:
            return "The stack is already empty"
        else:
            self.t-=1
            x = self.s.pop()
            return x

    def is_empty(self):
        if self.t==0:
            return True
        else:
            return False

    def top(self):
        if self.is_empty():
            return "The stack is  empty"
        else:
            return self.t[-1]






s1 = Stack()
print(s1.length())
s1.push(5)
s1.push(1)
s1.push(18)
s1.push(90)
print(s1.pop())
# print(s1.top())
print(s1.is_empty())