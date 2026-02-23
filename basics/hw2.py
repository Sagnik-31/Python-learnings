#username must not contain spaces
#username no more than 12 characters
#username must not contain digits

username = input("enter your name: ")

if len(username) > 12:
    print("username cannot contain digits")

elif not username.find(" ") == -1: #username.find(" ") returns -1 if there are NO spaces.
    print("username cant contain spaces")

elif not username.isalpha():
    print("username cant contain numbers")
    
else:
    print(f"Welcome {username}")
