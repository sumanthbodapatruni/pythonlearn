from numpy import *

arr= array([1,2,3,4,5,6,7])
print(arr)
arr= array([1,2,3,4,5.0,6,7])
print(arr.dtype)
print(arr)
arr= array([1,2,3,4,5,6,7],float)
print(arr)


ar=linspace(0,15)
print(ar)               # prints values that breaks into 15 parts by default coz we gave 15

a=linspace(0,15,16)
print(ar)               # prints 16 parts as we mentioned step 16

b= arange(1,15,2)
print(b)                # prints values skipping by 2 ie.. 1,3,5,7,9,111,13,15,

c=logspace(1,14,5)
print(c)                # 10^1 to 10^14 makes into 5 parts

print('%.2f'% c[0])     # after point prints upto 2 decimal values

d= ones(5,int)
print(d)
e=zeros(6)
print(e)
f=zeros(6,int)
print(f)



