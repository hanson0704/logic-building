'''Pattern 3:
E
D E
C D E
B C D E
A B C D E
'''
n=5
for i in range(n):
    ch = chr(ord('E') - i)
    for j in range(i + 1):
        print(ch, end=" ")
        ch = chr(ord(ch) + 1)
    print()
    
'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day19\p03.py"
E 
D E 
C D E 
B C D E 
A B C D E 
PS D:\CodeMonk> '''