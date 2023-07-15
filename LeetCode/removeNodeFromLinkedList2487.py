class ListNode:
    def __init__(self,val=0):
        self.val = val
        self.next = None
def solve(head):
    new_head = None
    temp = head
    while temp:
        tail = new_head
        new_head = ListNode(temp.val)
        new_head.next = tail
        temp = temp.next
    mx = new_head.val
    new_head = new_head.next
    head = ListNode(mx)
    while new_head:
        if new_head.val >= mx:
            tail = head
            head = ListNode(new_head.val)
            head.next = tail
            mx = new_head.val
        new_head = new_head.next
    return head
if __name__ == '__main__':
    s=[1]
    while s:
        print(s.pop())
        print('s')