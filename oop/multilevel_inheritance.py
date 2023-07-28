class A:
    def featureA(self):
        print('f1 feature')
class B(A):
    def featureB(self):
        print('f2 feature')
class C(B):
    def featureC(self):
        print('f3 feataure')
if __name__ == '__main__':
   c=C()
   c.featureA()
   c.featureB()
   c.featureC()
