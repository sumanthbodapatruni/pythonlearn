def fact(n):
    a=1
    for i in range(1,n+1):
       a=a*i
    return a
x=5
result= fact(x)
print(result)



# Recursion


import sys
sys.setrecursionlimit(1996)

print(sys.getrecursionlimit())
i=0
def greet():
    global i
    i+=1
    print('hello',i)
    greet()

greet()                 # infinite prints hello,limit is 1000 by default
