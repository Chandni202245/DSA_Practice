class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def startingPoint(head):
    slow=head
    fast=head
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            slow=head
            while slow!=fast:
                slow=slow.next
                fast=fast.next
            return slow
    return None


# Create linked list: 1 -> 2 -> 3 -> 4 -> 2 (cycle starts at 2)
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = head.next

start = startingPoint(head)
print(start.data if start else "No cycle")
# Time Complexity: O(N)

# Space Complexity: O(1)