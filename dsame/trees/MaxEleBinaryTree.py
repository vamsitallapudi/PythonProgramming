from dsame.trees.BinaryTreeNode import BinaryTreeNode


def maxEle(root: BinaryTreeNode) -> BinaryTreeNode:
    maximum = 0
    if root:
        root_val = root.data
        left = maxEle(root.left)
        right = maxEle(root.right)
        if left > right:
            maximum = left
        else:
            maximum = right

        if root_val > maximum:
            maximum = root_val
    return maximum


a = BinaryTreeNode(1)
b = BinaryTreeNode(2)
c = BinaryTreeNode(3, a, b)

print(maxEle(c))
