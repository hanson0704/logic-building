'''Finding the Most Frequent Element in an Array
Write a program to find the most frequent element in an array.
Input: array = [1, 2, 2, 3, 3, 3]
Output: 3
'''

array = [1, 2, 2, 3, 3, 3]
frequency = {}
for num in array:
    frequency[num] = frequency.get(num, 0) + 1
most_frequent = max(frequency, key=frequency.get)
print(array)
print(most_frequent)

'''PS D:\CodeMonk\LogicBuilding> python -u "d:\CodeMonk\LogicBuilding\day22\p03.py"
[1, 2, 2, 3, 3, 3]
3'''