"""
Q02 - Line Count

Problem:
Count and return the total number of lines in a text file.

Example File:
Hello
Python
World

Output:
3

Notes:
- Count all lines, including blank lines.
- Do not use readlines() or built-in shortcuts.

Concepts:
File Handling, Loops, Counters
"""
def line_count_loop(filename):
    cnt = 0
    with open(filename) as f:
        for x in f:
            cnt +=1
    return cnt    

def line_count_builtin(filename):
    with open(filename) as f:
        return len(f.readlines())
