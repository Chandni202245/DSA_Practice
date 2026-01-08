class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Brute Force Approach
"""def oddEvenLinkedList(head):
    if head is None or head.next is None:
        return head

    values = []
    temp = head

    # collect odd index nodes
    while temp:
        values.append(temp.data)
        if temp.next:
            temp = temp.next.next
        else:
            break

    # collect even index nodes
    temp = head.next
    while temp:
        values.append(temp.data)
        if temp.next:
            temp = temp.next.next
        else:
            break

    # rewrite values back to linked list
    temp = head
    index = 0
    while temp:
        temp.data = values[index]
        index += 1
        temp = temp.next

    return head

# For testing
def printLinkedList(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

# Creating linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Original Linked List:")
printLinkedList(head)

head = oddEvenLinkedList(head)

print("After Odd-Even Rearrangement:")
printLinkedList(head)"""
# Time Complexity: O(N)

# Space Complexity: O(N) (because of extra array)


# Optimal Solution
def oddEvenIndexes(head):
    if head is None or head.next is None:
        return head
    odd=head
    even=head.next
    even_head=even
    while even is not None and even.next is not None:
        odd.next=odd.next.next
        odd=odd.next
        even.next=even.next.next
        even=even.next
    odd.next=even_head
    return head

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

def printLinkedList(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

print("Original Linked List:")
printLinkedList(head)

head = oddEvenIndexes(head)

print("After Odd-Even Rearrangement:")
printLinkedList(head)

# TC-> O(N)
# SC-> O(1)
# I used two pointers to separate odd and even indexed nodes and merged them without extra space.