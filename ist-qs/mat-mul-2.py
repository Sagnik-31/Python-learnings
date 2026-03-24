
r1 = int(input("enter rows of matrix A: "))
c1 = int(input("enter cols of matrix A: "))

r2 = int(input("enter rows of matrix B: "))
c2 = int(input("enter cols of matrix B: "))

if c1!=r2:
    print("matrix multiplication not possible")
    exit(0)

A = []
for i in range(r1):
  o = []
  for j in range(c1):
    a = int(input(f"enter element first matrix:  {i}{j} "))
    o.append(a)
  A.append(o)
print("Matrix A: ")
print(A)

B = []
for i in range(r2):
  z = []
  for j in range(c2):
    x = int(input(f"enter element second matrix: {i}{j} "))
    z.append(x)
  B.append(z)
print("Matrix B: ")
print(B)

C = []
for i in range(r1):
  C.append([0]*c2)

for i in range(r1):
  for j in range(c2):
    for k in range(c1):
      C[i][j]+= A[i][k]*B[k][j]

print("resultant matrix: ")
print(C)
