class pycharm:
    def execute(self):
        print('compiling')
        print('running')

class myeditor:
    def execute(self):
        print('spellcheck')
        print('convention check')
        print('running')

class laptop:
    def code(self,ide):
        ide.execute()


ide=myeditor()

lap1=laptop()
lap1.code(ide)

ide=pycharm()
lap1=laptop()
lap1.code(ide)