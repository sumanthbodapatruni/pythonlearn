def topten():
    yield 5

values=topten()
print(values.__next__())
print(values.__next__())
print(values.__next__())

for i in values:
    print(i)

