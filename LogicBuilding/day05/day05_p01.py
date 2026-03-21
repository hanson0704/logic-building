'''Calculate the Sum of Digits of a Given Number:
Write a program that calculates the sum of the digits of a number entered by the user. For example:
Input: Enter a number: 1234
Output: Sum of digits: 10'''

num = input("Enter a number: ")
sum = 0

for i in num:
    sum = sum + int(i)
print(f"Sum of digits: {sum}")


'''Enter a number: 1234
Sum of digits: 10'''