'''Print Prime Numbers Within a Range:
Write a program to display all prime numbers between two intervals entered by the user. For example:
Input: Enter two numbers: 10, 30
Output: Prime numbers between 10 and 30: 11, 13, 17, 19, 23, 29
'''

lowerRange = int(input("Enter the lower range: "))
upperRange = int(input("Enter the upper range: "))
print(f"Prime numbers between {lowerRange} and {upperRange}: ", end="")
for num in range(lowerRange, upperRange + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, end=" ")

'''Enter the lower range: 1
Enter the upper range: 5
Prime numbers between 1 and 5: 2 3 5 
PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day15\day15_p02.py"
Enter the lower range: 10
Enter the upper range: 20
Prime numbers between 10 and 20: 11 13 17 19 '''
            