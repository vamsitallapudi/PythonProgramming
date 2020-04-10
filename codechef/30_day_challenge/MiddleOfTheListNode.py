# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slowptr = head
        fastptr = head
        if head != None:
            while(fastptr is not None and fastptr.next is not None):
                fastptr = fastptr.next.next
                slowptr = slowptr.next
            return slowptr
            
print(Solution().middleNode(ListNode([1,2,3,4,5,6])))

