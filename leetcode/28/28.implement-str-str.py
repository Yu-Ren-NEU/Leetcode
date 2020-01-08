#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
# Author: Liu Song

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 先判断needle不在haystack的情况

        if needle not in haystack:
            return -1
        
        return haystack.index(needle)

    def test(self):
        haystack = "hello"
        needle = "ll"
        print(self.strStr(haystack, needle))

# sol = Solution()
# sol.test()

# @lc code=end

