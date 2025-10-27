n = input("enter a string: ")
count = 0
for i in n:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count += 1
        print(i)
print("total number of vowel is", count)

