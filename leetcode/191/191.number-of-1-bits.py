#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count('1')
    def test(self):
        assert(self.hammingWeight(0b00000000000000000000000000001011) == 3)
sol = Solution()
sol.test()
# @lc code=end

