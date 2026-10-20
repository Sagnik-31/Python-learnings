# lambda argument: expression
add10 = lambda x: x+10
print(add10(5))

pt = [(1,2),(15,1),(5,-1),(10,4)]
pt_sort = sorted(pt, key=lambda x: x[1])
print(pt_sort)