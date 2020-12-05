class BinarySearchTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def initialize_BST():
    a = BinarySearchTreeNode(6)
    b = BinarySearchTreeNode(8)
    return BinarySearchTreeNode(7, a, b)


def print_BST(root: BinarySearchTreeNode):
    if not root:
        return root
    if root.left:
        print_BST(root.left)
    print(root.data)
    if root.right:
        print_BST(root.right)
