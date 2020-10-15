from dsame.trees.BinaryTreeNode import BinaryTreeNode


# as it is a binary tree, we can insert wherever we want

def insertElement(ele, root: BinaryTreeNode):
    values = []
    newNode = BinaryTreeNode(ele)

    if not root:
        return newNode

    values.append(root)
    while len(values):
        temp = values.pop()

        if temp.left:
            values.append(temp.left)
        else:
            temp.left = newNode
            return
        if temp.right:
            values.append(temp.right)
        else:
            temp.right = newNode
            return


a = BinaryTreeNode(1)
b = BinaryTreeNode(2)
c = BinaryTreeNode(3, a, b)
print(insertElement(4, c))
print(insertElement(5, c))