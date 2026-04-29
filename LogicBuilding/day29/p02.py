'''Search an Element in a Matrix
Search for a given element in a matrix and return its position.
Input:
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], Target = 5
Output:
Position: (1, 1) (0-based index)
'''

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
target = 5
position = None
for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j] == target:
            position = (i, j)
            break
    if position is not None:
        break
if position is not None:
    print(f"Position: {position}")
else:
    print("Element not found")

'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day29\p02.py"
Position: (1, 1)'''