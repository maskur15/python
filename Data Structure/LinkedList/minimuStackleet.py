class MinStack():
    class Node:
        def __init__(self, val=0,next=None,prev=None,min=99999999999):
            self.val = val
            self.next = next
            self.prev = prev
            self.min = min
    def __init__(self):
        self.head =None
        self.tail=None
    def push(self,val):
        if self.head==None:
            self.head= MinStack.Node(val,None,None,val)
            self.tail= self.head
        else:
            node=MinStack.Node(val,None,self.tail,min(self.tail.min,val))
            self.tail.next= node
            self.tail=node
    def showBackward(self):
        temp=self.tail
        while temp:
            print(temp.val,end=' ')
            temp=temp.prev
    def showFroward(self):
        temp=self.head
        while temp:
            print(temp.val-temp.min,end=' ')
            temp=temp.next
    def pop(self):
        if self.tail:
            self.tail=self.tail.prev
            if self.tail:
                self.tail.next=None
    def top(self):
        if self.tail:
            return self.tail.val
    def getMin(self):
        if self.tail:
            return self.tail.min
stack=MinStack()
stack.push(-2)
stack.push(0)
stack.push(-3)
m=stack.getMin()
print(m)
stack.pop()
t=stack.top()
print(t)
m=stack.getMin()
print(m)