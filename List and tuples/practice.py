num  = int(input())
temp = num
nod = len(str(num))
total = 0

while temp>0:
    ld = temp%10
    total += ld**nod
    temp //= 10
    
if total==num:
    print("Armstrong number")

