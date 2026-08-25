nums = [1,2,3,3,3,3,3,5,6,8,9,9,10]
n = len(nums)
target = 3
first = -1
last = -1
for i in range(n):
    if nums[i] == target:
        if first == -1:
            first = i

        last = i

if first == -1:
    print(0)

print(last-first+1)