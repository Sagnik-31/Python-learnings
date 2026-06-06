v = int(input("enter number of vertices: "))
A = []
for i in range(v):
    A.append([0]*v)

e = int(input("enter number of edges: "))
edges = []

for m in range(e):
    print("enter",m+1,"edges: ")
    i = int(input("u: "))
    j = int(input("j: "))
    A[i-1][j-1] = 1
    A[j-1][i-1] = 1
    edges.append((i,j))
for row in A:
    print(row)


class GraphList:
    head = None
    class NodeEdge:
        def __init__(self,data):
            self.edge = data
            self.next = None
    
    class NodeVertex:
        def __init__(self,data):
            self.data = data
            self.next_vertex = None
            self.edge_list = None
    
    def insert_vertex(self,data):
        n = self.NodeVertex(data)
        if self.head == None:
            self.head = n
        else:
            curr = self.head
            while curr.next_vertex is not None:
                curr = curr.next_vertex
            curr.next_vertex = n
    
    def insert_edge(self,u,v):
        t = self.head
        while t is not None and t.data != u:
            t = t.next_vertex
        if t == None:
            print("Vertex is not found")
            return 
        r = t.edge_list
        n = self.NodeEdge(v)
        if r == None:
            t.edge_list = n
        else:
            while r.next is not None:
                r = r.next
            r.next = n

    def traverse(self):
        if self.head == None:
            print("Graph empty")
        else:
            d = self.head
            while d is not None:
                print(d.data, end="->")
                b = d.edge_list
                while b is not None:
                    print(b.edge,end="->")
                    b = b.next
                print(None)
                d = d.next_vertex

g = GraphList()
for i in range(v+1):
    g.insert_vertex(i)

for u,v in edges:
    g.insert_edge(u,v)
    g.insert_edge(v,u)
g.traverse()


                









