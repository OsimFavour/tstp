"""Create a Linked list
"""

class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = Node(data)

    def __str__(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data)
            current_node = current_node.next


a_list = Linkedlist()
a_list.append("Tuesday")
a_list.append("Wednesday")
a_list.append("Thursday")
a_list.append("Friday")

a_list.__str__()
# print(a_list)