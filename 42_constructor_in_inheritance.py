class a:
    def __init__(self):
        print('in a init')
    def feature1(self):
        print('f1 is working')

    def feature2(self):
        print('f2 is working')

class b(a):
    def __init__(self):
        super().__init__()
        print('in b init')
    def feature3(self):
        print('f3 is working')

    def feature4(self):
        print('f4 is working')

class c(a,b):
    def __init__(self):
        super().__init__()
        print('in c init')

s1=a()
s2=b()
s3=c()
