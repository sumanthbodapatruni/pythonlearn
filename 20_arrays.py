'''
'b' signed char   int 1
'B' unsigned char   int 1
'u' wchar_t Unicode character 2
'h' signed short    int 2
'H' unsigned short  int 2
'i' signed int      int 2
'I' unsigned int    int 2
'l' signed long     int 4
'L' unsigned long   int 4
'q' signed long long int 8
'Q' unsigned long long int 8
'f' float           float 4
'd' double          float 8
'''


from array import *

room = array('i',[1,2,3,4,5,6])
print(room)
print(room.buffer_info())
room.reverse()
for i in range(6):
    print(room[i])
for i in range(len(room)):
    print(room[i])
for i in room:
    print(i)


room1=array('u',['a','b','c','d','e'])
for i in range(4):
    print(room1[i])

room2=array(room1.typecode,(a for a in room1))
for i in range(5):
    print(room2[i])

room3=array(room.typecode,(a*a for a in room))
for i in range(5):
    print(room3[i])

arr= array('i',[])
n= int (input('length of array'))
for i in range(n):
    x=int(input('enter the next value'))
    arr.append(x)

print(arr)

y=int(input('enter search value'))
k=0
for i in arr:
    if i==y:
        print(k)
        break

    k=k+1
# or
print(arr.index(y))
