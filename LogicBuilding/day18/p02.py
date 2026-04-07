'''Pattern - 2
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *'''

for i in list(range(1, 5+1)) + list(range(5-1, 0, -1)):
    left = "* " * (5 - i + 1)
    spaces = " " * (i - 1) * 4
    print(left + spaces + left)


''''
PS D:\CodeMonk\LogicBuilding> python -u "d:\CodeMonk\LogicBuilding\day18\p02.py"
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * *
'''