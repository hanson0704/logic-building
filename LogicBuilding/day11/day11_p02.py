'''Write a Program to Check Whether a Year Entered by the User is a Leap Year:

Write a program to determine whether a given year is a leap year. For example:

Input: Enter a year: 2024
Output: 2024 is a leap year.
Write a Program to Calculate the Sum of the First N Natural Numbers:'''

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day11\day11_p02.py"
Enter a year: 2024
2024 is a leap year.
PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day11\day11_p02.py"
Enter a year: 2025
2025 is not a leap year.
'''