class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


"""
 Deleting a node at start. 
"""


def delete_at_start(head):
    # edge case: return if head is null
    if not head:
        return None

    temp = head  # creating temp pointer and pointing to head node
    head = head.next  # moving head to next node
    temp = None  # making temp as null
    return head


"""
 Deleting a node at end. 
"""


def delete_at_end(head: Node):
    if not head:
        return None

    prev_node = head
    while prev_node.next.next is not None:
        prev_node = prev_node.next
    prev_node.next = None
    return head


def insert(head, data):
    if not head:
        return Node(data)
    temp = Node(data)
    temp.next = head
    head = temp
    return head


if __name__ == '__main__':

    # start with empty list
    head = None

    head = insert(head, 12)
    head = insert(head, 29)
    head = insert(head, 11)
    head = insert(head, 23)
    head = insert(head, 8)

    # deleting a node at start
    head = delete_at_start(head)

    # deleting a node at end
    head = delete_at_end(head)

    while head:
        print("{}".format(head.data), end=" ")
        head = head.next
