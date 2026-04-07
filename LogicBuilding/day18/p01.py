'''Pattern - 1
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                  *
'''


n = 5

for i in list(range(1, n+1)) + list(range(n-1, 0, -1)):
    left = "* " * i
    spaces = " " * (n - i) * 4
    print(left + spaces + left)
    
'''
PS D:\CodeMonk\LogicBuilding> python -u "d:\CodeMonk\LogicBuilding\day18\p01.py"
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 
'''
