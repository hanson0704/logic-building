'''Find the Frequency of Each Element in an Array
Calculate the frequency of each element in the array.
Input: [1, 2, 2, 3, 1, 4, 5, 1]
Output: {1: 3, 2: 2, 3: 1, 4: 1, 5: 1}
'''

input_array = [1, 2, 2, 3, 1, 4, 5, 1]
frequency = {}
for element in input_array:
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1
print(frequency)

'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day25\p01.py"
{1: 3, 2: 2, 3: 1, 4: 1, 5: 1}'''