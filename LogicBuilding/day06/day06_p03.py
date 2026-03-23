'''Pattern 3: Hallow Rectangle
* * * * *
*       *
*       *
*       *
* * * * *
'''
n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
'''PS D:\CodeMonk\LogicBuilding> python -u "d:\CodeMonk\LogicBuilding\day06\day06_p03.py"
* * * * * 
*       * 
*       * 
*       * 
* * * * * '''