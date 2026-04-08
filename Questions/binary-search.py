# arr = [10,20,30,40,50]
# left = 0
# right = len(arr) - 1
# target = 40
# while left<=right:
#     mid = (left+right)//2

#     if arr[mid] == target:
#         print(mid)
#         break
#     elif arr[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

def binarysearch(arr,target,left,right):
    if left<=right:

        mid = (left+right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid]<target:
            return binarysearch(arr,target,mid+1,right)
        
        else:
            return binarysearch(arr,target,left,mid-1)
    else:
        return -1

nums = [1,2,3,4,5,6,7,8,9,10]
target = 8
result = binarysearch(nums,target,0,len(nums)-1)
print(result)

        

    
        



