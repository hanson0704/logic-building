'''Pattern 1
1             1
1 2         2 1
1 2 3     3 2 1
1 2 3 4 4 3 2 1
'''
n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(1,2*(n-i)+1):
        print(" ",end=" ")
    for l in range(i,0,-1):
        print(l,end=" ")
    print()
    
'''PS D:\CodeMonk\LogicBuilding> python -u "d:\CodeMonk\LogicBuilding\day09\day09_p01.py"
1             1 
1 2         2 1 
1 2 3     3 2 1 
1 2 3 4 4 3 2 1 '''