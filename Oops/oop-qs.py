class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll = roll_number
        self.marks = marks
        
    
    def calc_avg(self):
        for val in self.marks: 
            total += val
        self.avg = total / len(self.marks) 
        print("Hi", self.name, "your roll no is:", self.roll, "and your avg is", self.avg)

    def check_result(self):
        if self.avg >= 30:
            print("Passed")
        else:
            print("Failed")

s1 = Student("Sagnik", 52, [91,90,95])
s1.calc_avg()
s1.check_result()
    

        