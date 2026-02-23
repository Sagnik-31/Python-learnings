nums = [2,3,2,4,5,5,6,6,7,8,9,9,8] #O(N)
freq_map = {}
x = 5
for i in range(0,len(nums)):

    if nums[i] in freq_map:
        freq_map[nums[i]] += 1
    else:
        freq_map[nums[i]] = 1
print(freq_map)
print(freq_map[x])