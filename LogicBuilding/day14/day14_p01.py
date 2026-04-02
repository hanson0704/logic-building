'''Print Numbers in Words in Reverse Order Using a Switch Case:
Write a program that takes an integer, reverses it, and prints each digit as a word using a switch case. For example:
Input: Enter a number: 321
Output: One Two Three'''

num = int(input("Enter a number: "))
print("Output:", end=" ")
if num == 0:
    print("Zero")
else:
    while num > 0:
        digit = num % 10
        match digit:
            case 0: print("Zero", end=" ")
            case 1: print("One", end=" ")
            case 2: print("Two", end=" ")
            case 3: print("Three", end=" ")
            case 4: print("Four", end=" ")
            case 5: print("Five", end=" ")
            case 6: print("Six", end=" ")
            case 7: print("Seven", end=" ")
            case 8: print("Eight", end=" ")
            case 9: print("Nine", end=" ")
        num //= 10

'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day14\day14_p01.py"
Enter a number: 321
Output: One Two Three
PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day14\day14_p01.py"
Enter a number: 546
Output: Six Four Five '''