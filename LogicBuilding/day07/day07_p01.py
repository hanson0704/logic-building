'''Pattern 1: Inverted Right-angled triangle
* * * * *
* * * *
* * *
* *
*'''
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print('*', end=' ')
    print()

'''PS D:\CodeMonk\LogicBuilding\day07> python -u "d:\CodeMonk\LogicBuilding\day07\day06_p01.py"
* * * * * 
* * * * 
* * * 
* * 
* '''