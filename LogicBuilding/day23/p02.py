'''Find the Majority Element in an Array
Find the element that appears more than n/2 times in the array (if any).
Input: [3, 3, 4, 2, 4, 4, 2, 4, 4]
Output: Majority Element: 4
'''

nums = [3, 3, 4, 2, 4, 4, 2, 4, 4]
frequency = {}
for num in nums:
    frequency[num] = frequency.get(num, 0) + 1
majority_element = None
for num, count in frequency.items():
    if count > len(nums) // 2:
        majority_element = num
        break
print(nums)
print("Majority Element:", majority_element)


'''PS D:\CodeMonk\LogicBuilding> python -u "d:\CodeMonk\LogicBuilding\day23\p02.py"
[3, 3, 4, 2, 4, 4, 2, 4, 4]
Majority Element: 4'''