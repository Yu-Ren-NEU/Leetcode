#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: []):
        # 对于长度为n, 只会有 (n(n-1))/2 种组合, 时间复杂度是n^2
        # 这种方法会超时
        # 我们可以从前往后扫描, 只需要记录之前的最低值, 并找出之后的最大值就可以了
        # 这样的复杂度为n
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(profit, max_profit)
        return max_profit
    def test(self):
        assert(self.maxProfit([7,1,5,3,6,4]) == 5)
        assert(self.maxProfit([7,6,5,4,3,2]) == 0)

sol = Solution()
sol.test()



# @lc code=end

