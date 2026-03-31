'''Write a Program to Find the GCD or HCF of Two Numbers:
Write a program where the user enters two numbers, and the program calculates their greatest common divisor (GCD) or highest common factor (HCF). For example:
Input: Enter two numbers: 60, 48
Output: The GCD of 60 and 48 is 12.'''

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}.")

'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day12\day12_p03.py"
Enter the first number: 60
Enter the second number: 48
The GCD of 60 and 48 is 12.
PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day12\day12_p03.py"
Enter the first number: 10
Enter the second number: 20
The GCD of 10 and 20 is 10.'''