from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_so_far, max_till_now = 0, 0

        for i in nums:
            if i == 1:
                max_till_now +=1
                if max_till_now > max_so_far:
                    max_so_far = max_till_now
            else:
                max_till_now = 0
        return max_so_far

