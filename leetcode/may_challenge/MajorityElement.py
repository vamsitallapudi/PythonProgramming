from typing import List
import math


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        eleMap = {}
        majority = nums[0]
        for i in nums:
            if eleMap.get(i) is None:
                eleMap[i] = 1
            else:
                eleMap[i] += 1
            if eleMap[i] >= math.ceil(len(nums)/2):
                majority = i
        return majority


print(Solution().majorityElement([6,6,6,7,7]))