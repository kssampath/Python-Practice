"""
Q05 - Merge Two Files

Problem:
Merge the contents of two text files into a third output file.

Example:

file1.txt
-----------
A
B

file2.txt
-----------
C
D

output.txt
-----------
A
B
C
D

Notes:
- Preserve line breaks.
- Read from both files and write to a new file.

Concepts:
File Handling, Multiple Files, Writing Files
"""
def merge_files(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
        for line in f1:
            out.write(line)
        for line in f2:
            out.write(line)
    
if __name__ == "__main__":
    merge_files('file1.txt', 'file2.txt', 'merged_output.txt')
    