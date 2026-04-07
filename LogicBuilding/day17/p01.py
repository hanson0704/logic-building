'''Write a Program to Convert Binary Numbers to Decimal and Vice Versa Manually:
Write a program that uses user-defined functions to convert binary numbers to decimal and decimal numbers to binary. For example:
Input: Enter a binary number: 1010
Output: Decimal equivalent: 10
Input: Enter a decimal number: 10
Output: Binary equivalent: 1010

NOTE: Binary to Decimal Conversion
Binary Number:
 A binary number consists of 0 and 1 digits and follows base 2.
Instruction:
Start from the rightmost digit (position = 0).
Multiply each bit by 2position2^{position}2position.
Add all the values to get the decimal number.

Decimal to Binary Conversion
Decimal Number:
 A decimal number uses digits from 0–9 and follows base 10.
Instruction:
Divide the number by 2 repeatedly.
Store the remainder at each step.
Continue until the quotient becomes 0.
Read the remainders from bottom to top to get the binary number.
String Repeat in Python
Instruction:
Use the * operator to repeat a string.
Syntax:
string * count
Where:
string → The string to repeat
count → Number of times to repeat (non-negative integer)

'''

def binary_to_decimal(binary_str):
    decimal_value = 0
    for index, digit in enumerate(reversed(binary_str)):
        decimal_value += int(digit) * (2 ** index)
    return decimal_value

def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"
    binary_str = ""
    while decimal_num > 0:
        binary_str = str(decimal_num % 2) + binary_str
        decimal_num //= 2
    return binary_str

binary_input = input("Enter a binary number: ")
decimal_output = binary_to_decimal(binary_input)
print(f"Decimal equivalent: {decimal_output}")

decimal_input = int(input("Enter a decimal number: "))
binary_output = decimal_to_binary(decimal_input)
print(f"Binary equivalent: {binary_output}")


'''
Output:
Enter a binary number: 1010
Decimal equivalent: 10
Enter a decimal number: 10
Binary equivalent: 1010

'''
