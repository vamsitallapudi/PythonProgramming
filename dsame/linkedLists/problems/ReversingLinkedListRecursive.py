from dsame.linkedLists.problems.BaseLinkedList import BaseLinkedList


def recursive_reverse(head):
    # if no elements in head
    if not head:
        return None
    if not head.next:
        return head
    second_ele = head.next
    head.next = None
    reverse_rest = recursive_reverse(second_ele)
    second_ele.next = head
    return reverse_rest


if __name__ == '__main__':
    bll = BaseLinkedList()
    head = bll.initializebll(bll)
    head = recursive_reverse(head)
    bll.print_data(head)
