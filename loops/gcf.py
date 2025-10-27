a = int(input("enter a num: "))
b = int(input("enter another num: "))
gcf = 1
for i in range(1, min(a,b)):
    if(a%i == 0 and b%i == 0):
        gcf = i

print(gcf)
    