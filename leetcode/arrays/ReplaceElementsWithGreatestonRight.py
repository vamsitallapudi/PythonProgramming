from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        n = len(arr)
        max_val = arr[n - 1]
        for i in range(n - 2, -1, -1):
            arr[i] = max(arr[i], max_val)
            max_val = arr[i]
        arr.append(-1)
        arr.pop(0)
        return arr


print(Solution().replaceElements([1]))
