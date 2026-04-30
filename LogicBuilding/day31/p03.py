''' Fibonacci Sequence
Task: Create a recursive function fibonacci(n) that returns the number in the Fibonacci sequence. Then, use a loop to print the sequence up to the term.
Input: n = 5
Expected Output: 0, 1, 1, 2, 3'''

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
n = 5
print(f"Fibonacci sequence up to term {n}: ", end="")
for i in range(n):
    print(fibonacci(i), end=" ")
n = 10
print(f"\nFibonacci sequence up to term {n}: ", end="")
for i in range(n):
    print(fibonacci(i), end=" ")
    
    '''PS D:\CodeMonk\LogicBuilding\day31> python -u "d:\CodeMonk\LogicBuilding\day31\p03.py"
Fibonacci sequence up to term 5: 0 1 1 2 3
Fibonacci sequence up to term 10: 0 1 1 2 3 5 8 13 21 34 '''