# Linked list operation in Python

# Creating a node
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Linkedlist:

    def __init__(self) -> None:
        self.head = None

        # Insert at the beginning
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

        # Insert after a node
    def insertAfter(self, prev_node, new_data):
        if prev_node == None:
            print("The given previous node must inLinkedlist.")
            return
        
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node