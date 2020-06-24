from dsame.linkedLists.circularLinkedLists.Common import print_and_iterate


class CLLNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CLL:
    def __init__(self, head=None):
        self.head = head

    def delete_at_end(self, head):
        if not head or not head.next:
            return None

        previous, current = head, head.next
        while current.next != head:
            previous = previous.next
            current = current.next
        previous.next = head
        return head

    def delete_at_start(self, head):
        if not head or not head.next:
            return None

        current = head
        while current.next != head:
            current = current.next
        head = head.next
        current.next = head
        return head

    def insert_at_start(self, head, data):
        new_node = CLLNode(data=data)
        # initialize new variable called current
        if not head:
            new_node.next = new_node
            head = new_node
            return head
        current = head
        while current.next != head:
            current = current.next

        new_node.next = head
        current.next = new_node
        head = new_node
        return head


if __name__ == "__main__":
    head = None
    cll = CLL(head)
    head = cll.insert_at_start(head, 3)
    head = cll.insert_at_start(head, 2)
    head = cll.insert_at_start(head, 1)
    head = cll.delete_at_start(head)
    head = cll.delete_at_end(head)

    curr = head
    curr = print_and_iterate(curr)
    while curr != head:
        curr = print_and_iterate(curr)
