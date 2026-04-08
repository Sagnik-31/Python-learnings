def pascal_triangle(numRows):
    if numRows == 0:
        return []
    
    ans = [[1]]
    
    for i in range(1, numRows):
        row = [1]
        for j in range(1, i):
            row.append(ans[i-1][j-1] + ans[i-1][j])
        row.append(1)
        ans.append(row)
    
    return ans

numRows = int(input("enter number of rows: "))
triangle = pascal_triangle(numRows)

for row in triangle:
    print(row)