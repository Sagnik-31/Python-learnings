n = int(input("Enter a number: "))
length = len(str(n))
temp = n
sum=0
while temp>0:
    ld = temp%10
    sum += ld ** length
    temp = temp//10

if( sum == n):
    print("Armstrong number")
else:
    print("Not an armstrong number")

