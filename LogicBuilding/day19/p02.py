'''Pattern 2:
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 4 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
'''

for i in range(7):
    for j in range(7):
        print(max(abs(i - 3), abs(j - 3)) + 1, end=" ")
    print()
    
    
'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day19\p02.py"
4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 
PS D:\CodeMonk> '''