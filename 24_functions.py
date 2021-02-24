def greet():
    print('hello')
    print('good morning')


def add(x,y):
    c=x+y
    return c


def sub(x,y):
    d=x-y
    print(d)

def add_sub(x,y):
    c=x+y
    d=x-y
    return c,d

greet()

result= add(5,4)

print(result)

sub(9,7)


res1,res2=add_sub(9,6)
print(res1,res2)



