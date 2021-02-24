class student:

    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.lap=self.laptop()

    def show(self):
        print(self.name,self.roll)
        self.lap.show()
    class laptop:
        def __init__(self):
            self.brand='hp'
            self.cpu='i5'
            self.ram=8

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=student('sumanth',8)
s2=student('yeswanth',10)

s1.show()
s2.show()


