'''. Power of a Number
Task: Write a recursive function power(base, exponent) to calculate the value of a base raised to a specific power.
Input: base = 2, exponent = 3
Expected Output: 8 '''

def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)
base = 2
exponent = 3
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")

base = 5
exponent = 4
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")

'''PS D:\CodeMonk\LogicBuilding\day31> python -u "d:\CodeMonk\LogicBuilding\day31\p02.py"
2 raised to the power of 3 is: 8
5 raised to the power of 4 is: 625'''