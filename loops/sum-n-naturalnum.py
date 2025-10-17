
# sum of first N natural numbers.

n = int(input("enter a number: "))
sum = 0
for i in range(0,n+1):
    sum += i
print(sum)

#or

'''
n = int(input("enter a number: "))

i = 0
sum = 0
while i <= n:
    sum += i
    i += 1
print(sum)
'''
