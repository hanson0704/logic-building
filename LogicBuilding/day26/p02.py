'''Find the First Non-Repeating Character
Identify the first character that does not repeat in the string.
Input: "swiss"
Output: "w"
'''

input_string = "swiss"
char_count = {}
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
first_non_repeating = None
for char in input_string:
    if char_count[char] == 1:
        first_non_repeating = char
        break
if first_non_repeating:
    print(first_non_repeating)
else:
    print("No non-repeating character found")

'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day26\p02.py"
w'''