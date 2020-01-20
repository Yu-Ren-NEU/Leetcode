#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
# Author: Liu Song

# @lc code=start
class Solution:
    def searchInsert(self, nums: [], target: int) -> int:
        # 直接搜
        for idx, item in enumerate(nums):
            if target == item:
                return idx
            elif target < item:
                return idx
            elif target > item:
                continue
        else:
            return len(nums)
            
    def test(self):
        testcase = [1,3,5,6]
        target = 0
        print(self.searchInsert(testcase, target))

# sol = Solution()
# sol.test()
# @lc code=end

