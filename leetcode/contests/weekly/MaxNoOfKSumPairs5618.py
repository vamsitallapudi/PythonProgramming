from typing import List


# using 2 pointer solution
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        i, j = 0, len(nums) - 1
        count = 0
        while i < j:
            total = nums[i] + nums[j]
            if total == k:
                i += 1
                j -= 1
                count += 1
            elif total < k:
                i += 1
            else:
                j += 1


print(Solution().maxOperations([3, 1, 3, 4, 3], 6))
