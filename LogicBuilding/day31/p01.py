'''1. Factorial of a Number
Task: Define a recursive function factorial(n) that returns the product of all positive integers from 1 up to n.
Input: n = 5
Expected Output: 120'''

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
n = 5
result = factorial(n)
print(f"The factorial of {n} is: {result}")

n=10
result = factorial(n)
print(f"The factorial of {n} is: {result}")

'''PS D:\CodeMonk\LogicBuilding\day31> python -u "d:\CodeMonk\LogicBuilding\day31\p01.py"
The factorial of 5 is: 120
The factorial of 10 is: 3628800'''