class BinaryTreeNode:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


def initializeBinaryTree() -> BinaryTreeNode:
    a = BinaryTreeNode(2)
    b = BinaryTreeNode(3)
    c = BinaryTreeNode(1, a, b)
    return c


def initializeBinaryTreeWithTwoLevels() -> BinaryTreeNode:
    d = BinaryTreeNode(5)
    e = BinaryTreeNode(6)
    a = BinaryTreeNode(2, d, e)
    b = BinaryTreeNode(3)
    c = BinaryTreeNode(1, a, b)
    return c


def printBinaryTree(root):
    if not root:
        return
    print(root.data)
    if root.left:
        printBinaryTree(root.left)
    if root.right:
        printBinaryTree(root.right)
