nums = [5,7,8,4,1,6,9,2]

for i in range(0,len(nums)):
    min_ind = i

    for j in range(i+1,len(nums)):
       if nums[j] < nums[min_ind]:
           min_ind = j
    
    nums[i] , nums[min_ind] = nums[min_ind] , nums[i]

print(nums)

