'''Program to Check Whether the Number is a Multiple of 7:
Write a program that verifies if a number entered by the user is a multiple of 7. For example:
Input: Enter a number: 14
Output: 14 is a multiple of 7.
'''

num = int(input("Enter a number: "))
if num%7==0:
    print(f"{num} is a multiple of 7")
else:
    print(f"{num} is not a multiple of 7")

'''
Output:

Enter a number: 14
14 is a multiple of 7

Enter a number: 49
49 is a multiple of 7

Enter a number: 50
50 is not a multiple of 7
'''