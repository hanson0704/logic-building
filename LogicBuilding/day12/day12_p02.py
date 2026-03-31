'''Print Fibonacci Series:
Write a program to print the Fibonacci series up to a number N entered by the user. For example:
Input: Enter the number of terms: 7
Output: Fibonacci series: 0 1 1 2 3 5 8'''

num = int(input("Enter the number of terms: "))
a, b = 0, 1
fibonacci_series = []
for _ in range(num):
    fibonacci_series.append(a)
    a, b = b, a + b
print("Fibonacci series:", ' '.join(map(str, fibonacci_series)))


'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day12\day12_p02.py"
Enter the number of terms: 5
Fibonacci series: 0 1 1 2 3
PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day12\day12_p02.py"
Enter the number of terms: 7
Fibonacci series: 0 1 1 2 3 5 8'''