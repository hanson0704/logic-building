'''Program to Perform Swapping of Two Numbers:
Write a program to swap two numbers entered by the user. For example:
Input: Enter first number: 10, Enter second number: 20
Output:
   Before swapping: a = 10, b = 20
    After swapping: a = 20, b = 10'''

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(f"Before swapping: a = {a}, b = {b}")
a,b=b,a
print(f"After swapping: a = {a}, b = {b}")


'''PS D:\CodeMonk\LogicBuilding> python -u "d:\CodeMonk\LogicBuilding\day10\day10_p03.py"
Enter first number: 123
Enter second number: 321
Before swapping: a = 123, b = 321
After swapping: a = 321, b = 123'''
