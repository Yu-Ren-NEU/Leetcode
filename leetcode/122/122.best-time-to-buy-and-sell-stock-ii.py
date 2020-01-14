#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: []) -> int:
        # 我们将数值画到x-y坐标系里
        # 其实要求的就是单调上升的曲线, 找到相应的波峰

        if not prices or len(prices) == 1: 
            return 0
        
        result = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                result += prices[i] - prices[i-1]

        return result
    def test(self):
        assert(self.maxProfit([7,1,5,3,6,4]) == 7)
        assert(self.maxProfit([1,2,3,4,5]) == 4)
        assert(self.maxProfit([7,6,4,3,1]) == 0)

sol = Solution()
sol.test()


# @lc code=end

