"""
Q03 - Count Word Occurrences

Problem:
Count the total number of occurrences of a given word in a text file.

Example File:
Python Python
I like Python

Input:
Python

Output:
3

Notes:
- Count every occurrence.
- Not just the number of lines containing the word.

Concepts:
File Handling, Strings, Counting
"""
def count_occurrences(filename, word):
    cnt = 0
    with open(filename) as f:
        for line in f:
                cnt += line.count(word)
    return cnt