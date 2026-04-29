'''3. Swap Keys and Values
Task: Create a new dictionary where the original keys become values and the original values become keys (Dictionary Comprehension).
Input:
data = {"name": "John", "age": 25, "city": "New York"}
Expected Output:
{'John': 'name', 25: 'age', 'New York': 'city'}
'''

data = {"name": "John", "age": 25, "city": "New York"}
swapped_dict = {value: key for key, value in data.items()}
print(swapped_dict)

'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day30\p03.py"
{'John': 'name', 25: 'age', 'New York': 'city'}'''