class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

# Brute Force
"""def pairsOfSum(head, target):
    temp1 = head
    result = []
    while temp1 is not None:
        temp2 = temp1.next
        while temp2 is not None:
            if temp1.val + temp2.val == target:
                result.append([temp1.val, temp2.val])
            temp2 = temp2.next
        temp1 = temp1.next
    return result


# Function to insert nodes at the end
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

# -------- TEST CASE --------
arr = [1, 2, 3, 4, 5]
target = 5

head = create_dll(arr)
print("Pairs with sum", target, ":", pairsOfSum(head, target))"""

# TC-> O(N^2)
# SC-> O(1)

# Better Approach

"""def pairsOfSum(head,target):
    my_set=set()
    temp=head
    result=[]
    while temp is not None:
        remaining=target-temp.val
        if remaining in my_set:
            result.append([remaining,temp.val])
        my_set.add(temp.val)
        temp=temp.next
    return result"""

# TC-> O(N)
# SC-> O(N)


# Optimal Solution
# Function to insert nodes at the end
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

# Optimal Solution (Two Pointer)
def pairsOfSum(head, target):
    result = []

    if head is None:
        return result

    left = head
    right = head

    # move right to last node
    while right.next:
        right = right.next

    while left != right and left.prev != right:
        total = left.val + right.val

        if total == target:
            result.append([left.val, right.val])
            left = left.next
            right = right.prev
        elif total > target:
            right = right.prev
        else:
            left = left.next

    return result

# -------- TEST CASE --------
arr = [1, 2, 3, 4, 5]
target = 5

head = create_dll(arr)
print("Pairs with sum", target, ":", pairsOfSum(head, target))

# TC-> O(N)
# SC-> O(1)