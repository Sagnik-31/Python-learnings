r = int(input("enter number of rows: "))
c = int(input("enter number of cols: "))

A = []
for i in range(r):
    o = []
    for j in range(c):
        x = int(input(f"enter element: {i}{j} "))
        o.append(x)
    A.append(o)

print("original matrix: ")
for row in A:
    print(row)

T = []
for j in range(c):
    row = []
    for i in range(r):
        row.append(A[i][j])
    T.append(row)

print("transposed matrix: ")
for row in T:
    print(row)

