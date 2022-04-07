class Node:
    """Class representing one node in a linked list."""
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList():
    """Class representing a linked list data structure"""
    def __init__(self) -> None:
        self.head = None

    def add(self, data):
        """Add a new node to the linked list."""
        # if not self.head:
        #     self.head = Node(data)
        #     return
        self.head = Node(data)
        current_data = self.head
        while current_data.next != None: 
            current_data = current_data.next
        current_data = Node(data)

    def display(self):
        """To display the data in the node"""
        current_node = self.head
        while current_node.next != None:
            print(current_node.data)
            current_node.next = current_node
            

linked_list = LinkedList()
 
linked_list.add(6)
linked_list.add(3)
linked_list.add(4)
linked_list.add(2)
linked_list.add(1)

linked_list.display()




