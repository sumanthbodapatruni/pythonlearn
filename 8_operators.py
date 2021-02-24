a,b=5,6

n=7
n=-n
print(n)

print(a<b and b>a)
'''prints acc to AND truth table
   0 0 0
   0 1 0 
   1 0 0
   1 1 1'''

print(a<b or b>a)
'''prints acc to OR truth table
   0 0 0 
   0 1 0
   1 0 1
   1 1 1 '''


x= True
print(not x)
x= not x
print(x)
