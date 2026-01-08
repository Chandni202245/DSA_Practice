class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def removeNthNode(head, n):
    if head is None:
        return None

    # Step 1: find length
    temp = head
    length = 0
    while temp:
        length += 1
        temp = temp.next

    # If n is greater than length, do nothing
    if n > length:
        return head

    # Step 2: remove head node
    if length == n:
        return head.next

    # Step 3: remove nth node from end
    position_to_stop = length - n
    temp = head
    count = 1

    while count < position_to_stop:
        temp = temp.next
        count += 1

    temp.next = temp.next.next
    return head

# Time Complexity: O(N)
# Space Complexity: O(1)


# Optimal Solution
def removeNthNode(head, n):
    if head is None:
        return None
    slow = head
    fast = head
    for _ in range(n):
        if fast is None:     # safety check
            return head
        fast = fast.next

    if fast is None:
        return head.next

    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head


# TC-> O(N)
# SC-> O(1)