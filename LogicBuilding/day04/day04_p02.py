'''Write a Program to Make a Simple Calculator Using a Switch Case:
Write a program that acts as a calculator, taking two numbers and an operator (+, -, *, /) from the user, and performing the operation based on the operator. For example:
Input: Enter first number: 10, Operator: +, Second number: 20
Output: 10 + 20 = 30'''

num1 = float(input("Enter first number: "))
operator = input("Operator: ")
num2 = float(input("Enter second number: "))
match operator:
    case "+":
        print(f"{num1} + {num2} = {num1+num2}")
    case "-":
        print(f"{num1} - {num2} = {num1-num2}")
    case "*":
        print(f"{num1} * {num2} = {num1*num2}")
    case "/":
        if num2 != 0:
            print(f"{num1} / {num2} = {num1/num2}")
        else:
            print("Division by zero is not possible.")

'''
Enter first number: 10
Operator: +
Enter second number: 20
10.0 + 20.0 = 30.0

Enter first number: 6
Operator: /
Enter second number: 0
Division by zero is not possible.
PS D:\CodeMonk> '''