class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def InsertAtEnd(head,x):
    new_node=Node(x)
    if head is None:
        return new_node
    curr=head
    while curr.next is not None:
        curr=curr.next
    curr.next=new_node
    return head

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

head = InsertAtEnd(head, 40)

temp = head
while temp:
    print(temp.data, end=" ")
    temp = temp.next