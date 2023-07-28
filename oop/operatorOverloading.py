class Student:
    def __init__(self,m1,m2):
        self.marks1=m1
        self.marks2=m2
    #overloading the plus operator
    def __add__(self, other):
        m1=self.marks1+other.marks1
        m2=self.marks2+other.marks2
        return Student(m1,m2)
    def __gt__(self, other):
        if self.marks2+self.marks1 > other.marks1+other.marks2:
            return True
        else:
            return False
    def show(self):
        print(self.marks1,' ',self.marks2)
if __name__ == '__main__':
    s1=Student(299,34)
    s2=Student(33,44)
    s3=s1+s2 #to overload the + overload the __add__ magic method
    s3.show()
    if s1>s2:
        print('s1 win')
    else:
        print('s2 win')
