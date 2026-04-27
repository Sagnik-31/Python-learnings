class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self._size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def pop(self):
        if self.head is None:
            print("Stack Underflow - Cannot pop from empty stack")
            return None
        self.head = self.head.next
        self._size -= 1
        return self.data

    def peek(self):
        if self.head is None:
            print("Stack is empty")
            return None
        return self.head.data

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size

    def display(self):
        if self.head is None:
            print("Stack is empty")
            return
        current = self.head
        print("Stack elements (top to bottom):")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def clear(self):
        self.head = None
        self._size = 0



if __name__ == "__main__":
    stack = Stack()
    
    print("Pushing elements: 10, 20, 30, 40")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    
   
    stack.display()
    
    # Peek top element
    print(f"\nTop element (peek): {stack.peek()}")
    
    # Check size
    print(f"Stack size: {stack.size()}")
    
    # Pop elements
    print(f"\nPopping: {stack.pop()}")
    print(f"Popping: {stack.pop()}")
    stack.display()
    
    # Check if empty
    print(f"Is stack empty? {stack.is_empty()}")
    
    # Pop remaining elements
    print(f"\nPopping: {stack.pop()}")
    print(f"Popping: {stack.pop()}")
    stack.display()
    
    # Try to pop from empty stack
    print(f"\nPopping from empty stack: {stack.pop()}")