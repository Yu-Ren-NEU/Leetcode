#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
# Author: Liu Song

# @lc code=start
class Solution:
    def maxSubArray(self, nums: []) -> int:
        # 先求出前n-1个的最大和, 如果最大和小于0, 那么当前n是最大的
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]

        idx = 1
        sum_before = nums[0]
        result = sum_before
        while(idx < len(nums)):
            if sum_before < 0:
                # 前idx+1个的最大和小于0
                # 最大和就是当前这个数
                sum_before = nums[idx]
            else:
                # 最大和大于0
                sum_before += nums[idx]

            idx += 1
            # 记录每次的最大值
            if sum_before > result:
                result = sum_before

        return result

    def test(self):
        assert(self.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6)
        assert(self.maxSubArray([-2,1]) == 1)

sol = Solution()
sol.test()
# @lc code=end

