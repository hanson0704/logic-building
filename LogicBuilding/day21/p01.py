'''Perfect Number Write a program to determine if a number is a perfect number.

Input: number = 6
Output: Perfect Number
Explanation: 6 is a perfect number because its divisors (1, 2, 3) sum up to 6.'''

number = int(input("Enter a number: "))
divisors_sum = 0
for i in range(1, number):
    if number % i == 0:
        divisors_sum += i
if divisors_sum == number:
    print(f"{number} is a Perfect Number be")
else:
    print(f"{number} is not a Perfect Number")


'''Enter a number: 6
6 is a Perfect Number be
PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day21\p01.py"
Enter a number: 5
5 is not a Perfect Number'''