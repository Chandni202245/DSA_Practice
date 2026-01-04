class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
    
class SinglyLinkedList:
    def __init__(self):
        self.head=None

    def append(self,val):
        new_node=Node(val)
        if self.head==None:
            self.head=new_node

        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=new_node

    def traverse(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            curr=self.head
            while curr is not None:
                print(curr.val,end=" ")
                curr=curr.next

    def insert(self,val,position):
        new_node=Node(val)
        if position==0:
            new_node.next=self.head
            self.head=new_node
        else:
            current=self.head
            prev_node=None
            count=0
            while current is not None and count<position:
                prev_node=current
                current=current.next
                count+=1
            prev_node.next=new_node
            new_node.next=current

    def delete(self,val):
        temp=self.head
        if temp.next is not None:
            if temp.val==val:
                self.head=temp.next
                return
            else:
                found=False
                prev=None
                while temp is not None:
                    if temp.val==val:
                        found=True
                        break
                    prev=temp
                    temp=temp.next
                if found:
                    prev.next=temp.next
                    return
                else:
                    print("Node not found")

sll=SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.traverse()
print()
sll.insert(90,3)
sll.traverse()
print()
sll.delete(20)
sll.traverse()


# Time & Space Complexity

# append(val)
# Time: O(n)
# Space: O(1)

# traverse()
# Time: O(n)
# Space: O(1)

# insert(val, position)
# Time: O(n)
# Space: O(1)

# delete(val)
# Time: O(n)
# Space: O(1)