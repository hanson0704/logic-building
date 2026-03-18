'''Program to Calculate the Area of a Circle and Triangle:
Write a program to calculate the area of a circle given its radius and a triangle given its base and height. For example:
Input: Radius: 5, Base: 10, Height: 4
Output:Area of Circle: 78.5
Area of Triangle: 20'''
import math

radius = float(input("Enter Radius: "))
base = float(input("Enter Base: "))
height = float(input("Enter Height: "))
area_circle = round((math.pi * pow(radius,2)),2)
area_triangle = round((0.5 * base * height),2)

print(f"Area of Circle: {area_circle}")
print(f"Area of Triangle: {area_triangle}")

'''
Output

Enter Base: 10
Enter Height: 4
Area of Circle: 78.54
Area of Triangle: 20.0

Enter Radius: 10
Enter Base: 5
Enter Height: 6
Area of Circle: 314.16
Area of Triangle: 15.0'''