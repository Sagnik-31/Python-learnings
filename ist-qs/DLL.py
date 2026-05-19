class DLL:
    def __init__(self):
        self.head = None
    
    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None
            self.prev = None
        
    def traversal(self):
        if self.head == None:
            print("DLL underflow")
        else:
            curr = self.head
            while curr is not None:
                print(curr.data, end="<->")
                curr = curr.next
    
    def add_begin(self,data):
        new_node = self.Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_end(self,data):
        new_node = self.Node(data)
        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
    
    def delete_begin(self):
        if self.head == None:
            print("DLL is already empty")
        elif self.head.next is None:
            self.head = None
            print("DLL is empty after deleting the element")
        else:
            self.head = self.head.next
            self.head.prev = None
    
    def delete_end(self):
        if self.head == None:
            print("DLL empty")
        elif self.head.next is None:
            self.head = None
            print("DLL is empty after deleting the element")
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.prev.next = None


    

dll = DLL()
dll.add_begin(5)
dll.add_end(6)
dll.add_end(7)
dll.add_end(8)
dll.add_end(9)
dll.traversal()
dll.delete_end()
dll.traversal()