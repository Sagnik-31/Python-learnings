n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
hash_dict = {}
for i in range(0,len(n)):
    hash_dict[n[i]] = hash_dict.get(n[i],0)+1

for num in m:
    if num in hash_dict:
        print(hash_dict[num])
    else:
        print("0")
    