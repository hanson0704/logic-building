'''Write a Program to Check Whether a Character is a Vowel or Consonant:
Write a program to check whether a character entered by the user is a vowel (a, e, i, o, u) or a consonant. For example:
Input: Enter a character: e
Output: e is a vowel.'''

ch = input("Enter a character: ")

if ch.lower() in ('a', 'e', 'i', 'o', 'u'):
    print(f"{ch} is an vowel.")
else:
    print(f"{ch} is a consonant.")


'''Enter a character: e
e is an vowel.'''