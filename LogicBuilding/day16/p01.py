'''Write a Program to Check Whether a Number is a Palindrome:
Write a program to determine if a number is a palindrome. For example:
Input: Enter a number: 121
Output: 121 is a palindrome.'''

number = int(input("Enter a number: "))
temp = number
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
if number == reverse:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")


'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day16\p01.py"
Enter a number: 121
121 is a palindrome.
PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day16\p01.py"
Enter a number: 200
200 is not a palindrome.
PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day16\p01.py"
Enter a number: 202
202 is a palindrome.'''