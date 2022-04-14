# Linked list implementation in python

class Node:
    # creating a node
    def __init__(self, item) -> None:
        self.item = item
        self.next = None

class Linkedlist:
    def __init__(self) -> None:
        self.head = None

if __name__ == "__main__":          # N/B: this program can be written without the if name == main statement

    linked_list = Linkedlist

        # Assign item values
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)

        # connect nodes
    linked_list.head.next = second
    second.next = third

        # Print the linked list item
    while linked_list.head != None:
        print(linked_list.head.item, end = " ")
        linked_list.head = linked_list.head.next