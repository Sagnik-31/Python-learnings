class Graph:
    def __init__(self,vertices):
        self.v = vertices
        self.g = {}

        for i in range(vertices):
            self.g[i] = []
    
    def add_edge(self,v1,v2):
        self.g[v1].append(v2)
        self.g[v2].append(v1)
    
    def DFS(self,node,visited):
        if node not in visited:
            print(node)
            visited.add(node)
            for i in self.g[node]:
                self.DFS(i,visited)

visited = set()

