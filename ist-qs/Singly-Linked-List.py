class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node

        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def remove_from_end(self):

        if self.head is None:
            print("SLL is empty/underflow")
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next is not None:
            current = current.next

        current.next = None


    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def remove_from_beginning(self):
        if self.head is None:
            print("SLL is empty/underflow")
            return
        self.head = self.head.next
    
    def traverse(self):
        if self.head == None:
            print("SLL is empty/underflow")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end='->')
                curr = curr.next

SLL = SinglyLinkedList()

SLL.insert_at_end(6)
SLL.insert_at_end(5)
SLL.insert_at_end(9)
SLL.traverse()