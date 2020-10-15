from dsame.trees.BinaryTreeNode import BinaryTreeNode


# using level order

def findMax(root: BinaryTreeNode):
    values = []
    max = 0
    values.append(root)

    while len(values):
        temp = values.pop()
        if max < temp.data:
            max = temp.data
        if temp.left:
            values.append(temp.left)
        if temp.right:
            values.append(temp.right)

    return max


a = BinaryTreeNode(5)
b = BinaryTreeNode(2)
c = BinaryTreeNode(3, a, b)
print(findMax(c))
