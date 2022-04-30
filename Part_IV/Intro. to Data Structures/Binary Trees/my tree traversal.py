class Node():
    def __init__(self, value) -> None:
        self.root = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        if self.left == None:
            self.left = Node(value)
        else:
            binary_tree = Node(value)
            binary_tree.left = self.left
            self.left = binary_tree

    def insert_right(self, value):
        if self.right == None:
            self.right = Node(value)
        else:
            binary_tree = Node(value)
            binary_tree.right = self.right
            self.right = binary_tree

    def pre_order(self):
        print(self.root, end="->")
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.root, end="->")
        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.root, end="->")

tree = Node(1)
tree.insert_left(2)
tree.insert_right(3)
tree.left.insert_left(4)
tree.left.insert_right(5)

print("Pre_order traversal ")
tree.pre_order()

print()
print("\nInorder traversal ")
tree.inorder()

print()
print("\nPostorder traversal")
tree.postorder()


