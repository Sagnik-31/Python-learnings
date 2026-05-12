class BST:

    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key == None:  # empty tree 
            self.key = data

        if self.key == data:  # duplicate value then do nothing
            return
        
        if self.key > data:

            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)

        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def search(self,data):
        if self.key == data:
            print("Node is found")
            return

        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in tree")

        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not found in tree")

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inorder()
    


root = BST(10)
list = [6,3,1,6,98,3,7]
for i in list:
    root.insert(i)
root.search(70)
root.inorder()
    
