nums = [2,3,2,4,5,5,6,6,7,8,9,9,8] #O(N)
hash_map = {}

for i in range(0,len(nums)):
    hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
    
print(hash_map)