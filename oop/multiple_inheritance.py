class A:
    def featureA(self):
        print('f1 feature')
class B():
    def featureB(self):
        print('f2 feature')
class C(A,B):
    def featureC(self):
        print('f3 feature')

if __name__ == '__main__':
    c=C()
    c.featureA()
    c.featureB()
    c.featureC()
