'''2. Merge Two Dictionaries
Task: Combine the items of two dictionaries into a single new dictionary.
Input:
dict1 = {"name": "John", "age": 25}
dict2 = {"city": "New York", "country": "USA"}
'''

dict1 = {"name": "John", "age": 25}
dict2 = {"city": "New York", "country": "USA"}
merged_dict = {**dict1, **dict2}
print(merged_dict)


# PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day30\p02.py"
# {'name': 'John', 'age': 25, 'city': 'New York', 'country': 'USA'}