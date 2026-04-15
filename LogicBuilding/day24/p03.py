'''Move Zeros to the End of an Array
Move all zeros in the array to the end while maintaining the relative order of non-zero elements.
Input: [0, 1, 2, 0, 3, 4, 0]
Output: [1, 2, 3, 4, 0, 0, 0]
'''

nums = [0, 1, 2, 0, 3, 4, 0]
print(nums)
non_zero_index = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[non_zero_index] = nums[i]
        non_zero_index += 1
for i in range(non_zero_index, len(nums)):
    nums[i] = 0
print(nums)

''''PS D:\CodeMonk\LogicBuilding> python -u "d:\CodeMonk\LogicBuilding\day24\p03.py"
[0, 1, 2, 0, 3, 4, 0]
[1, 2, 3, 4, 0, 0, 0]'''