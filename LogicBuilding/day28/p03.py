'''Matrix Addition
Add two matrices of the same dimensions.
Input: 
A = [[1, 2], [3, 4]], B = [[5, 6], [7, 8]]
Output:
[[6, 8], [10, 12]]
'''

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    result.append(row)
print(result)

'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day28\p03.py"
[[6, 8], [10, 12]]'''