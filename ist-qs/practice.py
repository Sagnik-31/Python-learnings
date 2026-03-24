r1 = int(input("enter rows for first matrix: "))
c1 = int(input("enter cols for first matrix: "))

r2 = int(input("enter rows for second matrix: "))
c2 = int(input("enter cols for second matrix: "))

A = []
for i in range(r1):
    o = []
    for j in range(c1):
        a = int(input(f"enter element first mat {i}{j} "))
        o.append(a)
    A.append(o)

print("first matrix: ", A)

B = []
for i in range(r2):
    l = []
    for j in range(c2):
        x = int(input(f"enter element first mat {i}{j} "))
        l.append(x)
    B.append(l)
print("second matrix: ",B)

C = []
for i in range(r1):
    C.append([0]*c2)





