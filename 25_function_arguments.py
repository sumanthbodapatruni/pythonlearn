def update(x):
    x=8
    print(x)


update(10)

a=10
update(a)
print(a)



Types of arguments-----------------------------------------------------------

def person(name,age=18):
    print(name)
    print(age)

person('navin')
person("navin",28)


def sum(a,*b):     # take multiple values
    c=a
    for i in b:
        c=c+i
    print(c)

sum(5,6,34,78)

def sum1(*b):
    c = 0
    for i in b:
        c = c + i
    print(c)


sum1(5, 6, 34, 78)



