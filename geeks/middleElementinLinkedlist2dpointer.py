class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.headNode = None
        self.lastNode = None
    def append(self,data):
        new_node = Node(data)
        if self.headNode is None:
            self.headNode= new_node
            self.lastNode = new_node
            return
        self.lastNode.next= new_node
        self.lastNode = new_node
    def show(self):
        current = self.headNode
        while current is not None:
            print(current.data)
            current=current.next
    def length(self):
        current = self.headNode
        i=0
        while current is not None:
            current=current.next
            i+=1
        return i
    def getNthElement(self,n):
        current = self.headNode
        for _ in range(n-1):
            if current is None:
                return  -1
            current=current.next
        return current.data
    def findMiddle(self):
        first = self.headNode
        second = self.headNode
        if first is None:
            return -1
        while second is not None:
            second=second.next
            if second is None:
                break
            second=second.next
            first=first.next
        return first.data
if __name__=='__main__':
    s = LinkedList()
    ar = list(map(int,input().split()))
    for v in ar:
        s.append(v)

    print(s.findMiddle())