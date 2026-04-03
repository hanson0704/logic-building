'''Print Factorial Series:
Write a program that prints the factorial of numbers from 1 to N, where the user enters N. For example:
Input: Enter a number: 5
Output:
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
'''

number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
    print(f"{i}! = {factorial}")

'''Enter a number: 5
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day15\day15_p03.py"
Enter a number: 10
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
6! = 720
7! = 5040
8! = 40320
9! = 362880
10! = 3628800'''