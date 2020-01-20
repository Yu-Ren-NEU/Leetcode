#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        import math 
        return int(str(math.sqrt(x)).split('.')[0], 10)

    def test(self):
        assert(self.mySqrt(4) == 2)
        assert(self.mySqrt(8) == 2)


sol = Solution()
sol.test()
# @lc code=end

