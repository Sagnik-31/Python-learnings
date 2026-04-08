r1 = int(input("enter no of rows of first matrix :"))
c1 = int(input("enter no of cols of second matrix: "))

r2 = int(input("enter no of rows of second matrix :"))
c2 = int(input("enter no of cols of second matrix: "))

if c1!=r2:
    print("mat mult not possible")
    exit(0)

A=[]
for i in range(r1):
    o=[]
    for j in range(c1):
        x = int(input(f"enter element of first matrix {i}{j}: "))
        o.append(x)
    A.append(o)
print(A)

B = []
for i in range(r2):
    z = []
    for j in range(c2):
        v = int(input(f"enter element of second matrix {i}{j}: "))
        z.append(v)
    B.append(z)
print(B)

C = []
for i in range(r1):
    C.append([0]*c2)

for i in range(r1):
    for j in range(c2):
        for k in range(c1):
            C[i][j] += A[i][k] * B[k][j]
print(C)

# r1 = int(input("enter no of rows of first matrix :"))
# c1 = int(input("enter no of cols of first matrix: "))

# r2 = int(input("enter no of rows of second matrix :"))
# c2 = int(input("enter no of cols of second matrix: "))

# A = []
# for i in range(r1):
#     o = []
#     for j in range(c1):
#         x = int(input(f"enter element {i}{j}: "))
#         o.append(x)
#     A.append(o)
# print(A)

# B = []
# for i in range(r2):
#     d = []
#     for j in range(c2):
#         f = int(input(f"enter element {i}{j}"))
#         d.append(f)
#     B.append(d)
# print(B)

# res = []
# for i in range(len(A)):
#     p = []
#     for j in range(len(A[0])):
#         p.append(A[i][j]+B[i][j])
#     res.append(p)

# print(res)