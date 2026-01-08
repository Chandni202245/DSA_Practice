class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def LinkedListCycle(head):
    slow=head
    fast=head
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    return False

# Create nodes
# head = Node(1)
# head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)

# # Create cycle: 4 -> 2
# head.next.next.next.next = head.next

# print(LinkedListCycle(head))  # True


# Without cycle
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print(LinkedListCycle(head))  # False

# Time Complexity: O(N)
# Space Complexity: O(1)
