def print_list(list, i):
    if(i==len(list)):
        return
    print(list[i])
    print_list(list, i+1)

fruits = ["mango", "apple", "banana", "litchi"]
print_list(fruits,0)


# fruits = ["mango", "apple", "banana", "litchi"]
# i = 0
# while i<len(fruits):
#     print(fruits[i])
#     i += 1