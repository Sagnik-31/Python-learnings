
    
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class StackLL:
    def __init__(self):
        self.head = None   # top of stack

    # PUSH (insert at beginning)
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # POP (remove from beginning)
    def pop(self):
        if self.head is None:
            print("Stack Underflow")
            return None
        
        popped = self.head.val
        self.head = self.head.next
        return popped

    # PEEK (see top element)
    def peek(self):
        if self.head is None:
            print("Stack is empty")
            return None
        return self.head.val

    # DISPLAY
    def display(self):
        if self.head is None:
            print("Stack is empty")
            return
        
        curr = self.head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")