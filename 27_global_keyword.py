a = 10


def something():
    a = 15
    print(a)


print(a)
something()


def something1():
    print(a)


something1()


def something2():
    global a
    a = 15
    print(a)


something2()


def something3():
    a = 9
    print(a)
    x = globals()['a']
    print(x)
    globals()['a'] = 17
    print(a)


something3()


def something4():
    x = globals()['a']
    print(x)
    globals()['a'] = 17
    print(a)


something4()
