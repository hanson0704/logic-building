'''Write a Program to Find the LCM of Two Numbers:
Write a program where the user enters two numbers, and the program calculates their least common multiple (LCM). For example:
Input: Enter two numbers: 4, 6
Output: The LCM of 4 and 6 is 12.
'''

def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

gcd = find_gcd(num1, num2)

lcm = (num1 * num2) // gcd

print(f"The LCM of {num1} and {num2} is {lcm}")


'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day13\day13_p01.py"
Enter first number: 4
Enter second number: 6
The LCM of 4 and 6 is 12
PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day13\day13_p01.py"
Enter first number: 5
Enter second number: 1
The LCM of 5 and 1 is 5'''