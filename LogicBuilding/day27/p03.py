'''Remove All Non-Alphabetic Characters
Remove all characters that are not letters.
Input: "abc123!@#"
Output: "abc"
'''

input_str = "abc123!@#"
output_str = ''.join(filter(str.isalpha, input_str))
print(output_str)

'''hanson@victus:~/Documents/CodeMonk/LogicBuilding$ python3 -u "/home/hanson/Documents/CodeMonk/LogicBuilding/day27/p03.py"
abc'''
