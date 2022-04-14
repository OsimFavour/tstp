"""www.programiz.com"""

class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.value = key

        # Traverse preorder
    def traversePreorder(self):
        print(self.value, end=" ")
        if self.left:
            self.left.traversePreorder()
        if self.right:
            self.right.traversePreorder()

        # Traverse inorder
    def traverseInorder(self):
        if self.left:
            self.left.traverseInorder()
        print(self.value, end=" ")
        if self.right:
            self.right.traverseInorder()

        # Traverse PostOrder
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.value, end=" ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print("Pre order Traversal: ", end="")
root.traversePreorder()
print("\nIn order Traversal: ", end="")
root.traverseInorder()
print("\nPost order Traversal: ", end="")
root.traversePostOrder()
