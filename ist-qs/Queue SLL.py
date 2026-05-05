class Queue:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, x):
        n = self.Node(x)
        if self.rear is None:
            self.front = n
            self.rear = n
        else:
            self.rear.next = n
            self.rear = n

    def dequeue(self):
        if self.front is None:
            return None
        x = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return x.data

    def is_empty(self):
        return self.front is None

    def traverse(self):
        if self.front is None:
            print("Queue is empty")
            return
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print(None)
        


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.traverse()
print("Dequeue:", q.dequeue())
q.traverse()
