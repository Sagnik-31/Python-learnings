class student:
    college_name = "ABC College" # college ki name same chaiye isiliye init ke andr nhi gye

    def __init__(self, name, marks): # parameterized constructor
        self.name = name    # .name use kiya kyuki har object ki name alag hogi
        self.marks = marks
        print("adding a new student...")

s1 = student("sagnik", 90)
print(s1.name, s1.marks)
print(s1.college_name)