class computer:

    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        print('ill print without calling and called')

    def conf(self):
        print('i5','16gb','1tb')


    def config(self):
        print(self.cpu,self.ram)

co1=computer('i3','4')
co1.config()



com1=computer('i5',16)
com2=computer('ryzen','8')

computer.config(com1)
computer.config(com2)

com1.config()
com2.config()

