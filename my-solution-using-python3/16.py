'''Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.'''

values = input()
numbers = [x for x in values.split(",") if int(x)%2!=0]
print(",".join(numbers))