# find next greater node and print it
# eg:
# Input: [2,1,5]
# Output: [5,5,0]

# Definition for singly-linked list.
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        position = -1
        stack, ans = [], []

        while head:
            position += 1
            ans.append(0)
            while stack and stack[-1][1] < head.val:
                index, value = stack.pop()
                ans[index] = head.val

            stack.append((position, head.val))
            head = head.next
        return ans

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(4)
    d = ListNode(1)
    a.next = b
    b.next = c
    c.next = d
    x = Solution().nextLargerNodes(a)

    for i in x:
        print(i)
