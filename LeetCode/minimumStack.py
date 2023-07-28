class MinStack:
    def __init__(self):
        self.minimus={}
        self.stack={}
        self.minIndex=0
        self.topIndex=0
    def push(self,val=None):

        self.stack[self.topIndex]=val
        self.topIndex+=1
        if self.minIndex==0:
            self.minimus[0]=val
            self.minIndex+=1
        else:
            if val <=self.minimus[self.minIndex-1]:
                self.minimus[self.minIndex]=val
                self.minIndex+=1
    def pop(self):
        val= self.stack[self.topIndex-1]
        del self.stack[self.topIndex-1]
        self.topIndex-=1
        if val== self.minimus[self.minIndex-1]:
            del self.minimus[self.minIndex-1]
            self.minIndex-=1
    def top(self):
        return self.stack.get(self.topIndex-1)
    def getMin(self):
        return self.minimus.get(self.minIndex-1)
if __name__ == '__main__':
    m=MinStack()
    m.push(-2)
    m.push(0)
    m.push(-3)
    print(m.getMin())
    m.pop()
    print(m.top())
    print(m.getMin())


