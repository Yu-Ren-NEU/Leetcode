#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
# 

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 转成二进制然后相加再转回字符串
        return "{0:b}".format(int(a, 2)+int(b, 2))

    def test(self):
        assert(self.addBinary("11", "1") == "100")
        assert(self.addBinary("1010", "1011") == "10101")
    
sol = Solution()
sol.test()
# @lc code=end

