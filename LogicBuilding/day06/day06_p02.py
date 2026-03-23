'''Pattern 2: Right-angled trinagle
*
* *
* * *
* * * *
* * * * *'''
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
    
'''PS D:\CodeMonk\LogicBuilding> python -u "d:\CodeMonk\LogicBuilding\day06\day06_p02.py"
*
* *
* * *
* * * *
* * * * * '''