class Node:
    def __init__(self, data):
        self.data = data  # assigning the data passed
        self.next = None  # initializing the node as null


class BaseLinkedList:
    def __init__(self):
        self.head = None

    # code to append / insert at end
    def insert_at_end(self, head, data):
        # creating a new node and put data in it
        new_node = Node(data=data)
        current = head

        # if Linked List is empty, make new node as head
        if not head:
            head = new_node
            return head

        # traversing till end
        while current.next:
            current = current.next
        # pointing the last node's next to new node
        current.next = new_node
        # pointing new node's previous
        new_node.prev = current
        return head


    def initializebll(self, bll):
        for i in range(1, 7):
            self.head = bll.insert_at_end(self.head, i)
        return self.head


if __name__ == '__main__':
    bll = BaseLinkedList()
    head = bll.initializebll(bll)
    while head:
        print(head.data, end=" ")
        head = head.next
