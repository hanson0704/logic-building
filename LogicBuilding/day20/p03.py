'''Pattern 3
0 1 0 1
1 0 1 0
0 1 0 1
1 0 1 0
'''

for i in range(1, 5):
    for j in range(1, 5):
        if (i == 1 and (j == 2 or j == 4)) or (i == 2 and (j == 1 or j == 3)) or (i == 3 and (j == 2 or j == 4)) or (i == 4 and (j == 1 or j == 3)):
            print("1", end="")
        else:
            print("0", end="")
    print()
    
'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day20\p03.py"
0101
1010
0101
1010'''