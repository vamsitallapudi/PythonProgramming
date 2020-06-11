class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def listLength(self, head: Node):
        current = head
        count = 0
        while next is not None:
            count += 1
            current = current.next
        return count

    def insertInLinkedList(self, head: Node, data:int, position:int):
        k = 1
        
