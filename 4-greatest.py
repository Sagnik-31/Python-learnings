a = int(input("enter 1st num: "))
b = int(input("enter 2nd num: "))
c = int(input("enter 3rd num: "))
d = int(input("enter 4th num: "))

if(a>b and a>c and a>d):
    print(f"{a} is greatest")
elif(b>c and b>d):
    print(f"{b} is greatest")
elif(c>d):
    print(f"{c} is greatest")
else:
    print(f"{d} is greatest")