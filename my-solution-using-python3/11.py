'''Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check
whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated
sequence. '''

value = []
items=[x for x in input().split(',')]
for p in items:
    r = int(p, 2)
    if not r%5:
        value.append(p)

print(','.join(value))

