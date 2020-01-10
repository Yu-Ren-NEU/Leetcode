#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # 不管是走几个台阶. 
        # 要么走1步, 要么走2步
        # 那么对于n级台阶, 只有两种情况
        # 从n-1级走1步, 或者, 从n-2级台阶走2步
        # 第 n 阶的情况只能是上面两种情况之和
        # 类似汉诺塔问题
        # x=1 -> 1
        # x=2 -> 2
        
        if n == 1: return 1
        if n == 2: return 2

        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2 
        idx = 3
        while(idx <= n):
            # print(idx)
            dp[idx] = dp[idx-1] + dp[idx-2]
            idx += 1
        return dp[n]
        
    def test(self):
        assert(self.climbStairs(2) == 2)
        assert(self.climbStairs(3) == 3)
        assert(self.climbStairs(4) == 5)

sol = Solution()
sol.test()

# @lc code=end

