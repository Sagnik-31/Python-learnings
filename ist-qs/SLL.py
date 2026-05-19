class SL:
    def __init__(self):
        self.head = None
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    

    def add_at_beggining(self, data):
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node

    
    def add_at_end(self,data):
        new_node = self.Node(data)
        if self.head == None:
            self.head = new_node

        else:                # go to last node
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def delete_begin(self):
        if self.head == None:
            print("LL is empty")
        else:
            x = self.head
            self.head = self.head.next
            return x.data

    def traversal(self):
        if self.head == None:
            print("LL is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.data, "-->", end=" ")
                curr = curr.next

    def delete_end(self):
        if self.head == None:
            print("LL is empty")
        elif self.head.next is None:
            x = self.head
            self.head = None
            return x.data
        else:
            curr = self.head   # go to second last node

            while curr.next.next is not None:
                curr = curr.next 
            x = curr.next
            curr.next = None
            return x.data

LL = SL()
LL.add_at_beggining(5)
LL.add_at_end(6)
LL.add_at_end(7)
LL.add_at_end(8)
print(LL.delete_begin())
LL.traversal()