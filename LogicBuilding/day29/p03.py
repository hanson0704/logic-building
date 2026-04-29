'''Matrix Transpose
Find the transpose of a matrix (convert rows to columns and vice versa).
Input:
A = [[1, 2, 3], [4, 5, 6]]
Output:
[[1, 4], [2, 5], [3, 6]]
'''

A = [[1, 2, 3], [4, 5, 6]]
transpose = []
for i in range(len(A[0])):
    row = []
    for j in range(len(A)):
        row.append(A[j][i])
    transpose.append(row)
print(transpose)

'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day29\p03.py"
[[1, 4], [2, 5], [3, 6]]'''