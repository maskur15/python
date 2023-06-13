class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self,value):
        nd = Node(value)
        if self.head == None:
            self.head= nd
            self.tail = nd
        else:
            self.tail.next=nd
            self.tail = nd
    def showList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp= temp.next
    def delete_lastNode(self):
        temp = self.head
        pre = temp
        while temp.next:
            pre = temp
            temp=temp.next
        pre.next = None


class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

if __name__ =='__main__':

    l = LinkedList()
    l.insert(4)
    l.insert(5)
    l.insert(8)
    l.insert(51)
    l.insert(25)
    l.showList()
    l.delete_lastNode()
    print('After deleting last node: ')
    l.showList()