'''Find the Missing Number in an Array
Given an array of numbers from 1 to n with one number missing, find the missing number.
Input: [1, 2, 4, 5, 6]
Output: Missing Number: 3
'''

nums = [1, 2, 4, 5, 6]
n = len(nums) + 1
total_sum = n * (n + 1) // 2
array_sum = sum(nums)
missing_number = total_sum - array_sum
print(nums)
print("Missing Number:", missing_number)

'''PS D:\CodeMonk\LogicBuilding> python -u "d:\CodeMonk\LogicBuilding\day23\p01.py"
[1, 2, 4, 5, 6]
Missing Number: 3'''