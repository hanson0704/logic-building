'''Pattern 3: Inverted traingle
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *'''

n= 5
for i in range(n):
    for j in range(i):
        print(' ', end=' ')
    for k in range(2*(n-i)-1):
        print('*', end=' ')
    print()
    
'''PS D:\CodeMonk\LogicBuilding\day07> python -u "d:\CodeMonk\LogicBuilding\day07\day06_p03.py"
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *'''