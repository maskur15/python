class LRUCache:
    class Node:
        def __init__(self,key,next=None):
           self.key=key
           self.next=next
    class linkedList:
        def __init__(self):
            self.head=None
            self.tail=None

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.keys=self.linkedList()
        self.key_dict={}
    def __str__(self):
        temp=self.keys.head
        ans=''
        while temp:
            ans+=str(temp.key)+' '
            temp=temp.next
        return ans
    def get(self,key):
        node = self.Node(key)
        print(node)
        if key in self.key_dict:
            value,pre, next = self.key_dict[key][0], self.key_dict[key][1], self.key_dict[key][2]
            if pre == None and next == None:
                self.keys.head = self.keys.tail = None
            elif pre == None:
                self.keys.head = self.keys.head.next
                self.key_dict[self.keys.head.key][1] = None
            elif next == None:
                self.keys.tail = pre
                self.key_dict[self.keys.tail.key][2] = None
            else:
                self.key_dict[pre.key][2] = next
                self.key_dict[next.key][1] = pre
                pre.next = next
            del self.key_dict[key]

            # after deletion insert the key,value as new node
            if self.keys.head == None:
                self.keys.head = node
                self.keys.tail = node
                self.key_dict[key] = [value, None, None]
            else:
                temp_tail = self.keys.tail
                self.keys.tail.next = node
                self.keys.tail = node
                self.key_dict[key] = [value, temp_tail, None]
                self.key_dict[temp_tail.key][2] = node
            return value

        else:
            return -1


    def put(self,key,value):
        node = self.Node(key)
        print(node)
        if key  in self.key_dict:
            #first remove the existing key node from list
            pre,next=self.key_dict[key][1],self.key_dict[key][2]
            if pre==None and next==None:
                self.keys.head=self.keys.tail=None
            elif pre==None:
                self.keys.head=self.keys.head.next
                self.key_dict[self.keys.head.key][1]=None
            elif next==None:
                self.keys.tail=pre
                self.key_dict[self.keys.tail.key][2]=None
            else:
                self.key_dict[pre.key][2]=next
                self.key_dict[next.key][1]=pre
                pre.next=next
            del self.key_dict[key]

            #after deletion insert the key,value as new node
            if self.keys.head == None:
                self.keys.head = node
                self.keys.tail = node
                self.key_dict[key] = [value, None, None]
            else:
                temp_tail = self.keys.tail
                self.keys.tail.next = node
                self.keys.tail = node
                self.key_dict[key] = [value, temp_tail, None]
                self.key_dict[temp_tail.key][2] = node

        else:
            if self.capacity>=1:
                if self.keys.head==None:
                    self.keys.head=node
                    self.keys.tail=node
                    self.key_dict[key]=[value,None,None]
                else:
                    temp_tail = self.keys.tail
                    self.keys.tail.next=node
                    self.keys.tail=node
                    self.key_dict[key]=[value,temp_tail,None]
                    self.key_dict[temp_tail.key][2]=node
                self.capacity-=1
            else:
                head=self.keys.head
                pre, next = self.key_dict[head.key][1], self.key_dict[head.key][2]
                if pre == None and next == None:
                    self.keys.head = self.keys.tail = None
                elif pre == None:
                    self.keys.head = self.keys.head.next
                    self.key_dict[self.keys.head.key][1] = None
                elif next == None:
                    self.keys.tail = pre
                    self.key_dict[self.keys.tail.key][2] = None
                else:
                    self.key_dict[pre.key][2] = next
                    self.key_dict[next.key][1] = pre
                    pre.next = next
                del self.key_dict[head.key]

                # after deletion insert the key,value as new node
                if self.keys.head == None:
                    self.keys.head = node
                    self.keys.tail = node
                    self.key_dict[key] = [value, None, None]
                else:
                    temp_tail = self.keys.tail
                    self.keys.tail.next = node
                    self.keys.tail = node
                    self.key_dict[key] = [value, temp_tail, None]
                    self.key_dict[temp_tail.key][2] = node

if __name__ == '__main__':
    l=LRUCache(1)
    l.put(2,1)
    print(l)
    l.get(2)
    print(l)
    l.put(3,2)
    print(l)
    l.put(5,3)
    print(l)
    l.get(5)
    l.put(1,2)





    print(l.key_dict)