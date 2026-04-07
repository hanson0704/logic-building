'''Check if an Integer Can Be Expressed as the Sum of Two Prime Numbers:
Write a program to check if a number can be expressed as the sum of two prime numbers. Print all such combinations. For example:
Input: Enter a number: 34
Output:
34 = 3 + 31
34 = 5 + 29
34 = 11 + 23
34 = 17 + 17
'''

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_sum_combinations(num):
    found = False
    for i in range(2, num // 2 + 1):
        if is_prime(i) and is_prime(num - i):
            print(f"{num} = {i} + {num - i}")
            found = True
    if not found:
        print(f"{num} cannot be expressed as sum of two primes.")

num = int(input("Enter a number: "))
prime_sum_combinations(num)

'''PS D:\CodeMonk\LogicBuilding> python -u "d:\CodeMonk\LogicBuilding\day16\p02.py"
Enter a number: 34
34 = 3 + 31
34 = 5 + 29
34 = 11 + 23
34 = 17 + 17
PS D:\CodeMonk\LogicBuilding> python -u "d:\CodeMonk\LogicBuilding\day16\p02.py"
Enter a number: 25
25 = 2 + 23
PS D:\CodeMonk\LogicBuilding> python -u "d:\CodeMonk\LogicBuilding\day16\p02.py"
Enter a number: 10
10 = 3 + 7
10 = 5 + 5'''