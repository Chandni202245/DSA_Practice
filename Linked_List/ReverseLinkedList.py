from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        while current:
            front = current.next
            current.next = prev
            prev = current
            current = front

        return prev


# Creating linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original Linked List:")
temp = head
while temp:
    print(temp.val, end=" -> ")
    temp = temp.next
print("None")

# Reverse
sol = Solution()
reversed_head = sol.reverseList(head)

print("Reversed Linked List:")
temp = reversed_head
while temp:
    print(temp.val, end=" -> ")
    temp = temp.next
print("None")
