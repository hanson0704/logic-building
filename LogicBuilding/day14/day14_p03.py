'''Amstrong Number or Not:
Write a program to check if a number is an Armstrong number. For example:
Input: Enter a number: 153
Output: 153 is an Armstrong number.
'''

num = int(input("Enter a number: "))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if num == sum:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
    
'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day14\day14_p03.py"
Enter a number: 121
121 is not an Armstrong number.
PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day14\day14_p03.py"
Enter a number: 153
153 is an Armstrong number.'''