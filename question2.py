"""
Write a method that accepts a CamelCase string which splits it into separate words in "sentence
case". Please do not use regular expressions.

Example
Input: string "thisIsMySentence"
Output: string "This is my sentence"
"""

# In camelCase, every word from the second word starts with a capital letter
# Function to convert camel case string to individual words in the string using the above camel case property
# Function uses enumerate to go over all indices that have a change in case
def camelCaseSplit(str):
    start_idx = [i for i, e in enumerate(str) if e.isupper()] + [len(str)]
    start_idx = [0] + start_idx
    return [str[x: y] for x, y in zip(start_idx, start_idx[1:])] 

# Function to convert camel case to sentence case
def camelToSentenceCase(input):
    # Gets an array of individual words in the camel case string
    words = camelCaseSplit(input)
    # using join to combine all the words in the array with a white space
    sentenceCase = ' '.join(words)
    # Converting the first character to upper case and the remaining to lower case
    sentenceCase = sentenceCase[0].upper() + sentenceCase[1:].lower()
    return sentenceCase

print(camelToSentenceCase("thisIsMySentenceCase"))