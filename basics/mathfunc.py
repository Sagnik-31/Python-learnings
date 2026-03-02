li = [1,2,3,4,5,6,7,8]

left = 0
right = len(li)-1
while right>=left:
    li[right] , li[left] = li[left] , li[right]
    left += 1
    right -= 1
print(li)