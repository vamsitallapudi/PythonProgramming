from dsame.trees.BinaryTreeNode import BinaryTreeNode


def search_element(ele, root: BinaryTreeNode):
    if not root:
        return False

    if ele == root.data:
        return True

    if search_element(ele, root.left):
        return True
    else:
        return search_element(ele, root.right)


a = BinaryTreeNode(5)
b = BinaryTreeNode(2)
c = BinaryTreeNode(3, a, b)
print(search_element(4, c))
print(search_element(5, c))
