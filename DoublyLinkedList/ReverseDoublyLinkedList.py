class Node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None
"""def reverseDoublyLinkedList(head):
    stack=[]
    temp=head
    while temp is not None:
        stack.append(temp.val)
        temp=temp.next
    temp=head
    while temp is not None:
        e=stack.pop()
        temp.val=e
        temp=temp.next
    return head"""


# Optimal Solution
def reverseDoublyLinkedList(head):
    if head is None or head.next is None:
        return head

    curr = head
    prev = None

    while curr is not None:
        # store next node
        front = curr.next

        # reverse pointers
        curr.next = prev
        curr.prev = front

        # move forward
        prev = curr
        curr = front

    return prev

# Time Complexity: O(N)
# Space Complexity: O(1) (in-place, no extra data structure)



def printList(head):
    temp = head
    while temp:
        print(temp.val, end=" <-> ")
        temp = temp.next
    print("None")

# -------- Test Case --------

# Create DLL: 1 <-> 2 <-> 3 <-> 4
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

head.next = second
second.prev = head

second.next = third
third.prev = second

third.next = fourth
fourth.prev = third

print("Original Doubly Linked List:")
printList(head)

# Reverse DLL
head = reverseDoublyLinkedList(head)

print("\nReversed Doubly Linked List:")
printList(head)