class computer:
    def __init__(self):
        self.name='sumanth'
        self.age=22

    def update(self):
        self.age=20

    def compare(self,other_or_c2):
        if self.age==other_or_c2:
            return True
        else:
            return False
c1=computer()
c2=computer()

c1.name='satya'
c1.age=21

print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)

c1.update()

print(c1.age)

if c1.compare(c2):
    print('same')
else:
    print('different')