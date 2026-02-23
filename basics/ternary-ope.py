n = int(input())
rev=0
while n!=0: # algorithm for reversing the digits 
    ld = n%10
    rev = (rev*10) + ld 
    n = n//10
print(rev)