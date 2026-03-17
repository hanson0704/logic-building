# Program to Check Whether the Number is Odd or Even:
# Write a program that checks whether a number entered by the user is odd or even. For example:
# Input: Enter a number: 7
# Output: 7 is an odd number

num=int(input("Enter an number: "))
if num%2==0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")
    

'''
Output:

Enter an number: 7
7 is an odd number

Enter an number: 6
6 is an even number
'''