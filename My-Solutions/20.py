class iterator(object):
    def __init__(self, n):
        super(iterator, self).__init__()
        self.n = n

    def divBySeven(self):
        for i in range(0, self.n):
            if i % 7 == 0:
                yield i


n = int(input())
for num in iterator(n).divBySeven():
    print(num)