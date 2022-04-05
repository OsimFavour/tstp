class Node:
    """Class representing one node in a linked list."""
    def __init__(self, data) -> None:
        self.data = Node(data)
        self.next = None

class LinkedList:
    """Class representing a linked list data structure"""
    def __init__(self, head) -> None:
        self.head = head

    def add(self, data):
        """Add a new node to the linked list."""
        previous_head = self.head
        self.head = Node(data)
        self.head.next = previous_head

linked_list = LinkedList()
linked_list.add(1)
linked_list.add(2)
linked_list.add(3)

node = linked_list.head
while node:
    print(node.data)
    node = node.next