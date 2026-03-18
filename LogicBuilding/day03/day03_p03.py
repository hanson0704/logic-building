'''Write a Program to Find the Quotient and Remainder of Two Integers:
Write a program where the user enters two integers (divisor and dividend) and calculates their quotient and remainder. For example:
Input: Dividend: 22, Divisor: 7
Output:Quotient: 3
Remainder: 1'''

dividend = int(input("Enter Dividend: "))
divisor = int(input("Enter Divisor: "))
quotient = round((dividend/divisor),2)
remainder = dividend%divisor
print(f"Quotient: {quotient}\nRemainder: {remainder}")

'''
Output

Enter Dividend: 22
Enter Divisor: 7
Quotient: 3.14
Remainder: 1

Enter Dividend: 15
Enter Divisor: 5
Quotient: 3.0
Remainder: 0
'''