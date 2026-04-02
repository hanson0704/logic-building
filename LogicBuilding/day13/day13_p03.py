'''Program to Print Integers in Words:
Write a program that converts each digit of an integer entered by the user into its corresponding word representation. For example:
Input: Enter a number: 123
Output: One Two Three'''

def digit_to_word(digit):
    words = {
        '0': 'Zero',
        '1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine'
    }
    return words.get(digit, '')
number = input("Enter a number: ")
word_representation = ' '.join(digit_to_word(digit) for digit in number)
print(word_representation)

'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day13\day13_p03.py"
Enter a number: 123
One Two Three
PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day13\day13_p03.py"
Enter a number: 678
Six Seven Eight'''