def reverse(head):
    if head is None or head.next is None:
        return head
    rev_head = reverse(head.next)
    head.next.next = head
    head.next = None
    return rev_head
def reverse_linkedlist(head):
    temp = head
    temp.next = None
    print(temp.next.data)
    print(head.next.data)

