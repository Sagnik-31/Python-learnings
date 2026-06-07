import heapq
class Graph:
    def __init__(self,vertices,directed):
        self.v = vertices
        self.graph = {}
        self.directed = directed

        for i in range(vertices):
            self.graph[i] = []

    def add_edge(self, v1, v2, cost):
        if v1 not in self.graph:
            print(v1, "not present in graph")
        elif v2 not in self.graph:
            print(v2, "not present in graph")
        else:
            if self.directed == True:
                self.graph[v1].append((v2, cost))
            else:
                self.graph[v1].append((v2, cost))
                self.graph[v2].append((v1,cost))

    def dijkstra(self, start):
        distance = {vertex: float("inf") for vertex in self.graph}
        distance[start] = 0

        queue = [(0, start)]  

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if current_distance > distance[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                new_distance = current_distance + weight

                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    heapq.heappush(queue, (new_distance, neighbor))

        return distance


vertices = int(input("enter no of vertices: "))

choice = int(input("enter 1 for directed and 0 for undirected: "))

if choice == 1:
    g = Graph(vertices,True)
else:
    g = Graph(vertices, False)

edges = int(input("enter no of edges: "))

for i in range(edges):
    print("enter edge",i+1)

    u = int(input("enter source vertex: "))
    v = int(input("enter destination vertex: "))
    w = int(input("enter weight: "))
    print()

    g.add_edge(u,v,w)

start = int(input("enter source vertex: "))
print()

result = g.dijkstra(start)

print(result)