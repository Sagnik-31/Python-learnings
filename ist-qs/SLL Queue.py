class Queue:
    def __init__(self):
        self.head = None
    
    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None
    
    def enqueue(self,data):
        new_node = self.Node(data)
        if self.head == None:
            self.head = new_node 
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
    
    def dequeue(self):
        if self.head == None:
            print("Empty")
        else:
            x = self.head
            self.head = self.head.next
            print(x.data)

    def traversal(self):
        if self.head == None:
            print("Empty")
        else:
            curr = self.head
            while curr.next is not None:
                print(curr.data,end=" -> ")
                curr = curr.next

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.dequeue()
q.traversal()
