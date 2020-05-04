class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magSet, ranSet = {}, {}

        def helper(str, my_set):
            for i in str:
                if i not in my_set:
                    my_set[i] = 1
                else:
                    my_set[i] += 1

        helper(magazine, magSet)
        helper(ransomNote, ranSet)
        for i in ranSet.keys():
            if magSet.get(i) is not None and magSet.get(i) >= ranSet.get(i):
                continue
            else:
                return False
        return True


print(Solution().canConstruct("ae", "adca"))
