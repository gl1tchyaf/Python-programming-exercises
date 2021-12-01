'''
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
'''


def fact(x):
    if x==0:
        return 1
    return x*fact(x-1)

x=int(input())
print(fact(x))