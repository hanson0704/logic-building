'''Write a Program to Display All Factors of a Number:
Write a program to find and print all factors of a number entered by the user. For example:
Input: Enter a number: 28
Output: Factors of 28: 1, 2, 4, 7, 14, 28'''

num = int(input("Enter a number: "))
print(f"Factors of {num}:")
for i in range(1, num + 1):
    if num % i == 0:
        print(f"{i}")

'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day14\day14_p02.py"
Enter a number: 28
Factors of 28:
1
2
4
7
14
28
PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day14\day14_p02.py"
Enter a number: 10
Factors of 10:
1
2
5
10'''