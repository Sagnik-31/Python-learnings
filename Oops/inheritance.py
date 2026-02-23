class Student:

    def __init__(self,name,grade,percentage):
        self.name = name
        self.grade = grade
        self.percentage = percentage 
    
    def student_details(self):
        print(self.name, "is in", self.grade, "with", self.percentage, "%")

class GraduateStudent(Student): # this class inherits from student

    def __init__(self,name,grade,percentage,stream):
        super().__init__(name,grade,percentage) #call parent class initialiazer
        self.stream = stream
    
    def student_details(self):
        super().student_details() # method inherit from parent class
        print("student stream: ", self.stream)
       
grad_student = GraduateStudent("Vishakha", 12, 94, "PCM")
grad_student.student_details()


    