class CLLNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        if self.head is None:
            return 0
        current = self.head
        count = 0
        while current.next != self.head:
            count += 1
            current = current.next
        return count

    def print_data(self):
        if self.head is None:
            return 0
        current = self.head
        while current.next != self.head:
            print(current.data, end=" ")
            current = current.next
