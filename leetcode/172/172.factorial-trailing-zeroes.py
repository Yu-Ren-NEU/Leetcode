#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 对于一个数, 要想结果以0结尾, 那么必须得是2*5, 10的倍数

        result = 0
        while(n):
            n = n // 5
            result += n
        return result

    def test(self):
        assert(self.trailingZeroes(25))

sol = Solution()
sol.test()
# @lc code=end

