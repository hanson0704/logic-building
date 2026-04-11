'''Largest Prime Factor Write a program to find the largest prime factor of a given number.

Input: number = 28
Output: 7'''

number = int(input("Enter a number: "))
largest_prime_factor = None
for i in range(2, number + 1):
    while number % i == 0:
        largest_prime_factor = i
        number //= i
if largest_prime_factor is not None:
    print(f"The largest prime factor is: {largest_prime_factor}")
else:
    print("No prime factors found.")

''' Enter a number: 28
The largest prime factor is: 7
PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day21\p02.py"
Enter a number: 30
The largest prime factor is: 5'''