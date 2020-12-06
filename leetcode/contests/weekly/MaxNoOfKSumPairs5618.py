from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        for i in list(nums):
            remaining = k - i
            if remaining in nums:
                count += 1
                nums.remove(i)
                nums.remove(remaining)
        return count


print(Solution().maxOperations([3, 1, 3, 4, 3], 6))
