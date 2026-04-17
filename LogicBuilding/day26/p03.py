'''Find All Substrings of a String
Print all possible substrings of a string.
Input: "abc"
Output: ["a", "b", "c", "ab", "bc", "abc"]
'''

input_string = "abc"
substrings = []
for i in range(len(input_string)):
    for j in range(i + 1, len(input_string) + 1):
        substrings.append(input_string[i:j])
print(substrings)

'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day26\p03.py"
['a', 'ab', 'abc', 'b', 'bc', 'c']'''