# def print_list(list, i):
#     if(i==len(list)):
#         return
#     print(list[i])
#     print_list(list, i+1) 

# fruits = ["mango", "apple", "banana", "litchi"]
# print_list(fruits,0)

def print_list(list, i):
    if(i==len(list)):
        return
    print(list[i])
    return print_list(list,i+1)


fruits = ["litchi", "banana", "apple", "mango"]
print_list(fruits, 0)
