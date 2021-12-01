'''Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. '''

from operator import itemgetter, attrgetter


freq = {}   # frequency of words in text
line = input()
for word in line.split():
    freq[word] = freq.get(word,0)+1

words = freq.keys()
for w in sorted(words, key=itemgetter(0)):
    print("%s:%d" % (w,freq[w]))