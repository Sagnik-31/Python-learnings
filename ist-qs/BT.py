class BT:
    def __init__(self):
        self.root = None
    
    class Node:
        def __init__(self,data):
            self.data = data
            self.parent = None
            self.left = None
            self.right = None
    
    def create_node(self,data):
        n = self.Node(data)
        return n
    
    def assign_root(self,n):
        if self.root != None:
            print("root is present")
        else:
            self.root = n
    
    def assign_left(self,parent,left):
        if parent.left != None:
            print("Left already exist")
        else:
            parent.left = left
            left.parent = parent
    
    def assign_right(self,parent,right):
        if parent.right != None:
            print("right already exists")
        else:
            parent.right = right
            right.parent = parent
    
    def preorder(self,root):
        if root == None:
            return
        print(root.data, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)
    
    def postorder(self,root):
        if root == None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        self.postorder(root.data, end="")
    
    def inorder(self,root):
        if root == None:
            return
        self.inorder(root.left)
        self.inorder(root.data, end="")
        self.inorder(root.right)

bt = BT()

n = bt.create_node(12)
bt.assign_root(n)

n1 = bt.create_node(13)
n2 = bt.create_node(14)

bt.assign_left(n,n1)
bt.assign_right(n,n2)

bt.preorder(bt.root)