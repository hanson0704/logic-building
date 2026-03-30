'''Write a Program to Find the Largest Number Among Three Numbers:

Write a program where the user enters three numbers, and the program finds and displays the largest number among them. For example:

Input: Enter three numbers: 12, 25, 7
Output: The largest number is: 25'''

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1>=num2 and num1>=num3:
    largest = num1
elif num2>=num1 and num2>=num3:
    largest = num2
else:
    largest = num3
print("The largest number is:", largest)

'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day11\day11_p01.py"
Enter the first number: 25
Enter the second number: 62
Enter the third number: 99
The largest number is: 99'''