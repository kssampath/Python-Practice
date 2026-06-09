"""
Q01 - Longest Line

Return the longest line from a text file.

Example:
Hello
Python Programming
Hi

Output:
Python Programming
"""
def longest_line(filename):
    with open(filename) as f:
        l= 0
        longest = ""
        for x in f:
            if l < len(x.strip()):
                longest = x
                l = len(longest)
        return longest