class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

def middleOfLinkedList(head):
    if head is None:
        return
    slow=head
    fast=head
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
    return slow

head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
middle=middleOfLinkedList(head)
print(middle.val)