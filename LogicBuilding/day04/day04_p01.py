'''Print the Multiplication Table of a Given Number:
Write a program where the user enters a number, and the program prints its multiplication table. For example:
Input: Enter a number: 5
Output:
5 x 1 = 5
5 x 2 = 10
5 x 10 = 50
'''
num = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")
    
'''
Enter a number: 6
6 X 1 = 6
6 X 2 = 12
6 X 3 = 18
6 X 4 = 24
6 X 5 = 30
6 X 6 = 36
6 X 7 = 42
6 X 8 = 48
6 X 9 = 54
6 X 10 = 60'''