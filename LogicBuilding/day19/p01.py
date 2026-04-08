'''Pattern 1:
1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
'''

for i in range(1, 6):
    for j in range(1, i + 1):
        if (i + j) % 2 == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
    
'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day19\p01.py"
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 '''