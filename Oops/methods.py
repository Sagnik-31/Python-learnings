class student:
    college_name = "ABC College" 

    def __init__(self, name, marks): 
        self.name = name   
        self.marks = marks

    def info(self):
        print("welcome student", self.name)
        print("Marks is: ", self.marks )

s1 = student("sagnik", 90)
s1.info()


