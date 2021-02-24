from numpy import *
arr =array([[1,2,3,7,8,9],[4,5,6,1,2,3]])
print(arr)


print(arr.dtype)        # int 32  ...type of data
print(arr.ndim)         # dimensional -2d
print(arr.shape)        # (2,6)
print(arr.size)         # 12
arr1=arr.flatten()
print(arr1)             # [1,2,3,7,8,9,4, 5,6,1,2,3]
arr2= arr1.reshape(2,6)
print(arr2)
arr3=arr1.flatten()
arr3=arr1.reshape(2,2,3)
print(arr3)
m= matrix(arr1)
n=matrix('1 2 3;4 5 6;7 8 9')
print(diagonal(m))      # [1 5 8]
print(m.min())      # 1
print(m.max())      # 9
n1=matrix('1 2 3;4 5 6;7 8 9')
n2=matrix('1 2 3;4 5 6;7 8 9')

n3=n1+n2
n4=n1*n2

