from typing import List

class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.lcs(0, 0, list(text1), list(text2))

    def lcs(self, i, j, arr1: List, arr2: List):
        if i == len(arr1) or j == len(arr2):
            return 0
        elif arr1[i] == arr2[j]:
            return 1 + self.lcs(i + 1, j + 1, arr1, arr2)
        else:
            return max(self.lcs(i+1, j, arr1, arr2), self.lcs(i, j+1, arr1, arr2))

print(Solution().longestCommonSubsequence("bd", "abcd"))