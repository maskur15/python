class ListNode:
    def __init__(self, val:int=0, next=None,random=None):
        self.val = val
        self.next = next
        self.random=random
class Solution:
    def swapPairs(self, head:[ListNode]):
        pass
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,val):
        node=ListNode(val)
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
def deepCopy(head):
    nodes=[]
    nodes_index={}
    nodes_index[head]=0
    new_head=ListNode(head.val)
    tail=new_head
    i=1
    nodes.append(new_head)
    temp=head.next
    while temp:
        tail.next=ListNode(temp.val)
        nodes_index[temp]=i
        nodes.append(tail.next)
        tail=tail.next
        temp=temp.next
        i+=1
    tail=new_head
    while head:
        if head.random:
            tail.random= nodes[nodes_index[head.random]]
        new_head=new_head.next
    return new_head

def show(head):
    if head:
        print(head.val,end=' ')
        show(head.next)




if __name__ == '__main__':
    l=LinkedList()
    for i in range(1,8):
        l.insert(i)
    show(l.head)
    deepCopy(l.head)