'''Find the Second Largest Element in an Array
Find the second largest element in the array.
Input: [10, 20, 4, 45, 99]
Output: Second Largest: 45
'''

nums = [10, 20, 4, 45, 99]
largest = second_largest = float('-inf')
for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    elif largest > num > second_largest:
        second_largest = num
print(nums)
print("Second Largest:", second_largest)

'''PS D:\CodeMonk\LogicBuilding> python -u "d:\CodeMonk\LogicBuilding\day24\p01.py"
[10, 20, 4, 45, 99]
Second Largest: 45'''
