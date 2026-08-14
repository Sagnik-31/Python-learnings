class LL:
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None
    
    def add_begin(self,data):
        n = self.Node(data)
        n.next = self.head
        self.head = n
    
    def add_end(self,data):
        n = self.Node(data)
        if self.head == None:
            self.head = n
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = n
    
    def delete_end(self):
        if self.head == None:
            print("LL empty")
        else:
            curr = self.head
            while curr.next.next is not None:
                curr = curr.next
            curr.next = None
    
    def traversal(self):
        if self.head == None:
            print("empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.data,end=" -> ")
                curr = curr.next


ll = LL()
ll.add_end(1)
ll.add_end(2)
ll.add_end(3)
ll.add_end(4)
ll.traversal()

            


    

