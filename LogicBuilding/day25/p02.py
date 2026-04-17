'''Check Palindrome
Determine if a string reads the same backward as forward.
Input: "madam"
Output: "Palindrome"
'''

input_string = "Madam"
if input_string.lower() == input_string[::-1].lower():
    print("Palindrome")
else:
    print("Not a Palindrome")
    

'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day25\p02.py"
Palindrome'''