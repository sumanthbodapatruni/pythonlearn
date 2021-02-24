class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def sum(self,a=None,b=None):
      if a!=None and b!= None:

          s=a+b

      else:
          s=a

      return s

s1=student(34,67)
print(s1.sum(5,8))


#

class a:
    def show(self):
        print('in a show')
class b(a):
    def show(self):
        print('in b show')  # if pass prints above one
a1=b()
a1.show()
