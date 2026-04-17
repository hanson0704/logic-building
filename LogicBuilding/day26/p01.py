'''Longest Word in a Sentence
Find the longest word in a given sentence.
Input: "The quick brown fox"
Output: "quick"
'''

input_sentence = "The quick brown fox"
words = input_sentence.split()
longest_word = max(words, key=len)
print(longest_word)

'''PS D:\CodeMonk> python -u "d:\CodeMonk\LogicBuilding\day26\p01.py"
quick'''