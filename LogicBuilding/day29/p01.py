'''Matrix Multiplication
Multiply two matrices if the number of columns in the first matrix equals the number of rows in the second.
Input:
A = [[1, 2], [3, 4]], B = [[5, 6], [7, 8]]
Output:
[[19, 22], [43, 50]]
'''

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = []
for i in range(len(A)):
    row = []
    for j in range(len(B[0])):
        sum_product = 0
        for k in range(len(B)):
            sum_product += A[i][k] * B[k][j]
        row.append(sum_product)
    result.append(row)
print(result)

'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day29\p01.py"
[[19, 22], [43, 50]]'''