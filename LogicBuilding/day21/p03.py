'''Sum of the series of n terms Write a program to calculate the sum of the series 1 + 1/2 + 1/3 + ... + 1/n up to the nth term.

Input: n = 4
Output: 2.083333'''

n = int(input("Enter the number of terms: "))
series_sum = 0
for i in range(1, n + 1):
    series_sum =series_sum + (1 / i)
print(f"The sum of the series is: {series_sum:.4f}")

'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day21\p03.py"
Enter the number of terms: 4
The sum of the series is: 2.0833
PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day21\p03.py"
Enter the number of terms: 6
The sum of the series is: 2.4500'''