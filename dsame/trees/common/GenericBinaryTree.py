class GenericTreeNode:
    def __init__(self, data=None, firstChild=None, nextSibling=None):
        self.data = data
        self.firstChild = firstChild
        self.nextSibling = nextSibling


def initializeGenericTree() -> GenericTreeNode:
    c = GenericTreeNode(4)
    a = GenericTreeNode(3, firstChild=c)
    b = GenericTreeNode(2, nextSibling=a)
    d = GenericTreeNode(1, firstChild=b)
    return d
