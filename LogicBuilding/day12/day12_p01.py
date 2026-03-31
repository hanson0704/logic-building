'''Factorial of a Number Using a For Loop:
Write a program to calculate the factorial of a number entered by the user using a for loop. For example:
Input: Enter a number: 4
Output: Factorial of 4 is 24.
'''
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num} is {factorial}.")

'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day12\day12_p01.py"
Enter a number: 4
Factorial of 4 is 24.
PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day12\day12_p01.py"
Enter a number: 5
Factorial of 5 is 120.'''