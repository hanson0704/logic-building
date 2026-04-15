'''Finding the Longest Sequence of Consecutive 1s in a Binary Array
Write a program to find the longest sequence of consecutive 1s in a binary array.
Input: binaryArray = [1, 1, 0, 1, 1, 1]
Output: 3
'''
binaryArray = [1, 1, 0, 1, 1, 1]
max_length = 0
current_length = 0
for num in binaryArray:
    if num == 1:
        current_length += 1
        max_length = max(max_length, current_length)
    else:
        current_length = 0
print(binaryArray)
print(max_length)

'''PS D:\CodeMonk\LogicBuilding> python -u "d:\CodeMonk\LogicBuilding\day22\p02.py"
[1, 1, 0, 1, 1, 1]
3'''