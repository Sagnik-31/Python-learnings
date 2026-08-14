# brute force 

# k = 3
# nums = [3,9,5,6,7,2]
# n = len(nums)
# rotations = k%n

# for i in range(0,rotations):
#     e = nums.pop()
#     nums.insert(0,e)
# print(nums)

# or nums[:] = nums[n-k: ] + nums[ :n-k]

# optimal -> three reversals

nums = [3,9,5,6,7,2]
n = len(nums)
k = 3
def reverse(nums,left,right):

    while left < right:
        nums[left] , nums[right] = nums[right] , nums[left]
        left += 1
        right -= 1
    return nums

reverse(nums,n-k,n-1) # reverse last k elements
reverse(nums,0,n-k-1) # reverse first remaining elements
print(reverse(nums,0,n-1)) # reverse entire array