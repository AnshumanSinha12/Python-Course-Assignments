''''
Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
'''

try:
  with open("sample.txt") as f:
    print("Reading file content:")
    line_no=1
    for line in f:
        clean_line = line.strip()
        print(f"Line {line_no}: {clean_line}")
        line_no+=1
    print(f.read())
except FileNotFoundError:
  print("Error:The file 'sample.txt' was not found.")
