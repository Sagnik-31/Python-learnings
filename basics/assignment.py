digits = [1,2,3]
n = len(digits)
new_li = []
for i in range(0,len(digits)):
    digits[n] += 1
    new_li.append(digits[i])
print(new_li)