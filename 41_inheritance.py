class a:
    def feature1(self):
        print('f1 is working')

    def feature2(self):
        print('f2 is working')

class b(a):     
    def feature3(self):
        print('f3 is working')

    def feature4(self):
        print('f4 is working')

class c(b):     # can access b and a because above b(a0 i.e b is accessing a   ... or c(a,b) - c can access from a and b
    def feature5(self):
        print('f5 is working')

A=a()

A.feature1()
A.feature2()


B=b()

B.feature3()
B.feature1()

C=c()

C.feature1()
C.feature3()
C.feature5()