class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def appendEnd(self,node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    def showList(self):
        current = self.head
        while current:
            print(current.data , end=' ')
            current = current.next
    def loopHere(self,position):
        if position==0:
            return
        temp = self.head
        for _ in range(1,position):
            temp=temp.next
        #set the loop node as tail
        self.tail=temp
    def isLoop(self,head):
        if head is None:
            return False
        fast = head.next
        slow = head
        while slow != fast:
            if fast ==None or fast.next ==None:
                return False # there is no looop
            slow=slow.next
            fast=fast.next.next
        return True

class Solution:
    def isLoop(self,head):
        if head is None:
            return False
        fast = head.next
        slow = head
        while slow != fast:
            if fast ==None or fast.next ==None:
                return False # there is no looop
            slow=slow.next
            fast=fast.next.next
        return True
    def showList(self,head):
        current = head
        while current:
            print(current.data , end=' ')
            current = current.next
        print('comp')
    def removeloop(self,head):
        mp = dict()
        mp[head]=1
        l= LinkedList()
        l.appendEnd(Node(head.data))
        temp = head
        while temp:
            if temp.next !=None and temp.next in mp:
                break
            temp=temp.next
            mp[temp]=1
            l.appendEnd(Node(temp.data))
        return l.head







if __name__ == '__main__':
    while True:

        l = LinkedList()
        ar = list(map(int,input().split()))

        nodelist = [Node(nd) for nd in ar]
        for node in nodelist:
            l.appendEnd(node)

        l.showList()
        print()
        l.appendEnd(nodelist[1])

        l.loopHere(2)

        print(l.tail.data,l.tail.next.data)

        s = Solution()
        print(l.head.data)
        print(s.isLoop(l.head))
        head = s.removeloop(l.head)
        s.showList(head)
        print(s.isLoop(head))