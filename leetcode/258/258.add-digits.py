#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        # 直接取每一位的值相加
        # 当结果小于10的时候停止
        while(num >= 10):
            num = sum(int(x) for x in str(num))
        return num
    
    def test(self):
        assert(self.addDigits(38) == 2)
    
sol = Solution()
sol.test()
# @lc code=end

