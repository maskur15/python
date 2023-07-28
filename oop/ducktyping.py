'''
if a birds walks like a duck,
swim likes  a duck, quacks like a duck then
it s a duck
-This is one kind of polymorphism - since the method_name is same but work
differently
'''
class Pycharm:
    def execute(self):
        print('Debug,run')
class MyEditor:
    def execute(self):
        print('run,compile,debug')
        print('and more')
class Laptop:
    def code(self,ide):
        ide.execute() #this is where ductyping- if any object has execute() method we can pass it

if __name__ == '__main__':
        l=Laptop()
        ide1=Pycharm()
        ide2=MyEditor()
        l.code(ide2)