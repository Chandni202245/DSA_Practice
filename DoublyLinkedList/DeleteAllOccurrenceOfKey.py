class Node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None

def deleteAllOccurrenceOfKey(head, key):
    if head is None:
        return None

    if head.next is None and head.val == key:
        return None

    temp = head
    prev = None
    new_head = head

    while temp is not None:
        if temp.val == key:
            if prev is not None:
                prev.next = temp.next
            if temp.next is not None:
                temp.next.prev = prev
            if temp == new_head:
                new_head = temp.next
            temp = temp.next
        else:
            prev = temp
            temp = temp.next

    return new_head


# ---------- TESTING CODE ----------

def create_dll(arr):
    if not arr:
        return None

    head = Node(arr[0])
    temp = head

    for val in arr[1:]:
        new_node = Node(val)
        temp.next = new_node
        new_node.prev = temp
        temp = new_node

    return head


def print_dll(head):
    temp = head
    while temp:
        print(temp.val, end=" ")
        temp = temp.next
    print()


# Test case
arr = [2, 5, 2, 4, 8, 10, 2, 2]
key = 2

head = create_dll(arr)

print("Original DLL:")
print_dll(head)

head = deleteAllOccurrenceOfKey(head, key)

print("After deleting", key, ":")
print_dll(head)

# TC-> O(N)
# SC-> O(1)