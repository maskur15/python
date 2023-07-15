class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self,value):
        node= ListNode(value)
        if self.head is None:
            self.head= node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
def sum(head):
    p=-1
    temp=head
    while head:
        p+=1
        head =head.next
    result=0
    while temp:
        result+= temp.val*pow(2,p)
        temp=temp.next
        p-=1
    return result
def  sum_withreverse(head):
    result = 0
    while head:
        result=(result+head.val)*2
    return result
if __name__ == '__main__':
    l=LinkedList()

    l.insert(1)
    l.insert(0)
    l.insert(0)

    print(sum(l.head))

