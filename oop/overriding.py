class Teacher:
    def show(self):
        print('working on  hp corei3')
class Student(Teacher):
    def show(self,*name):
        print('got a lenovo i5')
        for n in name:
            print(n)
    pass
if __name__ == '__main__':
    s=Student()
    s.show(3,8,3,'mask')