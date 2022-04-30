"""tutorialspoint.com"""

class Node():
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data

    def insert(self, value):
# Compare the new value with the parent node
        if self.data:
            if value < self.data:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.data:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.data = value

# Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data, end=" ")
        if self.right:
            self.right.print_tree()

# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.print_tree()