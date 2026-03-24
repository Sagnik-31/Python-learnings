r = int(input("enter no of rows: "))
c = int(input("enter no of coloumns: "))
A = []
for i in range(r):
  temp = []
  for j in range(c):
    a = int(input(f"enter element:  {i}{j} "))
    temp.append(a)
  A.append(temp)
print(A)

print()

B = []
for i in range(r):
    temp2 = []
    for j in range(c):
        k = int(input(f"enter element: {i}{j} "))
        temp2.append(k)
    B.append(temp2)
print(B)

result = []
for i in range(len(A)):
    output = []
    for j in range(len(A[0])):
        output.append(A[i][j]+B[i][j])
    result.append(output)
print(result)

