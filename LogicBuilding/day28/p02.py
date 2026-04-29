'''Count Vowels and Consonants
Count the number of vowels and consonants in a string.
Input: "hello"
Output: Vowels: 2, Consonants: 3
'''
input_string = "hello"
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
for char in input_string:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")

input_string2 = "bye"
vowel_count2 = 0
consonant_count2 = 0
for char in input_string2:
    if char.isalpha():
        if char in vowels:
            vowel_count2 += 1
        else:
            consonant_count2 += 1
print(f"Vowels: {vowel_count2}, Consonants: {consonant_count2}")

'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day28\p02.py"
Vowels: 2, Consonants: 3
Vowels: 1, Consonants: 2'''