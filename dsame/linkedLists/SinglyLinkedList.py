class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # insertion of new node at front of ll
    def insert_at_front(self, data):
        # creating new node to be inserted
        new_node = Node(data)
        new_node.next = self.head  # pointing the new node's next to head
        self.head = new_node  # making the new node as head

    def insert_at_end(self, data):
        new_node = Node(data)
        current = self.head
        while current.next is not None:  # traversing till the last node
            current = current.next
        # change the next of last node
        current.next = new_node

    def insert_at_pos(self, data, prev_node: Node):
        # edge case: check if prev_node exists
        if prev_node is None:
            return

        new_node = Node(data)
        current = self.head
        # iterating till the previous node is reached
        while current.next is not prev_node:
            current = current.next
        # making new node's next as previous node's next
        new_node.next = current.next
        # making previous node's next point to new node
        current.next = new_node
