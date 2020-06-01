from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if self.is_even(i):
                count +=1
        return count

    def is_even(self, i) -> bool:
        count = 1
        if i < 10:
            return False
        while i > 10:
            i /= 10
            count += 1
        if count % 2 == 0:
            return True
        else:
            return False
