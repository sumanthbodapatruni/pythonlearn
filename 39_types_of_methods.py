class student:

    school = 'ecorvi'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return(self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self):
        self.m1=33

    @classmethod
    def getschool(cls):
        return cls.school
    @staticmethod
    def info():
        print('this is ecorvi')

s1=student(32,45,67)
s2=student(54,78,32)

print(s1.avg())
print(s2.avg())

print(s1.set_m1())
print(student.getschool())
student.info()


