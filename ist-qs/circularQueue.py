class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.items = [None] * size
        self.front = self.rear = -1

    def enqueue(self,value):
        if (self.rear + 1) % self.size == self.front: # full
            print("Queue is full")
        
        elif self.front == -1:  # if empty
            self.front = self.rear = 0
            self.items[self.rear] = value
        
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = value
    
    def dequeue(self):
        if self.front == -1:  # empty
            print("queue is empty")
        
        elif self.front == self.rear: # only one element
            print(self.items[self.front])   
            self.front = self.rear = -1

        else:
            print(self.items[self.front])
            self.front = (self.front + 1) % self.size
    
    def display(self):
        if self.front == -1:
            print("Queue is empty")
            return

        i = self.front
        while True:
            print(self.items[i],end=" ")

            if i == self.rear:
                break

            i = (i+1) % self.size
        print()
    
    def first(self):
        if self.front == -1:
            print("Queue is empty")
            return None

        return self.items[self.front]

cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.display()
