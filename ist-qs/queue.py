# dequeue , enqueue , front , rear , size , is_empty
# TC -> O(N)

class Queue:
    def __init__(self):
        self.items = []
        self.l = 0
    
    def enqueue(self,val):
        self.items.append(val)
        self.l += 1
    
    def dequeue(self):
        if self.l == 0:
            return "queue is empty cannot remove element"
        self.l -= 1
        x = self.items.pop(0)
        return x
      
    
    def front(self):
        if self.l == 0:
            return "queue is empty cant view front element"
        return self.items[0]
    
    def rear(self):
        if self.l == 0:
            return "queue is empty cant view rear element"
        return self.items[-1]
    
    def size(self):
        return self.l
    
    def is_empty(self):
        if self.l == 0:
            return "True"
        else:
            return "False"

queue = Queue()
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
queue.enqueue(8)
queue.enqueue(9)
queue.enqueue(10)
print(queue.dequeue())  

    
