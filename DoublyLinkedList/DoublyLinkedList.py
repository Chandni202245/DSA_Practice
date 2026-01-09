class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class doublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def insert_at(self, val, position):
        if position == 0:
            self.insert_at_head(val)
            return

        new_node = Node(val)
        current = self.head
        count = 0

        while current and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print("Position out of bound")
            return

        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    # helper function to print list
    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end=" <-> ")
            temp = temp.next
        print("None")

dll = doublyLinkedList()

dll.insert_at_head(10)
dll.insert_at_head(5)
dll.append(20)
dll.append(25)

dll.display()      # 5 <-> 10 <-> 20 <-> 25 <-> None

dll.insert_at(15, 2)
dll.display()      # 5 <-> 10 <-> 15 <-> 20 <-> 25 <-> None

dll.insert_at(1, 0)
dll.display()      # 1 <-> 5 <-> 10 <-> 15 <-> 20 <-> 25 <-> None
