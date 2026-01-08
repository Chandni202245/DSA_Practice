class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def ReverseLinkedList(head):
    temp=head
    prev=None
    while temp is not None:
        front=temp.next
        temp.next=prev
        prev=temp
        temp=front
    return prev

def printLinkedList(head):
    temp=head
    while temp is not None:
        print(temp.data,end="->")
        temp=temp.next
    print("None")

head=Node(1)
head.next=Node(2)
head.next.next=Node(3)

print("Original List")
printLinkedList(head)


head=ReverseLinkedList(head)

print("Reversed Linked list")
printLinkedList(head)
temp=head


# TC->O(N)
# SC-> O(1)