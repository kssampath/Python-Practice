"""
Q06 - Unique Words

Problem:
Count the number of unique words in a text file.

Example File:
Python is good
Python is powerful

Output:
4

Explanation:
Unique words:
- Python
- is
- good
- powerful

Notes:
- Duplicate words should only be counted once.
- Use a set to store unique words.
- Process the file efficiently.

Concepts:
File Handling, Sets, Strings

Difficulty: Moderate
Topic: File Handling
Date Solved: 2026-06-09

Key Learning:
- Using sets to remove duplicates automatically.
- Difference between total word count and unique word count.
- Processing files line by line is more memory efficient than loading the entire file.

Time Complexity:
O(n)

Space Complexity:
O(u)
where u = number of unique words.

Interview Notes:
- For large files, process line by line instead of using read() or readlines().
- Sets provide O(1) average lookup and insertion.

Common Mistakes:
- Counting total words instead of unique words.
- Forgetting to split lines into words before adding them to a set.
"""
def unique_words_read(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        return len(set(words))

def unique_words_readlines(filename):
    with open(filename, 'r') as file:
        text = file.readlines()
        words = [word for line in text for word in line.split()]
        return len(set(words))

def unique_words_readline(filename):
    with open(filename, "r") as file:
        words = set()
        for line in file:
            words.update(line.split())
        return len(words)