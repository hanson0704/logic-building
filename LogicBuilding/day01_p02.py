# Write a Program to Find the Size of int, float, double, and char on Your Computer:
# Write a program that displays the size of fundamental data types (int, float, double, and char) on your system. For example:
# Output:
# Size of int: 4 bytes
# Size of float: 4 bytes
# Size of double: 8 bytes
# Size of char: 1 byte
import sys

intType = 10
floatType = 10.0
doubleType = 10.0
charType = 'C'
stringType = "HelloWorld"


print(f"Size of int: {sys.getsizeof(intType)}")
print(f"Size of float: {sys.getsizeof(floatType)}")
print(f"Size of double: {sys.getsizeof(doubleType)}")
print(f"Size of char: {sys.getsizeof(charType)}")
print(f"Size of string: {sys.getsizeof(stringType)}")