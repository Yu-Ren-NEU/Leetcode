#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
# Author: Liu Song

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 垃圾题目, 去死吧你
        return len(s.rstrip().split(' ')[-1])

    def test(self):
        assert(self.lengthOfLastWord('Hello World') == 5)

sol = Solution()
sol.test()
# @lc code=end

