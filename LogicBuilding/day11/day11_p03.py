'''Write a program where the user enters a number N, and the program calculates the sum of all natural numbers up to N. For example:

Input: Enter a number: 5
Output: The sum of the first 5 natural numbers is 15.'''

num = int(input("Enter a number: "))
sumOfNaturalNumbers = (num*(num+1))/2
print(f"The sum of the first {num} natural number is {sumOfNaturalNumbers}")

'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day11\day11_p03.py"
Enter a number: 5
The sum of the first 5 natural number is 15.0
PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day11\day11_p03.py"
Enter a number: 10
The sum of the first 10 natural number is 55.0'''