nums = [1,4,9,16,25,36,49,100]
x = 49

i = 0
for el in nums:
    if(el == x):
        print("number found at index", i)
        break
    i += 1