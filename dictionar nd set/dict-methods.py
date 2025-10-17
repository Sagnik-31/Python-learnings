student = {
    "name" : "sagnik ghosh",
    "subjects" : {
        "phy" : 90,
        "chem" : 95,
        "math" : 85
    } 
}
print(list(student.keys())) #type casted
print(len(student))

print(student.keys()) #returns all keys
print(student.values()) # returns all values
print(student.items()) # returns all (key,val) pairs as tuples
print(student.get("name")) # returns the value

student.update({"city" : "bangalore"}) # inserts a new key:value pair
# or
# new_dict = {"city" : "bangalore"}
# student.update(new_dict)