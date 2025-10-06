# while loop = execute some code while some condition remains true 

name = input("Enter your name: ")

while name == "":
    print("you did not enter your name")
    name = input("enter your name: ")
    
print(f"Hello {name}")