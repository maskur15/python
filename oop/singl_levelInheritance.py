class A:
    def featureA(self):
        print('f1 feature')
class B(A):
    def featureB(self):
        print('f2 feature')
if __name__ == '__main__':
    b=B()
    b.featureA()
    b.featureB()
