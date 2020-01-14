#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        # 实际上是求商和余数

        rest = n
        result = ''
        while(rest > 0):
            result += chr((rest-1)%26+65)
            rest = (rest-1) // 26
            
        return result[::-1]
    def test(self):
        assert(self.convertToTitle(1) == "A")
        assert(self.convertToTitle(26) == "Z")
        assert(self.convertToTitle(28) == "AB")
        assert(self.convertToTitle(701) == "ZY")
        assert(self.convertToTitle(704) == "AAB")

sol = Solution()
sol.test()

# @lc code=end

