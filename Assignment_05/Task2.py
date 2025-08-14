'''
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
'''

number=list(range(1,11))
print("Original list:",number)

first_five=number[:5]
print("Extracted first five elements:",first_five)

reversed_first_five=first_five[::-1]
print("Reveresed extracted elements:",reversed_first_five)
