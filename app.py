# armstrong
# n = 153
# num = n
# res = 0
# nod = len(str(n))

# while num!=0:
#     ld = num%10
#     res = res + (ld**nod)
#     num = num//10

# print((res==n))

# print factors of a given number
from math import sqrt 
result = []
num = int(input())

for i in range(1,int(sqrt(num))+1):

    if num%i == 0:
        result.append(i)

        if num//i != i:
            result.append(num//i)

print(result)


