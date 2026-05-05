class CircularQueue:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            self._resize()
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1  

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def first(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.front]



cq = CircularQueue()
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
print("First:", cq.first())  
print("Dequeue:", cq.dequeue())  
print("First:", cq.first())  
cq.enqueue(4)
cq.enqueue(5)
