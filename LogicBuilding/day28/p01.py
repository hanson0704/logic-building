'''Find Duplicate Characters in a String
Identify all characters that appear more than once in a string.
Input: "programming"
Output: ["r", "g", "m"]
'''

input_string = "programming"
char_count = {}
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
duplicates = [char for char, count in char_count.items() if count > 1]
print(duplicates)

'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day28\p01.py"
['r', 'g', 'm']'''