class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self,new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node
    def getNthFromLast(self,head,n):
        ar =list()
        current = head
        while current is not None:
            ar.append(current.data)
            current=current.next
        if len(ar)>=n:
            return ar[len(ar)-n]
        return -1
    def show(self):
        current =self.head
        while current is not None:
            print(current.data)
            current = current.next

if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n,nth_node = map(int,input().strip().split())
        a = LinkedList()
        nodes_a = list(map(int,input().strip().split()))
        for x in nodes_a:
            a.append(x)
        a.show()

        ans = a.getNthFromLast(a.head,n)
        print(ans)