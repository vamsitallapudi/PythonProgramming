from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if not arr:
            return False

        for i in range(0, len(arr)):
            req = arr[i] / 2
            for j in range(0, len(arr)):
                if j != i and arr[j] == req:
                    return True
        return False


print(Solution().checkIfExist([3,1,7,11]))
