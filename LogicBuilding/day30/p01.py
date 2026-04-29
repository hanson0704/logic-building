'''1. Dictionary Keys and Values
Task: Extract and print all the keys and values of a dictionary as separate lists.
Input:
data = {"name": "John", "age": 25, "city": "New York"}
Expected Output:
Keys: ["name", "age", "city"], Values: ["John", 25, "New York"]
'''

data = {"name": "John", "age": 25, "city": "New York"}
keys = list(data.keys())
values = list(data.values())
print(f"Keys: {keys}, Values: {values}")

'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day30\p01.py"
Keys: ['name', 'age', 'city'], Values: ['John', 25, 'New York']'''