'''Print the Array in Sorted Order (Ascending and Descending):
Write a program to sort an array in ascending and descending order. For example:
Input: [5, 3, 8, 1]
Output:
Ascending: [1, 3, 5, 8]
Descending: [8, 5, 3, 1]
'''

nums = [5, 3, 8, 1]
ascending = sorted(nums)
print("Ascending:", ascending)
descending = sorted(nums, reverse=True)
print("Descending:", descending)

'''PS D:\CodeMonk\LogicBuilding> python -u "d:\CodeMonk\LogicBuilding\day22\p01.py"
Ascending: [1, 3, 5, 8]
Descending: [8, 5, 3, 1]'''