class BinaryTree:
    def __init__(self, value) -> None:
        self.key = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree
        

    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.right_child = self.right_child
            self.right_child = bin_tree

    def print_tree(self):
        print(self.key, end="->")      
        if self.left_child:
            self.left_child.print_tree()
        if self.right_child:
            self.right_child.print_tree()
           

tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_right(3)
tree.left_child.insert_left(4)
tree.left_child.insert_right(5)
# tree.insert_right(5)
tree.print_tree()