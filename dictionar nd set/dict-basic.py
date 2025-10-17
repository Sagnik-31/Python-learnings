# used to store key:value pairs
# unordered , mutable , dont allow duplicate keys

# value can be of any data type but key cant be list or dict

info = {
    "key" : "value",
    "name" : "sagnik",
    "age" : 18,
    "marks" : 90,
    "subjects" : ["python" , "html", "maths"],
    "topic" : ("dict", "set")
}
print(info)
info["name"] = "sagnik ghosh" #overwrite
print(info["name"])

null_dict = {}
null_dict["name"] = "sagnik"
print(null_dict)
