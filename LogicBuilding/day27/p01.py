'''Check Anagrams
Determine if two strings are anagrams of each other.
Input: "listen", "silent"
Output: "Anagrams"
'''

def are_anagrams(s1, s2):
    return "Anagrams" if sorted(s1) == sorted(s2) else "Not Anagrams"

print(are_anagrams("listen", "silent"))



'''hanson@victus:~/Documents/CodeMonk/LogicBuilding$ python3 -u "/home/hanson/Documents/CodeMonk/LogicBuilding/day27/p01.py"
Anagrams'''