'''Pattern 2
   1
  1 2 1
1 2 3 2 1
'''

for i in range(1, 4):
    for j in range(1, 8):
        if (i == 1 and j == 4) or (i == 2 and (j == 3 or j == 5)) or (i == 3 and (j == 1 or j == 7)):
            print("1", end="")
        elif i == 2 and j == 4:
            print("2", end="")
        elif i == 3 and (j == 2 or j == 6):
            print("2", end="")
        elif i == 3 and j == 4:
            print("3", end="")
        else:
            print(" ", end="")
    print()

'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day20\p02.py"
   1   
  121  
12 3 21'''