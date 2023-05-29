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
if __name__=='__main__':
    s = LinkedList()
    ar = list(map(int,input().split()))
    for v in ar:
        s.append(v)
    s.show()
