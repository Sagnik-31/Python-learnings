def fact(n):
    if(n==0 or n==1):
        return 1
    return n * fact(n-1)

x = int(input())
print(f"factorial of {x} is {fact(x)}")