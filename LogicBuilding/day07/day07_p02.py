'''Pattern 2: traingle
       *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *'''
n= 5
for i in range(n):
    for j in range(n-i-1):
        print(' ', end=' ')
    for k in range(2*i+1):
        print('*', end=' ')
    print()

'''PS D:\CodeMonk\LogicBuilding\day07> python -u "d:\CodeMonk\LogicBuilding\day07\day06_p02.py"
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * '''