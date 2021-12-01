value = []
items=[x for x in input().split(',')]
for p in items:
    r = int(p, 2)
    if not r%5:
        value.append(p)

print(','.join(value))

