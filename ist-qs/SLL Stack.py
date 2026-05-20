# stack -> add at front , remove at front

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None
    
    def push(self,data):
        new_node = self.Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    
    def pop(self):
        if self.top == None:
            print("Queue Underflow")
        x = self.top
        self.top = self.top.next
        self.size -= 1
        return x.data
    
    def peek(self):
        if self.top == None:
            print("Queue Underflow")
        return self.top.data
    
    def traversal(self):
        if self.top == None:
            print("Queue Underflow")
        else:
            curr = self.top
            while curr is not None:
                print(curr.data,end=" ")
                curr = curr.next
            print()

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.traversal()
s.pop()
s.traversal()
