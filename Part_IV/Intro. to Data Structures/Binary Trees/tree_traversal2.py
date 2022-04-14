"""www.programiz.com"""

class Node:
    def __init__(self, item) -> None:
        self.left = None
        self.right = None
        self.value = item

    def inorder(self, root):
        if root:
            # Traverse left
            self.inorder(root.left)
            # Traverse root
            print(str(root.value) + "->", end="")
            # Traverse right
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            # Traverse left
            self.postorder(root.left)
            # Traverse right
            self.postorder(root.right)
            # Traverse root
            print(str(root.value) + "->", end="")

    def preorder(self, root):
        if root:
            # Traverse root
            print(str(root.value) + "->", end="")
            # Traverse left
            self.preorder(root.left)
            # Traverse right
            self. preorder(root.right)


# Preorder traversal 
# 1->2->4->5->3->
# Inorder traversal 
# 4->2->5->1->3->
# Postorder traversal
# 4->5->2->3->1->

#  
#           1
#
#        /     \
#      
#       2        3
#
#     /   \     
#
#    4     5   

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal ")
root.inorder(root)

print("\nPreorder traversal ")
root.preorder(root)

print("\nPostorder traversal")
root.postorder(root)