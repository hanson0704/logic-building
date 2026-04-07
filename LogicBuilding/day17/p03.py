'''Pattern - 2
       *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
'''

for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2 * i - 1))
for i in range(4, 0, -1):
    print(" " * (5 - i) + "*" * (2 * i - 1))

'''PS D:\CodeMonk\LogicBuilding> python -u "d:\CodeMonk\LogicBuilding\day17\p03.py"
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *'''