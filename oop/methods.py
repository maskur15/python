'''
Two types of varibale
instance varibale: varibale related to object
class variable/static variable: variable not asscociate to a specific object rather its associate with class

'''

'''three types of methods 
->class method : works with class variabl
-> instance method: works with object
-> static method: nothing to do with class variable and instance variable
'''
class Student:
    school='Telusko'#class/static variable
    def __init__(self,m1,m2):
        self.m1=m1 #instance variable
        self.m2=m2
        #self.school='bd' #thiswill create school as instance variable
        #print(self.school)

    def avg(self):
        self.school='Banladesh'# this will not cahnge the class variable rather it creates  a new attirbute of that object
        return (self.m1+self.m2)/2
    """class method use to work with class varibale"""
    @classmethod
    def get_school(cls):
        return cls.school
    #static method doesnt deal with class varible nor instance variable
    @staticmethod
    def info():
        print('This a static method in student class')
if __name__ == '__main__':
    s1=Student(2,5)
    s2=Student(83,21)
    print(id(s1.school),id(Student.school),s1.school,Student.school)
    print(s1.info())
    print(Student.get_school())
    print(s1.get_school())
    print(s1.avg())
    print(s1.get_school(),s2.get_school(),s1.school,s2.school)