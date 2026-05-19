
n = int(input("enter number of vertices: "))
z = int(input("enter number of edges: "))

adj_matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(0) 
    adj_matrix.append(row) 


print("\nEnter edges (format: vertex1 vertex2):")
for i in range(z):
    u, v = map(int, input(f"Edge {i+1}: ").split())
    
    
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1


print("\nAdjacency Matrix:")
for row in adj_matrix:
    print(row)