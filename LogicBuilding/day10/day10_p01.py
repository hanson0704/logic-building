'''Pattern 1
A
B B
C C C
D D D D
E E E E E
'''
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+i),end=' ')
    print()

'''PS D:\CodeMonk\LogicBuilding> python -u "d:\CodeMonk\LogicBuilding\day10\day10_p01.py"
A 
B B 
C C C 
D D D D 
E E E E E '''