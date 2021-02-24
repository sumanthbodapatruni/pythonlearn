class Car:
    wheels = 4                  # clas variable
    def __init__(self):
        self.mil=10             # instant variables
        self.comp='benz'

c1=Car()
c2=Car()


c1.mil=8

print(c1.comp,c1.mil,c1.wheels)
print(c2.comp,c2.mil,c2.wheels)

Car.wheels=5

print(c1.comp,c1.mil,c1.wheels)
print(c2.comp,c2.mil,c2.wheels)