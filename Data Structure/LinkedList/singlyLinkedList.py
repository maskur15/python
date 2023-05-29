class Node:
   def __init__(self,data):
      self.data = data
      self.next = None
class singlyLinkedlist:
   def __init__(self):
      self.head = None
   #insert node in the end of the list
   def insertEnd(self,node):
      if self.head==None:
         self.head = node
      else:
         currnent = self.head
         while currnent.next is not None:
            currnent=currnent.next
         currnent.next=node
   def showList(self):
      if self.head == None:
         print('Empty list')
      current = self.head
      while current is not None:
         print(current.data)
         current=current.next
   #insert a new node as a head node of the list
   def insertFront(self,node):
      node.next= self.head
      self.head = node
   # find the length of the list
   def listLength(self):
       current = self.head
       i=0
       while current is not None:
           current=current.next
           i+=1
       return  i
   #insert a node  in between two node
   def insertinPosition(self,index,node):
       current = self.head
       i=0
       if index==0:
           self.insertFront()

           return
       while current is not None:
           if i== index-1:
               break
           current=current.next
           i+=1
       node.next = current.next
       current.next = node


if __name__ == '__main__':

    link = singlyLinkedlist()
    link.insertEnd(Node(2))
    link.insertEnd(Node(1))
    link.insertEnd(Node(33))
    link.insertEnd(Node(3))
    link.showList()
    print('insert in 1th position')
    link.insertinPosition(2,Node(99))
    link.showList()
    print('insert in head ')
    link.insertFront(Node(222))
    link.insertFront(Node(111))
    link.showList()