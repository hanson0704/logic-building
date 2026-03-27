'''
Pattern 3
A B C D E
A B C D
A B C
A B
A

'''

n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()

'''PS D:\CodeMonk\LogicBuilding> python -u "d:\CodeMonk\LogicBuilding\day09\day09_p03.py"
A B C D E 
A B C D
A B C
A B
A'''