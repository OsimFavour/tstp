"""My own linked_list"""

class Node:
    """Class representing one node in a linked list."""
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList():
    """Class representing a linked list data structure"""
    def __init__(self) -> None:
        self.head = None

    def add(self, data):
        """Add a new node to the linked list."""
        if not self.head:
            self.head = Node(data)
            return
        new_node = Node(data)  
        current_data = self.head
        while current_data.next != None:
            current_data = current_data.next
        current_data.next = new_node

    def len(self):
        current_data = self.head
        count = 0
        while current_data.next != None:
            count += 1
            current_data = current_data.next
        return count 


    def display(self):
        """To display the data in the node"""
        element = []
        current_node = self.head
        while current_node != None:
            # current_node = current_node.next
            element.append(current_node.data)
            # print(current_node.data)
            current_node = current_node.next
        print(element)

linked_list = LinkedList()
 
linked_list.add(6)
linked_list.add(3)
linked_list.add(4)
linked_list.add(2)
linked_list.add(1)

linked_list.display()




