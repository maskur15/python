class A:
    def __init__(self):
        print('in A class')
    def featureA(self):
        print('f1 feature')
class B():
    def __init__(self,name):
        print('in b class',name)
    def featureB(self):
        print('f2 feature')
class C(A,B):
    def __init__(self):
        super().__init__()
        print('in c class')
        B.__init__(self,'mskur')
    def show_b(self):
        super().featureA()
        super().featureB()
    def featureC(self):
        print('f3 in c')
if __name__ == '__main__':
    c=C()
    c.show_b()