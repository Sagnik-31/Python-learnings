class BT:
    def __init__(self):
        self.root = None
        self.size = 0
    
    class Node:
        def __init__(self,d,p,l=None,r=None):
            self.data = d
            self.parent = p
            self.left = l
            self.right = r

    def create_node(self,d,p,l=None,r=None):
        n = self.Node(d,p,l,r)
        return n
    
    def assign_root(self,n):
        if self.root!=None:
            print("Root is already present")
            return None
        self.root = n

    def assign_left(self, parent, left):

        if parent.left != None: 
            print("Left child already exists")
            return None

        parent.left = left
        left.parent = parent
    
    def assign_right(self,parent,right):
        
        if parent.right!= None:
            print("Right child already exists")
            return None
        
        parent.right = right
        right.parent = parent

    def preorder(self,root):
        if root==None:
            return None

        else:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)
    
    def inorder(self,root):
        if root==None:
            return None
        else:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    def postorder(self,root):
        if root == None:
            return None
        else:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)

    

    

bt = BT()
n = bt.create_node(12,None)
bt.assign_root(n)
    
       