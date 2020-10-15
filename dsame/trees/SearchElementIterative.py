from dsame.trees.BinaryTreeNode import BinaryTreeNode


def search_ele_iterative(ele, root: BinaryTreeNode):
    if not root:
        return -1

    values = [root]
    while len(values):
        temp = values.pop()
        if ele == temp.data:
            return True
        if temp.left:
            values.append(temp.left)
        if temp.right:
            values.append(temp.right)

    return False


a = BinaryTreeNode(5)
b = BinaryTreeNode(2)
c = BinaryTreeNode(3, a, b)
print(search_ele_iterative(4, c))
print(search_ele_iterative(5, c))
