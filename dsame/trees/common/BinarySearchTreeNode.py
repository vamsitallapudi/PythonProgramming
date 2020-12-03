class BinarySearchTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def initializeBST():
    a = BinarySearchTreeNode(6)
    b = BinarySearchTreeNode(8)
    return BinarySearchTreeNode(7, a, b)
