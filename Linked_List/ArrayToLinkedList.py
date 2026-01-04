class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
def arrayToLinkedList(arr):
    if not arr:
        return None
    head=Node(arr[0])
    curr=head
    for i in range(1,len(arr)):
        curr.next=Node(arr[i])
        curr=curr.next
    return head
    

arr = [10, 20, 30, 40, 50]
head = arrayToLinkedList(arr)

# traverse to check
temp = head
while temp:
    print(temp.data, end=" ")
    temp = temp.next

# Time Complexity: O(n)

# Space Complexity: O(n)