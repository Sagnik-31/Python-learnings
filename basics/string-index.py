# li = ["Apple", 20, 30, 20, "aPple"]
# left = 0
# right = len(li) - 1

# while left < right:
#     if li[left] != li[right]:
#         print("Not Palindrome")
#         break
#     left += 1
#     right -= 1
# else:
#     print("Palindrome")

li = ["Apple", 20, 30, 20, "apPle"]

left = 0
right = len(li) - 1

while left < right:
    a = li[left]
    b = li[right]
    if isinstance(a, str) and isinstance(b, str):
        if a.lower() != b.lower():
            print("Not Palindrome")
            break
    else:
        if a != b:
            print("Not Palindrome")
            break

    left += 1
    right -= 1
else:
    print("Palindrome")
