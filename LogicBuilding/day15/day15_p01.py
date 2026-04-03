'''Check Whether a Number is Prime or Not:
Write a program that checks if a number entered by the user is a prime number. For example:
Input: Enter a number: 17
Output: 17 is a prime number.'''
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day15\day15_p01.py"
Enter a number: 17
17 is a prime number.
PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day15\day15_p01.py"
Enter a number: 12
12 is not a prime number.'''