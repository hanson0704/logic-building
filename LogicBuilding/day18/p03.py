'''Pattern - 3
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''

for i in range(1, 6):
    for j in range(i):
        print(i + j, end=" ")
    print()

'''
PS D:\CodeMonk\LogicBuilding> python -u "d:\CodeMonk\LogicBuilding\day18\p03.py"
1 
2 3 
3 4 5 
4 5 6 7 
5 6 7 8 9 
'''
