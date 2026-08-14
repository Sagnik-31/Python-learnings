class Graph:
    def __init__(self,vertices):
        self.g = {}
        self.v = vertices
        for i in range(vertices):
            self.g[i] = []
    
    def add_edge(self,v1,v2):
        if v1 not in self.g:
            print(v1,"not present in graph")
        elif v2 not in self.g:
            print(v2,"not present in graph")
        else:
            self.g[v1].append(v2)
            self.g[v2].append(v1)
    
    def DFS(self,node,visited):
        if node not in self.g:
            print("node is not present")
            return
        if node not in visited:
            print(node)
            visited.add(node)
            for i in self.g[node]:
                self.DFS(i,visited)


visited = set()
v = int(input("enter number of vertices: "))
e = int(input("enter number of edges: "))
dfs = Graph(v)
for i in range(e):
    print("enter edge",i," ")
    v1 = int(input("u: "))
    v2 = int(input("v: "))
    dfs.add_edge(v1,v2)

node = int(input("enter start vertex: "))
print("DFS Traversal")
dfs.DFS(node,visited)


