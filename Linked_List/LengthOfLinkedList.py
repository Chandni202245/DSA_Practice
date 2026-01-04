class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def LengthOfLinkedList(head):
    count=0
    curr=head
    while curr is not None:
        count+=1
        curr=curr.next
    return count

head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(40)
print(LengthOfLinkedList(head))

# Time: O(n)

# Space: O(1)