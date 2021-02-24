avl=5
i=1
while i< 10:
    if i > avl:
        print('out of stock')
        break
    print('candy')
    i=i+1


for i in range(1,101):
    if i % 2==0:
        continue
    print(i)

for i in range(1,101):              # skips which divisible by 2 and 5
    if i % 2==0 and i%5==0:
        continue

    print(i)


for i in range(10):     # to skip only odd numbers
    if i%2 != 0:
        pass
    else:
        print(i)


for i in range(5):
    if i ==3:
        continue
    print('hello',i)

for i in range(5):
    if i == 3:
        break
    print('hello', i)


def fun():      # dont know what to write now define later
    pass
