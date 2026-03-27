'''Pattern 2
A
A B
A B C
A B C D
A B C D E
'''
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()


'''PS D:\CodeMonk\LogicBuilding> python -u "d:\CodeMonk\LogicBuilding\day09\day09_p02.py"
A 
A B
A B C
A B C D
A B C D E'''