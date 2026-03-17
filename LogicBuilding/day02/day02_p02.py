'''Program to Check Whether the Number is Divisible by 5:
Write a program that determines if a number entered by the user is divisible by 5. For example:
Input: Enter a number: 25
Output: 25 is divisible by 5.'''

num=int(input("Enter an number: "))
if(num%5==0):
    print(f"{num} is divisible by 5")
else:
    print(f"{num} is not divisible by 5")


'''
Output:

Enter an number: 25
25 is divisible by 5

Enter an number: 16
16 is not divisible by 5

Enter an number: 155
155 is divisible by 5
'''
