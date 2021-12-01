"""Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically."""

items=[x for x in input().split(',')]
items.sort()
print (','.join(items))