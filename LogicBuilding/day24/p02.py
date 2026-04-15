'''Remove Duplicates from an Array
Remove all duplicates from the given array and return the unique elements..
Input: [1, 2, 2, 3, 4, 1, 5]
Output: [1, 2, 3, 4, 5]
'''

nums = [1, 2, 2, 3, 4, 1, 5]
unique_nums = list(set(nums))
print(nums)
print("Unique Elements:", unique_nums)

'''PS D:\CodeMonk\LogicBuilding> python -u "d:\CodeMonk\LogicBuilding\day24\p02.py"
[1, 2, 2, 3, 4, 1, 5]
Unique Elements: [1, 2, 3, 4, 5]'''