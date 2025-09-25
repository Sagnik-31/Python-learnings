name = "sagnik"
age = 18
cgpa = 9.5
is_student = True

print(type(name))      # Output: <class 'str'>
print(type(age))       # Output: <class 'int'>
print(type(cgpa))      # Output: <class 'float'> 

new_age = float(age)  # Convert int to float
print(new_age)

another_age = str(age)   # Convert int to string
print(another_age, type(another_age))