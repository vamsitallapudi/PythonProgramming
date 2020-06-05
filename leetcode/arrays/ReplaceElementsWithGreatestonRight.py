from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxVal = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = maxVal
            maxVal = max(maxVal, temp)
        return arr


print(Solution().replaceElements([17, 18, 5, 4, 6, 1]))
