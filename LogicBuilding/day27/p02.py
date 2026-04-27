'''Check if Two Strings are Rotations of Each Other Check if one string is a rotation of another. 
NOTE : the order of characters matters in rotations. Input: "abcd", "cdab" Output: "Yes"'''

def is_rotation(a, b):
    return "Yes" if len(a) == len(b) and b in (a + a) else "No"

print(is_rotation("abcd", "cdab"))

'''hanson@victus:~/Documents/CodeMonk/LogicBuilding$ python3 -u "/home/hanson/Documents/CodeMonk/LogicBuilding/day27/p02.py"
Yes'''